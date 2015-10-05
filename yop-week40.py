# This script is to add case notes to my overall case management program
# It simply adds a case note entry to the database with a date/time stamp
# and it hashes the entry.
#
# Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html

import sqlite3
import argparse
import os.path
from datetime import datetime
import hashlib

def casenote_entry(database):
    evdb = sqlite3.connect(database)
    cnote = evdb.cursor()
    timestamp = datetime.now()
    casenote = raw_input("Case Note Entry: ")
    casenote_hash = hashlib.sha256(casenote).hexdigest()
    cnote.execute("insert into casenotestbl values(NULL, ?, ?, ?);", (timestamp, casenote, casenote_hash))
    evdb.commit()
    return

parser = argparse.ArgumentParser()
parser.add_argument('-d', dest='casenotes_db', required=True, help='Name of case database file')
args = parser.parse_args()

if os.path.isfile(args.casenotes_db):
    print "{} exists...".format(args.casenotes_db)
else:
    evdb = sqlite3.connect(args.casenotes_db)
    cnote = evdb.cursor()
    print "Creating database file {}".format(args.casenotes_db)
    cnote.execute("create table casenotestbl(id int primary key, casenotes_date text, casenotes_text text, casenotes_hash text);")
    
casenote_entry(args.casenotes_db)