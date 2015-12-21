# This script is designed to search through the Windows DNS DB
# I created with Week 50 and search either the Remote IP field
# or the Question Name
#
# by Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html

import argparse
import csv
import re
import sqlite3
import os.path
import sys

def sql_search_ip(search_term, sql_db):
    db_connect = sqlite3.connect(sql_db)
    dns_db = db_connect.cursor()
    dns_db.execute("SELECT * FROM dns_record WHERE dns_ip = ?", (search_term,))
    for row in dns_db:
        print row
    return

def sql_search_dns(search_term, sql_db):
    db_connect = sqlite3.connect(sql_db)
    dns_db = db_connect.cursor()
    dns_db.execute("SELECT * FROM dns_record WHERE dns_ques_n = ?", (search_term,))
    for row in dns_db:
        print row
    return

parser = argparse.ArgumentParser()
parser.add_argument('-s', dest = 'sql_file', help = 'DNS DB File')
args = parser.parse_args()

if os.path.isfile(args.sql_file):
    print "{} exists...".format(args.sql_file)
else:
    print "Unable to file Database file {}.\n".format(args.sql_file)
    sys.exit()

db_connect = sqlite3.connect(args.sql_file)
dns_db = db_connect.cursor()

print "What do you want to search for?\n"
print "For IP address, enter IP,\n"
print "For DNS name, enter DNS.\n"
sql_selection = raw_input("Enter your choice: ")

if sql_selection.lower() == "ip":
    sql_ip_term = raw_input("Enter the IP to search for in the following format (xxx.xxx.xxx.xxx): ")
    sql_search_ip(sql_ip_term, args.sql_file)
elif sql_selection.lower() == "dns":
    sql_dns_term = raw_input("Enter the DNS name to search for in the following format (www.yahoo.com.): ")
    sql_search_dns(sql_dns_term, args.sql_file)
else:
    print "That isn't a valid option"
