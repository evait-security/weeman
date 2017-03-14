#
# misc.py - usefull functions
#
# This file if part of weeman project
#
# See 'LICENSE' file for copying
#


import sys
import time

# help options
help_options = {"url" : "The URL of the webpage, with https:// or http://.",
                "action_url" : "The form action URL of the webpage.",
                "port" : "The port weeman will listen",
                "user_agent" : "Weeman User-Agent string.",
                "html_file" : "allows you to load html file instead of URL.",
                "external_js" : "allows you to include an external script to be loaded.",
                "set" : "Set value for option, set <option> <value>.",
                "run" : "Run the server, alias = \'r\'.",
                "clear" : "clear the screen.",
                "help" : "We all know (:",
                "quit" : "quit, alias = \'q\'."}


def printt(s, msg):
    
    if s == 1:
        print("\033[01;31mError: %s\033[00m")
        sys.exit(1)
    elif s == 2:
        print("[%s]\033[01;32m %s\033[00m" %(time.strftime("%H:%M:%S"),msg))
    elif s == 3:
        print("\033[01;37m[%s] %s\033[00m" %(time.strftime("%H:%M:%S"),msg))
    else:
        print("\033[01;37m[%s] %s\033[00m" %(time.strftime("%H:%M:%S"),msg))

def print_help():

    print("\t\033[01;32m")
    print("\tshow        : show default settings.")
    print("\tset         : set value for option (set <option> <value>).")
    print("\trun         : start the server.")
    print("\tclear       : clear screen.")
    print("\thelp        : show help or (help <option>.)")
    print("\tframework   : load the modules framework.")
    print("\tquit        : quit.\033[00m")

def print_help_option(option):

    found = 0
    for opt in help_options.items():
        if opt[0] == option:
            found = 1
            printt(32, "%s - %s" %(option, opt[1]))
    if not found:
        printt(3, "Error: option \'%s\' not found." %option)

def isroot():

    if os.getuid() !=0:
        printt(1,"Please run weeman as root.")
