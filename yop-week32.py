"""This file is designed to parse vsFTPd log files.  It will pull out the IP addresses and sort by 
number of times the IP has connected to the server.  It will also do a dns lookup of the IP's and 
try to resolve them. It needs dnspython installed for that part to work."""
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# Version 1.0
# Tom Yarrish

import sys
import dns.resolver
import dns.reversename

ip_count = dict()
ip_top_count = list()

def ip_lookup(ip_address_to_resolve):
    my_dns_resolver = dns.resolver.Resolver()
    hostname_answer = dns.reversename.from_address(ip_address_to_resolve)
    try:
        return my_dns_resolver.query(hostname_answer, "PTR")[0]
    except dns.resolver.NXDOMAIN:
        return "No such domain"
    except dns.resolver.Timeout:
        return "Timeout"
    except dns.resolver.NoAnswer:
        return "No Response"
    except dns.resolver.NoNameservers:
        return "No Name Server"

try:
    ftp_log_files = open(sys.argv[1], "r")
except IndexError:
    print "Please enter a file to parse."
    exit()

try:
    ftp_report = open(sys.argv[2], "w")
except IndexError:
    print "Please enter a file to write output to."
    exit()
    
for ftp_entries in ftp_log_files.readlines():
    ftp_entries = ftp_entries.rstrip()
    ftp_fields = ftp_entries.split(" ")
    if len(ftp_fields[6]) < 5:
        continue
    else:
        if ftp_fields[6] not in ip_count:
            ip_count[ftp_fields[6]] = 1
        else:
            ip_count[ftp_fields[6]] = ip_count[ftp_fields[6]] + 1

for ip_address, ip_total in ip_count.items():
    ip_top_count.append((ip_total, ip_address))
    
ip_top_count.sort(reverse=True)

for ip_total, ip_address in ip_top_count:
    hostname = ip_lookup(ip_address)
    ftp_report.writelines("{} ({}) -> {}\n".format(hostname, ip_address, ip_total))

ftp_log_files.close()
ftp_report.close()