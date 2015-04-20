# This program will scan a list of servers, along all open TCP ports, for the MS15-034 vulnerability.
# Code is based off the information here:
# https://isc.sans.edu/forums/diary/MS15034+HTTPsys+IIS+DoS+And+Possible+Remote+Code+Execution+PATCH+NOW/19583/
#
#
# By Tom Yarrish
# Version 1.0
#
# TODO: Need to figure out why it's hanging on some ports

import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-s', dest = 'server_list', help = 'Server list to check')
parser.add_argument('-o', dest = 'output_file', help = 'File to output results too')
args = parser.parse_args()

headers = {'host':'ms15034', 'range': 'bytes=0-18446744073709551615'}
tcp_ports = range(1,65536)

ms15_output_file = open(args.output_file, "w")
ms15_output = {}

http_check = requests.Session()
http_check.stream = False

with open(args.server_list, "r") as servers_to_check:
    for ms15_034_server in servers_to_check.readlines():
        for ports in tcp_ports:
            try:
                url = 'http://' + ms15_034_server.rstrip() + ':' + str(ports)
                print "Checking: {}...".format(url)
                ms15_034_check = http_check.get(url, headers = headers)
                ms15_output[str(ports)] = ms15_034_check.status_code
                http_check.close()
            except:
                continue
        for key, value in sorted(ms15_output.iteritems()):
            ms15_output_file.writelines("Server: {}\tPort: {}\tResult: {}".format(ms15_034_server, key, value))

ms15_output_file.close()
