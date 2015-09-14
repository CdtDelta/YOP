# This is the SOOPER APT generator!
#
# Which is just a silly idea I got from the following site
# http://cyberattribution.com/#!/Dice/c/12550174/inview=product48202965&offset=0&sort=normal
#
# Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html

import random

def country():
    country_attrib = ['Russia', 'China', 'North Korea', 'USA', 'Iraq', 'Iran', 'Israel']
    return random.choice(country_attrib)

def actor():
    actor_attrib = ['NSA', 'GCHQ', 'Unit 21', 'Unit 61398', 'Cyber Crime', 'Hacktivist', 'Anonymous', 'LulzSec']
    return random.choice(actor_attrib)

def vulnerability():
    vuln_attrib = ['0-Day', 'XSS', 'SQL Injection', 'Bad BIOS', 'Java', 'Adobe Flash']
    return random.choice(vuln_attrib)

def vector():
    vector_attrib = ['Malware', 'DDOS', 'Phishing', 'SSL MITM', 'Brute Force', 'Backdoor']
    return random.choice(vector_attrib)

print "Welcome to the APT Excuse generator!\nThis program will help you determine how you were CYBER attacked.\n"
raw_input("Press any key to continue...\n")

quit = False

while not quit:
    print "OMG!  You've been CYBER HACKED!  But not to worry, our advanced technology has determined everything!\n"
    print "We've determined it was {} working out of {}\n".format(actor(), country())
    print "They used a {} {} attack to get in.\n".format(vulnerability(), vector())
    choice = raw_input("Would you like to generate another attack? (Y/N)")
    if choice.lower() == "y":
        continue
    else:
        quit = True
