# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
WPort class
"""


class WPort:
    def __init__(self, w={}):
        self.wpid = w.get("wpid")
        self.pname = w.get("pname")
        self.carryRate = w.get("carryRate")
        self.esTime = w.get("esTime")
        self.dist = w.get("dist")
        self.supCost = w.get("supCost")
        self.x_coor = w.get("x_coor")
        self.y_coor = w.get("y_coor")
        self.sortFlag = w.get("sortFlag")
