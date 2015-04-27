# This script parses out the hash table in an index.dat file
# It's still a work in progress I have some pieces to finish coding out
#
#
# By Tom Yarrish
# Version 0.5
#
# Usage yop-week17.py <index.dat>

import sys
import struct

def hash_header(parse_header):
    ie_hash_header = parse_header[0:4]
    ie_hash_length = struct.unpack("<I", parse_header[4:8])
    ie_hash_next_table = struct.unpack("<I", parse_header[8:12])
    ie_hash_table_no = struct.unpack("<I", parse_header[12:16])
    print "{}\nHash Table Length: {}\nNext Hash Table Offset: {}\nHash Table No: {}\n".format(ie_hash_header, (ie_hash_length[0] * 128), ie_hash_next_table[0], ie_hash_table_no[0])
    return ie_hash_header, (ie_hash_length[0] * 128), ie_hash_next_table[0], ie_hash_table_no[0]

def hash_table_records(parse_records):
    ie_hash_data = struct.unpack("<I", parse_records[0:4])
    ie_hash_record_pointer = struct.unpack("<I", parse_records[4:8])
    print "Hash Data: {}\t\tHash Record Pointer: {}".format(hex(ie_hash_data[0]), ie_hash_record_pointer[0])
    return

index_dat = sys.argv[1] 

with open(index_dat, "rb") as ie_file:
    ie_hash_parser = ie_file.read()
    ie_hash_head = ie_hash_parser[20480:20496]
    ie_hash_header = hash_header(ie_hash_head)
    ie_hash_record_start = 20496
    ie_hash_record_end = 20504
    ie_hash_record = ie_hash_parser[ie_hash_record_start:ie_hash_record_end]
    while ie_hash_record_start < (ie_hash_record_start + (int(ie_hash_header[1]) - 12)):
        ie_hash_record_table = hash_table_records(ie_hash_record)
        ie_hash_record_start = ie_hash_record_end
        ie_hash_record_end += 16
        ie_hash_record = ie_hash_parser[ie_hash_record_start:ie_hash_record_end]
