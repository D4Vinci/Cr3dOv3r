#Written by: Karim shoair - D4Vinci ( Cr3dOv3r )
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,argparse,time,random,requests
import mechanicalsoup as ms
from getpass import getpass
from websites import *
import ispwned,updater

#Colors
global G, Y, B, R, W , M , C , end ,Bold
if os.name=="nt":
	try:
		import win_unicode_console , colorama
		win_unicode_console.enable()
		colorama.init()
		#green - yellow - blue - red - white - magenta - cyan - reset
		G,Y,B,R,W,M,C,end= '\033[92m','\033[93m','\033[94m','\033[91m','\033[0m','\x1b[35m','\x1b[36m','\x1b[39m'
		Bold = "\033[1m"
	except:
		G = Y = B = R = W = G = Y = B = R = Bold = ''
else:
	#import colorama
	#colorama.init()
	#green - yellow - blue - red - white - magenta - cyan - reset
	G,Y,B,R,W,M,C,end= '\033[92m','\033[93m','\033[94m','\033[91m','\033[0m','\x1b[35m','\x1b[36m','\x1b[39m'
	Bold = "\033[1m"

parser = argparse.ArgumentParser(prog='Cr3d0v3r.py')
parser.add_argument("email", help="Email/username to check")
args    = parser.parse_args()
email   = args.email
version = updater.check()
if "but" in version:
	version = version.split("but")[0]+R+"but"+version.split("but")[1]

#with mechanicalsoup
def login( name ,dic ,email ,pwd ):
	url ,form,e_form ,p_form = dic["url"] ,dic["form"],dic["e_form"] ,dic["p_form"]
	browser = ms.StatefulBrowser(user_agent=random.choice(["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
	"Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.6.30 Version/10.61",
	"Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/0.8.12",
	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:14.0) Gecko/20100101 Firefox/14.0.1",
	"Mozilla/5.0 (X11; Linux) KHTML/4.9.1 (like Gecko) Konqueror/4.9"])
	)
	try:
		browser.open(url)
	except:
		return "{2} -[{1}{3} {0} {4}{2}] Couldn't even open the page! Do you have internet !?{4}".format(name,R,W,Bold,end)

	try:
		browser.select_form(form)
		browser[e_form] = email
		browser[p_form] = pwd
		browser.submit_selected()
	except ms.utils.LinkNotFoundError:
		return "{2} -[{1}{3} {0} {4}{2}] Something wrong with the website maybe it's blocked!{4}".format(name,R,W,Bold,end)

	#Now let's check if it was success by trying to use the same form again and if I could use it then the login not success
	try:
		browser.select_form(form)
		browser.close()
		return "{2} -[{1}{3} {0} {4}{2}] Login unsuccessful!{4}".format(name,R,W,Bold,end)
	except ms.utils.LinkNotFoundError:
		browser.close()
		return "{2} -[{1}{3} {0} {4}{2}] Login successful !{4}".format(name,G,W,Bold,end)

#websites that use two forms to login
def custom_login( name ,dic ,email ,pwd ):
	url ,form1,form2,e_form ,p_form = dic["url"] ,dic["form1"],dic["form2"],dic["e_form"] ,dic["p_form"]
	browser = ms.StatefulBrowser(user_agent=random.choice(["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
	"Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.6.30 Version/10.61",
	"Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/0.8.12",
	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:14.0) Gecko/20100101 Firefox/14.0.1",
	"Mozilla/5.0 (X11; Linux) KHTML/4.9.1 (like Gecko) Konqueror/4.9"]))
	try:
		browser.open(url)
	except:
		return "{2} -[{1}{3} {0} {4}{2}] Couldn't even open the page! Do you have internet !?{4}".format(name,R,W,Bold,end)

	try:
		browser.select_form(form1)
		browser[e_form] = email
	except ms.utils.LinkNotFoundError:
		return "{2} -[{1}{3} {0} {4}{2}] Something wrong with the website maybe it's blocked!{4}".format(name,R,W,Bold,end)

	try:
		browser.submit_selected()
		browser.select_form(form2)
		browser[p_form] = pwd
		browser.submit_selected()
	except ms.utils.LinkNotFoundError:
		browser.close()
		return "{2} -[{1}{3} {0} {4}{2}] Email not registered!{4}".format(name,R,W,Bold,end)
	#Now let's check if it was success by trying to use the same form again and if I could use it then the login not success
	try:
		browser.select_form(form2)
		browser.close()
		return "{2} -[{1}{3} {0} {4}{2}] Login unsuccessful!{4}".format(name,R,W,Bold,end)
	except:
		browser.close()
		return "{2} -[{1}{3} {0} {4}{2}] Login successful !{4}".format(name,G,W,Bold,end)
	#That's a lot of exceptions :"D

#Login to websites with post requests
def req_login( name ,dic ,email ,pwd ):
	url ,verfiy,e_form ,p_form = dic["url"] ,dic["verfiy"],dic["e_form"] ,dic["p_form"]
	data  = {e_form:email,p_form:pwd}
	req = requests.post(url,data=data).text
	#Now let's check if it was success by trying to find the verfiy words and if I could find them then login not successful
	for word in verfiy:
		if word in req:
			return "{2} -[{1}{3} {0} {4}{2}] Login unsuccessful!{4}".format(name,R,W,Bold,end)

	return "{2} -[{1}{3} {0} {4}{2}] Login successful !{4}".format(name,G,W,Bold,end)

web1 = list(websites.keys())
web1.sort()
web2 = list(custom_websites.keys())
web2.sort()
web3 = list(req_websites.keys())
web3.sort()
all_websites = web1+web2+web3

def random_banner():
	banners = open(os.path.join("Data","banners.txt")).read().split("$$$$$AnyShIt$$$$$$")
	banner  = random.choice(banners)
	banner_to_print  = G
	banner_to_print += banner.format(Name=B+"Cr3d0v3r By "+Bold+"@D4Vinci -"+M+" V"+version+G,
									Description=C+"Know the dangers of email credentials reuse attacks."+G,
									Loaded=B+"Loaded "+Y+str(len(all_websites))+B+" website."+G)
	banner_to_print += end
	print(banner_to_print)

def main():
	random_banner()
	print("\n"+W+"["+G+"+"+W+"]"+B+" Checking email in public leaks...")
	if ispwned.check(email):
		to_print = ispwned.parse_data(email)
		colors   = {"(C)":C,"(W)":W,"(B)":B,"(Y)":Y,"(G)":G,"(R)":R,"(M)":M,"(end)":end}
		for color in list(colors.keys()):
			to_print = to_print.replace(color,colors[color])
		print(to_print)
	else:
		print(C+"[!] "+R+"Email not found in any public leaks!\n")
	pwd   = getpass(C+"Please enter the password"+W+"=> ")

	print("\n"+W+"["+G+"+"+W+"]"+B+" Testing websites with one form (" + str(len(web1)) + ")!")
	for wd in web1:
		dic = websites[wd]
		print( login( wd ,dic ,email ,pwd ) )

	print("\n"+W+"["+G+"+"+W+"]"+B+" Testing websites with two forms (" + str(len(web2)) + ")!")
	for wd in web2:
		dic = custom_websites[wd]
		print( custom_login( wd ,dic ,email ,pwd ) )

	print("\n"+W+"["+G+"+"+W+"]"+B+" Testing websites with post requests (" + str(len(web3)) + ")!")
	for wd in web3:
		dic = req_websites[wd]
		print( req_login( wd ,dic ,email ,pwd ) )

if __name__ == '__main__':
	main()
