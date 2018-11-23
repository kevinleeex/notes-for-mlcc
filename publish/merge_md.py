#!/usr/bin/env python3
# author: Kevin T. Lee<hello@lidengju.com>
# description: merge the markdown files
import os
import glob

ignores = ['导航', '返回目录']

latex_head = """
---
title: "Notes for MLCC"
subtitle: "谷歌机器学习速成课程个人笔记"
author: [Kevin T. Lee]
date: "2018-11-23"
keywords: [MLCC, Notes]\n
logo: "./meta/tf.png"
logo-width: 200
...\n\n"""

md_list = sorted(glob.glob("../notes/*.md"))
md_list_processed = [os.path.split(x)[1] for x in md_list]

print(md_list_processed)

with open('notes-for-mlcc.md', 'w+') as out_f:
    out_f.write(latex_head)
    for ix, section in enumerate(md_list):
        with open(section) as sec:
            if ix != 0:
                out_f.write('\n\pagebreak\n\n')
            for line in sec:
                if any(ig in line for ig in ignores):
                    continue
                else:
                    out_f.write(line)
