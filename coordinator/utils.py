# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
constants and utils
"""
import json
import requests
from requests.auth import HTTPBasicAuth

HEADERS = {'Content-type': 'application/json; charset=UTF-8', 'Accept': 'application/json'}
AUTH = HTTPBasicAuth("admin", "test")
ACTIVITI_URL = "http://localhost:8080/activiti-app/api"
ZOOM_IN_RATE = 500  # 时间比例系数
K = 0.5  # 紧迫性参数

carRateMp = {
    "黄石" : 0.0021, "武穴": 0.0021, "九江": 0.0021, "安庆": 0.0021, "池州": 0.0021, "铜陵": 0.0021, "芜湖": 0.0021,
    "马鞍山": 0.0021, "南京": 0.0021, "仪征": 0.0021, "镇江": 0.0021, "泰州": 0.0021, "常州": 0.0021, "江阴": 0.0021
}

def getVariable(pid, variableName):
    """
    get variable in globalCache
    :param pid: string
    :param variableName: string
    :return: json.loads
    """
    get_url = ACTIVITI_URL + "/zbq/variables/{}/{}".format(pid, variableName)
    print(get_url)

    ret = requests.get(get_url, auth=AUTH, headers=HEADERS).json()
    print(ret)
    print(get_url, " DONE")

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
    print(data)

    resp = requests.put(set_url, auth=AUTH, data=data, headers=HEADERS)
    print(resp.url, resp.status_code, resp.text)


def setCache(pid, variableName, variableType, variableValue):
    """
    set variable in both globalCache
    :param pid: string
    :param variableName: string
    :param variableType: string
    :param variableValue: variableType
    :return:
    """
    set_url = ACTIVITI_URL + "/zbq/variables/{}/{}".format(pid, variableName)
    print(set_url)

    data = json.dumps({'name': variableName, 'type': variableType, 'value': variableValue, 'scope': 'local'})
    print(data)

    resp = requests.put(set_url, auth=AUTH, data=data, headers=HEADERS)
    print(resp.url, resp.status_code, resp.text)


def sendMSCEvent(event):
    """

    :param event: json.dumps
    :return:
    """
    url = ACTIVITI_URL + "/coord/msc_event"
    print(url)
    print(event)

    resp = requests.post(url, auth=AUTH, data=event, headers=HEADERS)
    print(resp.url, resp.status_code, resp.text)


def sendVWCEvent(event):
    """

    :param vmfvent: json.dumps
    :return:
    """
    url = ACTIVITI_URL + "/coord/vwc_event"
    print(url)
    print(event)

    resp = requests.post(url, auth=AUTH, data=event, headers=HEADERS)
    print(resp.url, resp.status_code, resp.text)


def sendMessage(msgName, data):
    """

    :param msgName: string
    :param data: json.dumps
    :return:
    """
    url = ACTIVITI_URL + "/coord/messages/{}".format(msgName)
    print(url)
    print(data)

    resp = requests.post(url, auth=AUTH, data=data, headers=HEADERS)
    print(resp.url, resp.status_code, resp.text)


def sendMessageToStartProcessInstance(msgName, data):
    """

    :param msgName: string
    :param data: json.dumps
    :return:
    """
    url = ACTIVITI_URL + "/coord/runtime/{}".format(msgName)
    print(url)
    print(data)

    resp = requests.post(url, auth=AUTH, data=data, headers=HEADERS)
    print(resp.url, resp.status_code, resp.text)
