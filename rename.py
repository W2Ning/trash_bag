import os

folder_name = "D:/video2"

file_name = os.listdir(folder_name)

os.chdir(folder_name)

for name in file_name:

    split_name = name.split(".",1)
    new_name = split_name[1]
    os.rename(name, new_name)
