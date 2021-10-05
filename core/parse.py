# -*- coding: utf-8 -*-
# @Time    : 2021/10/1 15:45
# @Author  : Hanqi
# @FileName: parse.py
# @Software: PyCharm


import os


def parse_m3u8(index_path, new_index_path, key_path, ts_path):
    if os.path.exists(new_index_path):
        return

    with open(index_path, 'r') as f:
        lines = f.readlines()

    for file in os.listdir(ts_path):
        for i in range(len(lines)):
            if file in lines[i]:
                lines[i] = "tmp/{}".format(file) + '\n'

    for i in range(len(lines)):
        if 'URI' in lines[i]:
            lines[i] = '{}"key.key"\n'.format(lines[i][:lines[i].find("URI") + 4])

    with open(new_index_path, 'w') as f:
        f.writelines(lines)


def output_mp4(new_index_path, output):
    output_path = output + ".mp4"
    if os.path.exists(output_path):
        return

    cmd = 'ffmpeg -allowed_extensions ALL -protocol_whitelist "file,http,https,tls,crypto,tcp" -i {} -acodec copy ' \
          '-vcodec copy -f mp4 {}'.format(new_index_path, output_path)

    os.system(cmd)
