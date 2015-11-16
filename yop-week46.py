# These are some updates to the Week 45 script
# mostly functions that parse certain parts of the data
#
# by Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#

# These functions go in place after line 34 from week 45.

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

# This replaces lines 48-53 from week 45
with open(args.output_file, 'wb') as csv_output:
    csvfile = csv.writer(csv_output, delimiter='\t')
    with open(args.backup_file, "r") as new_file:
        for line in new_file:
            dns_record = dns_record_parse(line)
            csvfile.writerow([dns_record[0], dns_record[1], dns_record[2], dns_record[3], dns_record[4], dns_record[5], dns_record[6], dns_record[7], dns_record[8], dns_record[9], dns_record[10], dns_record[11]
, dns_record[12], dns_record[13], dns_record[14], dns_record[15], dns_record[16]])
