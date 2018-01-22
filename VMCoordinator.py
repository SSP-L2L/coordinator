# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
Vessel/Manager Coordinator
"""
from . import *


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
