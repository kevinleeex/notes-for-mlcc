import os
import glob

ignores = ['导航']
md_list = sorted(glob.glob("./*.md"))
process_md_list = [x[2:] for x in md_list]  # remove ./
print(process_md_list)
nav_md_str = "\n\n## 导航\n\n [返回目录](../README.md) | [上一节 {}]({}) | [下一节 {}]({})"
for ix, item in enumerate(md_list):
    add_nav = True
    f = open(file=item,mode='a+')
    for line in f:
        print(line)
        if any(x in line for x in ignores):
            add_nav = False
            break
    print(add_nav, ix)
    if add_nav and ix > 0 and ix < 18:
        out_str = nav_md_str.format(process_md_list[ix-1][:-3],
        md_list[ix-1],
        process_md_list[ix+1][:-3], 
        md_list[ix+1])

        f.write(out_str)
