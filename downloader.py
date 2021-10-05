# -*- coding: utf-8 -*-
# @Time    : 2021/10/1 15:32
# @Author  : Hanqi
# @FileName: downloader.py
# @Software: PyCharm


import os

from core.download import download_m3u8, download_ts, download_key
from core.parse import parse_m3u8, output_mp4
from core.utils import remove_tmp, get_random_tmp_path


class Downloader:
    def __init__(self, m3u8_url, output_path):
        self.m3u8_url = m3u8_url
        self.output_path = output_path

        self.index_path, self.new_index_path, \
        self.key_path, self.ts_path, self.ran = get_random_tmp_path(m3u8_url)

        if not os.path.exists(self.ran):
            os.mkdir(self.ran)
        if not os.path.exists(self.ts_path):
            os.mkdir(self.ts_path)

        self.do()

    def do(self):
        print("Download m3u8 file.")
        download_m3u8(self.m3u8_url, self.index_path)

        print("Download key file.")
        download_key(self.index_path, self.key_path)

        print("Download ts files.")
        download_ts(self.index_path, self.ts_path, 40)

        print("Parse m3u8 file.")
        parse_m3u8(self.index_path, self.new_index_path, self.key_path, self.ts_path)

        print("Output mp4.")
        output_mp4(self.new_index_path, self.output_path)

        print("Remove tmp files.")
        remove_tmp(self.ran, self.output_path)

        print("Finish!")


if __name__ == '__main__':
    Downloader("https://video.dious.cc/20200728/hS0gQJm7/2000kb/hls/index.m3u8", "TheWalkingDeadS03E14")
