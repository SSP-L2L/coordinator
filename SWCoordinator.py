# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'
"""
Supplier/Wagon Coordinator
"""


def SWCoordinator(msgData):
    """
    msgType == "Msg_StartWeagon"
    :param msgData: dict
    :return:
    """
    wagon = {}
    wagon["wagon_name"] = "weagon_1"
    wagon["x"] = 113.2982254028
    wagon["y"] = 23.0958388047
    wagon["is_arrival"] = False
    msgData["W_Info"] = wagon
    msgData["msgType"] = "#"
    msgData["M_pid"] = "#"

    # ???
    # runtimeService.startProcessInstanceByMessage("Msg_StartWeagon", msgData);

    pass