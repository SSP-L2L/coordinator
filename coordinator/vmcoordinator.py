# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
Vessel/Manager Coordinator
"""
import json
import string

import requests
from requests.auth import HTTPBasicAuth

from coordinator.constants import *


def VMCoordinator(msg):
    """
    >>> msg = { \
        'msgType' : string, \
    }
    :param msg:
    :return:
    """
    msgType = msg.get("msgType")
    if msgType == "Msg_StartMana":
        msg.pop("msgType", None)
    print(msg)

    url = ACTIVITI_URL + "/coord/runtime/{}".format(msgType)
    auth = HTTPBasicAuth("admin", "test")
    print(requests.post(url, auth=auth, data=json.dumps(msg), headers=HEADERS))
