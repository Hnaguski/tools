#!/usr/bin/env python

#----------------------------------#
# ,--. ,--.         ,--.           #
# |  .'   / ,---. ,-'  '-. ,--,--. #
# |  .   ' | .-. |'-.  .-'' ,-.  | #
# |  |\   \' '-' '  |  |  \ '-'  | #
# `--' '--' `---'   `--'   `--`--' #
#            kotajacob.tk          #
# Copyright (C) 2017  Dakota Walsh #
#----------------------------------#

"""
Brightness

Usage:
  brightness.py (-a | -d | -s) <value>
  brightness.py -p
  brightness.py (-h | --help)
  brightness.py (-v | --version)

Options:
  -s                   set the brightness
  -p                   print the brightness
  -a                   add to the brightness
  -d                   decrement from the the brightness
  -h --help            show this help message and exit
  -v --version         show version and exit
"""
from lib.docopt import docopt # argument parsing
import os                     # changing the file
from shutil import copy       # copying the file

# brightness file directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
brightFile = "/sys/class/backlight/intel_backlight/brightness"
tmpFile    = os.path.join(ROOT_DIR, "tmp")

def getBrightness():
    # get the current brightness and sets to to an int
    f_name = open(brightFile, 'r')
    brightness = int(float(f_name.readline()))
    f_name.close()
    return brightness

def setBrightness(brightness):
    # create a tmp file with the new brightness
    # replace the old brightness file with the tmp one
    f_name = open(tmpFile, 'w')
    f_name.write(str(brightness))
    f_name.close()
    copy(tmpFile, brightFile)
    os.remove(tmpFile)

def main(arguments):
    if (arguments['-s'] == True):
        # set the value
        print("Setting the value")
        setBrightness(int(float(arguments['<value>'])))
    elif (arguments['-p'] == True):
        # print the brightness
        print(getBrightness())
    elif (arguments['-a'] == True):
        # add to the value
        print("Adding to the value")
        brightness = getBrightness()
        brightness = brightness + int(float(arguments['<value>']))
        setBrightness(brightness)
    elif (arguments['-d'] == True):
        # add to the value
        print("Decrementing from the value")
        brightness = getBrightness()
        brightness = brightness - int(float(arguments['<value>']))
        setBrightness(brightness)
    else:
        # error no option found
        print("Error. Invalid Option! (or lack there of)")

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Brightness 1.0.0') # create the flags from the comment
    main(arguments)
