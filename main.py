from pprint import pprint

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]


def search_terms(queriers):
    list_ = []
    for i in queriers:
        word = i.split()
        list_.append((len(word)))
    list1 = set(list_)
    list2 = list(list1)
    list2.sort()
    list_3 = []
    for i in list2:
        number = list_.count(i)
        list_3.append(f'Поисквых запросов из {i} слов {number * 100 / len(queriers):.2f}%')
    return list_3


def geo_id(ids):
    empty_list = []
    for i, b in ids.items():
        empty_list += b
    list1 = set(empty_list)
    list_2 = []
    for v in list1:
        list_2.append(v)
    return(sorted(list_2))


def maximum_volume(stat):
    number = 1
    for i, b in stat.items():
        if b > number:
            number = b
    for i, b in stat.items():
        if b == number:
            return (i)

