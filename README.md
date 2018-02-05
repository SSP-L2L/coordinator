# Coordinator

This repo contains code that simulates aws lambda locally.

As we all know, aws lambda can receive different requests from aws api gateway, for example, "GET" and "POST". Aws lambda accept "application/json" and response also in "application/json" by default. It can be coded in different languages, such as Python, Java, and Javascript.

In this project, we just take the default behaviour and use python as develop languages. Flask is a very light web framework in python and it can simply simulate lambda behaviour in several lines of code.
 
 ## repo organize
 lambda_function.py is as same as the one in aws lambda function. In this part, we use the lambda_function as the dispatcher of four coordinator function.
 ```text
 .
├── coordinator
│   ├── __init__.py
│   ├── mscoordinator.py
│   ├── swcoordinator.py
│   ├── utils.py
│   ├── vmcoordinator.py
│   ├── vport.py
│   ├── vwcoordinator.py
│   └── wport.py
├── __init__.py
├── lambda_function.py
└── server.py
 ```
 
 ## simple local lambda server written in flask
 ```python
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
```

## pre-install and run
```bash
sudo pip install flask
python server.py
```

##  Dependencies
-   [`The Simulator of vessel and wagon`](https://github.com/sonnyhcl/Frontend/tree/lambda)

    > Attention: In order to perform as demo shows, The Activiti Backend project must be coordinated with the Vessel Frontend project.

-   [`SPS Backend`](https://github.com/sonnyhcl/backend/tree/lambda)

    The backend of Spare Parts Supply-chain management implemented mainly based on `activiti` - the BPMN engine backend project