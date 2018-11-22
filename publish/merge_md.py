# !/usr/bin/env python3
# author: Kevin T. Lee<hello@lidengju.com>

import os
import glob

ignores = ['导航', '返回目录']

md_list = sorted(glob.glob("../notes/*.md"))
md_list_processed = [os.path.split(x)[1] for x in md_list]

print(md_list_processed)

with open('notes-for-mlcc.md', 'w+') as out_f:
    for ix, section in enumerate(md_list):
        with open(section) as sec:
            if ix != 0:
                out_f.write('\n<div style="page-break-after: always;"></div>\n')
            for line in sec:
                if any(ig in line for ig in ignores):
                    continue
                else:
                    out_f.write(line)
