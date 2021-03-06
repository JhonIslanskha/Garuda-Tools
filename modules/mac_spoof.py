#        Copyright (C) 2017 M4st3r L1nux Indonesia (Jh0n 1sl4nskh4_404)

from core.GarudaTools import *
import os
from core import colors
from scapy.all import *
from core import network_scanner
import random
from core import getpath
from core.setvar import setvar

conf = {
	"name": "mac_spoof",
	"version": "1.0",
	"shortdesc": "mac spoof",
	"author": "M4st3rL1nux",
	"github": "JhonIslanskha",
	"by": "Jh0n 1sl4nskh4_404",
	"initdate": "9.3.2016",
	"lastmod": "26.5.2017",
	"apisupport": True,
	"needroot": 1,
	"dependencies": ["ethtool"]
}

# Custom commands
customcommands = {
	'scan': 'scan network',
	'random_mac': 'generate random mac',
	'reset': 'end mac spoof'
}

# List of the variables
variables = OrderedDict((
	('fake_mac', ['02:a0:04:d3:00:11', 'fake mac']),
	('interface', ['eth0', 'network interface']),
))

# Additional help notes
help_notes = colors.red+"this module will not work without root permissions, and ethtool!"+colors.end

# Additional notes to options
option_notes = colors.yellow+" you can generate fake_mac using 'random_mac' command\n use 'reset' command to end mac spoof"+colors.end

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	xterm1 = "service network-manager stop"
	xterm2 = "ifconfig "+variables['interface'][0]+" hw ether "+variables['fake_mac'][0]
	xterm3 = "service network-manager start"
	printInfo("status: starting mac spoof")
	os.system(xterm1)
	printInfo("status: trying to set fake mac address...")
	os.system(xterm2)
	os.system(xterm3)
	printSuccess("status: done!")

def scan(args):
	network_scanner.scan()

def random_mac(args):
	mac = "f4:ac:c1:%02x:%02x:%02x" % (
		random.randint(0, 255),
		random.randint(0, 255),
		random.randint(0, 255),
	)
	setvar('fake_mac', mac, variables)

def reset(args):
	command = ['ethtool', '-P', variables['interface'][0]]
	output = subprocess.Popen( command, stdout=subprocess.PIPE ).communicate()[0]
	realmac = str(output)
	realmac = realmac.replace("b'Permanent address: ", "")
	realmac = realmac.replace("'", "")
	realmac =  realmac[:-2]
	if not realmac:
		printError("error")
		return ModuleError("error")
	else:
		printInfo("realmac: "+realmac)
		xterm1a = "service network-manager stop"
		xterm2a = "ifconfig "+variables['interface'][0]+" hw ether "+realmac
		xterm3a = "service network-manager start"
		printInfo("setting real mac")
		os.system(xterm1a)
		printInfo("trying to set real mac address...")
		os.system(xterm2a)
		os.system(xterm3a)
		printSuccess("done!")