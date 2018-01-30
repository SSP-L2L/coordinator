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
    msg = {}
    # msg['receivemsg'] = event
    msg['sendfrom'] = 'lambda'
    msg['timestamp'] = time.time()

    # dispatcher
    msgType = event.get("msgType")
    print(msgType)
    if msgType == "Msg_StartMana":
        VMCoordinator(event)
    elif msgType == "msg_UpdateDest" or msgType == "msg_CreateVWConn":
        VWCoordinator(event)
    elif msgType == "Msg_StartWeagon":
        SWCoordinator(event)
    elif msgType == "Msg_StartSupplier":
        MSCoordinator(event)

    return msg
