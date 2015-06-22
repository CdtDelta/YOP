# This script continues the work from the yop-week23.py script
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# Version 0.1
# By Tom Yarrish

# This is the function to parse the attributes

def lnk_attrib(attrib_to_parse):
    attrib = { 0: "FILE_ATTRIBUTE_READONLY",
              1: "FILE_ATTRIBUTE_HIDDEN",
              2: "FILE_ATTRIBUTE_SYSTEM",
              3: "Reserved1",
              4: "FILE_ATTRIBUTE_DIRECTORY",
              5: "FILE_ATTRIBUTE_ARCHIVE",
              6: "Reserved2",
              7: "FILE_ATTRIBUTE_NORMAL",
              8: "FILE_ATTRIBUTE_TEMPORARY",
              9: "FILE_ATTRIBUTE_SPARSE_FILE",
              10: "FILE_ATTRIBUTE_REPARSE_POINT",
              11: "FILE_ATTRIBUTE_COMPRESSED",
              12: "FILE_ATTRIBUTE_OFFLINE",
              13: "FILE_ATTRIBUTE_NOT_CONTENT_INDEXED",
              14: "FILE_ATTRIBUTE_ENCRYPTED" }
    
    for count, items in enumerate(attrib_to_parse):
        if int(items) == 1:
            print "{} is set.".format(attrib[count])
        else:
            continue

# This section replaces line 28
# These two lines will parse out the individual bits for the attributes
lnk_header_file_attrib = struct.unpack("<I", header_data[24:28])
lnk_header_file_attrib_bits = BitArray(hex(lnk_header_file_attrib[0]))

# This replaces line 47
print "\nAttributes:"
lnk_attrib(lnk_header_file_attrib_bits.bin)
