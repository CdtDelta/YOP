# This weeks example are actually updates to previous YOP code.
# These are just snippets of code, not designed to run on its own
#
# The follow code is designed to be included in the YOP - Week 17 script
#
# First add the bitstring module to the beginning of the script
from bitstring import BitArray, Bits

# I created a new function to parse some of the binary values to the bit level
# This is for the hash data piece 
def hash_data_parse(parse_data):
    bit_values = BitArray(parse_data)
    binary_values = bit_values.bin
    return binary_values

# With this function, we added a line of code to call the hash_data_parse function
# and then we print out the binary structures that are part of the record hash
def hash_table_records(parse_records):
    ie_hash_data = struct.unpack("<I", parse_records[0:4])
    ie_hash_record_pointer = struct.unpack("<I", parse_records[4:8])
    ie_hash_data_parse = hash_data_parse(hex(ie_hash_data[0]))
    print "Hash Data: {}\t\tHash Record Pointer: {}".format(hex(ie_hash_data[0]), ie_hash_record_pointer[0])
    print "Record Hash Flags: {}\tRecord Hash Value: {}".format(ie_hash_data_parse[:5], ie_hash_data_parse[6:])
    return

# The following are updates to YOP - Week 13 Script
# So in this section the first thing I write to the log is the number of items in the dictionary.
# We'll use this to make sure we have the same number in the source as in the destination
audit_log.write("There are {} items in the source directory.\n".format(len(source_file_list)))
audit_log.write("Source files....\n")
for key, value in source_file_list.items():
    audit_log.write("{}\t\t\t\t\tMD5: {}\n".format(key, value))

# In this section again we're looking at the number of items in the destination dictionary
# To make sure it matches up with the source dictionary
audit_log.write("There are {} items in the destination directory.\n".format(len(dest_file_list)))
audit_log.write("\nDestination files...\n")
for key, value in dest_file_list.items():
    audit_log.write("{}\t\t\t\t\tMD5: {}\n".format(key, value))

# This statement comparies both dictionaries and make sure the files we have in the source
# directory are in the destination.  And that the hashes match up correctly    
for (key, value) in set(source_file_list.items()) & set(dest_file_list.items()):
    audit_log.write("{}: {} is present in both source and destination.\n".format(key, value))
