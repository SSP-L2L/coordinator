# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
constants
"""
import inspect


def get_current_function_name():
    return inspect.stack()[1][3]


HEADERS = {'Content-type': 'application/json; charset=UTF-8', 'Accept': 'application/json'}
ACTIVITI_URL = "http://localhost:8080/activiti-app/api"
ZOOM_IN_RATE = 500  # 时间比例系数
k = 0.5  # 紧迫性参数
carRateMp = {
    "黄石" : 0.0021,
    "武穴" : 0.0021,
    "九江" : 0.0021,
    "安庆" : 0.0021,
    "池州" : 0.0021,
    "铜陵" : 0.0021,
    "芜湖" : 0.0021,
    "马鞍山": 0.0021,
    "南京" : 0.0021,
    "仪征" : 0.0021,
    "镇江" : 0.0021,
    "泰州" : 0.0021,
    "常州" : 0.0021,
    "江阴" : 0.0021
}
