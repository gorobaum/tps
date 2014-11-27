import sys
import scipy as sp
import numpy as np
import tps
import controlPoints as cp
from scipy import ndimage

staticXS = np.array([ 1,20,11,16, 7,20, 1])
staticYS = np.array([ 1, 1, 8,12,15,20,20])
movingXS = np.array([10,10,15,20,25,10,10])
movingYS = np.array([ 0, 0, 0, 0, 0, 0, 0])

staticCPS = cp.ControlPoints(staticXS, staticYS)
movingCPS = cp.ControlPoints(movingXS, movingYS)

tp = tps.TPS(staticCPS, movingCPS)
tp.solveLinearEquation()