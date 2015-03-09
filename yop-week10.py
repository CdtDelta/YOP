# This script parses a NTFS VBR file
#
# Tom Yarrish
# Version 0.1
#
# Usage: yop-week10.py <vbr file>

import struct
import sys

ntfs_vbr_file = sys.argv[1]

with open (ntfs_vbr_file, "r") as f:
    vbr_file = f.read()
    ntfs_vbr_jump_instr = struct.unpack("<3B", vbr_file[0:3])
    ntfs_vbr_oem_id = vbr_file[3:11]
    ntfs_vbr_bytes_sector = struct.unpack("<H", vbr_file[11:13])
    ntfs_vbr_sectors_cluster = struct.unpack("<B", vbr_file[13])
    ntfs_vbr_media_desc = struct.unpack("<B", vbr_file[21])
    ntfs_vbr_sectors_track = struct.unpack("<H", vbr_file[24:26])
    ntfs_vbr_num_heads = struct.unpack("<H", vbr_file[26:28])
    ntfs_vbr_hidden_sectors = struct.unpack("<I", vbr_file[28:32])
    ntfs_vbr_total_sectors = struct.unpack("<Q", vbr_file[40:48])
    ntfs_vbr_log_cluster_mft = struct.unpack("<Q", vbr_file[48:56])
    ntfs_vbr_log_cluster_mft_mirr = struct.unpack("<Q", vbr_file[56:64])
    ntfs_vbr_clus_file_seg = struct.unpack("<I", vbr_file[64:68])
    ntfs_vbr_clus_ind_blk = struct.unpack("<I", vbr_file[68:72])
    ntfs_vbr_vol_serial = struct.unpack("<Q", vbr_file[72:80])
    ntfs_vbr_chksum = struct.unpack("<I", vbr_file[80:84])


print "Jump Instruction: {}".format(ntfs_vbr_jump_instr[0])
print "OEM ID: {}".format(ntfs_vbr_oem_id)
print "Bytes per Sector: {}".format(ntfs_vbr_bytes_sector[0])
print "Sectors per Cluster: {}".format(ntfs_vbr_sectors_cluster[0])
print "Reserved Sectors: {}".format(ntfs_vbr_reserved_sectors[0])
print "Media Descriptor: {}".format(hex(ntfs_vbr_media_desc[0]))
print "Sectors per track: {}".format(ntfs_vbr_sectors_track[0])
print "Number of Heads: {}".format(ntfs_vbr_num_heads[0])
print "Hidden sectors: {}".format(ntfs_vbr_hidden_sectors[0])
print "Large/Total sectors: {}".format(ntfs_vbr_total_sectors[0])
print "Cluster of $MFT: {}".format(ntfs_vbr_log_cluster_mft[0])
print "Cluster of $MFTMirror: {}".format(ntfs_vbr_log_cluster_mft_mirr[0])
print "Clusters per File Record Segment: {}".format(ntfs_vbr_clus_file_seg[0])
print "Clusters per Index Block: {}".format(ntfs_vbr_clus_ind_blk[0])
print "Volume Serial Number: {}".format(hex(ntfs_vbr_vol_serial[0]))
print "Checksum: {}".format(hex(ntfs_vbr_chksum[0]))