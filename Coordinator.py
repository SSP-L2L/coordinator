# -*- coding: UTF-8 -*-
__author__ = 'sonnyhcl'

"""
imitate lambda container
"""
from flask import Flask, request, jsonify

from lambda_function import lambda_handler

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def hello_world():
    """
    input:  application/json
    output: application/json
    """
    print(request.json)
    if not request.json:
        return jsonify({"ErrorMsg": "Only Accept application/json"})
    return jsonify(lambda_handler(request.json, None))


@app.route('/post', methods=['post'])
def getpost():
    """
    测试跟activiti流程进行交互的Msg信号
    :return:
    """
    ret = request.json
    ret["status"] = "success"
    print(ret)

    import requests
    import json
    from requests.auth import HTTPBasicAuth

    url = "http://localhost:8080/activiti-app/api/coord/messages/Msg_StartRec"
    headers = {'Content-Type': "application/json", 'Accept': "application/json"}
    auth = HTTPBasicAuth("admin", "test")

    response = requests.post(url, auth=auth, data=json.dumps(ret), headers=headers)
    print(response)

    return jsonify(request.json)


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)
