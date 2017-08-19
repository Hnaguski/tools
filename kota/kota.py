#!/usr/bin/env python
#/home/kota/cloud/dots/scripts/alias_helper_data/alias

import os

# Open the config file
f = open(os.path.expanduser('/home/kota/git/tools/kota/data/alias'), 'r')

line = f.read()
f.close()

print(line)
