#        Copyright (C) 2017 M4st3r L1nux Indonesia (Jh0n 1sl4nskh4_404)

from core.GarudaTools import *
import socket

conf = {
	"name": "hostname_resolver",
	"version": "1.0",
	"shortdesc": "resolve hostname using ip",
	"author": "M4st3rL1nux",
	"github": "JhonIslanskha",
	"by": "Jh0n 1sl4nskh4_404",
	"initdate": "9.5.2016",
	"lastmod": "26.5.2017",
	"apisupport": True
}

# List of the variables
variables = OrderedDict((
	('target', ['192.168.1.1', 'target ip address']),
))

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	try:
		querly = socket.gethostbyaddr(variables['target'][0])
		printSuccess("resolved hostname: "+ querly[0])
		return querly[0]
	except(socket.herror):
		printError("unknown host")
		return ModuleError("unknown host")
	except(socket.gaierror):
		printError("name or service not known")
		return ModuleError("name or service not known")