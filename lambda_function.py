# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'
"""
lambda function in aws lambda
"""
from . import *


def lambda_handler(event, context):
    msg = {}
    msg['receivemsg'] = event
    msg['sendfrom'] = 'lambda'
    msg['timestamp'] = time.time()

    return msg
