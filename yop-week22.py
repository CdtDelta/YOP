# This script parses the header of an ESE DB File.
# the format is based on the documentation by Joachim Metz
# located here: 
# https://github.com/libyal/libesedb/blob/master/documentation/Extensible%20Storage%20Engine%20(ESE)%20Database%20File%20(EDB)%20format.asciidoc
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# By Tom Yarrish
# Version 0.1

import argparse
import struct

# This function is temporary and parses the data structures of Backup Information
def edb_backup_parse(bkup_data):
    bkup_pos = struct.unpack("<Q", bkup_data[0:8])
    bkup_create_datetime = struct.unpack("<Q", bkup_data[8:16]) # This line will be rewritten to use the log_time function
    bkup_gen_lwr_no = struct.unpack("<L", bkup_data[16:20])
    bkup_gen_upr_no = struct.unpack("<L", bkup_data[20:24])
    return bkup_pos[0], bkup_create_datetime[0], bkup_gen_lwr_no[0], bkup_gen_upr_no[0]

# This function parses out the Log Time data structures
def log_time(time_data):
    log_sec = struct.unpack("<B", time_data[0])
    log_min = struct.unpack("<B", time_data[1])
    log_hour = struct.unpack("<B", time_data[2])
    log_day = struct.unpack("<B", time_data[3])
    log_mon = struct.unpack("<B", time_data[4])
    log_year = struct.unpack("<B", time_data[5])
    return log_sec[0], log_min[0], log_hour[0], log_day[0], log_mon[0], (log_year[0] + 1900)

# This part is supposed to parse out the DB Time data structures, but it's not quite working right yet
def db_time(time_data):
    db_hours = struct.unpack("<H", time_data[0:2])
    db_min = struct.unpack("<H", time_data[2:4])
    db_sec = struct.unpack("<H", time_data[4:6])
    return db_hours[0], db_min[0], db_sec[0]

# This is the main function to parse out the ESE DB header information
def edb_header_parse(edb_header):
    edb_checksum = struct.unpack("<L", edb_header[0:4])
    edb_sig = struct.unpack("<L", edb_header[4:8])
    edb_file_format = struct.unpack("<L", edb_header[8:12])
    edb_file_type = struct.unpack("<L", edb_header[12:16])
    # So here's our first db_time function usage.
    datab_time = edb_header[16:24]
    edb_db_time = db_time(datab_time)
    
    edb_db_sig = struct.unpack("<7L", edb_header[24:52])
    edb_db_state = struct.unpack("<L", edb_header[52:56])
    edb_consistent_pos = struct.unpack("<Q", edb_header[56:64])
    # And here's our first usage of the log_time function
    consistent_time = edb_header[64:72]
    edb_consistent_time = log_time(consistent_time)
    # Again here we're going to use the log_time function
    attach_date_time = edb_header[72:80]
    edb_attach_date_time = log_time(attach_date_time)
    
    edb_attach_position = struct.unpack("<Q", edb_header[80:88])
    
    detach_date_time = edb_header[88:96]
    edb_detach_date_time = log_time(detach_date_time)
    
    edb_detach_position = struct.unpack("<Q", edb_header[96:104])
    edb_log_signature = struct.unpack("<7L", edb_header[104:132])
    # So for now I'm just running a quick function to break out the data
    # I'll work on actually parsing out the contents next
    bkup = edb_header[136:160]
    edb_prev_full_bkup = edb_backup_parse(bkup)
    bkup = edb_header[160:184]
    edb_prev_inc_bkup = edb_backup_parse(bkup)
    bkup = edb_header[184:208]
    edb_cur_full_bkup = edb_backup_parse(bkup)
    
    edb_shadow_disable = struct.unpack("<L", edb_header[208:212])
    edb_last_obj_id = struct.unpack("<L", edb_header[212:216])
    edb_maj_ver = struct.unpack("<L", edb_header[216:220])
    edb_min_ver = struct.unpack("<L", edb_header[220:224])
    edb_build_num = struct.unpack("<L", edb_header[224:228])
    edb_sp_num = struct.unpack("<L", edb_header[228:232])
    edb_file_format_ver = struct.unpack("<L", edb_header[232:236])
    edb_page_size = struct.unpack("<L", edb_header[236:240])
    edb_repair_count = struct.unpack("<L", edb_header[240:244])
    repair_datetime = edb_header[244:252]
    edb_repair_datetime = log_time(repair_datetime)
    scrub_database_time = edb_header[280:288]
    edb_scrub_db_time = db_time(scrub_database_time)
    scrub_date_time = edb_header[288:296]
    edb_scrub_date_time = log_time(scrub_date_time)
    edb_required_log = struct.unpack("<2L", edb_header[296:304])
    edb_up_exch_5_5_format = struct.unpack("<L", edb_header[304:308])
    edb_up_free_pages = struct.unpack("<L", edb_header[308:312])
    edb_up_space_map_pages = struct.unpack("<L", edb_header[312:316])
    edb_curr_shdwcp_bkup = struct.unpack("<6L", edb_header[316:340])
    edb_create_file_format_ver = struct.unpack("<L", edb_header[340:344])
    edb_create_file_format_rev = struct.unpack("<L", edb_header[344:348])
    edb_old_repair_count = struct.unpack("<L", edb_header[364:368])
    edb_ecc_fix_success_count = struct.unpack("<L", edb_header[368:372])
    ecc_fix_datetime = edb_header[372:380]
    edb_fix_succ_datetime = log_time(ecc_fix_datetime)
    edb_old_ecc_fix_success_count = struct.unpack("<L", edb_header[380:384])
    edb_ecc_fix_err_count = struct.unpack("<L", edb_header[384:388])
    last_ecc_fix_datetime = edb_header[388:396]
    edb_last_ecc_err_fix_datetime = log_time(last_ecc_fix_datetime)
    edb_old_ecc_err_count = struct.unpack("<L", edb_header[396:400])
    edb_bad_chksum_err_count = struct.unpack("<L", edb_header[400:404])
    last_bad_chksum_datetime = edb_header[404:412]
    edb_last_bad_chksum_err_datetime = log_time(last_bad_chksum_datetime)
    edb_old_bad_chksum_err_count = struct.unpack("<L", edb_header[412:416])
    edb_prev_shadow_cp_bkup = struct.unpack("<6L", edb_header[420:444])
    edb_prev_diff_backup = struct.unpack("<6L", edb_header[444:468])
    edb_nls_major_ver = struct.unpack("<L", edb_header[508:512])
    edb_nls_minor_ver = struct.unpack("<L", edb_header[512:516])
    
    # At this point I'm just printing out the data just to see what's there
    # Then I can format it properly later
    print hex(edb_checksum[0])
    print hex(edb_sig[0])
    print hex(edb_file_format[0])
    print edb_file_type[0]
    print "Database Time: {}:{}:{}".format(edb_db_time[0], edb_db_time[1], edb_db_time[2])
    print edb_db_sig
    print edb_db_state[0]
    print edb_consistent_pos[0]
    print "EDB Consistent Time: {}:{}:{}\t{}/{}/{}".format(edb_consistent_time[2], edb_consistent_time[1], \
                                                           edb_consistent_time[0], edb_consistent_time[4], \
                                                           edb_consistent_time[3], edb_consistent_time[5])
    print "EDB Attach Date/Time: {}:{}:{}\t{}/{}/{}".format(edb_attach_date_time[2], edb_attach_date_time[1], \
                                                            edb_attach_date_time[0], edb_attach_date_time[4], \
                                                            edb_attach_date_time[3], edb_attach_date_time[5])
    print edb_attach_position[0]
    print "EDB Detach Date/Time: {}:{}:{}\t{}/{}/{}".format(edb_detach_date_time[2], edb_detach_date_time[1], \
                                                            edb_detach_date_time[0], edb_detach_date_time[4], \
                                                            edb_detach_date_time[3], edb_detach_date_time[5])
    print edb_detach_position[0]
    print edb_log_signature
    # For these next three I'm just looping through the data to see what's there
    # Again I'm going to format it so the output is cleaner
    for bkup_item in edb_prev_full_bkup:
        print bkup_item
    for bkup_item in edb_prev_inc_bkup:
        print bkup_item
    for bkup_item in edb_cur_full_bkup:
        print bkup_item
    print edb_last_obj_id[0]
    print edb_maj_ver[0]
    print edb_min_ver[0]
    print edb_build_num[0]
    print edb_sp_num[0]
    print edb_file_format[0]
    print edb_page_size[0]
    print edb_repair_count[0]
    print "EDB Repair Date/Time: {}:{}:{}\t{}/{}/{}".format(edb_repair_datetime[2], edb_repair_datetime[1], \
                                                            edb_repair_datetime[0], edb_repair_datetime[4], \
                                                            edb_repair_datetime[3], edb_repair_datetime[5])
    print "EDB Scrub DB Time: {}:{}:{}".format(edb_scrub_db_time[0], edb_scrub_db_time[1], edb_scrub_db_time[2])
    print "EDB Scrub Date/Time: {}:{}:{}\t{}/{}/{}".format(edb_scrub_date_time[2], edb_scrub_date_time[1], \
                                                            edb_scrub_date_time[0], edb_scrub_date_time[4], \
                                                            edb_scrub_date_time[3], edb_scrub_date_time[5])
    print edb_required_log
    print edb_up_exch_5_5_format[0]
    print edb_up_free_pages[0]
    print edb_up_space_map_pages[0]
    print edb_curr_shdwcp_bkup
    print edb_create_file_format_ver[0]
    print edb_create_file_format_rev[0]
    print edb_old_repair_count[0]
    print edb_ecc_fix_success_count[0]
    print "ECC Fix Success Date/Time: {}:{}:{}\t{}/{}/{}".format(edb_fix_succ_datetime[2], edb_fix_succ_datetime[1], \
                                                            edb_fix_succ_datetime[0], edb_fix_succ_datetime[4], \
                                                            edb_fix_succ_datetime[3], edb_fix_succ_datetime[5])
    print edb_old_ecc_fix_success_count[0]
    print edb_ecc_fix_err_count[0]
    print "Last ECC Fix Error Date/Time: {}:{}:{}\t{}/{}/{}".format(edb_last_ecc_err_fix_datetime[2], edb_last_ecc_err_fix_datetime[1], \
                                                            edb_last_ecc_err_fix_datetime[0], edb_last_ecc_err_fix_datetime[4], \
                                                            edb_last_ecc_err_fix_datetime[3], edb_last_ecc_err_fix_datetime[5])
    print edb_old_ecc_err_count[0]
    print edb_bad_chksum_err_count[0]
    print "EDB Last Bad Checksum Error Date/Time: {}:{}:{}\t{}/{}/{}".format(edb_last_bad_chksum_err_datetime[2], edb_last_bad_chksum_err_datetime[1], \
                                                            edb_last_bad_chksum_err_datetime[0], edb_last_bad_chksum_err_datetime[4], \
                                                            edb_last_bad_chksum_err_datetime[3], edb_last_bad_chksum_err_datetime[5])
    print edb_old_bad_chksum_err_count[0]
    print edb_prev_shadow_cp_bkup
    print edb_prev_diff_backup
    print edb_nls_major_ver[0]
    print edb_nls_minor_ver[0]

parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='esedb_file', required=True, help='ESE DB file to process.')
args = parser.parse_args()

with open(args.esedb_file, "rb") as edb_file:
    edb_file_data = edb_file.read()
    edb_header_parse(edb_file_data[:688]) #Here we're just pulling in the first 688 bytes of the header