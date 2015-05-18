# Runs an MD5 comparison of files in two different directories.
# Writes the results to an output file
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
#
# Tom Yarrish
# Version 1.0

import os
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", dest="source_dir", help="Source directory")
parser.add_argument("-d", dest="dest_dir", help="Destination directory")
parser.add_argument("-o", dest="output_file", help="Output file")
args = parser.parse_args()

source_file_list = {}
dest_file_list = {}

print "Hashing files in {} and comparing them to {}...please wait...".format(args.source_dir, args.dest_dir)

audit_log = open(args.output_file, "w")

for path, subdirs, files in os.walk(args.source_dir):
    for name in files:
        hash_filepath = os.path.join(path, name)
        with open((hash_filepath), "rb") as file_to_hash:
            md5_buff = file_to_hash.read()
            md5_returned = hashlib.md5(md5_buff).hexdigest()
        source_file_list[name] = md5_returned
    
for path, subdirs, files in os.walk(args.dest_dir):
    for name in files:
        hash_filepath = os.path.join(path, name)
        with open((hash_filepath), "rb") as file_to_hash:
            md5_buff = file_to_hash.read()
            md5_returned = hashlib.md5(md5_buff).hexdigest()
        dest_file_list[name] = md5_returned

audit_log.write("Source files....\n")
for key, value in source_file_list.iteritems():
    audit_log.write("{}\t\t\t\t\tMD5: {}\n".format(key, value))

audit_log.write("\nDestination files...\n")
for key, value in dest_file_list.iteritems():
    audit_log.write("{}\t\t\t\t\tMD5: {}\n".format(key, value))
