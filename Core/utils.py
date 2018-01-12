#Written by: Karim shoair - D4Vinci ( Cr3dOv3r )
import sys,os,random
from . import updater
from .websites import *

def getinput(text):
	# Return the suitable input type according to python version
	ver = sys.version[0]
	if ver=="3":
		return input(text)
	else:
		return raw_input(text)

def random_banner():
	#Choose a random banner and prints it
	version = updater.check()
	if "but" in version:
		version = version.split("but")[0]+R+"but"+version.split("but")[1]
	banners = open(os.path.join("Data","banners.txt")).read().split("$$$$$AnyShIt$$$$$$")
	banner  = random.choice(banners)
	banner_to_print  = G
	banner_to_print += banner.format(Name=B+"Cr3d0v3r By "+Bold+"@D4Vinci -"+M+" V"+version+G,
									Description=W+"Know the dangers of email credentials reuse attacks."+G,
									Loaded=B+"Loaded "+Y+str(len(all_websites))+B+" website."+G)
	banner_to_print += end
	print(banner_to_print)


#Colors
global G, Y, B, R, W , M , C , end ,Bold,GG
if os.name=="nt":
	try:
		import win_unicode_console , colorama
		win_unicode_console.enable()
		colorama.init()
		#green - yellow - blue - red - white - magenta - cyan - reset
		G,Y,B,R,W,M,C,end= '\033[92m','\033[93m','\033[94m','\033[91m','\x1b[37m','\x1b[35m','\x1b[36m','\x1b[39m'
		Bold = "\033[1m"
		GG   = "\x1b[32m"
	except:
		G = Y = B = R = W = G = Y = B = R = Bold = BB = ''
else:
	#import colorama
	#colorama.init()
	#green - yellow - blue - red - white - magenta - cyan - reset
	G,Y,B,R,W,M,C,end= '\033[92m','\033[93m','\033[94m','\033[91m','\x1b[37m','\x1b[35m','\x1b[36m','\x1b[39m'
	Bold = "\033[1m"
	GG   = "\x1b[32m"

web1 = list(websites.keys())
web1.sort()
web2 = list(custom_websites.keys())
web2.sort()
web3 = list(req_websites.keys())
web3.sort()
all_websites = web1+web2+web3
