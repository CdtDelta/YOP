# This script is starting to parse out the header portion of a Windows LNK file
# I'm using the following two URLs for reference
# https://msdn.microsoft.com/en-us/library/dd891343.aspx
# https://github.com/libyal/liblnk/blob/master/documentation/Windows%20Shortcut%20File%20(LNK)%20format.asciidoc
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# Version 0.1
# By Tom Yarrish

import struct
import datetime
import argparse

# Parse the FILETIME data; someone else wrote this code
def FromFiletime(filetime):
  if filetime < 0:
    return None
  timestamp = filetime / 10

  return datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=timestamp)

def lnk_file_header(header_data):
    lnk_header_size = struct.unpack("<L", header_data[0:4])
    lnk_header_clsid = struct.unpack("<2Q", header_data[4:20])
    lnk_header_flags = struct.unpack("<L", header_data[20:24])
    lnk_header_file_attrib = struct.unpack("<L", header_data[24:28])
    # Parse the creation time stamp
    header_creation_time = struct.unpack("<Q", header_data[28:36])
    lnk_header_creation_time = FromFiletime(header_creation_time[0])
    # Parse the access time stamp
    header_access_time = struct.unpack("<Q", header_data[36:44])
    lnk_header_access_time = FromFiletime(header_access_time[0])
    # Parse the write time stamp
    header_write_time = struct.unpack("<Q", header_data[44:52])
    lnk_header_write_time = FromFiletime(header_write_time[0])
    
    lnk_header_file_size = struct.unpack("<L", header_data[52:56])
    lnk_header_icon_indx = struct.unpack("<L", header_data[56:60])
    lnk_header_show_window = struct.unpack("<L", header_data[60:64])
    lnk_header_hot_key = struct.unpack("<H", header_data[64:66])
    
    print "Header Size: {}".format(hex(lnk_header_size[0]))
    print "CLSID: {}".format(lnk_header_clsid)
    print "Flags: {}".format(hex(lnk_header_flags[0]))
    print "File Attributes: {}".format(hex(lnk_header_file_attrib[0]))
    print "Creation Time: {}".format(lnk_header_creation_time)
    print "Access Time: {}".format(lnk_header_access_time)
    print "Modification Time: {}".format(lnk_header_write_time)
    print "File Size: {}".format(lnk_header_file_size[0])
    print "Icon Index: {}".format(lnk_header_icon_indx[0])
    print "Show Window: {}".format(lnk_header_show_window[0])
    print "Hot Key: {}".format(lnk_header_hot_key[0])

parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='lnk_file', required=True, help='LNK file to process.')
args = parser.parse_args()

with open(args.lnk_file, "rb") as lnk_file:
    lnk_file_data = lnk_file.read()
    lnk_header = lnk_file_header(lnk_file_data[:76])
