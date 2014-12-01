import numpy as np

class ControlPoints:
	def __init__(self, cps):
		self.cps = cps
		self.len = len(cps)

	def addNewCP(self, cp):
		self.cps.append(cp)
		self.len = len(cps)

	def getXs(self):
		xs = []
		for cp in self.cps:
			xs.append(cp[0])
		return np.array(xs)

	def getYs(self):
		ys = []
		for cp in self.cps:
			ys.append(cp[1])
		return np.array(ys)