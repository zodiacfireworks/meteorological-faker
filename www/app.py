from flask import Flask
from flask import Response
from flask import render_template

from processor import RecordCollector

from datetime import datetime

import random
import json


app = Flask(__name__)

last_check = ''
current_check = ''
data = {}

@app.route("/api/")
def api():
    global last_check
    global current_check
    global data

    current_check = datetime.now()

    if current_check.strftime("%Y%m%dT%H%M") != last_check:
        data = {
            'date': current_check.strftime("%Y/%m/%d"),
            'time': current_check.strftime("%H:%M"),
            'temperature': float("{0:.2f}".format(25 + 4*(0.5 - random.random()))),
            'humidity': float("{0:.2f}".format(75 + 10*(0.5 - random.random()))),
            'dew_point': float("{0:.2f}".format(15 + 4*(0.5 - random.random()))),
            'pressure': float("{0:.2f}".format(768 + 5*(0.5 - random.random()))),
            'uv_index': float("{0:.2f}".format(10 + 6*(0.5 - random.random()))),
            'solar_radiation': float("{0:.2f}".format(100 + 20*(0.5 - random.random()))),
        }

        last_check = current_check.strftime("%Y%m%dT%H%M")

    response = Response(
        response=json.dumps(
            {"success": True, "data": data},
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
    response.headers['Access-Control-Allow-Headers'] = '*'

    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
