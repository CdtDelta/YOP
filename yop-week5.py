# This code parses the header for the index.dat file
#
# Tom Yarrish
# Version 1.0
#
# TODO: Finish parsing the rest of the file
#
# Format of the command:
# index_dat_parser.py <index.dat>

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
    num_cache_dir_entries = ie_ind_four_byte(ie_index_header[72:76])
    num_cache_dir_parse = num_cache_dir_entries
    start = 76
    end = 88
    dict_cache_dir_entry = {} # initialize a dictionary to put the cached directory name and no of cached files
    while num_cache_dir_parse > 0:
        cache_dir_entry = ie_ind_cache_dir_entry(ie_index_header[start:end])
        dict_cache_dir_entry[cache_dir_entry[1]] = cache_dir_entry[0]
        # increment our variables
        start = end # Pass the previous ending point to the start
        end = end + 12 # Now add 12 to the previous ending point to get the new one
        num_cache_dir_parse -= 1


print "Signature and version:\t\t\t {}".format(ind_sig_ver)
print "Index.dat File Size:\t\t\t {} bytes".format(ie_index_dat_file_size)
print "First Hash Table Offset:\t\t {}".format(ie_first_hash_table_rec)
print "Total Number of Blocks:\t\t\t {} blocks".format(ie_total_no_blocks)
print "Allocated Number of Blocks:\t\t {} blocks".format(ie_allocated_no_blocks)
print "Cache Size Quota:\t\t\t {} bytes".format(ie_cache_size_quota)
print "Cache Size:\t\t\t\t {} bytes".format(ie_cache_size)
print "Non-Release Cache Size:\t\t\t {} bytes".format(ie_non_release_cache_size)
print "Number of cache directory entries:\t\t {}".format(num_cache_dir_entries)
print "Name of cache directory and number of files:\n"
for dir_name, no_cache in dict_cache_dir_entry.iteritems():
    print "{}\t\t{}".format(dir_name, no_cache)