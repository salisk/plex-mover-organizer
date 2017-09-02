#! /usr/bin/env python

import sys, os, shutil

if len(sys.argv) != 3:
    sys.exit('You need to specify the source directory and target destination')

source = sys.argv[1]
target = sys.argv[2]

if os.path.isdir(source) == False:
    sys.exit('Source directory not found')
if os.path.isdir(target) == False:
    sys.exit('Target directory not found')

