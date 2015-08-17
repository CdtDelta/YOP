# This script parses out the start of a Windows Platform Binary Table file
# It's based off the document located here:
# http://go.microsoft.com/fwlink/p/?LinkId=234840
#
# Unfortunately as of this initial commit I don't have a file to test it against.
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# Version 1.0
# Tom Yarrish

import argparse
import struct

def wpbtfileparse(wpbtfile):
    wpbt_signature = wpbtfile[0:4]
    wpbt_length = struct.unpack("<L", wpbtfile[4:8])
    wpbt_revision = struct.unpack("<B", wpbtfile[8])
    wpbt_checksum = struct.unpack("<B", wpbtfile[9])
    wpbt_oemid = wpbtfile[10:16]
    wpbt_oemtableid = wpbtfile[16:24]
    wpbt_oemrevision = struct.unpack("<L", wpbtfile[24:28])
    wpbt_creatorid = struct.unpack("<L", wpbtfile[28:32])
    wpbt_creatorrev = struct.unpack("<L", wpbtfile[32:36])
    wpbt_handoffmemsize = struct.unpack("<L", wpbtfile[36:40])
    wpbt_handofflocation = struct.unpack("<Q", wpbtfile[40:48])
    wpbt_contentlayout = wpbtfile[49]
    wpbt_contenttype = wpbtfile[50]
    
    print "Signature: {}".format(wpbt_signature)
    print "Length: {}".format(wpbt_length[0])
    print "Revision: {}".format(wpbt_revision[0])
    print "Checksum: {}".format(wpbt_checksum[0])
    print "OEM ID: {}".format(wpbt_oemid)
    print "OEM Table ID: {}".format(wpbt_oemtableid)
    print "OEM Revision: {}".format(wpbt_oemrevision[0])
    print "Creator ID: {}".format(wpbt_creatorid[0])
    print "Creator Revision: {}".format(wpbt_creatorrev[0])
    print "Handoff Memory Size: {}".format(wpbt_handoffmemsize[0])
    print "Handoff Memory Location: {}".format(hex(wpbt_handofflocation[0]))
    print "Content Layout: {}".format(wpbt_contentlayout)
    print "Content Type: {}".format(wpbt_contenttype)
    
    return

parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='file_to_parse', required=True, help='WPBT File to parse')
args = parser.parse_args()

with open(args.file_to_parse, "rb") as wpbt_file:
    wpbt_file_data = wpbt_file.read()
    wpbtfileparse(wpbt_file_data[:49])