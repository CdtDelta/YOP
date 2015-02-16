# Agent checker
#
# By Tom Yarrish
# Version 1.0
#
# This script checks a list of IP's and connects to a specific port
# to see if the machine/agent is active

import socket
import os
import sys
import argparse

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
            srv_check.settimeout(10)
            srv_check.connect((server, tcp_port))
            script_output.write(server + "Connected\n")
            srv_check.close()
        except socket.error, error:
            script_output.write(str(error) + server)
            srv_check.close()
        
print "All ip's checked..."
script_output.close()
