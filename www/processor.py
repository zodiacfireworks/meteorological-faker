from urllib.request import urlopen

from parser import RecordParser

import json
import re


def RecordCollector():
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
        recordParser = RecordParser()
        recordParser.feed(responseHTML)
        recordData = recordParser.getData()

    except Exception as e:
        record

    record["success"] = True
    record["data"] = recordData

    return record
