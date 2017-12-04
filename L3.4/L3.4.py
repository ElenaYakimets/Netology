import requests
from time import sleep
from collections import Counter

VERSION = 5.68
vk_id = 151952


def get_friends(vk_id, VERSION):
    params = {
        'user_id': vk_id,
        'v': VERSION
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    data = response.json()
    try:
        result = data['response']['items']
    except:
        result = data['error']['error_msg']
    return result


def friends_each_other(vk_id, VERSION):
    j = 1
    friends_each_other_list = []
    my_friends = get_friends(vk_id, VERSION)
    for i in my_friends:
        sleep(3)
        print(j, 'из', len(my_friends), 'проверено')
        j += 1
        if type(get_friends(i, VERSION)) is list:
            friends_each_other_list.append(get_friends(i, VERSION))
            print(len(friends_each_other_list), 'Список друзей найден')
    return friends_each_other_list


def list_lists(list_of_lists):
    result = []
    for i in list_of_lists:
        result += i
    return result


my_friends_each_other = friends_each_other(vk_id, VERSION)
fof_list = Counter(list_lists(my_friends_each_other)).most_common()