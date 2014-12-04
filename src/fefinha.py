import sys
import os
from time import time

def getConsoleWidth():
    #only works on unix
    try:
        rows, columns = os.popen('stty size', 'r').read().split()
        return int(columns)
    except:
        return 80
    
class ProgressBar:
    def __init__(self, text, totalWork):
        self.text = text
        self.totalWork = float(totalWork)
        self.currentWork = 0
        self.mark = time()
        
    def update(self, add=1):
        self.currentWork += add
        sys.stdout.write("\r%s" % self.__str__())
        sys.stdout.flush()
        
    def finish(self):
        sys.stdout.write("\r%s\n" % self.__str__())
        sys.stdout.flush()
        
    def clear(self):
        sys.stdout.write("\r" + (" "*(getConsoleWidth())) + "\r")
        sys.stdout.flush()
        
    def __str__(self):
        s = self.text + ": ["
        p = self.currentWork/self.totalWork
        elapsed = time()-self.mark
        estimated = elapsed * ( (self.totalWork/self.currentWork) - 1 )
        timeText = "] (%.2f secs | %.2f secs)" % (elapsed, estimated)
        barSize = getConsoleWidth() - len(s) - len(timeText)
        barDone = int(barSize*p)
        s += "=" * barDone
        s += " " * (barSize - barDone)
        s += timeText
        s += " " * (getConsoleWidth() - len(s))
        return s