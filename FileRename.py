import os

path = "C://Projects//PIC_Assembly_C_Scripts"
dir_list = os.listdir(path)
print(dir_list)

for dir in dir_list:
    if dir[0].isdigit() or dir[0] == '_':
        old_name = dir
        new_name = dir[1:]
        old_path = path + "//" + old_name
        new_path = path + "//" + new_name
        print("Old path: " + old_path + " | New path: " + new_path)
        os.rename(old_path, new_path)