import numpy as np
import math
import controlPoints

class TPS:
	def __init__(self, staticImage, movingImage, staticCPs, movingCPs):
		self.staticImage = staticImage
		self.movingImage = movingImage
		self.staticCPs = staticCPs
		self.movingCPs = movingCPs

	def squaredR(self, x, y, xi, yi):
		return pow((x-xi),2)+pow((y-yi),2)

	def sumInteration(n, x, y, xi, yi):
		r = squaredR(x,y,xi,yi)
		return r*math.log(r)

	def createCoefMatrix(self):
		numberOfCPs = self.staticCPs.len
		numberOfEquations = numberOfCPs+3
		zeros = np.array([0,0,0])
		ones = np.ones(numberOfCPs)
		coefMatrix = np.zeros([numberOfEquations, numberOfEquations])
		coefMatrix[0] = np.concatenate((zeros,ones))
		coefMatrix[1] = np.append(zeros, self.staticCPs.xs)
		coefMatrix[2] = np.append(zeros, self.staticCPs.ys)
		for n in range(numberOfCPs):
			xn = self.staticCPs.xs[n]
			yn = self.staticCPs.ys[n]
			newEqu = np.array([1,xn,yn])
			for i in range(numberOfCPs):
				xi = self.staticCPs.xs[i]
				yi = self.staticCPs.ys[i]
				newEqu = np.append(newEqu, squaredR(xn,yn,xi,yi))
			coefMatrix[n+3] = newEqu

