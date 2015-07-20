# This will be the sql code for the database to track FV encryption keys that have been already used.

import sqlite3
import argparse
import random
import os.path
import string

# This is the function to generate the random FV key from Week 11 script
def fvde_key():
    chars = string.letters.upper() + string.digits
    pwdSize = 4
    key_attempt = ''.join((random.choice(chars)) for x in range(pwdSize))
    return key_attempt

# This function checks the generated key to see if we've seen it before
def check_key(key_select, db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("select * from tracking where enc_key = ( ? );", (key_select,))
    enc_key_exists = c.fetchone()
    if enc_key_exists:
        print "{} already tried...skipping...".format(key_select) # The key has been tried already move on
        return False
    else:
	print "Adding key {}...".format(key_select) # It's a new key, lets add it to the DB
        c.execute("insert into tracking values(NULL, ? );", (key_select,))
	conn.commit()
        return True

parser = argparse.ArgumentParser()
parser.add_argument('-d', dest='db_name', required=True, help='Name of database file to track keys')
args = parser.parse_args()

# This just checks if the db file in the command line exists or not
if os.path.isfile(args.db_name):
    print "{} exists...".format(args.db_name)
else:
    conn = sqlite3.connect(args.db_name)
    c = conn.cursor()
    c.execute("create table tracking(id int primary key, enc_key char(29));")
    
locked = True

# This is a variation of the week 11 script, it'll be update to incorporate the Week 11 code loop
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
