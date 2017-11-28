#        Copyright (C) 2017 M4st3r L1nux Indonesia (Jh0n 1sl4nskh4_404)
from core.GarudaTools import *
import whois

conf = {
	"name": "whois", # Module's name (should be same as file name)
	"version": "1.0", # Module version
	"shortdesc": "perform whois query", # Short description
	"github": "JhonIslanskha", # Author's github
	"author": "M4st3r L1nux", # Author
	"by": "Jh0n 1sl4nskh4_404", #
	"initdate": "18.12.2016", # Initial date
	"lastmod": "26.5.2017",
	"apisupport": True
}

# List of the variables
variables = OrderedDict((
	("target", ["google.com", "target address"]),
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	# Run
	w = whois.whois(variables["target"][0])
	print(w)
	return w