## -*- coding: UTF-8 -*-
from __future__ import print_function
from PIL import Image
from tkFileDialog import askopenfilename
import sys


# WARNING: This program can not handle alpha layers.
# If the image contains an alpha layer,
# the program will crash with the phrase Too Many Values to Unpack

def getFile():  # asks for an image file and returns it
    filename = askopenfilename()
    print(filename)
    im = Image.open(filename)
    print(im.format, im.size, im.mode)
    # im.show()                                     #opens file in firefox
    return im


def loopPixels(im):
    outputString = ""
    allPixels = list(im.getdata())
    width, height = im.size

    allPixels = [allPixels[i * width:(i + 1) * width] for i in xrange(height)]

    # create outputString
    x = 0;
    y = 0;
    Xmax, Ymax = im.size

    while (y < Ymax-1):
        while (x < Xmax-1):
            summed = sum(allPixels[y][x]) / float(len(allPixels[y][x]))
            if summed < 20:
                outputString += "H"
            elif summed < 50:
                outputString += "W"
            elif summed < 70:
                outputString += "@"
            elif summed < 120:
                outputString += "/"
            elif summed < 155:
                outputString += "|"
            elif summed < 190:
                outputString += "-"
            elif summed < 230:
                outputString += "."
            else:
                outputString += " "
            x += 1
        x = 0
        y += 2
        outputString += "\n"

    return outputString


def exportTxt(outputString):
    print('exporting string: ')
    print(str(len(outputString)))
    #print(outputString)
    f = open("file.rtf", "w")
    f.write(outputString)
    f.close()


#####
##MAIN FUNCTION
#####
im = getFile()
outputString = loopPixels(im)
exportTxt(outputString)
