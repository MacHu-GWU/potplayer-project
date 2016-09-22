#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
potplayer unittest.
"""

import os
import sys
import pytest
from pathlib_mate import Path
from potplayer import PlayList, run, kill


def test_IO():
    #
    path_list1 = [p.absolute().abspath for p in Path("files").select_by_ext(".jpg")]
    playlist1 = PlayList()
    playlist1.add_many(path_list1)
    playlist1.nowplaying = path_list1[0]
    playlist1.nowplaytime = 300
    playlist1.dump("playlist1")
    
    path_list2 = [p.absolute().abspath for p in Path("files").select_by_ext(".png")]
    playlist2 = PlayList()
    playlist2.add_many(path_list2)
    playlist2.nowplaying = path_list2[0]
    playlist2.nowplaytime = 600
    playlist2.dump("playlist2")

    
    playlist1 = PlayList.load("playlist1.dpl") # load
    assert len(playlist1) == 3
    assert playlist1.nowplaying == path_list1[0]
    
    playlist2 = playlist1.merge("playlist2.dpl") # merge
    assert len(playlist1) == 6
    assert playlist1.nowplaying == path_list1[0]
    assert len(playlist2) == 3


def test_run():
    try:
        run("playlist1.dpl")
    except Exception as e:
        sys.stderr.write(e)
    

# Clear All
for p in Path(".").select_by_ext(".dpl"):
    p = p.absolute()
    try:
        p.remove()
    except:
        pass


if __name__ == "__main__":
    import os
    pytest.main(["--tb=native", "-s", os.path.basename(__file__)])