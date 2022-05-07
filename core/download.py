# -*- coding: utf-8 -*-
# @Time    : 2021/10/1 15:31
# @Author  : Hanqi
# @FileName: download.py
# @Software: PyCharm

import os
import requests
from core.utils import _print
from concurrent.futures import ThreadPoolExecutor, as_completed


def download_m3u8(url, output_path):
    if os.path.exists(output_path):
        return

    content = _download(url)

    with open(output_path, 'wb') as f:
        f.write(content)


def download_key(index_path, key_output_path):
    if os.path.exists(key_output_path):
        return

    with open(index_path, "r") as f:
        lines = f.readlines()
    for line in lines:
        if 'key.key' in line:
            url = line[line.find("URI") + 5:-2]

            content = _download(url)

            with open(key_output_path, 'wb') as f:
                f.write(content)


def download_ts(index_path, ts_output_path, m3u8_url, use_gui, max_workers=40):
    pre_url = m3u8_url[:m3u8_url.find("index")]

    urls = []
    with open(index_path, "r") as f:
        lines = f.readlines()
    for line in lines:
        if '.ts' in line and 'http' not in line:
            urls.append(pre_url + line[:-1])
        elif '.ts' in line:
            urls.append(line[:-1])

    executor = ThreadPoolExecutor(max_workers=max_workers)
    all_task = []
    for url in urls:
        all_task.append(executor.submit(_download_ts, url, ts_output_path, ))

    cnt = 0
    for future in as_completed(all_task):
        cnt += 1
        _print("[{}/{}]".format(cnt, len(all_task)), use_gui)


def _download_ts(url, output_path):
    print(url)
    file_name = url.split('/')[-1]
    if file_name in os.listdir(output_path):
        return

    content = _download(url)

    with open('{}/{}'.format(output_path, file_name), 'wb') as f:
        f.write(content)


def _download(url):
    while True:
        try:
            resp = requests.get(url, timeout=30, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
            })
            break
        except:
            continue
    return resp.content
