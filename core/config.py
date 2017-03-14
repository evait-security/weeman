#
# config.py - config variables
#
# This file if part of weeman project
#
# See 'LICENSE' file for copying
#


import os
import sys

__author__ = "Hypsurus <hypsurus@mail.ru>"
__version__ = "1.7.1"
__codename__ = "end"

say = "There are plenty of fish in the sea"

def history_getkey(key):
    try:
        history = open("history.log", "r").readlines()
    except Exception as e:
        return 0
    if history == None:
        return 0
    for line in history:
        if line.startswith("\n") or line.startswith("#"):
            pass
        (skey,value) = line.split(" = ")
        if skey == key:
            return str(value[:-1])
    return 0

url = history_getkey("url") or None
port = int(history_getkey("port")) or int(8080)
action_url = history_getkey("action_url") or None
user_agent = history_getkey("user_agent") or "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"
html_file = None
external_js = history_getkey("external_js") or None
quiet_mode = False
