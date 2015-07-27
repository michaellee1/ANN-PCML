__author__ = 'Michael'
from src import PClass

class PLayer(object):
    m_p_num = None
    p_list = []

    def __init__(self, p_num, p_num_inputs):
        self.m_p_num = p_num
        for x in range(0, self.m_p_num):
            self.p_list.append(PClass(p_num_inputs))
