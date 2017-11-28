#        Copyright (C) 2017 M4st3r L1nux Indonesia (Jh0n 1sl4nskh4_404)
from core import colors

def setvar(variable, value, variables):
	variables[variable][0] = value
	print(colors.bold+variable +" => "+ value + colors.end)