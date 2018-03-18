# Coordinator

This repo contains code that simulates aws lambda locally.

As we all know, aws lambda can receive different requests from aws api gateway, for example, "`GET`" and "`POST`". Aws lambda accept "`application/json`" and response also in "`application/json`" by default. It can be coded in different languages, such as Python, Java, and Javascript.

In this project, we just take the default behaviour and use python as develop languages. Flask is a very light web framework in python and it can simply simulate lambda behaviour in several lines of code.
 
 ## deploy our python code on lambda
 
 > ref: [https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)
 
Before uploading code to lambda, we need to install the libraries we used in our code  directly in the working directory.

For example, we use `requests` package in this coordinator project. 
```bash
pip install requests -t .
```
 Note that `server.py` is only used in local simulation and it won't and shouldn't run in lambda. So we don't need to `pip install` `flask` inside the directory.
 
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

## pre-install and run locally
```bash
sudo pip install flask requests
python server.py
```

##  Dependencies
-   [`The Simulator of vessel and wagon`](https://github.com/SSP-L2L/Frontend/tree/lambda)

    > Attention: In order to perform as demo shows, The Activiti Backend project must be coordinated with the Vessel Frontend project.

-   [`SPS Backend`](
https://github.com/SSP-L2L/backend/tree/lambda)

    The backend of Spare Parts Supply-chain management implemented mainly based on `activiti` - the BPMN engine backend project
    
## Video URL
-   [`SSP-L2L`](https://www.dropbox.com/s/2r6iiy8cf0bjsjf/SSP-L2L.mpg?dl=0)
    > This is an eight-minute video that shows the operation and effect of the system.
