import sys
import scipy
import time
import tps
import draw
import deformations
import fefinha
import numpy as np
import controlPoints as cp
import controlPointFactory as cpf
from scipy import ndimage

def drawAuxImages(staticCPS, movingCPS, imageShape, modified):
	draw.drawCPs(staticCPS, "staticCPS.png", imageShape)
	draw.drawCPs(movingCPS, "movingCPS.png", imageShape)

original = scipy.misc.imread(sys.argv[1], True)
modified = deformations.deformSinusiodal(original)
scipy.misc.imsave("movingSin.png", modified)

imageShape = original.shape
CPGrid = [8,8]

staticCps = cpf.createUniformGrid(CPGrid, imageShape)
movingCps = deformations.deformCPsSinusiodal(imageShape, staticCps)

# staticCps = [[74,29],[148,25],[18,118],[236,137],[54,215],[192,215],[158,158],[164,132],[123,146]]
# movingCps = [[74,29],[148,25],[18,118],[236,137],[54,215],[192,215],[163,162],[164,133],[98,161]]

staticCPS = cp.ControlPoints(staticCps)
movingCPS = cp.ControlPoints(movingCps)

drawAuxImages(staticCPS, movingCPS, imageShape, modified)

tp = tps.TPS(staticCPS, movingCPS)
tp.solveLinearEquation()

newImage = np.ndarray(original.shape, original.dtype)
bar = fefinha.ProgressBar("Progress",original.shape[0]*original.shape[1])
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
		bar.update()
bar.finish()
scipy.misc.imsave("resultUniform.png", newImage)