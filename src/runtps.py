import sys
import scipy
import time
import numpy as np
import tps
import controlPoints as cp
import controlPointFactory as cpf
from scipy import ndimage

original = scipy.misc.imread("static.png")
modified = scipy.misc.imread("moving.png")

imageShape = original.shape
gridShape = [2,2]

staticCps = cpf.createUniformGrid(gridShape, imageShape)
movingCps = cpf.createUniformGrid(gridShape, imageShape)

# staticCps = [[74,29],[148,25],[18,118],[236,137],[54,215],[192,215],[158,158],[164,132],[123,146]]
# movingCps = [[74,29],[148,25],[18,118],[236,137],[54,215],[192,215],[163,162],[164,133],[98,161]]

staticCPS = cp.ControlPoints(staticCps)
movingCPS = cp.ControlPoints(movingCps)

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
scipy.misc.imsave("resultUniform.png", newImage)