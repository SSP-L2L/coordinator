# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
VPort class
"""


class VPort:
    def __init__(self, v=None):
        self.pname = v.get("pname")
        self.quayRate = v.get("quayRate")
        self.weight = v.get("weight")
        self.isCraneStart = v.get("isCraneStart")
        self.EStart = v.get("EStart")
        self.EEnd = v.get("EEnd")
        self.isMeetWeightCond = v.get("isMeetWeightCond")
        self.State = v.get("State")
        self.cost = v.get("cost")
        self.x_coor = v.get("x_coor")
        self.y_coor = v.get("y_coor")
        self.sortFlag = v.get("sortFlag")
