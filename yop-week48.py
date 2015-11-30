# This script continues on parsing out the Norton NPE
# log format.  Infections and Suspicious Items summary only
#
# by Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html

from bs4 import BeautifulSoup
import itertools
import argparse

# Usual stuff to get the file we want to parse
parser = argparse.ArgumentParser()
parser.add_argument('-f', dest = 'xml_file', help = 'NPE Log File to parse')
args = parser.parse_args()

soup = BeautifulSoup(open(args.xml_file))

# We initialize our dictionary to store the values
infections = {}

# Here we walk through the Infections Detected section to get a quick look at
# anything we may want to dig into deeper.
for infect in soup.find_all('infections_detected'):
    subsection = { 'Drivers' : infect.drivers.attrs,
        'Services' : infect.services.attrs,
        'Processes' : infect.processes.attrs,
        'Layered Service Providers' : infect.layered_service_providers.attrs,
        'Desktop Shortcuts' : infect.desktop_shortcuts.attrs,
         'Autorun Files' : infect.autorun_files.attrs,
         'Startup Items' : infect.startup_items.attrs,
         'BHO' : infect.browser_helper_objects.attrs,
         'Browser Toolbars' : infect.browser_toolbars.attrs,
         'Browser Plugins' : infect.browser_plugins.attrs,
         'Shell Extensions' : infect.shell_extensions.attrs,
         'Explorer Plugins' : infect.explorer_plugins.attrs,
         'Directories' : infect.directories.attrs,
         'Files' : infect.files.attrs,
         'System Settings' : infect.system_settings.attrs
        }
    infections.update(subsection)

# And then we just print out what's there.
print "Infections Detected Summary:\n"
for keys, values in sorted(infections.iteritems()):
    print "{} -> {}".format(keys, values['count'])

# Now we go through the Suspicious Items section
# Basically the same code
suspicious = {}

for suspect in soup.find_all('suspicious_items'):
    subsection = { 'Drivers' : suspect.drivers.attrs,
        'Services' : suspect.services.attrs,
        'Processes' : suspect.processes.attrs,
        'Layered Service Providers' : suspect.layered_service_providers.attrs,
        'Desktop Shortcuts' : suspect.desktop_shortcuts.attrs,
         'Autorun Files' : suspect.autorun_files.attrs,
         'Startup Items' : suspect.startup_items.attrs,
         'BHO' : suspect.browser_helper_objects.attrs,
         'Browser Toolbars' : suspect.browser_toolbars.attrs,
         'Browser Plugins' : suspect.browser_plugins.attrs,
         'Shell Extensions' : suspect.shell_extensions.attrs,
         'Explorer Plugins' : suspect.explorer_plugins.attrs,
         'Directories' : suspect.directories.attrs,
         'Files' : suspect.files.attrs,
         'System Settings' : suspect.system_settings.attrs
        }
    suspicious.update(subsection)

# And then again we just print out what's there.
print "\nSuspicious Items Summary:\n"
for keys, values in sorted(suspicious.iteritems()):
    print "{} -> {}".format(keys, values['count'])
