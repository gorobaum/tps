import sys
import scipy
import deformations
from scipy import ndimage

original = scipy.misc.lena()
scipy.misc.imsave("static.png", original)
modified = deformations.deformSinusiodal(original)
scipy.misc.imsave("movingSin.png", modified)
modified = deformations.deformDist(original)
scipy.misc.imsave("movingDist.png", modified)
print "Transformation sucessful with the name modified-teste.jpg"