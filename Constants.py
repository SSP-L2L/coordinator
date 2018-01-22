# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'
import time
import json
import requests
from .VPort import VPort
from .WPort import WPort

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
activiti_url = "http://10.131.245.91:8084"
zoomInRate = 500  # 时间比例系数
k = 0.5  # 紧迫性参数
serialVersionUID = 5334846840309131394
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
