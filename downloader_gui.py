# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 9:48
# @Author  : Hanqi
# @FileName: downloader_gui.py
# @Software: PyCharm

import threading
from tkinter import *
from concurrent.futures import ThreadPoolExecutor

from downloader import Downloader


class DownloaderGUI:
    def __init__(self):
        self.tk = Tk()

        self.record_path = "record/record"
        self.data = []
        self.thread = None

        self.tk.title("m3u8Downloader (dev by: Hanqi)")
        self.font = ('微软雅黑', 12)

        self.url_frame = None
        self.url_label = None
        self.url_entry = None

        self.name_frame = None
        self.name_label = None
        self.name_entry = None

        self.btn_frame = None
        self.add_btn = None
        self.clear_btn = None
        self.start_btn = None

        self.text_frame = None
        self.text = None

        self.info_frame = None
        self.info = None

        self.pack_url_frame()
        self.pack_name_frame()
        self.pack_btn_frame()
        self.pack_text_frame()
        self.pack_info_frame()

        self.init_record()

        self.tk.protocol('WM_DELETE_WINDOW', self.close_window)
        self.tk.mainloop()

    def pack_url_frame(self):
        self.url_frame = Frame(self.tk)
        self.url_label = Label(self.url_frame, text="url: ", font=self.font)
        self.url_entry = Entry(self.url_frame, font=self.font)

        self.url_frame.pack(side=TOP, fill=X, expand=YES, padx=5, pady=5)
        self.url_label.pack(side=LEFT, ipadx=2, ipady=2)
        self.url_entry.pack(side=LEFT, fill=X, expand=YES, ipadx=2, ipady=2)

    def pack_name_frame(self):
        self.name_frame = Frame(self.tk)
        self.name_label = Label(self.name_frame, text="name: ", font=self.font)
        self.name_entry = Entry(self.name_frame, font=self.font)

        self.name_frame.pack(side=TOP, fill=X, expand=YES, padx=5, pady=5)
        self.name_label.pack(side=LEFT, ipadx=2, ipady=2)
        self.name_entry.pack(side=LEFT, fill=X, expand=YES, ipadx=2, ipady=2)

    def pack_btn_frame(self):
        self.btn_frame = Frame(self.tk)
        self.add_btn = Button(self.btn_frame, text="ADD", font=self.font, command=self.btn_add_command)
        self.clear_btn = Button(self.btn_frame, text="CLEAR", font=self.font, command=self.btn_clear_command)
        self.start_btn = Button(self.btn_frame, text="START", font=self.font, command=self.btn_start_command)

        self.btn_frame.pack(side=TOP, fill=X, expand=YES, padx=5, pady=5)
        self.add_btn.pack(side=LEFT, fill=X, expand=YES, padx=2, ipadx=2, ipady=2)
        self.clear_btn.pack(side=LEFT, fill=X, expand=YES, padx=2, ipadx=2, ipady=2)
        self.start_btn.pack(side=LEFT, fill=X, expand=YES, padx=2, ipadx=2, ipady=2)

    def pack_text_frame(self):
        self.text_frame = Frame(self.tk)
        self.text = Text(self.text_frame, font=self.font, height=5)

        self.text.configure(state=DISABLED)

        self.text_frame.pack(side=TOP, fill=BOTH, expand=YES, padx=5, pady=5)
        self.text.pack(side=LEFT, fill=BOTH, expand=YES, ipadx=2, ipady=2)

    def pack_info_frame(self):
        self.info_frame = Frame(self.tk)
        self.info = Text(self.info_frame, font=self.font, height=10)

        # scroll = Scrollbar()
        # scroll.config(command=self.info.yview)
        # self.info.config(yscrollcommand=scroll.set)

        self.info.configure(state=DISABLED)

        self.info_frame.pack(side=TOP, fill=BOTH, expand=YES, padx=5, pady=5)
        self.info.pack(side=LEFT, fill=BOTH, expand=YES, ipadx=2, ipady=2)

    def init_record(self):
        with open(self.record_path, "r", encoding="UTF-8") as f:
            lines = f.readlines()
        for line in lines:
            t = line[:-1].split(",")
            url = t[0]
            name = t[1]

            self.text.configure(state=NORMAL)
            self.text.insert(INSERT, name + " | " + url + "\n")
            self.text.configure(state=DISABLED)

            self.data.append((url, name))

    def close_window(self):
        self.tk.destroy()

    def btn_add_command(self):
        url = self.url_entry.get()
        name = self.name_entry.get()

        self.text.configure(state=NORMAL)
        self.text.insert(INSERT, name + " | " + url + "\n")
        self.text.configure(state=DISABLED)

        self.data.append((url, name))

        with open(self.record_path, "a+", encoding="UTF-8") as f:
            f.write(url + "," + name + "\n")

    def btn_clear_command(self):
        self.text.configure(state=NORMAL)
        self.text.delete(1.0, END)
        self.text.configure(state=DISABLED)

        self.data = []

        with open(self.record_path, "w", encoding="UTF-8") as f:
            pass

    def btn_start_command(self):
        executor = ThreadPoolExecutor(max_workers=1)
        for url, name in self.data:
            executor.submit(Downloader, url, name, self.info, )


if __name__ == '__main__':
    DownloaderGUI()
