#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
potplayer unittest.
"""

from __future__ import print_function

import os
import unittest

from potplayer import PlayList

class Unittest(unittest.TestCase):
    def test_all(self):
        playlist = PlayList()
        dir_path = r"files"
        for path in os.listdir(dir_path):
            abspath = os.path.join(dir_path, path)
            playlist.add(abspath)
        playlist.set_nowplaying(r"files\life_goes_on.jpg", nowplaytime=5)
        playlist.dump("play")
        
        playlist.load("play.dpl")
        print(playlist.to_text())
        
unittest.main()