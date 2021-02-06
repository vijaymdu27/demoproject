from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
import json


def index(request):
    print("test")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        "Upgrade-Insecure-Requests": "1", "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}

    response = requests.get("https://www1.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch"
                            ".json", headers=headers)
    print("hello")
    data = response.text
    print(data)

    return HttpResponse(data)


def test(request):
    url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json"

    payload = {}
    headers = {
        'Cookie': 'ak_bmsc=70E878B7E89756A8FB74F73AC084DBDF172C0A0F662000004F9B1E601B1D5023~plNtjHD5vScybwiWjrIek6meVsVgp38dXL9rPi8CxOYt4aP5wy1USKaDfL1iCn9o/CTWDSZbmQ0B6wfvHBkBP+BYfbsFrxuULxAQ7uKlkxTBOr02CV/NO4uXmCQm2JAklMvBEgLhhakjWnIzJBqWRNFeTM2TxYHlTx7Z7FTpOmUn1BYxnqBta+TaY/TeSsdNAM8/kYpA+usD/GUGQmXcDOx6xV4qECBkDOEM7MkD4bp8I='
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)