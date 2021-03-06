# -*- coding: UTF-8 -*-

__author__ = 'sonnyhcl'

"""
Manager/Supplier Coordinator
"""
import time
import string
import json
import requests
from requests.auth import HTTPBasicAuth

from coordinator.utils import *
from coordinator.vport import VPort
from coordinator.wport import WPort


def MSCoordinator(msg):
    """
    :param msg: dict
    :return:
    """
    msgType = msg.get("msgType")
    if msgType == "Msg_StartSupplier":
        vpid = msg.get("V_pid")
        w_thre = msg.get("SparePartWeight")
        targLocMap = msg.get("V_TargLocList")
        targLocList = [VPort(v) for v in targLocMap]

        candidateVPorts = []
        lastId = -1
        for i, now in enumerate(targLocList):
            if now.weight >= w_thre:
                now.isMeetWeightCond = True
            else:
                now.isMeetWeightCond = False

            if now.isCraneStart == False:
                now.isMeetWeightCond = False

            if now.isMeetWeightCond == True:
                candidateVPorts.append(now)
                lastId = i
        print("last valid port={}\nvpid={}".format(lastId, vpid))
        setVariable(vpid, "lastValidId", 'integer', lastId)

        # SendMsg to VWF
        event = {'data': {}}
        event['type'] = 7 # MSC_MeetWeightCond
        event['createAt'] = time.time()
        event["MSC_TargPorts"] = [i.__dict__ for i in targLocList]
        sendMSCEvent(json.dumps(event))

        msg.pop("V_TargLocList", None)
        print("根据港口起重机启动与否及载重筛选港口完毕！")

        # 消息启动Supplier流程
        wtarglocs = []
        for i, vp in enumerate(candidateVPorts):
            wp = WPort({})
            wp.pname = vp.pname
            wp.carryRate = carRateMp[vp.pname]
            wp.x_coor = vp.x_coor
            wp.y_coor = vp.y_coor
            if vp.isMeetWeightCond:
                wtarglocs.append(wp)

        msg["W_TargLocList"] = [i.__dict__ for i in wtarglocs]
        msg.pop("msgType", None)

        sendMessageToStartProcessInstance(msgType, json.dumps(msg))
        print("Supplier流程实例已启动")
