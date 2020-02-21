#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Шаблон проектирования "Стратегия"

import json
import pic

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
        with open(self.__filename, 'w', encoding='UTF-8') as f:
            json.dump(d, f, ensure_ascii=False)
            
class JSONStringDriver(IStructureDriver):
    def __init__(self, s='{}'):
        self.__s = s
        
    def get_string(self):
        return self.__s

    def read(self):
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


# In[2]:


class SDWorker:
    def __init__(self, structure_driver: IStructureDriver):
        self.__structure_driver = structure_driver
        
    def do_work(self):
        try:
            d = self.__read_from_sd()
        except:
            self.__set_default()
            self.do_work()
            return
        
        print(f'Before set name: {d}')
        d['name'] = 'Python'
        print(f'After set name: {d}')
        self.__write_to_sd(d)
    
    def __set_default(self):
        d = {}
        self.__write_to_sd(d)        
        
    def __read_from_sd(self):
        return self.__structure_driver.read()
    
    def __write_to_sd(self, d):
        self.__structure_driver.write(d)
        
class SDBuilder:
    
    def build(self):
        return None
    
class JSONFileBuilder(SDBuilder):
    
    def build(self):
        filename = input('Enter filename (.json)>')
        return JSONFileDriver(filename)
    
class JSONStrBuilder(SDBuilder):
    def build(self):
        return JSONStringDriver()
    
class PickleBuilder(SDBuilder):
    def build(self):
        filename = input('Enter filename (.bin)>')
        return PickleDriver(filename)
    
class SDFabric:
    def get_sd_driver(self, driver_name):
        builders = {'json': JSONFileBuilder,
                    'json_str': JSONStrBuilder,
                    'pickle': PickleBuilder}
        try:
            return builders[driver_name]()
        except:
            return SDBuilder()


# In[3]:


# main

driver_name = input('Please enter driver name >')

builder = SDFabric().get_sd_driver(driver_name)
sd = builder.build()

sd_worker = SDWorker(sd)
sd_worker.do_work()

if isinstance(sd, JSONStringDriver):
    print('Для JSONStringDriver')
    print(sd.get_string())


# In[4]:


# Наблюдатель

class Observer:
    def update(self):#вызыватеся тогда когда ведутся изменения
        pass

class Subject:
    
    def __init__(self):
        self.__o = set()
        
    def add_observer(self, o: Observer):
        self.__o.add(o)
        
    def remove_observer(self, o: Observer):
        self.__o[o].remove(o)
    
    def notify(self):
        for o in self.__o:
            o.update(self)            


# In[5]:


class PrintView(Observer):
    def update(self, subject):
        print(f'Value changed: {hex(id(subject))}')
        
class SimpleView(Observer):
    def update(self, subject):
        print(f'SimpleView: {hex(id(subject))}')


# In[6]:


class InputSubject(Subject):
    
    def __init__(self):
        super().__init__()
        self.__value = 0
    
    def enter_value(self):
        value = input("Enter new value >")
        if value != self.__value:
            self.__value = value
            self.notify()


# In[7]:


import numpy as np


# In[8]:


a = np.array([1, 5, 6, 8])


# In[14]:


# Адаптер
class ListAdaper(list):
    def __init__(self, nparray):
        self.__nparray = nparray
        
    def __len__(self):
        return len(self.__nparray)
    
    def index(self, el):
        for i, ela in enumerate(self.__nparray):
            if ela == el:
                return i
        return -1       
        #return list(self.__nparray).index(el)


# In[15]:


la = ListAdaper(a)


# In[18]:


la.index(5)


# In[19]:


for i in {5, 2, 'fd'}:
    print(i)


# In[ ]:




