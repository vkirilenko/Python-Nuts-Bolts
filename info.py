#!/usr/bin/env python3

import os
import platform

def get_info():
    PID = os.getpid()
    UNAME = 'root' if os.path.expanduser('~') == '/root' else os.getenv('SUDO_USER', os.getenv('USER'))
    OSNAME = platform.system()
    OSVERSION = platform.release()
    return [PID, UNAME, OSNAME, OSVERSION]

if __name__ == "__main__":
    list_of_sysvals = get_info()
    print(f"This script has the following PID: {list_of_sysvals[0]}.")
    print(f"It was ran by {list_of_sysvals[1]} to work happily on {list_of_sysvals[2]}-{list_of_sysvals[3]}.")
