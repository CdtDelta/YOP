# This code parses the first 72 bytes of an index.dat file
#
# Tom Yarrish
# Version 1.0

import sys
import struct

# This code parses the signature and version string; offset 0-27
def ie_sig_ver_parse(decoder):
    ie_sig_ver_func = decoder[0:28] 
    return ie_sig_ver_func

# This code is to parse any of the four byte sections of the header
def ie_ind_four_byte(decoder):
    ind_four_byte = struct.unpack("<L", decoder[0:4])
    return ind_four_byte[0]

# This code is to parse any of the eight byte sections of the header
def ie_ind_eight_byte(decoder):
    ind_eight_byte = struct.unpack("<Q", decoder[0:8])
    return ind_eight_byte[0]


index_dat = sys.argv[1]

with open(index_dat, "rb") as ie_file:
    ie_index_header = ie_file.read()
    ind_sig_ver = ie_sig_ver_parse(ie_index_header[0:28])
    ie_index_dat_file_size = ie_ind_four_byte(ie_index_header[28:32])
    ie_first_hash_table_rec = ie_ind_four_byte(ie_index_header[32:36])
    ie_total_no_blocks = ie_ind_four_byte(ie_index_header[36:40])
    ie_allocated_no_blocks = ie_ind_four_byte(ie_index_header[40:44])
    ie_cache_size_quota = ie_ind_eight_byte(ie_index_header[48:56])
    ie_cache_size = ie_ind_eight_byte(ie_index_header[56:64])
    ie_non_release_cache_size = ie_ind_eight_byte(ie_index_header[64:72])
    

print "Signature and version:\t\t\t {}".format(ind_sig_ver)
print "Index.dat File Size:\t\t\t {} bytes".format(ie_index_dat_file_size)
print "First Hash Table Offset:\t\t {}".format(ie_first_hash_table_rec)
print "Total Number of Blocks:\t\t\t {} blocks".format(ie_total_no_blocks)
print "Allocated Number of Blocks:\t\t {} blocks".format(ie_allocated_no_blocks)
print "Cache Size Quota:\t\t\t {} bytes".format(ie_cache_size_quota)
print "Cache Size:\t\t\t\t {} bytes".format(ie_cache_size)
print "Non-Release Cache Size:\t\t\t {} bytes".format(ie_non_release_cache_size)
