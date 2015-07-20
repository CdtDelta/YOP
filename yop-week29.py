# This will be the sql code for the database to track FV encryption keys that have been already used.

import sqlite3
import argparse
import random
import os.path
import string

def fvde_key():
    chars = string.letters.upper() + string.digits
    pwdSize = 4
    key_attempt = ''.join((random.choice(chars)) for x in range(pwdSize))
    return key_attempt

def check_key(key_select, db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("select * from tracking where enc_key = ( ? );", (key_select,))
    enc_key_exists = c.fetchone()
    if enc_key_exists:
        print "{} already tried...skipping...".format(key_select)
        return False
    else:
	print "Adding key {}...".format(key_select)
        c.execute("insert into tracking values(NULL, ? );", (key_select,))
	conn.commit()
        return True

parser = argparse.ArgumentParser()
parser.add_argument('-d', dest='db_name', required=True, help='Name of database file to track keys')
args = parser.parse_args()

if os.path.isfile(args.db_name):
    print "{} exists...".format(args.db_name)
else:
    conn = sqlite3.connect(args.db_name)
    c = conn.cursor()
    c.execute("create table tracking(id int primary key, enc_key char(29));")
    
locked = True

while locked == True:
    decryption_key = "-".join([fvde_key(),fvde_key(),fvde_key(),fvde_key(),fvde_key(),fvde_key()])
    print "Checking decryption key {}...".format(decryption_key)
    already_used_key = check_key(decryption_key, args.db_name)
    if already_used_key:
        print "Haven't seen {}...".format(decryption_key)
        continue
    else:
        print "Ok we're done..."
        locked == False
        break
