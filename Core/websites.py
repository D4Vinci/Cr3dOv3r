# -*- encoding: utf-8 -*-
#Written by: Karim shoair - D4Vinci ( Cr3dOv3r )
#Instead of creating many config/text files and parse them I think this better because I'm lazy and it's easier to add new website :D .
#See how to add a website in the repo wiki

#Normal websites (That use one form)
#Facbook data
facebook = { "url":"https://en-gb.facebook.com/login.php" ,
	"form":"#login_form",
	"e_form":"email" ,
	"p_form":"pass" }

#Twitter data
twitter = { "url":"https://mobile.twitter.com/sessions" ,
	"form":'form[action="/sessions"]',
	"e_form":"session[username_or_email]",
	"p_form":"session[password]"}

#Ask.fm data
ask = { "url":"https://ask.fm/login" ,
	"form":'form[action="/login"]',
	"e_form":"login" ,
	"p_form":"password" }

#linkedin
#the reason for LinkedIn false positives :3 it's because of captcha appears from the second attempt!
# let's solve that
linkedin = { "url":"https://www.linkedin.com/uas/login" ,
	"form":'#login',
	"e_form":"session_key" ,
	"p_form":"session_password" }

#Github
github = { "url":"https://github.com/login" ,
	"form":'form[action="/session"]',
	"e_form":"login" ,
	"p_form":"password" }

'''#Needs to enable JS ? Okay I do that later with dryscrape maybe
#Protonmail
protonmail = { "url":"https://mail.protonmail.com/login" ,
	"form":'form[action="login"]',
	"e_form":"username" ,
	"p_form":"password" }
'''

#VirusTotal
virustotal = { "url":"https://www.virustotal.com/en/account/signin/",
	"form":'form[id="frm-signin"]',
	"e_form":"username" ,
	"p_form":"password" }

#Ebay
ebay = { "url":"https://signin.ebay.com/ws/eBayISAPI.dll" ,
	"form":'#SignInForm',
	"e_form":"userid" ,
	"p_form":"pass" }

#Wikipedia
wikipedia = { "url":"https://en.wikipedia.org/w/index.php?title=Special:UserLogin" ,
	"form":'form[action="/wiki/Special:UserLogin"]',
	"e_form":"wpName" ,
	"p_form":"wpPassword" }

#StackOverFlow
stackoverflow = { "url":"https://stackoverflow.com/users/login" ,
	"form":'form[id="login-form"]',
	"e_form":"email" ,
	"p_form":"password" }

#FourSquare
foursquare = { "url":"https://foursquare.com/login" ,
	"form":'form[id="loginToFoursquare"]',
	"e_form":"emailOrPhone" ,
	"p_form":"password" }

#Gitlab
gitlab = { "url":"https://gitlab.com/users/sign_in" ,
	"form":'form[action="/users/sign_in"]',
	"e_form":"user[login]" ,
	"p_form":"user[password]" }

#Airdroid
air = { "url":"https://www.airdroid.com/en/signin/",
	"form":'form[id="form_sign"]',
	"e_form":"email" ,
	"p_form":"password" }

#---------------------------------------------------
#Websites that uses two forms
#Gmail
google = { "url":"https://accounts.google.com/signin" ,
	"form1":'form[id="gaia_loginform"]',
	"form2":'form[id="gaia_loginform"]',
	"e_form":"Email",
	"p_form":"Passwd"}

#Yahoo
yahoo = { "url":"https://login.yahoo.com" ,
	"form1":'form[id="login-username-form"]',
	"form2":'form[class="pure-form pure-form-stacked"]',
	"e_form":"username",
	"p_form":"password"}

#--------------------------------------
#Websites login with post requests
#MediaFire
mediafire = { "url":"https://www.mediafire.com/dynamic/client_login/mediafire.php" ,
	"e_form":"login_email" ,
	"p_form":"login_pass",
	"verify":["login"]#After submitting if this words exist in the response page then login not successful
	 }

##############################
#### Organizing websites #####
##############################
websites  = {" Facebook":facebook,
			 " Twitter ":twitter,
			 " Ask.fm  ":ask,
			 " Github  ":github,
			 "Virustotal":virustotal,
			 "LinkedIn ":linkedin,
             " Ebay.com":ebay,
             "Wikipedia":wikipedia,
			 " Airdroid":air,
             " StackOF ":stackoverflow,
             "FourSquare":foursquare,
             " Gitlab  ":gitlab
			 }

custom_websites = {" Google  ":google,
				   " Yahoo   ":yahoo
				   }

req_websites = { "Mediafire":mediafire
}
