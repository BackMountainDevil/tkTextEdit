#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   texteditor.py
@Time    :   2020/11/20 08:58:52
@Author  :   Kearney
@Version :   0.0.0
@Contact :   191615342@qq.com
@License :   GPL 3.0
@Desc    :   A simple text editor created by python3 with tkinter
'''

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
text = tk.Text(root)
text.grid()


def savetext():
    global text
    data = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    if(savelocation):
        with open(savelocation, 'w+', encoding='utf-8') as f:
            f.write(data)
    else:
        print("empty filepath")


button = tk.Button(root, text="Save", command=savetext)
button.grid()
root.mainloop()
