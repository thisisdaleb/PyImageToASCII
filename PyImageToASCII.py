from __future__ import print_function
from Tkinter import *
from tkFileDialog import asksaveasfile
from ImageInterpreter import ImageInterpreter

# WARNING: This program can not handle alpha layers.
# If the image contains an alpha layer,
# the program will crash with the phrase Too Many Values to Unpack

#Asks where you want the file, and then places the ASCII art in a .rtf file at that spot
def createTextFile(outputString):
		print('exporting string: ')
		print('length: ' + str(len(outputString)))
		outputName = asksaveasfile(mode='w', defaultextension=".rtf")
		if outputName is None:
			return
		outputName.write(outputString)
		outputName.close()

#run interpreter to get ASCII art from image
def runProgram():
	imInterpreter = ImageInterpreter()  # create image processor
	im = imInterpreter.getFile()  # get file to use with image interpreter
	outputString = imInterpreter.loopPixels(im)  # Interpret file to black and white and create string
	createTextFile(outputString)

def createGUI():
	root = Tk()
	frame = Frame(root)
	frame.pack()
	#place quit button
	button = Button(frame, text="QUIT", fg="red", command=frame.quit)
	button.pack(side=LEFT)
	#place button to pick file for conversion
	play = Button(frame, text="Use Image File", fg="black", command=runProgram)
	play.pack(side=BOTTOM)
	root.mainloop()
	root.destroy()

###############
##MAIN FUNCTION
###############
createGUI()