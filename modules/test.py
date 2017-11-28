#        Copyright (C) 2017 M4st3r L1nux Indonesia (Jh0n 1sl4nskh4_404)

from core.GarudaTools import *

# Info about the module

conf = {
	"name": "test", # Module's name (should be same as file's name)
	"version": "1.0", # Module version
	"shortdesc": "only test", # Short description
	"author": "M4st3rL1nux", # Author
	"github": "JhonIslanskha", # Author's github
	"by": "Jh0n 1sl4nskh4_404", #
	"initdate": "24.2.2016", # Initial date
	"lastmod": "26.5.2017",
	"apisupport": True, # Api support

	"message": "hello"
}

# List of the variables
variables = OrderedDict((
	("value", [0, "description"]),
))

customcommands = {
	"test": "test"
}

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	print(variables['value'][0])
	print(variables['value'][1])
	printWarning("warning")
	return variables

def test(args):
	return "ok"