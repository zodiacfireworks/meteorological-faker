# -*- encoding: utf-8 -*-
from html.parser import HTMLParser
from urllib.request import urlopen
from datetime import datetime

import json
import re

class meteorological_parser(HTMLParser):
    def __init__(self):
        super(meteorological_parser, self).__init__()
        self.Data = []

    def handle_data(self, data):
        data = data.replace('\xa0', '')

        if data:
            self.Data.append(data)

    def getData(self, mode=dict):
        dictData = {}

        try:
            DateTime = self.Data[4]+'m'
            DateTime = datetime.strptime(DateTime, "%d/%m/%y%I:%M%p")

            dictData = {
                'date': DateTime.strftime("%Y/%m/%d"),
                'time': DateTime.strftime("%H:%M"),
                'temperature': float(self.Data[8][:-1]),
                'humidity': float(self.Data[11][:-1]),
                'dew_point': float(self.Data[14][:-1]),
                'pressure': float(self.Data[17][:-2]),
                'uv_index': float(self.Data[26][:-5]),
                'solar_radiation': float(self.Data[29][:-3]),
            }

        except Exception as e:
            return dictData

        return dictData


def meteorological_collector():
    """
    Obtiene los registros de tiempo atmosférico y radiación solar de la
    estacion DAVIS identificada por STA0001, actualmente ubicada en el edificio
    de CONIDA.

    Los datos de esta estación estan disponibles en
    * http://www.conida.gob.pe/OTROS/joomla/astro/clima.htm
    y corresponden a los promedios cada 5 minutos de los datos registrados.
    """
    record = {
        "success": False,
        "data": []
    }

    try:
        response = urlopen(
            'http://www.conida.gob.pe/OTROS/joomla/astro/clima.htm',
            timeout=5
        )

    except Exception as e:
        return record

    responseHTML = response.read()
    responseHTML = str(responseHTML, errors='ignore')

    regexPattern = re.compile('&(\w)acute;')
    responseHTML = regexPattern.sub(r'\1', responseHTML)

    regexPattern = re.compile(' +|\r\n|,|\t')
    responseHTML = regexPattern.sub('', responseHTML)

    try:
        recordParser = meteorological_parser()
        recordParser.feed(responseHTML)
        recordData = recordParser.getData()

    except Exception as e:
        record

    record["success"] = True
    record["data"] = recordData

    return record
