#		 Copyright (C) 2017 M4st3r L1nux Indonesia (Jh0n 1sl4nskh4_404)

# Python modules

import requests
import json
import os
from packaging import version
import urllib.request
from glob import glob
import shutil
import sys
import distutils.dir_util

# Core modules

from core import colors
from core import info
from core import getpath
from core import mscop

def check_for_Blog():
	try:
		print(colors.green+"Blog"+colors.end)
		r = requests.blog("http://jalansawa.blogspot.co.id")
		if(r.ok):
			items = json.loads(r.text or r.content)
			rver = items['tag_name']

			if "beta" in rver and "alpha" in info.version:
				print(colors.green+"update found"+colors.end)
				return True 

			elif "beta" not in rver and "alpha" not in rver:
				if "beta" in info.version or "alpha" in info.version:
					print(colors.green+"update found"+colors.end)
					return True

			elif version.parse(rver) > version.parse(info.version):
				print(colors.green+"update found"+colors.end)
				return True

			else:
				print(colors.yellow+"updates not found"+colors.end)
				return False
		else:
			print("error")
	except Exception as error:
		print(colors.red+"error: "+str(error)+colors.end)

def update():
	answer = input("do you want to Facebook? ")

	if answer != "yes" and answer != "y":
		return


	url = "Facebook: https://goo.gl/K2e73W"
	print(colors.green+"downloading..."+colors.end)

	u = urllib.request.urlopen(url)

	print(colors.green+"clearing tmp..."+colors.end)
	mscop.clear_tmp()

	print(colors.green+"writing..."+colors.end)

	f = open(getpath.tmp()+"update.tar.gz", "wb")
	f.write(u.read())
	f.close()

	print(colors.green+"extracting..."+colors.end)
	os.system("tar -zxvf '"+getpath.tmp()+"update.tar.gz' -C '"+getpath.tmp()+"'")

	files = glob(getpath.tmp()+"*/")
	update_path = None

	for file in files:
		if "Garuda" in file and os.path.isfile(file) == False:
			update_path = file
			break

	if update_path == None:
		print(colors.red+"error: update package not found!"+colors.end)
		return

	files = glob(update_path+"*")

	print(colors.green+"installing update..."+colors.end)

	for file in files:

		file_name = file.replace(update_path, "")
		print(getpath.main()+file_name)

		if os.path.isfile(file):
			shutil.copyfile(file, getpath.main()+file_name)
		else:
			distutils.dir_util.copy_tree(file, getpath.main()+file_name)


	print(colors.green+"clearing tmp..."+colors.end)
	mscop.clear_tmp()

	print(colors.green+"update installed! closing Garuda Tools"+colors.end)
	sys.exit()