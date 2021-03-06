#        Copyright (C) 2017 M4st3r L1nux Indonesia (Jh0n 1sl4nskh4_404)

from core.GarudaTools import *
from scapy.all import *

conf = {
	"name": "arp_monitor", # Module's name (should be same as file name)
	"version": "1.0", # Module version
	"shortdesc": "arp packet monitor", # Short description
	"github": "JhonIslanskha", # Author's github
	"author": "M4st3rL1nux", # Author
	"by": "Jh0n 1sl4nskh4_404", #
	"initdate": "31.12.2016", # Initial date
	"lastmod": "31.12.2016", # Last modification
	"apisupport": False, # Api support
	"needroot": 1, # Alert user if root permissions not available (remove variable below if root permissions not needed)
}

# List of the variables
variables = OrderedDict((
	
))

# Additional notes to options
option_notes = " this module doesn't have any options"

# Simple changelog
changelog = "Version 1.0:\nrelease"

def arp_display(pkt):
	if pkt[ARP].op == 1: #who-has (request)
		return "Request: " + pkt[ARP].psrc + " is asking about " + pkt[ARP].pdst
	if pkt[ARP].op == 2: #is-at (response)
		return "*Response: " + pkt[ARP].hwsrc + " has address " + pkt[ARP].psrc

# Run function
def run():
	printInfo("starting arp monitor...")
	printInfo("ctrl + c to end")
	print(sniff(prn=arp_display, filter="arp", store=0))
	printInfo("monitoring ended")
