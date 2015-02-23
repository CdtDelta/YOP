# Agent checker
#
# By Tom Yarrish
# Version 1.2
#
# This script checks a list of IP's and connects to a specific port
# to see if the machine/agent is active
#
# Updates:
# (2015-2-20) Added rstrip() to server variable.  It was screwing up DNS
# (2015-2-20) Added socket.gethostbyname to do DNS. So you can either feed it hostname or IP's
# (2015-2-20) Changed output format to keep it consistent with 'server' 'connect/error'
# (2015-2-20) Added a time.sleep option if you don't want to hammer your DNS servers

import socket
import os
import sys
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("-i", dest="ip_list", help="Input file to read")
parser.add_argument("-o", dest="output_list", help="File to output to")
parser.add_argument("-p", dest="tcp_port", help="Port to use for check", type=int)
args = parser.parse_args()

ip_list = args.ip_list
output_list = args.output_list
tcp_port = args.tcp_port

script_output = open(output_list, "w")

with open(ip_list, "r") as server_list:
    for server in server_list:
        try:
            srv_check = socket.socket()
            server_ip = socket.gethostbyname(server.rstrip())
            srv_check.settimeout(10)
            srv_check.connect((server_ip, tcp_port))
            script_output.write(server.rstrip() + "\tConnected\n")    # Need to remove the CRLF to not screw up the lookups
            srv_check.close()
            time.sleep(2)
        except socket.error, error:
            script_output.write(server.rstrip() + "Error: {}\n".format(str(error)))
            srv_check.close()
            time.sleep(2)
        
print "All ip's checked..."
script_output.close()
