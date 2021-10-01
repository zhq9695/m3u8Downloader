# -*- coding: utf-8 -*-
# @Time    : 2021/10/1 15:31
# @Author  : Hanqi
# @FileName: download.py
# @Software: PyCharm

import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


def download_m3u8(url):
    content = _download(url)

    with open("index.m3u8", 'wb') as f:
        f.write(content)


def download_key():
    with open("index.m3u8", "r") as f:
        lines = f.readlines()
    for line in lines:
        if 'URI' in line:
            url = line[line.find("URI") + 5:-2]

            content = _download(url)

            with open("key.key", 'wb') as f:
                f.write(content)


def download_ts(max_workers=40):
    urls = []
    with open("index.m3u8", "r") as f:
        lines = f.readlines()
    for line in lines:
        if '.ts' in line:
            urls.append(line[:-1])

    executor = ThreadPoolExecutor(max_workers=max_workers)
    all_task = []
    for url in urls:
        all_task.append(executor.submit(_download_ts, (url)))

    cnt = 0
    for future in as_completed(all_task):
        cnt += 1
        print("[{}/{}]".format(cnt, len(all_task)))


def _download_ts(url):
    file_name = url.split('/')[-1]
    if file_name in os.listdir("tmp"):
        return

    content = _download(url)

    with open('tmp/{}'.format(file_name), 'wb') as f:
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
