import scipy
import numpy as np
from scipy import ndimage

def drawCPs(controlPoints, filename, shape):
	image = np.ndarray(shape, int)
	image.fill(255)
	for cp in controlPoints.cps:
		x = int(round(cp[0]))
		y = int(round(cp[1]))
		for i in range(x-1,x+2):
			for j in range(y-1,y+2):
				image[i,j] = 0
	scipy.misc.imsave(filename, image)

def drawCPsOverImage(image, controlPoints, filename, shape):
	aux = image
	for cp in controlPoints.cps:
		x = int(round(cp[0]))
		y = int(round(cp[1]))
		for i in range(x-1,x+2):
			for j in range(y-1,y+2):
				aux[i,j] = 0
	scipy.misc.imsave(filename, aux)

def createGridImage(shape, gridShape):
	image = np.ndarray(shape, int)
	image.fill(255)
	xStep = shape[0]/gridShape[0]
	yStep = shape[1]/gridShape[1]
	for x in range(gridShape[0]):
		X = x*xStep
		for y in range(shape[1]):
			image[X,y] = 0
	for y in range(gridShape[1]):
		Y = y*yStep
		for x in range(shape[0]):
			image[x,Y] = 0
	return image

