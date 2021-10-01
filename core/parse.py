# -*- coding: utf-8 -*-
# @Time    : 2021/10/1 15:45
# @Author  : Hanqi
# @FileName: parse.py
# @Software: PyCharm


import os


def parse_m3u8():
    with open("index.m3u8", 'r') as f:
        lines = f.readlines()

    for file in os.listdir('tmp'):
        for i in range(len(lines)):
            if file in lines[i]:
                lines[i] = "tmp/{}".format(file) + '\n'

    for i in range(len(lines)):
        if 'URI' in lines[i]:
            lines[i] = lines[i][:lines[i].find("URI") + 4] + '"key.key"' + '\n'

    new_path = "index.m3u8.new"
    with open(new_path, 'w') as f:
        f.writelines(lines)


def output_mp4(output):
    cmd = 'ffmpeg -allowed_extensions ALL -protocol_whitelist "file,http,https,tls,crypto,tcp" -i index.m3u8.new -acodec copy -vcodec copy -f mp4 {}.mp4'.format(
        output)

    os.system(cmd)
