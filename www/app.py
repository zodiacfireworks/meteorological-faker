# -*- encoding: utf-8 -*-
from flask import Flask
from flask import Response
from flask import render_template

from datetime import datetime

from processor import meteorological_collector

import random
import json
import sys

app = Flask(__name__)

faker = True
last_check = ''
current_check = ''
response_data = {}

@app.route("/api/")
def api():
    global last_check
    global current_check
    global response_data

    current_check = datetime.now().strftime("%Y%m%dT%H%M")

    if current_check != last_check:
        if faker == True:
            response_data = {
                "success": True,
                "data": {
                    'date': current_check.split("T")[0],
                    'time': current_check.split("T")[1],
                    'temperature': float("{0:.2f}".format(25 + 4*(0.5 - random.random()))),
                    'humidity': float("{0:.2f}".format(75 + 10*(0.5 - random.random()))),
                    'dew_point': float("{0:.2f}".format(15 + 4*(0.5 - random.random()))),
                    'pressure': float("{0:.2f}".format(768 + 5*(0.5 - random.random()))),
                    'uv_index': float("{0:.2f}".format(10 + 6*(0.5 - random.random()))),
                    'solar_radiation': float("{0:.2f}".format(100 + 20*(0.5 - random.random()))),
                }
            }
        else:
            response_data = meteorological_collector()

        last_check = current_check

    response = Response(
        response=json.dumps(
            response_data,
            indent=4
        ),
        status=200,
        content_type="application/json; charset=utf-8"
    )

    response.headers['Access-Control-Allow-Origin'] = '*'

    return response


@app.route('/')
def index():
    response = Response(
        response=render_template('index.html'),
        status=200,
        content_type="text/html; charset=utf-8"
    )

    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

    return response


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "no-fake":
            faker = False
        elif sys.argv[1] == "fake":
            faker = True
        else:
            raise(Exception("Unknown flag {0}".format(sys.argv[1])))

    app.run(host='0.0.0.0')
