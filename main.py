#! /usr/bin/env python
# -*- coding: utf-8 -*-
from sd_bilder import SDFabric
from linked_list import*

if __name__== '__main__':
    driver_name = input( 'Введите название драйвера')
    driver_bilder = SDFabric.get_sd_driver(driver_name)
    driver = driver_bilder.build()
    ll = LinkedList()
    ll.set_stucture_driver(driver)
    ll.insert_node(20,gkj)
    ll.save()


