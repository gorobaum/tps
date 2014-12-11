import scipy
import tps
import draw
import deformations
import numpy as np
import controlPoints as cp
import controlPointFactory as cpf
from scipy import ndimage

class TPSTestEngine:
	def __init__(self, staticImage, CPGrid):
		listOfCPS = cpf.createUniformGrid(CPGrid, staticImage.shape)
		self.staticImage = staticImage
		self.movingImage = staticImage
		self.staticCPs = cp.ControlPoints(listOfCPS)
		self.movingCPs = cp.ControlPoints(listOfCPS)

	def applySinuosidalDeformation(self):
		self.movingImage = deformations.deformSinusiodal(self.movingImage)
		lisfOfMovingCPs = deformations.deformCPsSinusiodal(self.staticImage.shape, self.staticCPs.listOfCPs)
		self.movingCPs = cp.ControlPoints(lisfOfMovingCPs)

	def applyInvDistDeformation(self):
		self.movingImage = deformations.deformDist(self.movingImage)
		lisfOfMovingCPs = deformations.deformCPsDist(self.staticImage.shape, self.staticCPs.listOfCPs)
		self.movingCPs = cp.ControlPoints(lisfOfMovingCPs)

	def applyRotateDeformation(self):
		self.movingImage = deformations.deformRotate(self.movingImage)
		lisfOfMovingCPs = deformations.deformCPsRotate(self.staticImage.shape, self.staticCPs.listOfCPs)
		self.movingCPs = cp.ControlPoints(lisfOfMovingCPs)

	def applyDistSinDeformation(self):
		self.movingImage = deformations.deformDistSin(self.movingImage)
		lisfOfMovingCPs = deformations.deformCPsDistSin(self.staticImage.shape, self.staticCPs.listOfCPs)
		self.movingCPs = cp.ControlPoints(lisfOfMovingCPs)

	def drawAuxImages(self, sulfix):
		draw.drawCPs(self.staticCPs, "staticCPS"+sulfix+".png", self.staticImage.shape)
		draw.drawCPs(self.movingCPs, "movingCPS"+sulfix+".png", self.staticImage.shape)
		scipy.misc.imsave("movingImage"+sulfix+".png", self.movingImage)

	def saveMovingImage(filename):
		scipy.misc.imsave(filename, self.movingImage)		

	def createTPS(self):
		return tps.TPS(self.staticCPs, self.movingCPs)

	def getMovingImage(self):
		return self.movingImage