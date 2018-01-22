# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'
"""
Manager/Supplier Coordinator
"""
from . import *


def MSCoordinator(msg):
    """
    :param msg: dict
    :return:
    """
    msgType = msg.get("msgType")
    if msgType == "Msg_StartSupplier":
        w_threshold = (float)(msg.get("SparePartWeight"))
        targLocMap = msg.get("V_TargLocList")
        targLocList = [VPort(v) for v in targLocMap]

        candidateVPorts = []
        for i, now in enumerate(targLocList):
            if now.weight >= w_threshold:
                now.isMeetWeightCond = True
            else:
                now.isMeetWeightCond = False

            if now.isCraneStart == False:
                now.isMeetWeightCond = False

            if now.isMeetWeightCond == True:
                candidateVPorts.append(now)

        # 给VWF发送消息
        # TODO EventType.MSC_MeetWeightCond
        vmfevent = {}
        vmfevent["createAt"] = time.time()
        vmfevent["MSC_TargPorts"] = targLocList.__dict__
        # TODO globalEventQueue.sendMsg(e);
        msg.pop("V_TargLocList", None)
        print("根据港口起重机启动与否及载重筛选港口完毕！")

        # 消息启动Supplier流程
        wtarglocs = []
        for i, vp in enumerate(candidateVPorts):
            wp = WPort()
            vp = (VPort)(vp)
            wp.pname = vp.pname
            wp.carryRate = carRateMp[vp.pname]
            wp.x_coor = vp.x_coor
            wp.y_coor = vp.y_coor
            if vp.isMeetWeightCond:
                wtarglocs.append(wp)

        msg["W_TargLocList"] = wtarglocs.__dict__
        msg.pop("msgType", None)
        # TODO
        # runtimeService.startProcessInstanceByMessage("Msg_StartSupplier", msg);
        print("Supplier流程实例已启动")
