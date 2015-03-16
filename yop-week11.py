# This is my attempt at a Apple FileVault Recovery Key brute force tool
# This is supposed to be used with the libfvde library from here:
# https://github.com/libyal/libfvde


import os
import string
import random
import argparse
from subprocess import Popen

# This function creates the random 4 character key to be used in the larger key
def fvde_key():
    chars = string.letters.upper() + string.digits
    pwdSize = 4
    key_attempt = ''.join((random.choice(chars)) for x in range(pwdSize))
    return key_attempt

# This is just setting up the different arguments to use for the program
parser = argparse.ArgumentParser()
parser.add_argument('-o', dest='offset', required=True, help='Offset of image (if you use mmls multiply by sector size) to pass to fvdemount')
parser.add_argument('-e', dest='recovery', required=True, help='Path to the recovery key to use')
parser.add_argument('-i', dest='image_loc', required=True, help='Path to the encrypted image mount point')
parser.add_argument('-m', dest='mount_point', required=True, help='Mount point for decrypted image')
args = parser.parse_args()

locked = True   # This is just a control for the overall loop

while locked == True:
    decryption_key = "-".join([fvde_key(),fvde_key(),fvde_key(),fvde_key(),fvde_key(),fvde_key()])
    print "Trying {} for key...".format(decryption_key)
    # Note depending on where you install libfvde, you may have to change the following line
    proc = Popen(['/usr/local/bin/fvdemount', '-o', args.offset, '-e', args.recovery, '-r', decryption_key, args.image_loc, args.mount_point])
    proc.wait()     # I haven't tested yet that this part is necessary
    if proc.returncode == 0:
        print "We've found the key!  And it is {}".format(decryption_key)
        locked = False
    else:
        print "Not the correct decryption key, retrying..."
