import json
from django.http import HttpResponse
from django.shortcuts import render
from functools import reduce
from orderAndTrade.views import get_history

# Create your views here.

def index(request):
    data = get_history()
    first_price = float(data[-1].get('bidprice'))
    price = float(data[0].get('bidprice'))
    volume = reduce((lambda x, y: x + float(y.get('amount'))), data, 0)
    change = float((price - first_price) / first_price)
    result = {
        "code": 200,
        "data": [
            {
                'symbol': "btc", 'price': price, 'change': change, 'volume': volume
            }
        ]
    }
    return HttpResponse(json.dumps(result), content_type="application/json")
