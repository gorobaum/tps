import numpy as np
import math

def deformCPsSinusiodal(cps):
	newCPs = []
	for cp in cps:
		x = cp[0]
		y = cp[1]
		X = x-8.0*math.sin(y/16.0)
		Y = y+4.0*math.cos(x/32.0)
		newCPs.append([X,Y])
	return newCPs

def deformSinusiodal(imagePixels):
	deformedPixels = np.ndarray(imagePixels.shape)
	for x in range(imagePixels.shape[0]):
		for y in range(imagePixels.shape[1]):
			X = x-8.0*math.sin(y/16.0)
			Y = y+4.0*math.cos(x/32.0)
			deformedPixels[x,y] = bilinear(imagePixels, X, Y)
	return deformedPixels

def deformCPsDist(imagePixels, cps):
	xc = imagePixels.shape[0]/2
	yc = imagePixels.shape[1]/2
	for cp in cps:
		x = cp[0]
		y = cp[1]
		r = math.sqrt(pow(y-yc,2) + pow(x-xc,2))
		if r == 0:
			r = 1
		X = x + 50*(x-xc)/r
		Y = y + 50*(y-yc)/r
		newCPs.append([X,Y])
	return newCPs

def deformDist(imagePixels):
	deformedPixels = np.ndarray(imagePixels.shape)
	xc = imagePixels.shape[0]/2
	yc = imagePixels.shape[1]/2
	for x in range(imagePixels.shape[0]):
		for y in range(imagePixels.shape[1]):
			r = math.sqrt(pow(y-yc,2) + pow(x-xc,2))
			if r == 0:
				r = 1
			X = x + 50*(x-xc)/r
			Y = y + 50*(y-yc)/r
			deformedPixels[x,y] = bilinear(imagePixels, X, Y)
	return deformedPixels

def bilinear(imagePixels, x, y):
	u = math.trunc(x)
	v = math.trunc(y)
	interpolation = (u+1-x)*(v+1-y)*getPixel(imagePixels,u,v)+(x-u)*(v+1-y)*getPixel(imagePixels,u+1,v)+(u+1-x)*(y-v)*getPixel(imagePixels,u,v+1)+(x-u)*(y-v)*getPixel(imagePixels,u+1,v+1)

	return interpolation

def getPixel(pixels, x, y):
	# print width, height, x, y
	h = pixels.shape[1]
	w = pixels.shape[0]
	if x >= w or x < 0:
		return 0.0
	elif y >= h or y < 0:
		return 0.0
	else:
		return pixels[x, y]