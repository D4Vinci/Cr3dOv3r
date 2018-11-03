# Cr3dOv3r [![Python 3.5](https://img.shields.io/badge/Python-3.5-yellow.svg)](http://www.python.org/download/) [![Python 2.7](https://img.shields.io/badge/Python-2.7-yellow.svg)](http://www.python.org/download/) ![Build Status](https://img.shields.io/badge/Version-0.4.4-red.svg)

**Your best friend in credential reuse attacks.**

You give Cr3dOv3r an email then it does two simple useful jobs with it:
- Search for public leaks for the email and returns the result with the most useful details about the leak (Using haveibeenpwned API) and tries to get the plain text passwords from leaks it find (Using [@GhostProjectME](https://twitter.com/GhostProjectME)).
- Now you give it a password or a leaked password then it tries this credentials against some well-known websites (ex: Facebook, Twitter, Google...), tells if the login successful and if there's captcha some where blocking our way!

### Some of the scenarios Cr3dOv3r can be used in it
- Check if the targeted email is in any leaks and then use the leaked password to check it against the websites.
- Check if the target credentials you found is reused on other websites/services.
- Checking if the old password you got from the target/leaks is still used in any website.

# Screenshots
![screenshot](https://github.com/D4Vinci/Cr3dOv3r/blob/master/Data/Email1.png)
![screenshot](https://github.com/D4Vinci/Cr3dOv3r/blob/master/Data/Email2.png)
![screenshot](https://github.com/D4Vinci/Cr3dOv3r/blob/master/Data/Email3.png)

# Usage
```
usage: Cr3d0v3r.py [-h] [-p] [-np] [-q] email

positional arguments:
  email       Email/username to check

optional arguments:
  -h, --help  show this help message and exit
  -p          Don't check for leaks or plain text passwords.
  -np         Don't check for plain text passwords.
  -q          Quiet mode (no banner).

```

## Installing and requirements
### To make the tool work at its best you must have :
- Python 3.x or 2.x (preferred 3).
- Linux or Windows system.
- Worked on some machines with MacOS and python3.
- The requirements mentioned in the next few lines.

### Installing
**+For windows : (After downloading ZIP and upzip it)**
```
cd Cr3dOv3r-master
python -m pip install -r win_requirements.txt
python Cr3d0v3r.py -h
```
**+For Linux :**
```
git clone https://github.com/D4Vinci/Cr3dOv3r.git
cd Cr3dOv3r
python3 -m pip install -r requirements.txt
python3 Cr3d0v3r.py -h
```

**+For docker :**
```bash
git clone https://github.com/D4Vinci/Cr3dOv3r.git
docker build -t cr3dov3r Cr3dOv3r/
docker run -it cr3dov3r "test@example.com"
```


**If you want to add a website to the tool, follow the instructions in the [wiki](https://github.com/D4Vinci/Cr3dOv3r/wiki)**

## Contact
- [Twitter](https://twitter.com/D4Vinci1)

## Donation
If this tool has been useful for you, feel free to thank me by buying me a coffee :)

[![Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/d4vinci)

## Disclaimer
Cr3dOv3r is created to show how could credential reuse attacks get dangerous and it's not responsible for misuse or illegal purposes. Use it only for Pen-test or educational purpose !!!

Copying a code from this tool or using it in another tool is accepted as you mention where you get it from :smile:

> Pull requests are always welcomed :D
