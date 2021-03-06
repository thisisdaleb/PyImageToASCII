from __future__ import print_function
from PIL import Image
from tkFileDialog import askopenfilename

# WARNING: This program can not handle alpha layers.
# If the image contains an alpha layer,
# the program will crash with the phrase Too Many Values to Unpack

class ImageInterpreter:
	allPixels = list()

	# grabs file for use
	def getFile(self):
		filename = askopenfilename()
		print(filename)
		im = Image.open(filename)
		print(im.format, im.size, im.mode)
		return im

	# creates matrix of pixel values
	def createPixelMatrix(self, im):
		self.allPixels = list(im.getdata())
		width, height = im.size
		self.allPixels = [self.allPixels[i * width:(i + 1) * width] for i in xrange(height)]

	# creates output string of ASCII art
	def createASCIIart(self, im):
		# create outputString
		outputString = ""
		x = 0;
		y = 0;
		Xmax, Ymax = im.size
		maxSum = 0;
		minSum = 500;

		while (y < Ymax - 1):
			while (x < Xmax - 1):
				# black and white value for determining character of
				summed = sum(self.allPixels[y][x]) / float(len(self.allPixels[y][x]))
				if(summed>maxSum):
					maxSum = summed;
				if(summed<minSum):
					minSum = summed;

				# decides what character that pixel is equal to.
				# change these values to decide how it should look!
				if summed < 20:
					outputString += "H"
				elif summed < 40:
					outputString += "W"
				elif summed < 60:
					outputString += "@"
				elif summed < 80:
					outputString += "#"
				elif summed < 100:
					outputString += "/"
				elif summed < 120:
					outputString += "|"
				elif summed < 140:
					outputString += "!"
				elif summed < 160:
					outputString += "*"
				elif summed < 180:
					outputString += "-"
				elif summed < 200:
					outputString += "_"
				elif summed < 220:
					outputString += ","
				elif summed < 240:
					outputString += "."
				else:
					outputString += " "
				x += 1
			# moves 2 rows down, since Courier New is only width-fixed, not height
			x = 0
			y += 2
			outputString += "\n"
		print("min and max: " + str(minSum) + " " + str(maxSum))
		return outputString

	def loopPixels(self, im):
		self.createPixelMatrix(im)
		return self.createASCIIart(im)