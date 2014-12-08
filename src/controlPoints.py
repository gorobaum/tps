import numpy as np

class ControlPoints:
	def __init__(self, cps):
		self.listOfCPs = cps
		self.len = len(cps)

	def addNewCP(self, cp):
		self.listOfCPs.append(cp)
		self.len = len(cps)

	def getXs(self):
		xs = []
		for cp in self.listOfCPs:
			xs.append(cp[0])
		return np.array(xs)

	def getYs(self):
		ys = []
		for cp in self.listOfCPs:
			ys.append(cp[1])
		return np.array(ys)