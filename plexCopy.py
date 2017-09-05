#! /usr/bin/env python3

import sys, os, shutil, subprocess
from cursesWindow import *

def get_size(start_path = '.'):
    total_size = 0
    for dir_path, dir_name, file_name in os.walk(start_path):
        for file in file_name:
            fp = os.path.join(dir_path, file)
            total_size += os.path.getsize(fp)
            print(total_size)
    return total_size

if len(sys.argv) != 3:
    sys.exit('You need to specify the source directory and target destination')

source = sys.argv[-2]
target = sys.argv[-1]

if os.path.isabs(source) == False:
    source = os.getcwd() + source

if os.path.isabs(target) == False:
    target = os.getcwd() + target

if os.path.isdir(source) == False:
    sys.exit('Source directory not found')
if os.path.isdir(target) == False:
    sys.exit('Target directory not found')

os.chdir(source)

direct = sorted(os.listdir(source))

print("Calculating file sizes...")

amount = []
for index, dir in enumerate(direct):
    print("[%d/%d] %s" % (index+1, len(direct), dir))
    process = subprocess.Popen(['du', '-s', dir], stdout=subprocess.PIPE)
    out, err = process.communicate()
    out = out.decode('UTF-8')
    out = out.split('\t', 1)[0]
    amount.append(int(out))

dirList = GuiWindow(zip(direct, amount)).toSelect()

if dirList != False:
    if not dirList:
        print("No directories specified")
    else:
        cp = dirList.pop()
        print("to Copy = " + str(cp))
        print (dirList)

        for dir in dirList:
            folders = os.listdir(source + dir)
            if len(folders) == 1 and folders[0] == "Plex Versions":
                print()
            else:
                for dire in folders:
                    print()


