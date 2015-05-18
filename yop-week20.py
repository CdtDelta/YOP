# This file parses the header portion of a prefetch file.
# Future updates will parse the remaining parts of the file.
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# By: Tom Yarrish
# Version 1.0

import struct
import argparse

def prefetch_format(format_type):
    if format_type == "0x11":
        print "Windows XP/2003"
    elif format_type == "0x17":
        print "Windows Vista/7"
    elif format_type == "0x1a":
        print "Windows 8.1"
    return

def prefetch_header_parse(header):
    prefetch_header_format = struct.unpack("<L", header[0:4])
    prefetch_header_sig = header[4:8]
    prefetch_header_unk = struct.unpack("<L", header[8:12])
    prefetch_header_file_size = struct.unpack("<L", header[12:16])
    prefetch_header_file_name = header[16:76]
    prefetch_header_hash = struct.unpack("<L", header[76:80])
    prefetch_header_flags = struct.unpack("<L", header[80:84])
    print "Prefetch Header Information:\n"
    print "Header format: {}".format(hex(prefetch_header_format[0]))
    prefetch_format(hex(prefetch_header_format[0]))
    print "Header Signature: {}".format(prefetch_header_sig)
    print "Unknown: {}".format(hex(prefetch_header_unk[0]))
    print "Prefetch File Size: {}".format(prefetch_header_file_size[0])
    print "Prefetch File Name: {}".format(prefetch_header_file_name)
    print "Prefetch Hash: {}".format(hex(prefetch_header_hash[0]))
    print "Unknown: {}".format(hex(prefetch_header_flags[0]))
    return

parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='prefetch_file', required=True, help='Prefetch file to process.')
args = parser.parse_args()


with open(args.prefetch_file, 'rb') as prefetch:
    prefetch_header = prefetch.read()
    header = prefetch_header[:84]
    prefetch_header_parse(header)
