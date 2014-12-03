import numpy as np
import random

def createUniformGrid(gridShape, imageShape):
	xStep = imageShape[0]/(gridShape[0]-1)
	yStep = imageShape[1]/(gridShape[1]-1)
	cpList = []
	for x in range(gridShape[0]):
		for y in range(gridShape[1]):
			cpX = x*xStep
			cpY = y*yStep
			cpList.append([cpX,cpY])
	return cpList

def createRandomGrid(gridShape, imageShape):
	cpList = []
	for x in range(gridShape[0]):
		for y in range(gridShape[1]):
			cpX = random.randint(0,imageShape[0])
			cpY = random.randint(0,imageShape[1])
			cpList.append([cpX,cpY])
	return cpList
