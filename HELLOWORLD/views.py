from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def route2(request):
    responseData = {
        'message': 'Hello World'
    }

    return JsonResponse(responseData)


