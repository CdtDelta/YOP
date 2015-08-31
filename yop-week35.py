# This is one of my earlier tests when I was working on my OSX File Vault
# brute force script.  This just mounts an ewf image.
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# Version 1.0
# Tom Yarrish

import sys
import argparse
from subprocess import Popen

parser = argparse.ArgumentParser()
parser.add_argument('-i', dest='image_name', required=True, help='Name of image file to mount')
parser.add_argument('-l', dest='L01_image', required=False, help='Indicate if this is an L01 image')
parser.add_argument('-m', dest='mount_point', required=True, help='Where to mount the image')
args = parser.parse_args()

print "Trying to mount {}".format(args.image_name)
if args.L01_image == True:
    proc = Popen(['/usr/local/bin/ewfmount', '-f files', args.image_name, args.mount_point])
    proc.wait()
    if proc.returncode == 0:
        print "Image mounted."
    else:
        print "Unable to mount image...exiting"
        sys.exit()
else:
    proc = Popen(['/usr/local/bin/ewfmount', args.image_name, args.mount_point])
    proc.wait()
    if proc.returncode == 0:
        print "Image mounted."
    else:
        print "Unable to mount image...exiting"
        sys.exit()
