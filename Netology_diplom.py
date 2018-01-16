# import time
# import json
import requests

USER_ID = '5030613'


def call_vk(method, params):
    parameters = {
        'access_token': '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128',
        'v': '5.69',
        }
    parameters.update(params)
    response = requests.get('https://api.vk.com/method/{}'.format(method), parameters)
    return response.json()['response']


def get_user(user_id):
    response = call_vk('users.get', {'user_ids': user_id, 'fields': 'id'})
    user_id = response[0]['id']
    return user_id


def get_friends(user_id):
    response = call_vk('friends.get', {'user_id': user_id})
    friends = response['items']
    return friends


