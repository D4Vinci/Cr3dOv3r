# -*- encoding: utf-8 -*-
#Written by: Karim shoair - D4Vinci ( Cr3dOv3r )
import sys,os
from . import updater
from .websites import *
from .color import *

def getinput(text):
	# Return the suitable input type according to python version
	ver = sys.version[0]
	if ver=="3":
		return input(text)
	else:
		return raw_input(text)

def banner():
	if os.name=="nt":
		os.system("cls")
	else:
		os.system("clear")
	version = updater.check()
	banner = open(os.path.join("Data","banners.txt"), encoding="utf8").read()
	banner_to_print = G + banner.format(Name=R+"Cr3d0v3r By "+Bold+B+"D4Vinci -"+M+" V"+version+end+G,
									Description=C+"Know the dangers of email credentials reuse attacks."+G,
									Loaded=B+"Loaded "+Y+str(len(all_websites))+B+" website."+G) + end
	print(banner_to_print)

all_websites =list(websites.keys()) + list(custom_websites.keys()) + list(req_websites.keys())
