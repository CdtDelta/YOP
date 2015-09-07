# This is the start of a script to replace some values in a template I use
# It's allowing me to practice using Regular Expressions in Python
#
# Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html

import re
import shutil
import os
import sys

def make_directory(name, account):
    split_name = name.split(" ")
    directory_name = split_name[0], split_name[1], account
    separator = "_"
    directory = separator.join(directory_name)
    return directory

def full_name_replace(name, line):
    result_line = re.sub('<Full Name>', name, line)
    return result_line

def iphone_model_replace(iphone, line):
    result_line = re.sub('<Model>', iphone, line)
    return result_line

def os_version_replace(ios, line):
    result_line = re.sub('<OS Version>', ios, line)
    return result_line

def passcode_replace(pin, line):
    result_line = re.sub('<Passcode>', pin, line)
    return result_line

def directory_replace(filename, line):
    result_line = re.sub('<Directory Name>', filename, line)
    return result_line

file_to_search = sys.argv[1]

full_name = raw_input("Enter the full name of the employee: ")
account = raw_input("Enter the employees Username: ")
iphone_model = raw_input("Enter the model number of the iPhone (ex. A1533): ")
ios_version = raw_input("Enter the iOS version on the phone: ")
iphone_pin = raw_input("Enter the iPhone PIN/Password: ")

working_dir = os.getcwd()
directory_name = make_directory(full_name, account)


with open(file_to_search, "r") as searchfile:
    line = searchfile.read()
    name_result = re.search('<Full Name>', line)
    full_name_result = full_name_replace(full_name, name_result.group())
    print full_name_result
    
    model_result = re.search('<Model>', line)
    iphone_model = iphone_model_replace(iphone_model, model_result.group())
    print iphone_model
    
    os_result = re.search('<OS Version>', line)
    ios_version = os_version_replace(ios_version, os_result.group())
    print ios_version
    
    pass_result = re.search('<Passcode>', line)
    iphone_passcode = passcode_replace(iphone_pin, pass_result.group())
    print iphone_passcode
    
    dir_result = re.search('<Directory Name>', line)
    directory = directory_replace(directory_name, dir_result.group())
    print directory
