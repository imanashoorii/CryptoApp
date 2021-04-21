from django.forms.models import model_to_dict
import requests
from .models import Crypto

# Import shared_task decorator
from celery import shared_task


@shared_task
def get_coins_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    coins = []

    for coin in data:
        obj, created = Crypto.objects.get_or_create(name=coin['name'])
        
        obj.name = coin['name']
        obj.image = coin['image']

        # if obj.current_price > coin['current_price']:
        #     state = 'fall'
        # elif obj.current_price == coin['current_price']:
        #     state = 'same'
        # elif obj.current_price < coin['current_price']:
        #     state = 'raise'

        obj.current_price = coin['current_price']
        obj.market_cap_rank = coin['market_cap_rank']
        obj.market_cap = coin['market_cap']

        obj.save()

        new_data = model_to_dict(obj)
        # new_data.update({'state': state})

        coins.append(new_data)