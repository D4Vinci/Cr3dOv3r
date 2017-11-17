#Written by: Karim shoair - D4Vinci ( Cr3dOv3r )
import requests

def check(email,return_what=""):
    #Using the website API docs from https://hacked-emails.com/api_docs
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

def parse_data(email):
    #Colors is (green - yellow - blue - red - white - magenta - cyan)
    data         = check(email,"His shit :D")
    Final_text   = "\n(C)Results found (W): (Y)"+str(data["results"])
    General_form = "      (M)Name of leak (G)=> (B){web}"                    #title
    General_form+= "\n      (M)Date of leakage (G)=> (B){leakage_date}"   #date_leaked
    General_form+= "\n      (M)Details (G)=> (B){details}"              #details
    dash         = "\n(C)---------------------------------------(end)\n"
    for website in data["data"]:
        Final_text += dash
        Final_text += General_form.format(
            web=website["title"],
            leakage_date=website["date_leaked"],
            details=website["details"])
    return Final_text+"\n"
