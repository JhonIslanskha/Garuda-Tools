#        Copyright (C) 2017 M4st3r L1nux Indonesia (Jh0n 1sl4nskh4_404)

from core import colors
from core.GarudaTools import *
from dns import resolver
import dns

conf = {
	"name": "cloudflare_resolver",
	"version": "v1.10",
	"shortdesc": "tries to resolve ip from subdomains",
	"author": "M4st3rL1nux",
	"github": "JhonIslanskha",
	"by": "Jh0n 1sl4nskh4_404",
	"initdate": "24.2.2016",
	"lastmod": "26.5.2017",
	"apisupport": True
}

# List of variables
variables = OrderedDict((
	('target', ['google.com', 'target address']),
	('pos', ['false', 'print only success[true/false]']),
	('timeout', ['0.5', 'timeout'])
))

# Simple changelog
changelog = "Version 1.0:\nrelease\n\nVersion 2.0:\n+ fixed timeout bug\n+ module is now using dnspython library\n\nVersion 2.1:\n+ added more colors\n\nVersion 2.2:\n+ added ? when resolved is same than default ip\n+ added timeout variable\n\nVersion 2.2.1:\n+ added exception"

# Run function
def run():
	apianswer = {}

	ipresolver = resolver.Resolver()
	ipresolver.timeout = float(variables['timeout'][0])
	ipresolver.lifetime = float(variables['timeout'][0])

	variables['target'][0] = variables['target'][0].replace("http://", "")
	variables['target'][0] = variables['target'][0].replace("https://", "")
	sub = ('mail', 'webmail', 'email', 'direct-connect-mail',
	'direct', 'direct-connect', 'cpanel', 'phpmyadmin', 'ftp', 'forum', 'blog',
	'm', 'dev', 'record', 'ssl', 'dns', 'help', 'ns', 'ns1', 'ns2',
	'ns3', 'ns4', 'irc', 'server', 'status', 'portal', 'beta',
	'admin', 'alpha', 'imap', 'smtp', 'test')
	try:
		orgip = ipresolver.query(variables['target'][0], 'A')
		print(colors.green+"[-------------------------]"+colors.end)
		print(colors.green+"[+] Default IP Address : %s"%orgip[0]+colors.end)
		print(colors.green+"[-------------------------]"+colors.end)
		apianswer[variables['target'][0]] = orgip
	except(dns.exception.Timeout):
		print(colors.red+"[-] Error : Host is Down !"+colors.end)
	except dns.resolver.NoAnswer:
		print(colors.red+"[?] The DNS response does not contain an answer to the question"+colors.end)
	for i in sub:
		host = i+'.'+variables['target'][0]
		try:
			query = ipresolver.query(host, 'A')
			if query[0] == orgip[0]:
				print(colors.yellow+"[?] %s : %s"%(host, query[0])+colors.end)
				apianswer[host] = query[0]
			else:
				print(colors.green+"[+] %s : %s"%(host, query[0])+colors.end)
				apianswer[host] = query[0]
		except(dns.exception.Timeout):
			if variables['pos'][0] != 'true':
				print(colors.red+"[-] %s : N/A"%host+colors.end)
		except dns.resolver.NoAnswer:
			if variables['pos'][0] != 'true':
				print(colors.red+"[?] The DNS response does not contain an answer to the question"+colors.end)

	return apianswer