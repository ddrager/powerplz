from django.http import JsonResponse
from decimal import *
from datalogger.models import DataPoint
from notifier.push import *
import json


def logdata_hem(request, curwatts = 0):
    getcontext().prec = 8
    new_datapoint = {
        'type': 'WATTS',
        'value': curwatts,
    }
    datapoint = DataPoint(type=new_datapoint['type'], value=new_datapoint['value'])
    datapoint.save()

    result = {
        'id': datapoint.id,
        'value': datapoint.value,
        'type': datapoint.type,
        'success': True,
    }

    publish_push('hem', json.dumps(result))

    return JsonResponse(result, safe=True)


def logdata(request, value):
    result = {
        'value': value,
        'success': True,
    }
    return JsonResponse(result, safe=True)
