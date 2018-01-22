# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'
"""
Vessel/Manager Coordinator
"""
from Constants import *

def VMCoordinator(msg):
    """
    :param msg:
    :return:
    """
    msgType = msg.get("msgType")
    if msgType == "Msg_StartMana":
        msg.pop("msgType", None)


if __name__ == "__main__":
    from pprint import pprint
    msg = {}

    pprint(VMCoordinator(msg))
