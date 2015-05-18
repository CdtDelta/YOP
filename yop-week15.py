# This program with either convert text to an MD5 hash (to check pash the hash stuff)
# or it will decode a URL with %xx characters to their equivalent special characters
#
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# Version 1.0
# Tom Yarrish

import urllib
import hashlib

def decode_url(url_data):
    return urllib.unquote(url_data)

def create_md5(input_md5):
    set_md5 = hashlib.md5()
    set_md5.update(input_md5)
    return set_md5.hexdigest()

quit_prog = True

while quit_prog:
    choice = raw_input("Choose md5 or url (type quit to exit): ") 
    if choice.lower() == "md5":
        enter_md5 = raw_input("Enter the text to convert to md5: ")
        print create_md5(enter_md5)
    elif choice.lower() == "url":
        enter_url = raw_input("Enter the url text to convert: ")
        print decode_url(enter_url)
    elif choice.lower() == "quit":
        quit_prog = False
        
