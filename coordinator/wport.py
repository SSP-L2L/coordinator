# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
WPort class
"""


class WPort:
    def __init__(self, w={}):
        self.wpid = w.get("wpid") if w.get("wpid") else 0
        self.pname = w.get("pname")
        self.carryRate = w.get("carryRate") if w.get("carryRate") else 0.0
        self.esTime = w.get("esTime") if w.get("esTime") else 0.0
        self.dist = w.get("dist") if w.get("dist") else 0.0
        self.supCost = w.get("supCost") if w.get("supCost") else 0.0
        self.x_coor = w.get("x_coor") if w.get("x_coor") else 0.0
        self.y_coor = w.get("y_coor") if w.get("y_coor") else 0.0
        self.sortFlag = w.get("sortFlag") if w.get("sortFlag") else 0.0
