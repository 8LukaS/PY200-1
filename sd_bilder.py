#! /usr/bin/env python
# -*- coding: utf-8 -*-
from abc import abstractmethod
from structure_draiver import *

class SDBuilder:
    '''
    патерн стратегия ,строит новый обьект
    '''
    @abstractmethod
    def build(self):
        return None
    def __str__(self):
        return self.__class__.__name__
# возможность выбора билдера

class JSONFileBuilder(SDBuilder):

    def build(self):
        filename = input('Enter filename (.json)>')
        return JSONFileDriver(filename)


class JSONStrBuilder(SDBuilder):
    def build(self):
        filename = input('Enter jsonstring>')
        return JSONFileDriver(filename)
        # return JSONStringDriver()


class PickleBuilder(SDBuilder):
    def build(self):
        filename = input('Enter filename (.bin)>')
        return PickleDriver(filename)

class YAML(SDBuilder):
    def build(self):
        filename = input('Enter filename (.yml)>')
        return YAMLDriver(filename)

class SDFabric:
    @staticmethod
    def get_sd_driver(driver_name):
        builders = {'json': JSONFileBuilder,
                    'json_str': JSONStrBuilder,
                    'pickle': PickleBuilder}
        return builders[driver_name]()

if __name__ =='__main__':
    driver_name =input('Please enter driver name ->')
    driver_bilder = SDFabric.get_sd_driver(driver_name)
    # driver = driver_bilder.build()
    print(driver_bilder)
    # link =
