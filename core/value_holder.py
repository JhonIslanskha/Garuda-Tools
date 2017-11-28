#		Copyright (C) 2017 M4st3r L1nux Indonesia (Jh0n 1sl4nskh4_404)

saveddict = None

def save_values(variables):
	global saveddict
	saveddict = variables

def set_values(tdict):
	global saveddict

	for key0 in saveddict.keys():
		for key1 in tdict.keys():
			if key0 == key1:
				tdict[key0][0] = saveddict[key0][0]