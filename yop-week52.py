# This is a simple search program I made to help search through
# the string output from memory images.
#
# You need to run strings against the memory image, and then
# this script searches through that output
#
# by Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html

import re
import os.path
import argparse
import sys
import fileinput

def mem_string_search(search_term, memory_file):
    for line in fileinput.input(memory_file):
        if re.search(search_term, line, re.I):
            print line
        else:
            continue
    return

parser = argparse.ArgumentParser()
parser.add_argument('-f', dest = 'file_name', help = 'File to search')
args = parser.parse_args()

if os.path.isfile(args.file_name):
    print "{} exists...".format(args.file_name)
else:
    print "{} cannot be found, check the path and try again.".format(args.file_name)
    exit
    
print "This program will let you search through a memory image."
print "Make sure you are pointing this against the string output from the image.\n"
search_term = raw_input("Enter the search string: ")
mem_string_search(search_term, args.file_name)