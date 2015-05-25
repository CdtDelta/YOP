# These are updates to the YOP - Week 20 Script.  Where we start
# to parse out the file info section of the prefetch file.
# These code snippets need to be incorporated into the week 20
# script to work.
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
#
# By Tom Yarrish
#
# First we change the prefetch_format function to return the OS
# instead of printing it.
# This replaces lines 13-20

def prefetch_format(format_type):
    if format_type == "0x11":
        return "Windows XP"
    elif format_type == "0x17":
        return "Windows 7"
    elif format_type == "0x1a":
        return "Windows 8"
    return

# These next two functions parse out the file info for
# Windows XP and Windows 7 Prefetch files.
# These two functions should be placed right after the
# prefetch_header_parse header (line 40).

def winxp_file_info(file_info):
    metrics_offset = struct.unpack("<L", file_info[0:4])
    no_metrics = struct.unpack("<L", file_info[4:8])
    trace_chains = struct.unpack("<L", file_info[8:12])
    no_trace_chains = struct.unpack("<L", file_info[12:16])
    filename_str_offset = struct.unpack("<L", file_info[16:20])
    filename_str_size = struct.unpack("<L", file_info[20:24])
    volume_info = struct.unpack("<L", file_info[24:28])
    no_volumes = struct.unpack("<L", file_info[28:32])
    volume_info_size = struct.unpack("<L", file_info[32:36])
    last_run_time = struct.unpack("<Q", file_info[36:44])
    run_count = struct.unpack("<L", file_info[60:64])
    print "Metrics Array Offset: {}".format(hex(metrics_offset[0]))
    print "No. of Metrics: {}".format(no_metrics[0])
    print "Trace Chains Offset: {}".format(trace_chains[0])
    print "No. of Trace Chains: {}".format(no_trace_chains[0])
    print "Filename String Offset: {}".format(filename_str_offset[0])
    print "Filename String Size: {}".format(filename_str_size[0])
    print "Volume Info: {}".format(volume_info[0])
    print "No. of Volumes: {}".format(no_volumes[0])
    print "Volume Info Size: {}".format(volume_info_size[0])
    print "Last Run Time: {}".format(last_run_time[0])
    print "Run Count: {}".format(run_count[0])
    return

def win7_file_info(file_info):
    metrics_offset = struct.unpack("<L", file_info[0:4])
    no_metrics = struct.unpack("<L", file_info[4:8])
    trace_chains = struct.unpack("<L", file_info[8:12])
    no_trace_chains = struct.unpack("<L", file_info[12:16])
    filename_str_offset = struct.unpack("<L", file_info[16:20])
    filename_str_size = struct.unpack("<L", file_info[20:24])
    volume_info = struct.unpack("<L", file_info[24:28])
    no_volumes = struct.unpack("<L", file_info[28:32])
    volume_info_size = struct.unpack("<L", file_info[32:36])
    last_run_time = struct.unpack("<Q", file_info[44:52])
    run_count = struct.unpack("<L", file_info[68:72])
    print "Metrics Array Offset: {}".format(hex(metrics_offset[0]))
    print "No. of Metrics: {}".format(no_metrics[0])
    print "Trace Chains Offset: {}".format(trace_chains[0])
    print "No. of Trace Chains: {}".format(no_trace_chains[0])
    print "Filename String Offset: {}".format(filename_str_offset[0])
    print "Filename String Size: {}".format(filename_str_size[0])
    print "Volume Info: {}".format(volume_info[0])
    print "No. of Volumes: {}".format(no_volumes[0])
    print "Volume Info Size: {}".format(volume_info_size[0])
    print "Last Run Time: {}".format(last_run_time[0])
    print "Run Count: {}".format(run_count[0])
    return


# Here we update the process of opening the prefetch file
# We will still parse out the header, but now we're going to
# call different functions based on the OS type of Prefetch
# file
# This section replaces lines 46-49

with open(args.prefetch_file, 'rb') as prefetch:
    prefetch_file = prefetch.read()
    prefetch_header = prefetch_file[:84]
    windows_os = prefetch_header_parse(prefetch_header)
    if windows_os == "Windows XP":
        file_info = prefetch_file[84:152]
        winxp_file_info(file_info)
    elif windows_os == "Windows 7":
        file_info = prefetch_file[84:240]
        win7_file_info(file_info)
    elif windows_os == "Windows 8":
        file_info = prefetch_file[84:308]
        win8_file_info(file_info)
