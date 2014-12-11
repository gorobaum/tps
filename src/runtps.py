import sys
import scipy
import time
import tps
import draw
import math
import deformations
import fefinha
import numpy as np
import tpstestengine as tte
import controlPoints as cp
import controlPointFactory as cpf
from scipy import ndimage

# staticCps = [[74,29],[148,25],[18,118],[236,137],[54,215],[192,215],[158,158],[164,132],[123,146]]
# movingCps = [[74,29],[148,25],[18,118],[236,137],[54,215],[192,215],[163,162],[164,133],[98,161]]

def rms(staticImage, resultImage):
	rms = 0.0
	for x in range(staticImage.shape[0]):
		for y in range(staticImage.shape[1]):
			rms = rms + resultImage[x,y] - staticImage[x,y]
	rms = math.sqrt(rms/(staticImage.shape[0]*staticImage.shape[1]))
	return rms

def runTPS(tp, staticImage, movingImage, filename):
	tp.solveLinearEquation()

	resultImage = np.ndarray(staticImage.shape, staticImage.dtype)
	bar = fefinha.ProgressBar("Progress",staticImage.shape[0]*staticImage.shape[1])
	for x in range(staticImage.shape[0]):
		for y in range(staticImage.shape[1]):
			newPoint = tp.interpolateIn(x,y)
			newX = newPoint[0]
			newY = newPoint[1]
			if newX >= staticImage.shape[0]:
				newX = staticImage.shape[0]-1
			if newY >= staticImage.shape[1]:
				newY = staticImage.shape[1]-1
			resultImage[x, y] = movingImage[newX, newY]
			bar.update()
	bar.finish()
	scipy.misc.imsave(filename, resultImage)
	print rms(staticImage,resultImage)

staticImage = scipy.misc.imread(sys.argv[1], True)

# tpsTestEgine = tte.TPSTestEngine(staticImage, [8,8])
# tpsTestEgine.applySinuosidalDeformation()
# tpsTestEgine.drawAuxImages("Sin")
# movingImage = tpsTestEgine.getMovingImage()
# tp = tpsTestEgine.createTPS()

# runTPS(tp, staticImage, movingImage, "resultSin.png")

# tpsTestEgine = tte.TPSTestEngine(staticImage, [8,8])
# tpsTestEgine.applyInvDistDeformation()
# tpsTestEgine.drawAuxImages("Dist")
# movingImage = tpsTestEgine.getMovingImage()
# tp = tpsTestEgine.createTPS()

# runTPS(tp, staticImage, movingImage, "resultDist.png")

tpsTestEgine = tte.TPSTestEngine(staticImage, [8,8])
tpsTestEgine.applyDistSinDeformation()
tpsTestEgine.drawAuxImages("DistSin")
movingImage = tpsTestEgine.getMovingImage()
tp = tpsTestEgine.createTPS()

runTPS(tp, staticImage, movingImage, "resultDistSin.png")

