import sys
import scipy
import time
import tps
import draw
import deformations
import math
import fefinha
import numpy as np
import controlPoints as cp
import controlPointFactory as cpf
from scipy import ndimage

def squaredR(x, y, xi, yi):
	return pow((x-xi),2)+pow((y-yi),2)

def rlogr(x, y, xi, yi):
	r = squaredR(x,y,xi,yi)
	if r == 0:
		return 0
	else:
		return r*math.log(r)

def interpolateInWith(x ,y, system, staticCPs):
	rigid = system[0] + x*system[1] + y*system[2]
	numberOfCPs = staticCPs.len
	sumOfFs = 0
	bar = fefinha.ProgressBar("FALTAM ROLES AQUI CARA",numberOfCPs)
	for n in range(numberOfCPs):
		xi = staticCPs.getXs()[n]
		yi = staticCPs.getYs()[n]
		sumOfFs = sumOfFs + system[n+3]*rlogr(x,y,xi,yi)
		bar.update()
	bar.finish()
	return round(rigid+sumOfFs)

staticCps = [[1,1],[21,1],[11,8],[7,15],[16,12],[1,20],[20,20]]
movingCps = [[10,0],[10,0],[12,0],[25,0],[20,0],[10,0],[10,0]]

staticCPS = cp.ControlPoints(staticCps)
movingCPS = cp.ControlPoints(movingCps)

system = [0.005288,0.003588,0.009618,0.011928,-0.009627,0.035677,-0.079525,0.009886,0.014471,-0.001306]
print interpolateInWith(1,1,system,staticCPS)