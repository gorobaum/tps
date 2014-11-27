import numpy as np
import math
import controlPoints

class TPS:
	def __init__(self, staticCPs, movingCPs):
		self.staticCPs = staticCPs
		self.movingCPs = movingCPs

	def squaredR(self, x, y, xi, yi):
		return pow((x-xi),2)+pow((y-yi),2)

	def sumInteration(self, x, y, xi, yi):
		r = self.squaredR(x,y,xi,yi)
		if r == 0:
			return 0
		else:
			return math.log(r)*r

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
				newEqu = np.append(newEqu, self.sumInteration(xn,yn,xi,yi))
			coefMatrix[n+3] = newEqu
		return coefMatrix

	def solveLinearEquationFor(self, ordinates):
		return np.linalg.solve(self.coefMatrix, ordinates)

	def solveLinearEquation(self):
		self.coefMatrix = self.createCoefMatrix()
		zeros = np.array([0,0,0])
		ordinatesX = np.append(zeros, self.movingCPs.xs)
		print self.solveLinearEquationFor(ordinatesX)
		ordinatesY = np.append(zeros, self.movingCPs.ys)
		print self.solveLinearEquationFor(ordinatesY)

