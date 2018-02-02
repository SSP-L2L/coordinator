# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
lambda function in aws lambda
"""
import time

from coordinator.vmcoordinator import VMCoordinator
from coordinator.vwcoordinator import VWCoordinator
from coordinator.mscoordinator import MSCoordinator
from coordinator.swcoordinator import SWCoordinator

def lambda_handler(event, context):
    # dispatcher
    msgType = event.get("msgType", "肯定是哪里又落了msgType")
    print("msgType=", msgType)
    if msgType == "Msg_StartMana":
        VMCoordinator(event)
    elif msgType == "msg_UpdateDest" or msgType == "msg_CreateVWConn":
        VWCoordinator(event)
    elif msgType == "Msg_StartWeagon":
        SWCoordinator(event)
    elif msgType == "Msg_StartSupplier":
        MSCoordinator(event)

    msg = {}
    msg['send_from'] = 'lambda'
    msg['timestamp'] = time.asctime()
    return msg
