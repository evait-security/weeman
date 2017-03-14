#
# whois_ip.py - weeman module - WHO-IS IP
#
# Copyright (c) 2015 Hypsurus <hypsurus@mail.ru>
#
# See 'LICENSE' for module copying
#


from socket import *
from core.misc import printt 

# Module global configs
MODULE_AUTHOR = "Hypsurus <hypsurus@mail.ru>"
MODULE_LICENSE = "GPLv3"
MODULE_VERSION = "0.1"
MODULE_DATE = "18-12-2015"
# Keep it short
MODULE_DE   = "WHO-IS IP."

class whois(object):
    """ Get links from HTML page """
    def __init__(self, ip_addr):
        self.ip_addr = ip_addr

    def fetch(self):
        """ Create connection o the whois server """
        s = socket(AF_INET, SOCK_STREAM)
        code = s.connect_ex(("whois.ripe.net", 43))
        s.settimeout(2)
        if code != 0:
            printt(3, "Failed to connect to the whois server.")
            return

        data = s.recv(1024)
        print(data)
        s.send("%s -B\r\n" % (self.ip_addr) )
        while data:
            data = s.recv(8192)
            print(data)
        s.close()

def main(args):
    try:
        ip_addr = args[2]
    except IndexError:
        print("Usage: whois_ip [IP].")
        return # Exit main()

    run = whois(ip_addr)
    run.fetch()
