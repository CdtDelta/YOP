# This script is a start on parsing out Norton NPE Log Files
# Which are in an XML Format
#
# by Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html

from bs4 import BeautifulSoup
import argparse

# This just pulls in the OS information
def npe_target_product(xml):
    target_product = soup.productname.string
    target_version = soup.productversion.string
    if soup.servicepack.string == 'None':
        target_service_pack = "No SP Installed"
    else:
        target_service_pack = soup.servicepack.string
    target_system_type = soup.systemtype.string
    return target_product, target_version, target_service_pack, target_system_type

# Usual stuff to get the file we want to parse
parser = argparse.ArgumentParser()
parser.add_argument('-f', dest = 'xml_file', help = 'NPE Log File to parse')
args = parser.parse_args()

soup = BeautifulSoup(open(args.xml_file))

os_info = npe_target_product(soup)

print "The Product Name is: {}".format(os_info[0])
print "The Build Version is: {}".format(os_info[1])
print "The Service Pack is: {}".format(os_info[2])
print "The system is a {}".format(os_info[3])

# Right now all I'm doing is looking for the <File> references and printing out the strings
print "The following files were referenced in the log file."
for files in soup.findAll('file'):
    print files.string