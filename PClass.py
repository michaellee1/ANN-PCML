__author__ = 'Michael'
import random
class P(object):
    numInputs = None
    weightList = []
    def __init__(self):
        for x in range(0,self.numInputs+1):
            self.weightList.append(random.uniform(-1,1))

