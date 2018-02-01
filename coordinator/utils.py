# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
constants
"""
import json
import requests
from requests.auth import HTTPBasicAuth

HEADERS = {'Content-type': 'application/json; charset=UTF-8', 'Accept': 'application/json'}
ACTIVITI_URL = "http://localhost:8080/activiti-app/api"

ZOOM_IN_RATE = 500  # 时间比例系数
K = 0.5  # 紧迫性参数

carRateMp = {
    "黄石" : 0.0021, "武穴": 0.0021, "九江": 0.0021, "安庆": 0.0021, "池州": 0.0021, "铜陵": 0.0021, "芜湖": 0.0021,
    "马鞍山": 0.0021, "南京": 0.0021, "仪征": 0.0021, "镇江": 0.0021, "泰州": 0.0021, "常州": 0.0021, "江阴": 0.0021
}

# EventType
W_START = 0
W_UPDATE = 1
W_ARRIVAL = 2
V_STARTW_PLAN = 3
W_RUN = 4
W_Coord = 5
MSC_MeetWeightCond = 6
V_AnchorStart = 7
V_Dock = 8


def getVariable(pid, variableName):
    """

    :param pid: string
    :param variableName: string
    :return: json.loads
    """
    get_url = ACTIVITI_URL + "/zbq/variables/{}/{}".format(pid, variableName)
    print(get_url)

    auth = HTTPBasicAuth("admin", "test")
    ret = requests.get(get_url, auth=auth, headers=HEADERS).json()
    print(ret)

    return ret


def setVariable(pid, variableName, variableType, variableValue):
    """
    set variable in both globalCache and runtimeService
    :param pid: string
    :param variableName: string
    :param variableType: string
    :param variableValue: variableType
    :return:
    """
    set_url = ACTIVITI_URL + "/zbq/variables/{}/{}/complete".format(pid, variableName)
    print(set_url)

    data = json.dumps({'name': variableName, 'type': variableType, 'value': variableValue, 'scope': 'local'})
    auth = HTTPBasicAuth("admin", "test")
    print(requests.put(set_url, auth=auth, data=data, headers=HEADERS))


def sendEvent(vmfvent):
    """

    :param vmfvent: json.dumps
    :return:
    """
    url = ACTIVITI_URL + "/coord/event"
    print(url)

    auth = HTTPBasicAuth("admin", "test")
    print(requests.post(url, auth=auth, data=vmfvent, headers=HEADERS))


def sendMessage(msgName, data):
    """

    :param msgName: string
    :param data: json.dumps
    :return:
    """
    url = ACTIVITI_URL + "/coord/messages/{}".format(msgName)
    print(url)

    auth = HTTPBasicAuth("admin", "test")
    print(requests.post(url, auth=auth, data=data, headers=HEADERS))


def sendMessageToStartProcessInstance(msgName, data):
    """

    :param msgName: string
    :param data: json.dumps
    :return:
    """
    url = ACTIVITI_URL + "/coord/runtime/{}".format(msgName)
    print(url)

    auth = HTTPBasicAuth("admin", "test")
    print(requests.post(url, auth=auth, data=data, headers=HEADERS))
