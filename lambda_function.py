# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'
"""
lambda function in aws lambda
"""


def lambda_handler(event, context):
    import time

    msg = {}
    msg['receivemsg'] = event
    msg['sendfrom'] = 'lambda'
    msg['timestamp'] = time.time()
    serialVersionUID = 5334846840309131394

    # url = "http://18.218.117.121:7777/lambda"
    # headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    # ret = requests.post(url, data=json.dumps(msg), headers=headers)
    # print(ret)

    return msg
