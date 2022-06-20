from pprint import pprint

import stun
import requests

api_key = 'a4af42f30a2642699b4193057211810'


def get_my_ip():
    try:
        ip_list = stun.get_ip_info()
        return ip_list
    except Exception as ex:
        print(ex)


# print(get_my_ip())


def ip_to_city(my_ip: str):
    try:
        resp = requests.get(f'http://ip-api.com/json/{my_ip}?lang=ru')
        return resp.json()
    except Exception as ex:
        print(ex)


# print(city_to_ip(get_my_ip()[1]))


def get_weather_dict(ciy_name: str):
    try:
        weather_url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={ciy_name}&days=3&lang=ru'
        resp = requests.get(weather_url)
        return resp.json()
    except Exception as ex:
        print(ex)

