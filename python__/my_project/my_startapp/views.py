from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
import requests


# Create your views here.
def send_req(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    return None
