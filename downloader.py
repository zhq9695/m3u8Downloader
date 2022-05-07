# -*- coding: utf-8 -*-
# @Time    : 2021/10/1 15:32
# @Author  : Hanqi
# @FileName: downloader.py
# @Software: PyCharm


import os

from core.download import download_m3u8, download_ts, download_key
from core.parse import parse_m3u8, output_mp4
from core.utils import remove_tmp, get_random_tmp_path, _print


class Downloader:
    def __init__(self, m3u8_url, output_path, use_gui=None):
        self.m3u8_url = m3u8_url
        self.output_path = output_path
        self.use_gui = use_gui

        if os.path.exists(output_path + ".mp4"):
            _print("Exists!", self.use_gui)
            return

        self.index_path, self.new_index_path, \
            self.key_path, self.ts_path, self.ran = get_random_tmp_path(
                m3u8_url)

        if not os.path.exists(self.ran):
            os.mkdir(self.ran)
        if not os.path.exists(self.ts_path):
            os.mkdir(self.ts_path)

        self.do()

    def do(self):
        _print("Download m3u8 file.", self.use_gui)
        download_m3u8(self.m3u8_url, self.index_path)

        _print("Download key file.", self.use_gui)
        download_key(self.index_path, self.key_path)

        _print("Download ts files.", self.use_gui)
        download_ts(self.index_path, self.ts_path,
                    self.m3u8_url, self.use_gui, 40)

        _print("Parse m3u8 file.", self.use_gui)
        parse_m3u8(self.index_path, self.new_index_path,
                   self.key_path, self.ts_path)

        _print("Output mp4.", self.use_gui)
        output_mp4(self.new_index_path, self.output_path)

        _print("Remove tmp files.", self.use_gui)
        flag = remove_tmp(self.ran, self.output_path)

        if flag:
            _print("Success!", self.use_gui)
        else:
            _print("Fail!", self.use_gui)


if __name__ == '__main__':
    Downloader("https://b-hls-19.strpst.com/hls/37598507/37598507.m3u8", "123")
