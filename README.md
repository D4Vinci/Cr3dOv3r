# Cr3dOv3r [![Python 3.5](https://img.shields.io/badge/Python-3.5-yellow.svg)](http://www.python.org/download/) ![Build Status](https://img.shields.io/badge/Version-0.1-red.svg)

**Your best friend in credential reuse attacks.**

Cr3dOv3r simply you give it an email then it does two simple jobs (but useful) :
- Search for public leaks for the email and if it any, it returns with all available details about the leak (Using hacked-emails site API).
- Now you give it this email's old or leaked password then it checks this credentials against 16 websites (ex: facebook, twitter, google...) then it tells you if login successful in any website!

### Imagine with me this scenario
- You checking a targeted email with this tool.
- The tool finds it in a leak so you open the leakage link.
- You get the leaked password after searching the leak.
- Now you back to the tool and enters this password to check if there's any website the user uses the same password in it.
- You imagine the rest :smile:

# Screenshots
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

```

## Installing and requirements
### To make the tool work at its best you must have :
- Python 3.x.
- Linux or windows system.
- The requirements mentioned in the next few lines.

### Installing
**+For windows : (After downloading ZIP and upzip it)**
```
cd Cr3dOv3r-master
python -m pip install -r win_requirements.txt
python Cr3dOv3r.py -h
```
**+For linux :**
```
git clone https://github.com/D4Vinci/Cr3dOv3r.git
chmod 777 -R Cr3dOv3r-master
cd Cr3dOv3r-master
pip3 install -r requirements.txt
python Cr3dOv3r.py -h
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
