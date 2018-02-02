# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
VPort class
"""


class VPort:
    def __init__(self, v={}):
        self.pname = v.get("pname")
        self.quayRate = v.get("quayRate")
        self.weight = v.get("weight")
        self.isCraneStart = v.get("isCraneStart")
        self.EStart = v.get("estart")
        self.EEnd = v.get("eend")
        self.isMeetWeightCond = v.get("isMeetWeightCond")
        self.State = v.get("state")
        self.cost = v.get("cost")
        self.x_coor = v.get("x_coor")
        self.y_coor = v.get("y_coor")
        self.sortFlag = v.get("sortFlag")
