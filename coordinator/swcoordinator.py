# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
Supplier/Wagon Coordinator
"""
import string

from requests.auth import HTTPBasicAuth

from coordinator.utils import *


def SWCoordinator(msg):
    """
    :param msg: dict
    :return:
    """
    msgType = msg.get("msgType")
    if msgType == "Msg_StartWeagon":
        wagon = Wagon()
        wagon.W_Name = "wagon_lambda"
        wagon.X_Coor = 113.2982254028
        wagon.Y_Coor = 23.0958388047
        wagon.isArrival = False

        msg["W_Info"] = wagon.__dict__
        msg.pop("msgType", None)
        msg.pop("M_pid", None)

        sendMessageToStartProcessInstance(msgType, json.dumps(msg))
        print("Wagon流程实例已启动")


class Wagon:
    def __init__(self):
        self.pid = None
        self.W_id = None
        self.W_Name = None
        self.X_Coor = None
        self.Y_Coor = None
        self.W_Velocity = None
        self.Start = None
        self.End = None
        self.V_ETime = None
        self.pArri = None
        self.needPlan = None
        self.planRes = None
        self.isArrival = None
