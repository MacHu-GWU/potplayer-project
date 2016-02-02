#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import site
import subprocess

# If you didn't install PotPlayer to default path,
# This is your custom path to PotPlayer executable file.
EXECUTABLE_PATH = None

def find_executable():
    """Automatically find PotPlayer executable file path and process name.
    It depends on your system.
    """
    execute_file = os.path.join(
        site.getsitepackages()[1], "potplayer", "execute.py")

    x86 = r"C:\Program Files (x86)\DAUM\PotPlayer\PotPlayerMini.exe"
    x64 = r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"
    if os.path.exists(x86):
        return x86, os.path.basename(x86)
    elif os.path.exists(x64):
        return x64, os.path.basename(x64)
    else:
        try:
            process_name = os.path.basename(EXECUTABLE_PATH)
            if process_name not in ["PotPlayerMini.exe", "PotPlayerMini64.exe"]:
                raise ValueError("Cannot find potplayer executable! "
                                 "Please edit '%s' to add the valid path.")
            return EXECUTABLE_PATH, process_name
        except:
            raise ValueError("Cannot find potplayer executable! "
                             "Please edit '%s' to add the valid path.")

def run(path):
    """Open a playlist/a video/a audio/a image with PotPlayer.
    """
    executable, _ = find_executable()
    abspath = os.path.abspath(path)
    subprocess.call('"%s" "%s"' % (executable, abspath))

def kill():
    """Kill PotPlayer.
    """
    _, process_name = find_executable()
    subprocess.call("TASKKILL /F /IM %s" % process_name)