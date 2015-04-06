# This script does a quick parse of the utmz cookies from a cookies.sqlite file
#
# By Tom Yarrish
# Version 1.0
#
# Usage: yop-week14.py -f <cookies.sqlite>


import argparse
import datetime
import sqlite3

def unixtime(timevalue):
    return datetime.datetime.utcfromtimestamp(int(timevalue))

parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="cookie_file", help="Cookie file to parse")
args = parser.parse_args()

cookies_db = args.cookie_file

try:
    db_connect = sqlite3.connect(cookies_db)
    db_cursor = db_connect.cursor()
    db_cursor.execute('SELECT * FROM moz_cookies WHERE name = "__utmz"')
    db_row = db_cursor.fetchall()
except Exception, error:
    print error

for rows in db_row:
    utmz = rows[5]
    utmz_segment = utmz.split(".")
    cookie_last_time = unixtime(utmz_segment[1])
    print "Domain: {}\t\t\tLast Visit: {}:{}:{}\t\tNo of sessions: {}".format(rows[1], cookie_last_time.hour,\
                                                                                cookie_last_time.minute,\
                                                                                cookie_last_time.second, utmz_segment[3])