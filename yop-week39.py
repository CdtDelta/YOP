# This script is to start the set up of a new case file.
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
from datetime import date

def casenumber(counter):
    today_date = date.today()
    case_num = str(today_date.year)+str(today_date.month)+str(today_date.day)+str(counter)
    return case_num

def new_case(casenumber, database):
    evdb = sqlite3.connect(database)
    evidence = evdb.cursor()
    print "Creating case number {}...".format(casenumber)
    case_owner = raw_input("Enter the employee assigned to the case: ")
    case_desc = raw_input("Enter a short description of the case: ")
    evidence.execute("insert into casetbl values(NULL, ?, ?, ?);", (casenumber, case_desc, case_owner))
    evdb.commit()
    return

parser = argparse.ArgumentParser()
parser.add_argument('-d', dest='case_db', required=True, help='Name of case database file')
args = parser.parse_args()
counter = 1

if os.path.isfile(args.case_db):
    print "{} exists...".format(args.case_db)
else:
    evdb = sqlite3.connect(args.case_db)
    evidence = evdb.cursor()
    print "Creating database file {}".format(args.case_db)
    evidence.execute("create table casetbl(id int primary key, case_no int, case_desc text, case_owner text);")

print "Welcome to the case management system."
print "Choose one of the following options:\n"
print "1) Create a new case."
print "2) Open an existing case."
case_choice = raw_input("Enter choice (1 or 2):")

if case_choice == "1":
    new_case_num = casenumber(counter)
    new_case(new_case_num, args.case_db)
    counter += 1
elif case_choice == "2":
    old_case_num = raw_input("Enter the case number: ")
    print "Opening case number {}".format(old_case_num)
    evidence.execute("select * from casetbl where case_no = (?);", (old_case_num,))
else:
    print "Invalid case number, exiting..."