# -*- coding: utf-8 -*-
# @Time    : 2021/10/1 16:04
# @Author  : Hanqi
# @FileName: utils.py
# @Software: PyCharm

import shutil
import os

import hashlib


def remove_tmp(path, output):
    if os.path.exists(output + ".mp4"):
        shutil.rmtree(path)


def get_random_tmp_path(url):
    ran = hashlib.sha1(url.encode('utf-8')).hexdigest()
    index_file = ran + "/index.m3u8"
    new_index_file = ran + "/index.m3u8.new"
    key_file = ran + "/key.key"
    ts_files = ran + "/tmp"
    return index_file, new_index_file, key_file, ts_files, ran
