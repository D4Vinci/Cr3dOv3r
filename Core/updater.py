# -*- encoding: utf-8 -*-
#Written by: Karim shoair - D4Vinci ( Cr3dOv3r )
import os,sys
from .color import *
if sys.version_info[0]==3:
	from urllib.request import urlopen
elif sys.version_info[0]==2:
	from urllib import urlopen

def check():
	f = open( os.path.join("Data","version.txt"), 'r')
	file_data = f.read().strip()
	try:
		version = urlopen('https://raw.githubusercontent.com/D4Vinci/Cr3dOv3r/master/Data/version.txt').read().decode('utf-8').strip()
	except:
		error("Can't reach Internet !!!")
		sys.exit(0)

	if version=="1.0":
		return R+Bold+"This is very old version stop using it ! Cr3dOv3r became framework now, pull it! :D"
	elif version != file_data:
		return file_data+R+" but new version is available!"
	else:
		return file_data
