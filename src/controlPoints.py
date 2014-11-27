import numpy as np

class ControlPoints:
	def __init__(self, xs, ys):
		self.xs = xs
		self.ys = ys
		self.len = len(xs)

	def addNewCP(self, x ,y):
		self.xs = np.append(self.xs, x)
		self.ys = np.append(self.ys, y)
		self.len = self.len+1