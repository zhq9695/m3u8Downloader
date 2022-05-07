# -*- coding: utf-8 -*-
# @Time    : 2021/10/1 16:04
# @Author  : Hanqi
# @FileName: utils.py
# @Software: PyCharm

import shutil
import os
import hashlib
from tkinter import *


def remove_tmp(path, output):
    if os.path.exists(output + ".mp4"):
        shutil.rmtree(path)
        return True
    else:
        return False


def get_random_tmp_path(url):
    ran = hashlib.sha1(url.encode('utf-8')).hexdigest()
    index_file = ran + "/index.m3u8"
    new_index_file = ran + "/index.m3u8.new"
    key_file = ran + "/key.key"
    ts_files = ran + "/tmp"
    return index_file, new_index_file, key_file, ts_files, ran


def _print(str, output_text):
    if output_text is None:
        print(str)
    else:
        output_text.configure(state=NORMAL)
        output_text.insert(INSERT, str + "\n")
        output_text.configure(state=DISABLED)
        output_text.see(END)
