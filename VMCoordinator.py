# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
Vessel/Manager Coordinator
"""
import string


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
