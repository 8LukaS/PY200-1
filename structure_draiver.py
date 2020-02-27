#! /usr/bin/env python
# -*- coding: utf-8 -*-
# In[1]:


# Шаблон проектирования "Стратегия"
import os

import json
import pickle
import yaml
from pprint import pprint

class IStructureDriver:
    def read(self):
        pass

    def write(self, d):
        pass


class JSONFileDriver(IStructureDriver):

    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        with open(self.__filename, encoding='UTF-8') as f:
            return json.load(f)

    def write(self, d):
        print(os.getcwd())
        with open(self.__filename, 'w', encoding='UTF-8') as f:
            json.dump(d, f, ensure_ascii=False)


class JSONStringDriver(IStructureDriver):
    def __init__(self, s='{}'):
        self.__s = s

    def get_string(self):
        return self.__s

    def read(self,s=None):
        if s is None:
            return json.loads(self.__s)

    def write(self, d):
        self.__s = json.dumps(d, ensure_ascii=False)


class PickleDriver(IStructureDriver):
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        with open(self.__filename, 'rb') as f:
            return pickle.load(f)

    def write(self, d):
        with open(self.__filename, 'wb') as f:
            pickle.dump(d, f)

class YAMLDriver(IStructureDriver):
    def __init__(self, filename):
        self.__filename = filename

    def read(self): #чтение из YAML
        with open(self.__filename, 'rb') as f:
            yaml.safe_load(f)

    def write(self, d): #запись объектов Python в YAML
        with open(self.__filename, 'wb') as f:
            yaml.dump(d, f)


if __name__ == '__main__':

    class SDWorker:
        '''
        будет возврощать питоновский словарь
        '''
        def __init__(self, structure_driver: IStructureDriver):
            self.__structure_driver = structure_driver

        def load(self): # вызывает метод read   из IStructureDriver возвврошает словарь
            return self.__structure_driver.read()

        def save(self,d): #записывает в фаил
            self.__structure_driver.write(d)

        def set_stucture_driver(self,driver):     #установливает новый драивер для SDWorker
            self.__structure_driver = driver

    # json_driver = JSONFileDriver('test.json')
    # sd = SDWorker(json_driver)
    #
    # d ={1:1,
    #     2:2,
    #     3:3
    # }
    # sd.write(d)


