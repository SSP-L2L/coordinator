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
    print("lambda request.json=", request.json)
    if not request.json:
        return jsonify({"ErrorMsg": "Only Accept application/json"})

    msg = lambda_handler(request.json, None)
    return jsonify(msg)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, threaded=True, debug=True)
