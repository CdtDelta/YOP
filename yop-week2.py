# This script is for pulling new hash files from vxshare.com
# Version 1.0
# Tom Yarrish
#
# To do:
# - Create config file to track last file downloaded
# - Add code to replace first six lines with MD5 for X-Ways support


import requests

vxshare_config = open("vshare.cfg", "w")
vxshare_no = 0
vxshare_base_url = "http://virusshare.com/hashes/"
vxshare_file_name = "VirusShare_{:05d}.md5".format(vxshare_no)

vxshare_hash_url = vxshare_base_url + vxshare_file_name
file_is_valid = True

try:
    while file_is_valid == True:
        vxshare_file_name = "VirusShare_{:05d}.md5".format(vxshare_no)
        vxshare_hash_url = vxshare_base_url + vxshare_file_name
        vxshare_requests = requests.get(vxshare_hash_url)
        if vxshare_requests.status_code == 200:
            with open(vxshare_file_name, "w") as hash_file:
                print "Downloading {}...\n".format(vxshare_file_name)
                hash_file.write(vxshare_requests.content)
        else:
            file_is_valid = False
            vxshare_config.write(str(vxshare_no))
        vxshare_no += 1
except Exception,e:
    print str(e)
    
print "All files parsed..."
vxshare_config.close()