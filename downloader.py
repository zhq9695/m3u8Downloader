# -*- coding: utf-8 -*-
# @Time    : 2021/10/1 15:32
# @Author  : Hanqi
# @FileName: downloader.py
# @Software: PyCharm


import os

from core.download import download_m3u8, download_ts, download_key
from core.parse import parse_m3u8, output_mp4
from core.utils import remove_tmp


class Downloader:
    def __init__(self, m3u8_url, output_name):
        if not os.path.exists("tmp"):
            os.mkdir("tmp")

        self.m3u8_url = m3u8_url
        self.output_name = output_name

        self.do()

    def do(self):
        print("Download m3u8 file.")
        download_m3u8(self.m3u8_url)

        print("Download key file.")
        download_key()


        print("Download ts files.")
        download_ts(40)

        print("Parse m3u8 file.")
        parse_m3u8()

        print("Output mp4.")
        output_mp4(self.output_name)

        print("Remove tmp files.")
        remove_tmp()

        print("Finish!")


if __name__ == '__main__':
    m3u8_url = ""
    output_name = ""
    Downloader(m3u8_url, output_name)
