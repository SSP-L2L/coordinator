# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
Vessel/Manager Coordinator
"""
import json
import string
import time

import requests
from requests.auth import HTTPBasicAuth

from coordinator.constants import *


def VMCoordinator(msg):
    """
    :param msg:
    :return:
    """
    msgType = msg.get("msgType")
    if msgType == "Msg_StartMana":
        print(time.asctime())
        print("sending data to Manager")
        sendMessageToStartProcessInstance(msgType, msg)
