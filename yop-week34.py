# This script is the same as my week 20 script, but I've added a simple GUI to the interface
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# Version 1.0
# Tom Yarrish
#
# TODO: Add code to clean up the screen every time you open a new file
# TODO: Write it with actual OOP code

import Tkinter
import ttk
from tkFileDialog import askopenfile
import struct
import ScrolledText
import sys

def prefetch_format(format_type):
    if format_type == "0x11":
        print "Windows XP/2003"
    elif format_type == "0x17":
        print "Windows Vista/7"
    elif format_type == "0x1a":
        print "Windows 8.1"
    return

def prefetch_header_parse(header):
    prefetch_header_format = struct.unpack("<L", header[0:4])
    prefetch_header_sig = header[4:8]
    prefetch_header_unk = struct.unpack("<L", header[8:12])
    prefetch_header_file_size = struct.unpack("<L", header[12:16])
    prefetch_header_file_name = header[16:76]
    prefetch_header_hash = struct.unpack("<L", header[76:80])
    prefetch_header_flags = struct.unpack("<L", header[80:84])
    print "Prefetch Header Information:\n"
    print "Header format: {}".format(hex(prefetch_header_format[0]))
    prefetch_format(hex(prefetch_header_format[0]))
    print "Header Signature: {}".format(prefetch_header_sig)
    print "Unknown: {}".format(hex(prefetch_header_unk[0]))
    print "Prefetch File Size: {}".format(prefetch_header_file_size[0])
    print "Prefetch File Name: {}".format(prefetch_header_file_name)
    print "Prefetch Hash: {}".format(hex(prefetch_header_hash[0]))
    print "Unknown: {}".format(hex(prefetch_header_flags[0]))
    return

def openfile():
    prefetch_file = askopenfile(parent=root)
    prefetch_header = prefetch_file.read()
    header = prefetch_header[:84]
    prefetch_header_parse(header)    

# Thanks to Mouse vs Python for this function
# http://www.blog.pythonlibrary.org/2014/07/14/tkinter-redirecting-stdout-stderr/
# Make sure to buy his book!
class RedirectText(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, text_ctrl):
        """Constructor"""
        self.output = text_ctrl
 
    #----------------------------------------------------------------------
    def write(self, string):
        """"""
        self.output.insert(Tkinter.END, string)

root = Tkinter.Tk()
root.title("Windows LNK File Header Parser")
root.geometry("300x300")

# Insert a menu bar on the main window
menubar = Tkinter.Menu(root)
root.config(menu=menubar)

# Create a menu button labeled "File" that brings up a menu
filemenu = Tkinter.Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open', command=openfile)
filemenu.add_separator()
filemenu.add_command(label='Quit', command=sys.exit)

# The following code creates a frame for the output.
# Again thanks to the Mouse vs Python blog for the assist
# First we set up the frame
output_frame = Tkinter.Frame(root)
output_frame.pack()
# Then we set up the text output
output_text = ScrolledText.ScrolledText(output_frame)
output_text.pack()
output_redir = RedirectText(output_text)
# Now we redirect the output to the new frame
sys.stdout = output_redir

root.mainloop()