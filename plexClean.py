#! /usr/bin/env python3

import sys, os
from cursesWindow import *

quality_folder = "Original Quality"

if len(sys.argv) != 2:
    sys.exit('You need to specify the directory')

source = sys.argv[1]

if os.path.isabs(source) == False:
    source = os.getcwd() + source

if os.path.isdir(source) == False:
    sys.exit('Source directory not found')

direct = sorted(os.listdir(source))

dirList = GuiWindow(zip(direct, [0]*len(direct))).toSelect()

if dirList != False:
    if not dirList:
        sys.exit("No directories specified")


