"""""
#todo 1: создайте модуль serializer

# В модуле реализуйте три функции сериализации

# Функция сериализует объект в байтовый поток pickle
# Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.pkl"
def to_pickle(obj, file):
    pass
    # ваш код

#  Функция сериализует объект в json
#  Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.json"
def to_json(obj, file):
    pass
    # ваш код

# Функция сериализует объект в yaml
# Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.yml"
def to_yaml(obj, file):
    pass
    # ваш код


#todo 2: Cоздайте модуль deserializer. В модуле реализуйте три функции десериализации


# Функция десериализует объект из файла типа pickle
# file - файл для десериализации к примеру "data.pkl"
def from_pickle(file):
    pass
    # ваш код

# Функция десериализует объект из файла типа json
# from_json - функция сереализует объект в json
# Параметры
# file - файл для десериализации к примеру "data.json"
def from_json(file):
    pass
    # ваш код


# Функция десериализует объект из файла типа yaml
# Параметры
# file - файл для десериализации к примеру "data.yml"
def from_yaml(file):
    pass
    # ваш код

#todo 3: Cоздайте пакет из двух модулей serializer и deserializer.

# Импортируйте модули пакета в отдельный файл и протестируйте все функции.


"""""

import pickle
import json
import yaml

#сериализатор 
def to_pickle(obj, file):
    with open(file, 'wb') as f:
        pickle.dump(obj, f)


def to_json(obj, file):
    with open(file, 'w') as f:
        json.dump(obj, f)


def to_yaml(obj, file):
    with open(file, 'w') as f:
        yaml.dump(obj, f, default_flow_style=False)
        
#десериализатор
def from_pickle(file):
    with open(file, 'rb') as f:
        return pickle.load(f)


def from_json(file):
    with open(file, 'r') as f:
        return json.load(f)


def from_yaml(file):
    with open(file, 'r') as f:
        return yaml.safe_load(f)
#пакет из 2х модулей
from mypackage.serializer import to_pickle, to_json, to_yaml
from mypackage.deserializer import from_pickle, from_json, from_yaml


obj = {'a': 1, 'b': 2, 'c': 3}
to_pickle(obj, 'data.pkl')

to_json(obj, 'data.json')

to_yaml(obj, 'data.yml')

obj_pickle = from_pickle('data.pkl')
print(obj_pickle)
obj_json = from_json('data.json')
print(obj_json)
obj_yaml = from_yaml('data.yml')
print(obj_yaml)
