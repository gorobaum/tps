import sys
import scipy
import numpy as np
import tps
import controlPoints as cp
from scipy import ndimage


original = scipy.misc.imread("static.png")
modified = scipy.misc.imread("moving.png")

staticXS = np.array([ 74,148, 18,236, 54,192,158,164,123])
staticYS = np.array([ 29, 25,118,137,215,215,158,132,146])
movingXS = np.array([ 74,148, 18,236, 54,192,163,164,98])
movingYS = np.array([ 29, 25,118,137,215,215,162,133,161])

staticCPS = cp.ControlPoints(staticXS, staticYS)
movingCPS = cp.ControlPoints(movingXS, movingYS)

tp = tps.TPS(staticCPS, movingCPS)
tp.solveLinearEquation()

newImage = np.ndarray(original.shape, original.dtype)
for x in range(original.shape[0]):
	for y in range(original.shape[1]):
		newPoint = tp.interpolateIn(x,y)
		newX = newPoint[0]
		newY = newPoint[1]
		if newX >= original.shape[0]:
			newX = original.shape[0]-1
		if newY >= original.shape[1]:
			newY = original.shape[1]-1
		newImage[x, y] = modified[newX, newY]
scipy.misc.imsave("result.png", newImage)