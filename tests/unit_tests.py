__author__ = 'Michael'

from src import PClass

# Test for bias addition and correctness of range in init function
testClass = PClass(3)
assert testClass.weightList.size() == 4
for x in range(0, testClass.numInputs):
    assert -1 <= testClass.weightList[x] & testClass.weightList[x] <= 1
