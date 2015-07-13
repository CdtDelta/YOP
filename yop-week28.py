# This script allows you to run a URL against Google's Safe Browsing
# service.
# Note:  You'll need to get an API key from here:
# https://code.google.com/apis/console/
# in order to run this script.
#
# Follow the steps on this page to create the API key:
# https://developers.google.com/safe-browsing/lookup_guide
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# By: Tom Yarrish
# Version 1.0

from configobj import ConfigObj
import requests
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', dest='config_file', required=True, help='Configuration File.')
args = parser.parse_args()

# This does the check for the configuration file which will store the API key

if os.path.exists(args.config_file):
    print "File exists"
    config = ConfigObj(args.config_file)
    api_key = config['apikey']
else:
    print "File doesn't exist"
    config = ConfigObj()
    config.filename = args.config_file
    config['apikey'] = raw_input("Enter your API Key: ")
    api_key = config['apikey']
    config.write()

sburl = "https://sb-ssl.google.com/safebrowsing/api/lookup"   # This is Google's Safe Browser URL

url_to_check = raw_input("Enter the URL to check: ")

# These are the return codes that Safe Browsing uses

return_codes = { 200 : "The URL is malicious",
                204 : "The URL is legitimate",
                400 : "Bad request",
                401 : "API Key is not authorized",
                503 : "Service unavailable" }

payload = { "key" : api_key ,
              "appver" : "1.0" ,
              "pver" : "3.1" ,
              "url" : url_to_check ,
          "client" : "python-powered" } # Note you need to update the pver value if the API is updated

check_url = requests.get(sburl, params=payload)

print "This is the URL for verification: \n{}".format(check_url.url)
print "This is the return code: {} ({}) - {}".format(check_url.status_code, return_codes[check_url.status_code], check_url.text)
