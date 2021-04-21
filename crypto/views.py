from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

def home_view(request):
    # data = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'

    # url = requests.get(data).json()
    # return HttpResponse(url)
    # context = {'data': url}
    return render(request, 'crypto/main.html')