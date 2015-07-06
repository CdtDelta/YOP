# This script continues the work from the yop-week23.py script
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# Version 0.1
# By Tom Yarrish
#
# This part of the code parses out the Hotkey for a Windows LNK file

# This function parses the High Byte section of the hotkey value

def lnk_hot_key_high(hotkey_high):
    hotkey = { "0x0" : "None",
              "0x1" : "Shift",
              "0x2" : "Ctrl",
              "0x3" : "Shift + Ctrl",
              "0x4" : "Alt",
             "0x5" : "Shift + Alt", 
             "0x6" : "Ctrl + Alt" }
    bits_hotkey = BitArray(hex(hotkey_high))
    return hotkey[str(bits_hotkey)]

# This function parses out the Low Byte section of the hotkey value

def lnk_hot_key_low(hotkey):
    return chr(hotkey)   

# This kicks off parsing the hotkey value of the LNK file

def lnk_hot_key_parse(hotkey):
    hotkey_one = lnk_hot_key_high(hotkey[1])
    hotkey_two = lnk_hot_key_low(hotkey[0])
    return hotkey_one, hotkey_two

# This line replaces line 42

lnk_header_hot_key = struct.unpack("<2B", header_data[64:66])

# This line goes after line 42
    
hot_key = lnk_hot_key_parse(lnk_header_hot_key)

# This line replaces line 54

print "Hot Key: {} {}".format(hot_key[0], hot_key[1])
