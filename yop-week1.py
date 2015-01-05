# This script parses some of the ntuser.dat autorun keys.
# This is not a full program just a work in progress for a larger program.
#
# Version 1.0 - Tom Yarrish

import sys
from Registry import Registry

# This function parses the SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run key
def run_key(ntuser):
    try:
        user_run_key = ntuser_reg.open("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run")
        print "{}\n".format(user_run_key)
        for value in user_run_key.values():
            print "Program: {}\t Path: {}".format(value.name(), value.value())
    except Registry.RegistryKeyNotFoundException:
        print "Couldn't find Run key. Continuing...\n"

# This function parses the SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce key
def runonce_key(ntuser):
    try:
        user_runonce_key = ntuser_reg.open("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce")
        print "{}\n".format(user_runonce_key)
        for value in user_runonce_key.values():
            print "Program: {}\t Path: {}".format(value.name(), value.value())
    except Registry.RegistryKeyNotFoundException:
        print "Couldn't find RunOnce key. Continuing...\n"

# This function parses the SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce\Setup key        
def runoncesetup_key(ntuser):
    try:
        user_runoncesetup_key = ntuser_reg.open("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce\Setup")
        print "{}\n".format(user_runoncesetup_key)
        for value in user_runoncesetup_key.values():
            print "Program: {}\t Path: {}".format(value.name(), value.value())
    except Registry.RegistryKeyNotFoundException:
        print "Couldn't find RunOnceSetup key. Continuing...\n"

# This function parses the Control Panel\Desktop key, and looks specifically for the SCRNSAVE.EXE value        
def user_desktop_key(ntuser):
    try:
        user_desktop_key = ntuser_reg.open("Control Panel\Desktop")
        print "{}\n".format(user_desktop_key)
        for value in user_desktop_key.values():
            if value.name() == "SCRNSAVE.EXE":
                print "Program: {}\t Path: {}".format(value.name(), value.value())
            else:
                print "SCRNSAVE.EXE not found."
                break
    except Registry.RegistryKeyNotFoundException:
        print "Couldn't find Desktop key. Continuing...\n"
        
# This script parses the SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\run key
def run_nt_key(ntuser):
    try:
        user_runnt_key = ntuser_reg.open("SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\run")
        print "{}\n".format(user_runnt_key)
        for value in user_runnt_key.values():
            print "Program: {}\t Path: {}".format(value.name(), value.value())
    except Registry.RegistryKeyNotFoundException:
        print "Couldn't find Run (Windows NT) key. Continuing...\n"

# This script parses the SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\load key        
def load_nt_key(ntuser):
    try:
        user_loadnt_key = ntuser_reg.open("SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\load")
        print "{}\n".format(user_loadnt_key)
        for value in user_loadnt_key.values():
            print "Program: {}\t Path: {}".format(value.name(), value.value())
    except Registry.RegistryKeyNotFoundException:
        print "Couldn't find Load (Windows NT) key. Continuing...\n"

ntuser_reg_file = sys.argv[1]   # Parse the NTUSER.DAT file specified at the CLI prompt

ntuser_reg = Registry.Registry(ntuser_reg_file) # Open the registry file

# Run the NTUSER.DAT file through each of the functions
run_key(ntuser_reg)
runonce_key(ntuser_reg)
runoncesetup_key(ntuser_reg)
user_desktop_key(ntuser_reg)
run_nt_key(ntuser_reg)