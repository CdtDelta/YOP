# This script continues on parsing out the Norton NPE
# log format.
# This time I'm parsing out a File Entry under the
# Suspicious Items section.
#
# by Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html

from bs4 import BeautifulSoup
import itertools
import argparse

# Usual stuff to get the file we want to parse
parser = argparse.ArgumentParser()
parser.add_argument('-f', dest = 'xml_file', help = 'NPE Log File to parse')
args = parser.parse_args()

soup = BeautifulSoup(open(args.xml_file))

file_info = {}

# Because of the structure of the File entries under the section
# we have to do a for loop in a for loop.
for suspect in soup.find_all('suspicious_items'):
    for suspect_files in suspect.find_all('files'):
        try:
            file_sub_info = {
                'file_path' : suspect_files.path.text,
                'file_version' : suspect_files.fileversion.text,
                'product_version' : suspect_files.productversion.text,
                'company' : suspect_files.company.text,
                'md5' : suspect_files.md5.text,
                'sha256' : suspect_files.sha256.text,
                'file_size' : suspect_files.filesize.text,
                'file_name' : suspect_files.filename.text,
                'file_age' : suspect_files.age.text,
                'norton_rating' : suspect_files.nortonrating.text,
                'file_prev' : suspect_files.prevalence.text
            }
        except:
            continue
        file_info.update(file_sub_info)

# Now we just print out the information we're concerned with        
print "File Information\n"
print "File Name: {}".format(file_info['file_name'])
print "File Path: {}".format(file_info['file_path'])
print "File Size: {}".format(file_info['file_size'])
print "File Version: {}".format(file_info['file_version'])
print "MD5: {}".format(file_info['md5'])
print "SHA256: {}".format(file_info['sha256'])
print "Norton Rating: {}".format(file_info['norton_rating'])
