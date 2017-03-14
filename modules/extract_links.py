#
# extract_links.py - weeman module - extract links from HTML page
#
# Copyright (c) 2015 Hypsurus <hypsurus@mail.ru>
#
# See 'LICENSE' for module copying
#

import urllib2
import re
from core.misc import printt 

# Module global configs
MODULE_AUTHOR = "Hypsurus <hypsurus@mail.ru>"
MODULE_LICENSE = "GPLv3"
MODULE_VERSION = "0.1"
MODULE_DATE = "18-12-2015"
# Keep it short
MODULE_DE   = "Extract links from HTML page."

class Extract(object):
    """ Get links from HTML page """
    def __init__(self, ufile):
        self.ufile = ufile
        self.links = []
    
    def request(self):
        """ Send HTTP request to the target """
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla 5.0 (Linux)')]
        return opener.open(self.ufile).read()

    def extract(self, offline=0):
        """ Extract the links """
        if not offline:
            data = self.request()
        else:
            data = open(self.ufile, "r").read()
        
        self.links = re.findall(r'href=[\'"]?([^\'" >]+)', data)

    def show_links(self):
        """ Show the links """
        if not self.links:
            printt(3, "No links found.")
        else:
            for link in self.links:
                print("[*] %s" % ( link )) 

def main(args):
    try:
        ufile = args[2]
    except IndexError:
        print("Usage: extract_links [URL/FILE].")
        return # Exit main()

    run = Extract(ufile)
    if "://" in ufile:
        run.extract(0)
    else:
        run.extract(1)
    run.show_links()
