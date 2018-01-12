#Written by: Karim shoair - D4Vinci ( Cr3dOv3r )
import os,sys
if sys.version_info[0]==3:
	from urllib.request import urlopen
elif sys.version_info[0]==2:
	from urllib import urlopen

def check():
	f = open( os.path.join("Data","version.txt"), 'r')
	file_data = f.read().strip()
	try:
		response = urlopen('https://raw.githubusercontent.com/D4Vinci/Cr3dOv3r/master/Data/version.txt')
	except:
		return file_data
	version = response.read().decode('utf-8').strip()
	if version != file_data:
		return file_data+" but new version is available!"
	else:
		return file_data
