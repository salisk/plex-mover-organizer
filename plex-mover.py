#! /usr/bin/env python3

import sys, os, shutil
from cursesWindow import *

if len(sys.argv) != 3:
    sys.exit('You need to specify the source directory and target destination')

source = sys.argv[1]
target = sys.argv[2]

if os.path.isabs(source) == False:
    source = os.getcwd() + source

if os.path.isabs(target) == False:
    target = os.getcwd() + target

if os.path.isdir(source) == False:
    sys.exit('Source directory not found')
if os.path.isdir(target) == False:
    sys.exit('Target directory not found')

os.chdir(source)

print(os.listdir(os.getcwd()))
#print(sum(os.path.getsize(f) for f in os.listdir(os.getcwd()) if os.path.isfile(f)))

direct = ['C', 'D', 'E'] * 10
amount = [100] * 30
z = zip(direct, amount)
print(z)

dirList = GuiWindow(z)
