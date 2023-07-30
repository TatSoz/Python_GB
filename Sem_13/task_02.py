# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


def dict_get(dic: dict, key, value_def = None):
    value = value_def
    try:
        value = dic[key]
    except KeyError:
        pass
    return value



if __name__ == '__main__':
    test = {'1': 8, '2': 'Hello'}
    print(f"{dict_get(test, '1') = }")
    print(f"{dict_get(test, '2') = }")
    print(f"{dict_get(test, '3') = }")





