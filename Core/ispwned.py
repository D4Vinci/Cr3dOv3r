#Written by: Karim shoair - D4Vinci ( Cr3dOv3r )
import requests
#Will work on making this code cleaner as soon as I got time

def check_hackedEmails(email,return_what=""):
    #from hacked-emails API docs from https://hacked-emails.com/api_docs
    url = "https://hacked-emails.com/api?q="+str(email)
    req = requests.get(url)
    res = req.json()
    if res["status"]=="found":
        if return_what=="":
            return True
        else:
            return res
    else:
        return False

def check_haveibeenpwned(email,return_what=""):
    #from haveibeenpwnd API docs from https://haveibeenpwned.com/API/v2#BreachesForAccount
    url = "https://haveibeenpwned.com/api/v2/breachedaccount/"+str(email)
    req = requests.get(url)
    if req.status_code==200:
        if return_what=="":
            return True
        else:
            return req.json()
    else:
        #429 response means they blocked us
        return False

def parse_data(email,parse_what=0):
    #Colors is (green - yellow - blue - red - white - magenta - cyan)
    if parse_what==0:
        data         = check_hackedEmails(email,"His shit :D")
        Final_text   = "\n(GG)Results from hacked-emails website (W): (Y)"+str(data["results"])
        data         = data["data"]
    else:
        data         = check_haveibeenpwned(email,"His shit :D")
        Final_text   = "\n(GG)Results from haveibeenpwned website (W): (Y)"+str(len(data))

    General_form = "      (M)Name of leak (G)=> (B){web}"
    General_form+= "\n      (M)Date of leakage (G)=> (B){leakage_date}"

    if parse_what==0:
        General_form+= "\n      (M)Details (G)=> (B){details}"
    else:
        General_form+= "\n      (M)What leaked (G)=> (B){details}"
    dash         = "\n(Y)---------------------------------------(end)\n"

    keywords_1   = {"web":"title","leakage_date":"date_leaked","details":"details"}
    keywords_2   = {"web":"Name","leakage_date":"AddedDate","details":"DataClasses"}
    keys         = {0:keywords_1,1:keywords_2}[parse_what]
    for website in data:
        Final_text += dash
        Final_text += General_form.format(
            web=website[ keys["web"] ],
            leakage_date=website[ keys["leakage_date"] ],
            details=website[ keys["details"] ] if parse_what==0 else ",".join(website[ keys["details"] ]) )
    return Final_text+"\n"
