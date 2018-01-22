# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'
"""
Manager/Supplier Coordinator
"""


def MSCoordinator(msgData):
    """
    msgType == "Msg_StartSupplier"
    :param msgData: dict
    :return:
    """
    # 筛选港口
    w_threshold = msgData.get("SparePartWeight")
    targetLocationMap = msgData.get("V_TargLocList")

    # map to list ???
    # targetLocationList =

    candidateVPorts = []
    for key, value in targetLocationMap.items():
        pass
    pass


if __name__ == "__main__":
    msgData = {}
    from pprint import pprint

    pprint(MSCoordinator(msgData))
