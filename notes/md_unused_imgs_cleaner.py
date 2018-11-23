#!/usr/bin/env python3
# author: Kevin T. Lee<hello@lidengju.com>
# description: used for clean the unused imgs

import os
import glob
import re

# Match the markdown image tag
regex_pattern_str = '(!\[.*?\]\(.*?\))'
test_md_img_tag = "1231438190ssa\n![he2llo](./assets/test.png)12323sd \
                    ![he2llo](./assets/test.png)123"

regex_pattern = re.compile(regex_pattern_str)

out_tag = regex_pattern.findall(test_md_img_tag)
print(out_tag)

md_list = sorted(glob.glob("*.md"))
used_imgs_list = []
for md in md_list:
    with open(md) as md_file:
        for line in md_file:
            tags = regex_pattern.findall(line)
            for tag in tags:
                path = os.path.split(tag.split("(")[1][:-1])[-1]
                used_imgs_list.append(path)

for str_path in used_imgs_list:
    print("{}\n".format(str_path))

saved_imgs = glob.glob("./assets/*")
print(saved_imgs)

for img in saved_imgs:
    if any(x in img for x in used_imgs_list):
        continue
    else:
        print("Delete ", img)
        os.remove(img)
