# This script continues the work from the yop-week23.py script
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# Version 0.1
# By Tom Yarrish

# This function parses the SHOWCOMMAND data

def lnk_show_win(showwin):
    if showwin == hex(0x1):
        return "SW_SHOWNORMAL"
    elif showwin == hex(0x3):
        return "SW_SHOWMAXIMIZED"
    elif showwin == hex(0x7):
        return "SW_SHOWMINNOACTIVE"
    else:
        return "SW_SHOWNORMAL (default)"

# This replaces line 53
print "Show Window Value: {}".format(lnk_show_win(hex(lnk_header_show_window[0])))