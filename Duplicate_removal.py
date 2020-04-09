# -*- coding:utf-8 -*-

import shutil

print('''
┌┬┐┬ ┬┌─┐┬  ┬┌─┐┌─┐┌┬┐
 │││ │├─┘│  ││  ├─┤ │ 
─┴┘└─┘┴  ┴─┘┴└─┘┴ ┴ ┴ 
┬─┐┌─┐┌┬┐┌─┐┬  ┬┌─┐┬  
├┬┘├┤ ││││ │└┐┌┘├─┤│  
┴└─└─┘┴ ┴└─┘ └┘ ┴ ┴┴─┘
''')

old_file_path  = str(input(">>>>>>需要去重的文件路径: "))
new_file_path = str(input(">>>>>>新生成的文件路径: "))
a=0
readDir = old_file_path  #old
writeDir = new_file_path #new
lines_seen = set()
outfile = open(writeDir, "w")
f = open(readDir, "r")
for line in f:
  if line not in lines_seen:
    a+=1
    outfile.write(line)
    lines_seen.add(line)
outfile.close()
print("去重已完成")
print(type(lines_seen))