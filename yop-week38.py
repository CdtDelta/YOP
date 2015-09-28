# This script is to just add evidence to a sqlite database for storage.
# This is a small part of a planned larger program.
#
# Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html

import sqlite3
import argparse
import os.path

def add_evidence(database):
    evdb = sqlite3.connect(database)
    evidence = evdb.cursor()
    evidence_type = raw_input("Enter the evidence type (Hard Drive, Mobile, etc): ")
    evidence_manuf = raw_input("Enter the manufacturer: ")
    evidence_model = raw_input("Enter the model number: ")
    evidence_serial = raw_input("Enter the serial number: ")
    evidence.execute("insert into evidence values (NULL, ?, ?, ?, ? );", (evidence_type, evidence_manuf,\
                                                                          evidence_model, evidence_serial, ))
    evdb.commit()
    return

parser = argparse.ArgumentParser()
parser.add_argument('-d', dest='db_name', required=True, help='Name of database file to track evidence')
args = parser.parse_args()

keep_running = True

if os.path.isfile(args.db_name):
    print "{} exists...".format(args.db_name)
else:
    evdb = sqlite3.connect(args.db_name)
    evidence = evdb.cursor()
    evidence.execute("create table evidence(id int primary key, ev_type text, ev_manuf text, ev_model text, ev_serial text);")

while keep_running:
    evidence_add = raw_input("Would you like to enter an evidence item? ")
    if evidence_add.lower() == "y":
        add_evidence(args.db_name)
    else:
        print "All evidence added, program exiting."
        keep_running = False
