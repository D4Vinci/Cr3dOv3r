#Written by: Karim shoair - D4Vinci ( Cr3dOv3r )
# -*- coding: utf-8 -*-
import os,argparse,time,random,requests,getpass
import mechanicalsoup as ms
from Core import ispwned
from Core.utils import *

parser = argparse.ArgumentParser(prog='Cr3d0v3r.py')
parser.add_argument("email", help="Email/username to check")
parser.add_argument("-p",action="store_true", help="Use it if you only wants to check a password")
parser.add_argument("-api2",action="store_true", help="Use haveibeenpwned API too") #To avoid blocking
parser.add_argument("-q",action="store_true", help="Quit mode (no banner)")
args    = parser.parse_args()
email   = args.email

#with mechanicalsoup
def login( name ,dic ,email ,pwd ):
	url ,form,e_form ,p_form = dic["url"] ,dic["form"],dic["e_form"] ,dic["p_form"]
	browser = ms.StatefulBrowser(user_agent=random.choice(["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
	"Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.6.30 Version/10.61",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"])
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
	time.sleep(2)
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
	browser = ms.StatefulBrowser(user_agent=random.choice(["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
	"Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.6.30 Version/10.61",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"]))
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
	time.sleep(2)
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
	url ,verify,e_form ,p_form = dic["url"] ,dic["verify"],dic["e_form"] ,dic["p_form"]
	data  = {e_form:email,p_form:pwd}
	req = requests.post(url,data=data).text
	#Now let's check if it was success by trying to find the verify words and if I could find them then login not successful
	for word in verify:
		if word in req:
			return "{2} -[{1}{3} {0} {4}{2}] Login unsuccessful!{4}".format(name,R,W,Bold,end)

	return "{2} -[{1}{3} {0} {4}{2}] Login successful !{4}".format(name,G,W,Bold,end)

def main():
	if not args.q:
		random_banner()
	if not args.p:
		print("\n"+W+"["+G+"+"+W+"]"+B+" Checking email in public leaks...")
		if ispwned.check_hackedEmails(email):
			to_print = ispwned.parse_data(email)
			colors   = {"(C)":C,"(W)":W,"(B)":B,"(Y)":Y,"(G)":G,"(R)":R,"(M)":M,"(end)":end,"(GG)":GG}
			for color in list(colors.keys()):
				to_print = to_print.replace(color,colors[color])
			print(to_print)
		else:
			print(C+"[!] "+R+"Email not found in hacked-emails leaks!")

		if args.api2:
                        ans = ispwned.check_haveibeenpwned(email, 'His shit :D') 
                        if ans: 
                                to_print = ispwned.parse_data(email, 1, existing_data=ans)
                                colors   = {"(C)":C,"(W)":W,"(B)":B,"(Y)":Y,"(G)":G,"(R)":R,"(M)":M,"(end)":end}
                                for color in list(colors.keys()):
                                        to_print = to_print.replace(color,colors[color])
                                print(to_print)
                        else:
                                print(C+"[!] "+R+"Email not found in haveibeenpwned leaks!\n")

	if os.name=="nt":
		pwd   = getinput(GG+"Please enter the password "+W+"=> ") #to escape the echo warning,sorry windows users (¯\_(ツ)_/¯)
	else:
		pwd   = getpass.getpass(GG+"Please enter the password "+W+"=> ")

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
