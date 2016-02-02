#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Info(object):
    """Potplayer play list information building block.

    :param index: integer
    :param abspath: str
    :param played: boolean
    :param duration: integer, total video length in seconds
    :param start: integer, start play from ``start`` seconds
    """
    def __init__(self, index, abspath, played=None, duration=None, start=None):
        self.index = index
        self.abspath = abspath
        self.played = played
        self.duration = duration
        self.start = start

    def __str__(self):
        return self.abspath

    def __repr__(self):
        return "Info(index=%r, abspath=%r, played=%r, duration=%r, start=%r)" % (
            self.index, self.abspath, self.played, self.duration, self.start)

    def to_text(self):
        lines = list()
        lines.append("{0}*file*{1}".format(self.index, self.abspath))
        lines.append("{0}*played*0".format(self.index))
        if self.duration:
            lines.append("{0}*duration2*{1}".format(self.index, self.duration))
        if self.start:
            lines.append("{0}*start*{1}".format(self.index, self.start))
        return "\n".join(lines)

class PlayList(object):
    """Potplayer play list Class. Provide load dump and play list construction
    utility methods.
    """
    header = "﻿DAUMPLAYLIST"
    topindex = "topindex=0"
    ext = ".dpl"
    def __init__(self):
        self.nowplaying = None
        self.nowplaytime = None
        self.items = list()

    def __str__(self):
        lines = list()
        lines.append("{:-^79}".format("PlayList"))
        for info in self.items:
            lines.append(info.abspath)
        lines.append("-" * 79)
        return "\n".join(lines)

    def add(self, path):
        """

        **中文文档**

        添加一个文件到播放列表。
        """
        abspath = os.path.abspath(path)
        if os.path.exists(abspath):
            self.items.append(Info(index=0, abspath=abspath))
        else:
            print("'%s' not exists!" % abspath)

    def add_many(self, path_list):
        """

        **中文文档**

        添加许多文件到播放列表。
        """
        for path in path_list:
            self.add(path)

    def set_nowplaying(self, nowplaying, nowplaytime=None):
        """

        **中文文档**

        设置打开时播放的文件。
        """
        abspath = os.path.abspath(nowplaying)
        if os.path.exists(abspath):
            self.nowplaying = abspath
            if nowplaytime:
                self.nowplaytime = nowplaytime
            else:
                self.nowplaytime = 0
        else:
            print("'%s' not exists!" % abspath)

    def to_text(self):
        """

        **中文文档**

        将数据编码成potplayer可识别的 ``.dpl`` 播放列表文件的文本。
        """

        lines = list()
        lines.append(self.header)
        if self.nowplaying is not None:
            lines.append("playname={0}".format(self.nowplaying))
        if self.nowplaytime is not None:
            lines.append("playtime={0}".format(self.nowplaytime))
        for index, info in enumerate(self.items):
            index += 1
            info.index = index
            lines.append(info.to_text())
        return "\n".join(lines)

    def dump(self, fname):
        """

        **中文文档**

        导出数据到 ``.dpl`` 播放列表文件。
        """
        abspath = fname + self.ext
        with open(abspath, "wb") as f:
            f.write(self.to_text().encode("utf-8"))

    def load(self, abspath):
        """

        **中文文档**

        从 ``.dpl`` 文件中读取playlist中被播放的文件, 并创建一个新PlayList的实例。
        """
        with open(abspath, "rb") as f:
            text = f.read().decode("utf-8")

            playlist = PlayList()
            for line in text.split("\n"):
                if "*file*" in line:
                    playlist.add(line.split("*file*")[-1].strip())

        return playlist