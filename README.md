# Cr3dOv3r [![Python 3.5](https://img.shields.io/badge/Python-3.5-yellow.svg)](http://www.python.org/download/) [![Python 2.7](https://img.shields.io/badge/Python-2.7-yellow.svg)](http://www.python.org/download/) ![Build Status](https://img.shields.io/badge/Version-0.3.2-red.svg)

**Your best friend in credential reuse attacks.**

Cr3dOv3r simply you give it an email then it does two simple jobs (but useful) :
- Search for public leaks for the email and if there's any, it returns with all available details about the leak (Using hacked-emails site API and now haveibeenpwned API too).
- Now you give it this email's old or leaked password then it checks this credentials against 13 websites of well-known websites (ex: facebook, twitter, google...) then it tells you if login successful in any website!

### Some of the scenarios Cr3dOv3r can be used in it
- Searching for a targeted-email for leaks and then use the leaked password to check it against the websites.
- Testing an email and an old password you found on the websites.
- You got a target email and password and want to check if he uses the same password on other websites.

# Screenshots (Not updated)
![screenshot](https://github.com/D4Vinci/Cr3dOv3r/blob/master/Data/Email1-p1.png)
![screenshot](https://github.com/D4Vinci/Cr3dOv3r/blob/master/Data/Email1-p2.png)
![screenshot](https://github.com/D4Vinci/Cr3dOv3r/blob/master/Data/Email2.png)

# Usage
```
usage: Cr3d0v3r.py [-h] email

positional arguments:
  email       Email/username to check

optional arguments:
  -h, --help  show this help message and exit
  -p          Use it if you only wants to check a password
  -api2       Use haveibeenpwned API too
  -q          Quit mode (no banner)

```

## Installing and requirements
### To make the tool work at its best you must have :
- Python 3.x or 2.x (preferred 3).
- Linux or Windows system.
- Worked on some machines with MacOS and python3 (Thanks for @MansoorMajeed and needs to others to confirm that)
- The requirements mentioned in the next few lines.

### Installing
**+For windows : (After downloading ZIP and upzip it)**
```
cd Cr3dOv3r-master
python -m pip install -r win_requirements.txt
python Cr3dOv3r.py -h
```
**+For Linux :**
```
git clone https://github.com/D4Vinci/Cr3dOv3r.git
chmod 777 -R Cr3dOv3r
cd Cr3dOv3r
pip3 install -r requirements.txt
python3 Cr3dOv3r.py -h
```

**+For docker :**
```bash
git clone https://github.com/D4Vinci/Cr3dOv3r.git
docker build -t cr3dov3r Cr3dOv3r/
docker run -it cr3dov3r "example@gmail.com"
```


**If you want to add a website to the tool, follow the instructions in the [wiki](https://github.com/D4Vinci/Cr3dOv3r/wiki)**

## Contact
- [Twitter](https://twitter.com/D4Vinci1)

## Donation
If you liked my work and want to support me, you can give me a cup of coffee :)

<img src="https://github.com/D4Vinci/Dr0p1t-Framework/blob/master/donate.png"></img>

bitcoin address: 1f4KfYikfqHQzEAsAGxjq46GdrBKc8jrG

## Disclaimer
Cr3dOv3r is created to show how could credential reuse attacks get dangerous and it's not responsible for misuse or illegal purposes. Use it only for Pentest or educational purpose !!!

Copying a code from this tool or using it in another tool is accepted as you mention where you get it from :smile:

> Pull requests are always welcomed :D
