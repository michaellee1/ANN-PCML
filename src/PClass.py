__author__ = 'Michael'
import random


class P(object):
    m_numInputs = None
    weightList = []

    def __init__(self, n):
        self.m_numInputs = n
        for x in range(0, self.numInputs + 1):
            self.weightList.append(random.uniform(-1, 1))
