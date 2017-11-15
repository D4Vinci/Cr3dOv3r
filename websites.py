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
linkedin = { "url":"https://www.linkedin.com/uas/login" ,
	"form":'#login',
	"e_form":"session_key" ,
	"p_form":"session_password" }

#Github
github = { "url":"https://github.com/login" ,
	"form":'form[action="/session"]',
	"e_form":"login" ,
	"p_form":"password" }

'''#Needs to enable JS ? Okay I will mother fucker :D
#Protonmail
protonmail = { "url":"https://mail.protonmail.com/login" ,
	"form":'form[action="login"]',
	"e_form":"username" ,
	"p_form":"password" }
'''

'''#Need to work on
#Udemy
udemy = { "url":"https://www.udemy.com/join/login-popup" ,
	"form":'form[action="https://www.udemy.com/join/login-popup"]',
	"e_form":"email" ,
	"p_form":"password" }
'''

#MediaFire
mediafire = { "url":"https://www.mediafire.com/login" ,
	"form":'form[action="/dynamic/client_login/mediafire.php"]',
	"e_form":"login_email" ,
	"p_form":"login_pass" }

#Dropbox
dropbox = { "url":"https://www.dropbox.com" ,
	"form":'form[action="/ajax_login"]',
	"e_form":"login_email" ,
	"p_form":"login_password" }

'''#Need to work on
#Amazon
amazon = { "url":"https://www.amazon.com/ap/signin?openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_ya_signin&switch_account=" ,
	"form":'form[action="https://www.amazon.com/ap/signin"]',
	"e_form":"email" ,
	"p_form":"password" }
'''

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

#Bitbucket
bitbucket = { "url":"https://bitbucket.org/account/signin" ,
	"form":'form[action=""]',
	"e_form":"username" ,
	"p_form":"password" }

#Vimeo
vimeo = { "url":"https://vimeo.com/log_in" ,
	"form":'form[id="login_form"]',
	"e_form":"email" ,
	"p_form":"password" }

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

#Reddit
reddit = { "url":"https://www.reddit.com/login" ,
	"form":'form[action="https://www.reddit.com/post/login"]',
	"e_form":"user" ,
	"p_form":"passwd" }

#Hotmail
	#No it won't work it's .srf !! How stupid I am !!
hotmail = { "url":"https://login.live.com/login.srf" ,"form":'#f1',"e_form":"loginfmt","p_form":"passwd"}

# vk
vk = { "url":"https://vk.com/login" ,
      "form":'form[action="https://login.vk.com/?act=login"]' ,
      "e_form":"email" ,
      "p_form":"pass"
    }

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

##############################
#### Organizing websites #####
##############################
websites  = {"Facebook ":facebook,
			 " Twitter ":twitter,
			 " Ask.fm  ":ask,
			 "Linkedin ":linkedin,
			 " Github  ":github,
             #"Protonmail":protonmail,
             #"  Udemy ":udemy,
             "Mediafire":mediafire,
             " Dropbox ":dropbox,
             #" Amazon ":amazon,
             "Ebay.com ":ebay,
             "Wikipedia":wikipedia,
             "Bitbucket":bitbucket,
             "  Vimeo  ":vimeo,
             " StackOF ":stackoverflow,
             "FourSquare":foursquare,
             " Reddit  ":reddit,
             " VK ":vk
			 }

custom_websites = {"Google":google,
				   "Yahoo ":yahoo
				   }
