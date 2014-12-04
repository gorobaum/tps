import numpy as np
import time
import math
import controlPoints

class TPS:
	def __init__(self, staticCPs, movingCPs):
		self.staticCPs = staticCPs
		self.movingCPs = movingCPs

	def squaredR(self, x, y, xi, yi):
		return pow((x-xi),2)+pow((y-yi),2)

	def rlogr(self, x, y, xi, yi):
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
		coefMatrix[0] = np.append(zeros,ones)
		coefMatrix[1] = np.append(zeros, self.staticCPs.getXs())
		coefMatrix[2] = np.append(zeros, self.staticCPs.getYs())
		for n in range(numberOfCPs):
			xn = self.staticCPs.getXs()[n]
			yn = self.staticCPs.getYs()[n]
			newEqu = np.array([1,xn,yn])
			for i in range(numberOfCPs):
				xi = self.staticCPs.getXs()[i]
				yi = self.staticCPs.getYs()[i]
				newEqu = np.append(newEqu, self.rlogr(xn,yn,xi,yi))
			coefMatrix[n+3] = newEqu
		return coefMatrix

	def solveLinearEquationFor(self, ordinates):
		return np.linalg.solve(self.coefMatrix, ordinates)

	def solveLinearEquation(self):
		self.coefMatrix = self.createCoefMatrix()
		zeros = np.array([0,0,0])
		ordinatesX = np.append(zeros, self.movingCPs.getXs())
		start_time = time.time()
		self.systemX = self.solveLinearEquationFor(ordinatesX)
		print("--- solveLinearEquationFor X took %s seconds ---" % (time.time() - start_time))
		ordinatesY = np.append(zeros, self.movingCPs.getYs())
		start_time = time.time()
		self.systemY = self.solveLinearEquationFor(ordinatesY)
		print("--- solveLinearEquationFor Y took %s seconds ---" % (time.time() - start_time))

	def interpolateIn(self, x, y):
		x = self.interpolateInWith(x,y,self.systemX)
		y = self.interpolateInWith(x,y,self.systemY)
		return (x,y)

	def interpolateInWith(self, x ,y, system):
		variableVector = np.zeros(system.shape)
		numberOfCPs = self.staticCPs.len
		variableVector[0] = 1.0
		variableVector[1] = x
		variableVector[2] = y
		for n in range(numberOfCPs):
			xi = self.staticCPs.getXs()[n]
			yi = self.staticCPs.getYs()[n]
			variableVector[n+3] = self.rlogr(x,y,xi,yi)
		return round(np.dot(variableVector, system))
