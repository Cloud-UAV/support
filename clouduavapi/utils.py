import requests as req
import pytz
from flask import request
from datetime import date, datetime, timedelta

STA_URL = "STA_ENDPOINT"
local = pytz.timezone("America/Edmonton")

def getSTA(query):
    """ Return CloudUAV STA query """
    r = req.get(STA_URL)
    return r.json()

def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']