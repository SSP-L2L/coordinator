# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
Vessel/Wagon Coordinator
"""
import json
import string
import time

import requests

from coordinator.utils import *
from coordinator.vport import VPort
from coordinator.wport import WPort


def VWCoordinator(msg):
    """
    :param msg:
    :return:
    """
    msgType = msg.get('msgType')
    vpid = msg.get('V_pid')
    wpid = msg.get('W_pid')
    reason = msg.get('reason')

    setVariable(vpid, "wpid", 'integer', wpid)

    if (msgType == "msg_UpdateDest"):
        sp_weight = float(getVariable(wpid, "SparePartWeight"))
        vTargetLocationList = getVPorts(vpid, "TargLocList")
        wTargetLocationList = getWPorts(wpid, "W_TargLocList")

        # 将newTargLocList转为map
        vpMap = {port.pname: port for port in vTargetLocationList}

        # 计算当前时间 ， 以Vessel实例启动时间为基准
        # TODO 时间格式要统一
        vStartTime = time.mktime(time.strptime(getVariable(vpid, "StartTime"), "%Y-%m-%d %H:%M:%S"))  # ms
        curDate = time.time() * 1000  # ms
        t_ms = vStartTime + (curDate - vStartTime) * ZOOM_IN_RATE

        # 获取车的当前位置
        w_info = json.loads(getVariable(wpid, "W_Info"))
        w_value = w_info.get("value")
        w_xc = w_value.get("x_Coor")
        w_yc = w_value.get("y_Coor")
        print("车当前位置:{}, {}".format(w_xc, w_yc))

        candinateWports = []
        routeMp = {}
        for wport in wTargetLocationList:
            vport = (VPort)(vpMap.get(wport.pname))
            if vport.State == "InAD" or vport.State == "AfterAD":
                route = planPath(w_xc, w_yc, vport.x_coor, vport.y_coor)
                estiDate = getEsti_Ms(route) * 1000 + t_ms  # TODO 时间格式
                estiDist = getEsti_dist(route)
                wport.dist = estiDist
                wport.esTime = estiDate
                if vport.EEnd - wport.esTime > 0:
                    totalCost = max(vport.EStart - wport.esTime, 0) * \
                                vport.quayRate * sp_weight / 60 / 60 / 1000 + \
                                wport.dist * wport.carryRate * sp_weight
                    wport.supCost = totalCost
                    wport.sortFlag = vport.sortFlag
                    routeMp[wport.pname] = route
                    candinateWports.append(wport)

        import sys
        minCost = sys.maxsize
        destPort = None
        pathResult = None

        print(candinateWports)
        candinateWports.sort(key=lambda port: port.sortFlag)
        print(candinateWports)
        for i, twp in enumerate(candinateWports):
            co = (1 - pow(K, i + 1)) * twp.supCost
            twp.supCost = co
            if co < minCost:
                minCost = co
                destPort = (WPort)(twp)
                pathResult = routeMp.get(twp.pname)

        vmfEvent = {"createdAt": time.time()}
        if destPort:
            setVariable(vpid, "dpName", 'string', destPort.pname)
            setVariable(wpid, "DestPort", 'WPort', json.dumps(destPort))  # 格式
            setVariable(wpid, "W_TargPortList", 'WPort', json.dumps(candinateWports))
            vmfEvent["W_Info"] = json.dumps(w_info)
            vmfEvent["wDestPort"] = json.dumps(destPort)
            vmfEvent["vDestPort"] = json.dumps(vpMap[destPort.pname])
            vmfEvent["pathResult"] = json.dumps(pathResult)
            vmfEvent["V_pid"] = vpid
            vmfEvent["StartTime"] = vStartTime
            vmfEvent["State"] = "success"
            vmfEvent["Reason"] = reason
        else:
            vmfEvent["State"] = "fail"
        # TODO globalEventQueue.sendMsg(e);
        print("看起来跑完了这里")

    if msgType == "msg_CreateVWConn":
        print("Vessel 和 Weagon 联系建立")


def getVPorts(vpid, vname):
    """

    :param vpid: string
    :param vname: string
    :return: [VPorts]
    """
    ret = getVariable(vpid, vname)
    vPortList = ret.get('value', {"status": "wrong Vports"})
    print(vPortList)

    vports = [VPort(v) for v in vPortList]
    print(vports)

    return vports


def getWPorts(wpid, vname):
    """

    :param wpid: string
    :param vname: string
    :return: [WPorts]
    """
    ret = getVariable(wpid, vname)
    wPortList = ret.get('value', {"status": "wrong Wports"})
    print(wPortList)

    wports = [WPort(w) for w in wPortList]
    print(wports)

    return wports


def getEsti_Ms(route):
    paths = route.get("paths", [{"duration": -1}])
    path = paths[0]
    return path.get["duration"]


def getEsti_dist(route):
    paths = route.get("paths", [{'distance': -1.0}])
    path = paths[0]
    return (float)(path.get('distance'))


def planPath(x1, y1, x2, y2):
    map_url = "http://restapi.amap.com/v3/direction/driving?origin={},{}&destination={},{}&output=json&key=ec15fc50687bd2782d7e45de6d08a023".format(
        x1, y1, x2, y2)
    print(map_url)

    ret = requests.get(map_url, headers=HEADERS).json()
    print(ret)

    return ret.get("route", None)
