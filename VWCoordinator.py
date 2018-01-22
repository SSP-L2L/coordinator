# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
Vessel/Wagon Coordinator
"""
from . import *


def VWCoordinator(msg):
    """
    >>> msg = { \
        'msgType' : string, \
        'V_pid'  : string, \
        'W_pid' : string, \
        'reason' : string \
    }
    :param msg:
    :return:
    """
    msgType = msg.get('msgType')
    vpid = msg.get('V_pid')
    wpid = msg.get('W_pid')
    reason = msg.get('reason')

    setVairable(vpid, "wpid", wpid)

    if (msgType == "msg_UpdateDest"):
        vTargetLocationList = getVPorts(vpid, "TargLocList")
        wTargetLocationList = getWPorts(wpid, "W_TargLocList")
        sp_weight = getVariable(wpid, "SparePartWeight")

        # 将newTargLocList转为map
        vpMap = {nowWport.pname: nowWport for nowWport in vTargetLocationList}

        # 计算当前时间 ， 以Vessel实例启动时间为基准
        # TODO 时间格式要统一
        vStartTime = getVariable(vpid, "StartTime")
        curDate = time.time() * 1000  # ms
        t_ms = vStartTime
        t_ms += (curDate - vStartTime) * zoomInRate

        # 获取车的当前位置
        w_info = getVariable(wpid, "W_Info")
        w_value = w_info.get("value")
        w_xc = w_value.get("x_Coor")
        w_yc = w_value.get("y_Coor")
        print("车当前位置:{}, {}".format(w_xc, w_yc))

        candinateWports = []
        routeMp = {}
        for nowWport in wTargetLocationList:
            nowVport = (VPort)(vpMap.get(nowWport.pname))
            if nowVport.State == "InAD" or nowVport.State == "AfterAD":
                route = planPath(w_xc, w_yc, nowVport.x_coor, nowVport.y_coor)
                estiDate = getEsti_Ms(route) * 1000 + t_ms
                estiDist = getEsti_dist(route)
                nowWport.dist = estiDist
                nowWport.esTime = estiDate
                if nowVport.EEnd - nowWport.esTime > 0:
                    totalCost = max(nowVport.EStart - nowWport.esTime, 0) * \
                                nowVport.quayRate * sp_weight / 60 / 60 / 1000 + \
                                nowWport.dist * nowWport.carryRate * sp_weight
                    nowWport.supCost = totalCost
                    nowWport.sortFlag = nowVport.sortFlag
                    routeMp[nowWport.pname] = route
                    candinateWports.append(nowWport)
        candinateWports.sort(key=lambda port: port.sortFlag)

        import sys
        minCost = sys.maxsize
        destPort = None
        pathResult = None
        for i, twp in enumerate(candinateWports):
            co = (1 - pow(k, i + 1)) * twp.supCost
            twp.supCost = co
            if co < minCost:
                minCost = co
                destPort = (WPort)(twp)
                pathResult = routeMp.get(twp.pname)

        vmfEvent = {"createdAt": time.time()}
        if destPort:
            setVairable(vpid, "dpName", destPort.pname)
            setVairable(wpid, "DestPort", destPort)
            setVairable(wpid, "W_TargPortList", candinateWports)
            vmfEvent["W_Info"] = w_info
            vmfEvent["wDestPort"] = json.dumps(destPort)
            vmfEvent["vDestPort"] = json.dumps(vpMap[destPort.pname])
            vmfEvent["pathResult"] = pathResult
            vmfEvent["V_pid"] = vpid
            vmfEvent["StartTime"] = vStartTime
            vmfEvent["State"] = "success"
            vmfEvent["Reason"] = reason
        else:
            vmfEvent["State"] = "fail"
        # TODO globalEventQueue.sendMsg(e);


def getVariable(pid, variableName):
    get_url = activiti_url + "/zbq/variables/{}/{}".format(pid, variableName)
    print(get_url)

    ret = requests.get(get_url, headers=headers).json()
    print(ret)

    return ret


def setVairable(pid, variableName, value):
    set_url = activiti_url + "/zbq/variables/{}/{}/complete".format(pid, variableName)
    print(set_url)

    data = {variableName: value}
    requests.put(set_url, data=data, headers=headers)


def getVPorts(vpid, vname):
    ret = getVariable(vpid, vname)

    vPortList = json.loads(ret.get('vname', {"status": "wrong Vports"}))
    print(vPortList)

    V_Ports = [VPort(v) for v in vPortList]
    print(V_Ports)

    return V_Ports


def getWPorts(wpid, vname):
    ret = getVariable(wpid, vname)
    wPortList = json.loads(ret.get('vname', {"status": "wrong Wports"}))
    print(wPortList)

    W_Ports = [WPort(w) for w in wPortList]
    print(W_Ports)

    return W_Ports


def getEsti_Ms(route):
    paths = route.get("paths", [{"duration": -1}])
    path = paths[0]
    return path.get["duration"]


def getEsti_dist(route):
    paths = route.get("paths", [{'distance': -1.0}])
    path = paths[0]
    return (float)(path.get('distance'))


def planPath(x1, y1, x2, y2):
    map_url = "http://restapi.amap.com/v3/direction/driving?origin={},{}&destination={},{}&output=json&key=ec15fc50687bd2782d7e45de6d08a023" \
        .format(x1, y1, x2, y2)
    print(map_url)

    ret = requests.get(map_url, headers=headers).json()
    print(ret)

    return ret.get("route", None)
