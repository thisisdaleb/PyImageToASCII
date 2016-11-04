from __future__ import print_function
from PIL import Image
from tkFileDialog import askopenfilename
import sys
from ImageInterpreter import ImageInterpreter


# WARNING: This program can not handle alpha layers.
# If the image contains an alpha layer,
# the program will crash with the phrase Too Many Values to Unpack

#####
##MAIN FUNCTION
#####
imInterpreter = ImageInterpreter()				#create image processor
im = imInterpreter.getFile()					#get file to use with image interpreter
outputString = imInterpreter.loopPixels(im)		#Interpret file to black and white and create string
imInterpreter.exportTxt(outputString)           #output string to rtf file
