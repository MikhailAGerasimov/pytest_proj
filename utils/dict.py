def get_val(collection, key, default='git'):
    '''
    Возращает значение ключа словаря, если такой ключ есть
    иначе возвращает значение default
    :param collection: исходный словарь
    :param key:ключ, который необходимо найти
    :param default: значение default, по умолчанию == 'git'
    :return: возвращает значение словаря, соответствующее ключу key или default, если такого ключа нет
    '''
    if key in list(collection.keys()):
        return collection[key]
    else:
        return default
