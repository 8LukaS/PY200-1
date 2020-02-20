#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Тема 2. Инкапсуляция, наследование, полиморфизм
class A:
     рublic_class_attr_A= 'pubkic_class_attr_A'
     _protected_class_A ='_protected_class_attr_A'
     __privated_class_A = '_privated_class_A'

     def __init__(self):
          self.рublic_attr_metnhod = рublic__attr_metnhod
          self._protected_attr_metnhod = _protected_attr_metnhod
          self.__privated_attr_metnhod = __privated_attr_metnhod

     def рublic_object_metnhod(self):
          print('рublic_object_mtnhod')
     def _protected_object_metnhod(self):
          print('protected_object_metnhod')
     def __privated_object_metnhod(self):
          print('privated_object_metnhod')

     @classmethod

     @staticmethod


if __name__ = '__main__':
