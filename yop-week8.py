# This script is designed to parse out the beginning of a VBR script
#
#
# by Tom Yarrish
# Version 1.0
#
# TODO:
# - Add logic to determine FAT 12/16 versus FAT32

import struct
import sys

vbr_file = sys.argv[1]

with open (vbr_file, "r") as f:
    vbr_file = f.read()
    vbr_jump_instr = struct.unpack("<3B", vbr_file[0:3])
    vbr_oem_id = vbr_file[3:11]
    vbr_bytes_sector = struct.unpack("<H", vbr_file[11:13])
    vbr_sectors_cluster = struct.unpack("<B", vbr_file[13])
    vbr_reserved_sectors = struct.unpack("<H", vbr_file[14:16])
    vbr_num_fats = struct.unpack("<B", vbr_file[16])
    vbr_root_entries = struct.unpack("<H", vbr_file[17:19])
    vbr_small_sectors = struct.unpack("<H", vbr_file[19:21])
    vbr_media_desc = struct.unpack("<B", vbr_file[21])
    vbr_sectors_fat = struct.unpack("<H", vbr_file[22:24])
    vbr_sectors_track = struct.unpack("<H", vbr_file[24:26])
    vbr_num_heads = struct.unpack("<H", vbr_file[26:28])
    vbr_hidden_sectors = struct.unpack("<I", vbr_file[28:32])
    vbr_large_sectors = struct.unpack("<I", vbr_file[32:36])
    vbr_phys_drive_num = struct.unpack("<B", vbr_file[36])
    vbr_ext_boot_sig = struct.unpack("<B", vbr_file[38])
    vbr_vol_serial = struct.unpack("<I", vbr_file[67:71])
    vbr_volume_label = vbr_file[71:82]
    vbr_file_system = vbr_file[82:89]


print "Jump Instruction: {}".format(vbr_jump_instr[0])
print "OEM ID: {}".format(vbr_oem_id)
print "Bytes per Sector: {}".format(vbr_bytes_sector[0])
print "Sectors per Cluster: {}".format(vbr_sectors_cluster[0])
print "Reserved Sectors: {}".format(vbr_reserved_sectors[0])
print "Number of FATs: {}".format(vbr_num_fats[0])
print "Root Entries: {}".format(vbr_root_entries[0])
print "Small Sectors: {}".format(vbr_small_sectors[0])
print "Media Descriptor: {}".format(hex(vbr_media_desc[0]))
print "Sectors per FAT: {}".format(vbr_sectors_fat[0])
print "Sectors per track: {}".format(vbr_sectors_track[0])
print "Number of Heads: {}".format(vbr_num_heads[0])
print "Hidden sectors: {}".format(vbr_hidden_sectors[0])
print "Large/Total sectors: {}".format(vbr_large_sectors[0])
print "Physical Drive Number: {}".format(vbr_phys_drive_num[0])
print "External Boot Signature: {}".format(hex(vbr_ext_boot_sig[0]))
print "Volume Serial Number: {}".format(hex(vbr_vol_serial[0]))
print "Volume Label: {}".format(vbr_volume_label)
print "File System Type: {}".format(vbr_file_system)
