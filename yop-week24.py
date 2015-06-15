# This script continues the work from the yop-week23.py script
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# Version 0.1
# By Tom Yarrish

# First we have some new modules to import

import uuid
from bitstring import BitArray

# This is the function to parse the LNK Flags bitstring

def lnk_flags(flags_to_parse):
    flags = { 0: "HasLinkTargetIDList",
             1: "HasLinkInfo",
             2: "HasName",
             3: "HasRelativePath",
             4: "HasWorkingDir",
             5: "HasArguments",
             6: "HasIconLocation",
             7: "IsUnicode",
             8: "ForceNoLinkInfo",
             9: "HasExpString",
             10: "RunInSeparateProcess",
             11: "Unused1",
             12: "HasDarwinID",
             13: "RunAsUser",
             14: "HasExpIcon",
             15: "NoPidlAlias",
             16: "Unused2",
             17: "RunWithShimLayer",
             18: "ForceNoLinkTrack",
             19: "EnableTargetMetadata",
             20: "DisableLinkPathTracking",
             21: "DisableKnownFolderTracking",
             22: "DisableKnownFolderAlias",
             23: "AllowLinkToLink",
             24: "UnaliasOnSave",
             25: "PreferEnvironmentPath",
             26: "KeepLocalIDListForUNCTarget"}

    for count, items in enumerate(flags_to_parse):
        if int(items) == 1:
            print "{} is set.".format(flags[count])
        else:
            continue


# So we have some changes to the lnk_file_header function
# First, we change line 26 to the following, which parses the UUID:
header_clsid = header_data[4:20]
lnk_header_clsid = uuid.UUID(bytes_le=header_clsid)

# This section replaces line 27
# These two lines will parse out the individual bits in the flags section
lnk_header_flags = struct.unpack("<I", header_data[20:24])
lnk_header_flags_bits = BitArray(hex(lnk_header_flags[0]))

# These lines replace lines 45 and 46
print "Header CLSID: {}".format(lnk_header_clsid)
print "\nFlags:"
lnk_flags(lnk_header_flags_bits.bin)
