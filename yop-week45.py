# This is the start of a script to parse out Windows DNS logs
# It outputs to a CSV file to filter in Excel
#
# by Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#

import argparse
import csv

# This function removes the first 33 lines from the file
def cleanup_file(filename):
    with open(filename, "r") as orig_file:
        new_file = orig_file.readlines()
        bkup_file = new_file[34:]
    with open(filename, "w") as new_filename:
        new_filename.writelines(bkup_file)
    return

# This function goes through and removes all the empty lines from the file
# We do it on a backup file to be on the safe side.
def remove_newlines(filename, new_filename):
    with open(filename, "r") as orig_file:
        with open(new_filename, "w") as new_file:
            for line in orig_file:
                if line.isspace():
                    continue
                else:
                    new_file.write(line)
    return

# Set up the arguments we need
parser = argparse.ArgumentParser()
parser.add_argument('-f', dest = 'file_name', help = 'DNS Log to parse')
parser.add_argument('-b', dest = 'backup_file', help = 'Backup file name')
parser.add_argument('-o', dest = 'output_file', help = 'CSV Output File')
args = parser.parse_args()

# Go through and clean out the start of the file first
cleanup_file(args.file_name)
# Now we remove the blank lines in between each log entry
remove_newlines(args.file_name, args.backup_file)

# Now we just go through each line and output it to the CSV file
with open(args.output_file, 'wb') as csv_output:
    csvfile = csv.writer(csv_output, delimiter='\t')
    with open(args.backup_file, "r") as new_file:
        for line in new_file:
            line_array = line.split()
            csvfile.writerows([line_array])