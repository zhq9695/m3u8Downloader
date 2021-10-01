# -*- coding: utf-8 -*-
# @Time    : 2021/10/1 16:04
# @Author  : Hanqi
# @FileName: utils.py
# @Software: PyCharm

import shutil
import os


def remove_tmp():
    shutil.rmtree("tmp")
    os.remove("index.m3u8")
    os.remove("index.m3u8.new")
    os.remove("key.key")
