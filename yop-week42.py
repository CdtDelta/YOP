# This script is to add chain of custody entries to our overall database.
#
# TODO: Add link to existing evidence item in database
# TODO: Sanatize entries into database
#
# Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html

import sqlite3
import argparse
import os.path

def chain_of_custody(database):
    coc = sqlite3.connect(database)
    chain_custody = coc.cursor()
    event_date = raw_input("Enter the date of the event in the format MM-DD-YYYY: ")
    event_time = raw_input("Enter the time of the event in the 24 hour format HH:MM: ")
    who_started = raw_input("Enter the name of the individual handing over the item: ")
    who_ended = raw_input("Enter the name of the individual receiving the item: ")
    reason = raw_input("Enter the reason for the Chain of Custody change: ")
    chain_custody.execute("insert into custody values (NULL, ?, ?, ?, ?, ?);", (event_date, event_time,\
                                                                          who_started, who_ended, reason, ))
    coc.commit()
    return    

parser = argparse.ArgumentParser()
parser.add_argument('-d', dest='db_name', required=True, help='Name of database file to track chain of custody')
args = parser.parse_args()

if os.path.isfile(args.db_name):
    print "{} exists...".format(args.db_name)
else:
    coc = sqlite3.connect(args.db_name)
    chain_custody = coc.cursor()
    chain_custody.execute("create table custody(id int primary key, date text, time text, w_initiate text, w_received text, reason text);")

chain_of_custody(args.db_name)