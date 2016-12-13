# -*- encoding: utf-8 -*-
from datetime import datetime
from html.parser import HTMLParser

import json

class RecordParser(HTMLParser):

    def __init__(self):
        super(RecordParser, self).__init__()
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
