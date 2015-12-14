# This is an updated version of my Windows DNS script
# this version writes the data to a sqlite database.
#
# by Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
import argparse
import csv
import re
import sqlite3
import os.path

# This function removes the first 33 lines from the file
def cleanup_file(filename):
    with open(filename, "r") as orig_file:
        new_file = orig_file.readlines()
        bkup_file = new_file[30:]
    with open(filename, "w") as new_filename:
        new_filename.writelines(bkup_file)
    return

# This function goes through and removes all the empty lines from the file
# We do it on a backup file to be on the safe side.
def remove_newlines(filename, new_filename):
    with open(filename, "r") as orig_file:
        with open(new_filename, "w") as new_file:
            for line in orig_file:
                if line.isspace():
                    continue
                else:
                    new_file.write(line)
    return

# This parses the opcode value
def dns_opcode_parse(opcode):
    dns_opcode = { "Q" : "Standard Query",
                   "N" : "Notify",
                   "U" : "Update",
                   "?" : "Unknown"}
    opcode = dns_opcode[opcode]
    return opcode

# This parses the DNS Flag Character codes
def dns_flags_parse(flag):
    dns_flags = { "A" : "Authoritative Answer",
                  "T" : "Truncated Response",
                  "D" : "Recursion Desired",
                  "R" : "Recursion Available"}
    flaglist = list(flag)
    flag_values = []
    for flag_letter in flaglist:
        flag_values.append(dns_flags[flag_letter])
    return flag_values

# This removes the (#) from the hostnames and replaces them with periods
def dns_question_name_parse(dns_name):
    fix_dns_name = re.sub('\(\d+\)', '.', dns_name)
    return fix_dns_name[1:]

# This parses out each line of the DNS file
def dns_record_parse(dns_line):
    dns_record = dns_line.split()
    if dns_record[4] == "EVENT": # If we have an EVENT line it doesn't have all the fields so we skip it.
        return
    else:
        try:
            dns_date = dns_record[0]
            dns_time = dns_record[1]
            dns_ampm = dns_record[2]
            dns_thread_id = dns_record[3]
            dns_context = dns_record[4]
            dns_internal_packet_ident = dns_record[5]
            dns_udp_tcp = dns_record[6]
            dns_snd_rcv = dns_record[7]
            dns_remote_ip = dns_record[8]
            dns_hex_xid = dns_record[9]
            if dns_record[10] == "Q":
                dns_query_resp = "Query"
                dns_opcode = dns_opcode_parse(dns_record[10])
                dns_flag_hex = dns_record[11]
                # Based on the DNS Response Code, we may have to shift the values of the other fields
                if (dns_record[12] == "NOERROR]") or (dns_record[12] == "REFUSED]") or (dns_record[12] == "SERVFAIL]"):
                    dns_flag_char = "NONE"
                    dns_resp_code = dns_record[12]
                    dns_ques_type = dns_record[13]
                    dns_ques_name = dns_question_name_parse(dns_record[14])
                else:
                    dns_flag_char = dns_flags_parse(dns_record[12])
                    dns_resp_code = dns_record[13]
                    dns_ques_type = dns_record[14]
                    dns_ques_name = dns_question_name_parse(dns_record[15])
            else:
                dns_query_resp = dns_record[10]
                dns_opcode = dns_opcode_parse(dns_record[11])
                dns_flag_hex = dns_record[12]
                if (dns_record[13] == "NOERROR]") or (dns_record[13] == "REFUSED]") or (dns_record[13] == "SERVFAIL]"):
                    dns_flag_char = "NONE"
                    dns_resp_code = dns_record[13]
                    dns_ques_type = dns_record[14]
                    dns_ques_name = dns_question_name_parse(dns_record[15])
                else:
                    dns_flag_char = dns_flags_parse(dns_record[13])
                    dns_resp_code = dns_record[14]
                    dns_ques_type = dns_record[15]
                    dns_ques_name = dns_question_name_parse(dns_record[16])
            return dns_date, dns_time, dns_ampm,dns_thread_id, dns_context, dns_internal_packet_ident,\
                   dns_udp_tcp, dns_snd_rcv, dns_remote_ip, dns_hex_xid, dns_query_resp, dns_opcode, dns_flag_hex, \
                   dns_flag_char, dns_resp_code, dns_ques_type, dns_ques_name
        except (IndexError, KeyError): # This handles some Index and Key errors if the line is incomplete
            print "Invalid/Incomplete entry"
            return


parser = argparse.ArgumentParser()
parser.add_argument('-f', dest = 'file_name', help = 'DNS Log to parse')
parser.add_argument('-b', dest = 'backup_file', help = 'Backup file name')
parser.add_argument('-o', dest = 'output_file', help = 'SQLite Database')
args = parser.parse_args()

cleanup_file(args.file_name)
remove_newlines(args.file_name, args.backup_file)

if os.path.isfile(args.output_file):
    print "{} exists...".format(args.output_file)
    db_connect = sqlite3.connect(args.output_file)
    dns_db = db_connect.cursor()    
else:
    db_connect = sqlite3.connect(args.output_file)
    dns_db = db_connect.cursor()
    # create table
    dns_db.execute("CREATE TABLE dns_record (ID INTEGER PRIMARY KEY AUTOINCREMENT, dns_date text, dns_time text, dns_am_pm text,\
    dns_thread text, dns_context text, dns_ipi text, dns_udp_tcp text, dns_send_recv text, dns_ip text, dns_xid text, dns_query text,\
    dns_opcode text, dns_flagsh text, dns_flagsc text, dns_response text, dns_ques_t text, dns_ques_n text);")

with open(args.backup_file, "r") as new_file:
    for line in new_file:
        try:
            dns_record = dns_record_parse(line)
            dns_db.execute("insert into dns_record values(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",\
                           (dns_record[0], dns_record[1], dns_record[2], dns_record[3], dns_record[4], dns_record[5], dns_record[6],\
                            dns_record[7], dns_record[8], dns_record[9], dns_record[10], dns_record[11], dns_record[12], str(dns_record[13]),\
                            dns_record[14], dns_record[15], dns_record[16]))
            db_connect.commit()
        except Exception, e:
            print "{}: {}".format(str(e), dns_record)
            continue

