# This simple script is to help research IP addresses
# It'll pull DNS and whois information
# As well as pull down the web page from the IP
#
# Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html

from ipwhois import IPWhois
import dns.resolver, dns.reversename
import argparse
import pycurl

def iplookup(ip_addr, dns_srv):
    ip_resolver = dns.resolver
    ip_reverse = dns.reversename
    ip_resolver.nameservers = [dns_srv]
    ip_reverse.nameservers = [dns_srv]
    ip_rev = ip_reverse.from_address(ip_addr)
    domain_name = ip_resolver.query(ip_rev, 'PTR')
    return domain_name
    
def whois(ip_addr):
    query = IPWhois(ip_addr)
    whois_ans = query.lookup()
    return whois_ans

def pull_url(ip_addr):
    filename = ip_addr + ".txt"
    with open(filename, 'wb') as html_file:
        http_grab = pycurl.Curl()
        http_grab.setopt(http_grab.URL, ip_addr)
        http_grab.setopt(http_grab.WRITEDATA, html_file)
        http_grab.perform()
        http_grab.close()
    return

parser = argparse.ArgumentParser()
parser.add_argument('-i', dest = 'ip_addr', help = 'IP Address to query')
parser.add_argument('-s', dest = 'dns_server', help = 'DNS Server to use')
args = parser.parse_args()

domain_name = iplookup(args.ip_addr, args.dns_server)
whois_info = whois(args.ip_addr)
pull_url(args.ip_addr)

print "Checking info on {} using DNS server {}....\n".format(args.ip_addr, args.dns_server)
print "The IP Address resolves to:\n{}".format(domain_name.response)
print "\nThe WHOIS information for the IP {} is:\n".format(args.ip_addr)
whois_nets = whois_info['nets']
for key, value in whois_info.iteritems():
    print "{} -> {}".format(key, value)
