#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
from configobj import ConfigObj
import os
import sys

config_file = sys.argv[1]

if os.path.exists(config_file):
    print "File exists"
    config = ConfigObj(config_file)
    vxshare_no = int(config['last_vxshare_num'])
else:
    print "File doesn't exist"
    config = ConfigObj()
    config.filename = config_file
    config['last_vxshare_num'] = 0
    vxshare_no = int(config['last_vxshare_num'])
    config.write()
