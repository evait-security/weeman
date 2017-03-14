#
# is_website_up.py - weeman module - checks is website is online using extrnal source
#
# Copyright (c) 2015 Hypsurus <hypsurus@mail.ru>
#
# See 'LICENSE' for module copying
#

import urllib2
from core.misc import printt 

# Module global configs
MODULE_AUTHOR = "Hypsurus <hypsurus@mail.ru>"
MODULE_LICENSE = "GPLv3"
MODULE_VERSION = "0.1"
MODULE_DATE = "22-11-2015"
# Keep it short
MODULE_DE   = "checks is website up using hackertarget.com API."

class is_website_up(object):
    """ Checks is website is up and running """
    def __init__(self, website):
        self.website = website

    def test_connection(self):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-Agent', 
            "Mozilla/5.0 (iPhone; CPU iPhone OS 9_0 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13A342 Safari/601.1")]
        data = opener.open("http://api.hackertarget.com/nping/?q=%s" % (self.website)).read()
        if data == "error check your api query":
            printt(2, "Looks like \'%s\' is down for everyone." % (self.website))
        else:
            printt(3, "OK! \'%s\' is up and running!" % (self.website))

def main(args):
    try:
        website = args[2]
    except IndexError:
        print("Usage: is_website_up [URL].")
        return # Exit main()
    run = is_website_up(website)
    run.test_connection()



