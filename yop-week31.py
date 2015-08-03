# This script continues the work from the yop-week22.py script
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# Version 0.1
# By Tom Yarrish
#
# 

import struct
import argparse

# This is to work on the database state code
def trans_db_state(db_state):
    dict_db_state = { 1 : "JET_dbstateJustCreated",
                     2 : "JET_dbstateDirtyShutdown",
                     3 : "JET_dbstateCleanShutdown",
                     4 : "JET_dbstateBeingConverted",
                     5 : "JET_dbstateForceDetach"
                     }
    desc_db_state = dict_db_state[db_state]
    return desc_db_state

# This is to work on the log position
def log_position(logp):
    log_pos_block = struct.unpack("<H", logp[0:2])
    log_pos_sector = struct.unpack("<H", logp[2:4])
    log_pos_generation = struct.unpack("<L", logp[4:])
    return log_pos_block[0], log_pos_sector[0], log_pos_generation[0]

parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='file_to_parse', required=True, help='EDB File to parse')
args = parser.parse_args()

with open(args.file_to_parse, "rb") as edb_file:
    edb_file_data = edb_file.read()
    edb_db_state = struct.unpack("<L", edb_file_data[52:56])
    edb_consistent_pos = edb_file_data[56:64]
    edb_consistent_log_pos = log_position(edb_consistent_pos)    
    edb_db_state_code = trans_db_state(edb_db_state[0])
    
print "Database State: ({}) - {}".format(edb_db_state[0], edb_db_state_code)

print "JET_LGPOS Block: {}".format(edb_consistent_log_pos[0])
print "JET_LGPOS Sector: {}".format(edb_consistent_log_pos[1])
print "JET_LGPOS Generation: {}".format(edb_consistent_log_pos[2])