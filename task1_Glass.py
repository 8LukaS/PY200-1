#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Лука С.С. 2 группа
# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
class Glass:
    """Class Glass"""
    def __init__(self, capacity_volume, occupied_volume):
        """This bloc initialize variable for instance"""
        # проверяем типы и значения объема стакана чтоб были положительными и не строки
        if isinstance(capacity_volume, (int, float)):  # если экземпляр(Обьем стакана())
            if capacity_volume > 0:  # Обьем стакана > 0
                self.capacity_volume = capacity_volume  # (атрибут)тогда maximum glass volume
            else:
                raise ValueError
                # ошибка ValueError – возникает, когда встроенная операция
                # или функция получают аргумент, тип которого правильный, но
                # неправильно значение, и ситуация не может описано более
                # точно, как при возникновении IndexError
        else:  # TypeError – возникает, когда операция или функция применяется к
            raise TypeError  # объекту несоответствующего типа. Связанное значение представляет
            # собой строку, в которой приводятся подробные сведения о
            # несоответствии типов;
        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0:
                self.occupied_volume = occupied_volume  # current glass volume
            else:
                raise ValueError
        else:
            raise TypeError

    def get_self_id(self):
        return hex(id(self))
# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.
print(' ----------------Задание №1,2-------------------')
glass1 = Glass(500, 100)  # Первый стакан
print(f'1.1 Обьем первого стакана: {glass1.capacity_volume} (милилитров)')
print(f'1.2 Заполняемость первого стакана: {glass1.occupied_volume} (милилитров)')
glass2 = Glass(400, 600)  # Второй  стакан
print(f"2.1 Обьем второго стакана: {glass2.capacity_volume} (милилитров)")
print(f'2.2 Заполняемость второго стакана: {glass2.occupied_volume} (милилитров)')


# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
class GlassDefaultArg():
    '''Class GlassDefaultArg'''

    def __init__(self, capacity_volume: int, occupied_volume: int) -> int:
        """This metod initialize variable for instance
        :type capacity_volume: int
        """
        self.occupied_volume: 'an argument that defaults to 0' = 0
        if not isinstance(capacity_volume, (
                int,
                float)):  # почитать как работает Isinstanse и тогда можно будет понять как работает (передача аргументов )
            raise TypeError('Occuped volume must be int or float')
        if capacity_volume and occupied_volume < 0:
            raise ValueError('Occuped volume must be more then zero')
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


print(' ----------------Задание №3-------------------')
glass1_3_1 = GlassDefaultArg(200, 1)
glass1_3_2 = GlassDefaultArg(200, 200)
print(f'3.1 Пустой стакан |{glass1_3_1.occupied_volume}| (милилитров)')
print(f'3.2 Заполненый стакан на |{glass1_3_2.occupied_volume}| (милилитров)')


# 4. Создайте класс GlassDefaultListArg (нужен только __init__)
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?


class GlassDefaultListArg():
    '''GlassDefaultListArg'''

    def __init__(self, capacity_volume: int, occupied_volume: int):
        """This bloc initialize variable for instance"""
        occupied_volume = []  # пустой список
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(2)


print(' ----------------Задание № 4-------------------')
glass1_4_1 = GlassDefaultListArg(2, 0)
print(glass1_4_1.occupied_volume)
glass1_4_2 = GlassDefaultListArg(0, 0)
print(glass1_4_2.occupied_volume)
glass1_4_3 = GlassDefaultListArg(0, 0)
print(glass1_4_3.occupied_volume)


# # 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
# #    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
# #    Вызовите методы add_water и remove.
# #    Убедитесь, что методы правильно изменяют атрибут occupied_volume.
class GlassAddRemove():
    '''Class GlassAddRemove'''

    def __init__(self, capacity_volume: int, occupied_volume: int) -> int:
        """This bloc initialize variable for instance"""
        # проверяем типы и значения переменных
        if not isinstance(capacity_volume and occupied_volume, (int, float)):
            raise TypeError
        elif capacity_volume and occupied_volume < 0:
            raise ValueError
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def add_water(self, adding_water):
        space = self.capacity_volume - self.occupied_volume  # пустое место в стакане
        if adding_water <= space:
            self.occupied_volume += adding_water

        else:
            # space < self.adding_water
            return adding_water - space


#
#     def remove_water(self,removing_water:int)->int: #удаляем воду
#         if occupied_volume > capacity_volume:
#             return Exception
#         else:
# print(' ----------------Задание №5-------------------')
glass_5_1 = GlassAddRemove(300, 150)
print(glass_5_1.add_water(100))
#
# # 6. Создайте три объекта типа GlassAddRemove,
# #    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
# #    а. Получите типы объектов и класса
# #    б. Проверьте тип созданного объекта.
print(' ----------------Задание №6-------------------')
print(dir(GlassAddRemove))
print(GlassAddRemove.__dict__)  # список пользовательских aтрибутов
print(type(GlassAddRemove))
if isinstance(glass_5_1, GlassAddRemove):
    print('obj')

# # ---------------------------------------------------------------------------------------------
# # Внутренние объекты класса (стр. 25-33)
print(' ----------------Задание №7-------------------')


# # 7. Получите список атрибутов экземпляра класса в начале метода __init__,
# #    в середине __init__ и в конце __init__, (стр. 28-30)
# #    а также после создания объекта.
# #    Опишите результат.
class GlassDefaultListArgNew():
    '''GlassDefaultListArg'''

    def __init__(self, capacity_volume, occupied_volume):
        """This bloc initialize variable for instance"""
        print('Начало 1', dir(self))
        print('Начало 2', self.__dict__)
        self.capacity_volume = capacity_volume
        print('Cередина 1', dir(self))
        print('Cередина 2', self.__dict__)
        self.occupied_volume = occupied_volume
        print('Конец 1', dir(self))
        print('Конец 2', self.__dict__)


glass_7_1 = GlassDefaultListArgNew(200, 0)

# # 8. Создайте три объекта Glass. (стр. 27)
# #    Получите id для каждого объекта с соответсвующим id переменной self.
print(' ----------------Задание №8-------------------')


class GlassId():
    '''Class Glass'''

    def __init__(self, capacity_volume, occupied_volume):
        """This bloc initialize variable for instance"""
        self.capacity_volume = capacity_volume
        self.occupied_volume = capacity_volume


glass_8_1 = GlassId(200, 100)
print(hex(id(glass_8_1)))
glass_8_2 = GlassId(200, 100)
print(hex(id(glass_8_2)))
print(' ----------------Задание №9-------------------')


# # 9. Корректно ли следующее объявление класса с точки зрения:
# #     - интерпретатора Python;
# #     - соглашения о стиле кодирования
# #    Запустите код.
# class D:
#     def __init__(f, a=2): #нужно использовать self
#         f.a = a
#     def print_me(f):
#         print(f.a)
# class_d = D()
# print(' ----------------Задание №10-------------------')
# # # 10. Исправьте
# class A:
#     def __init__(self, a):
#         if 10 < a < 50:
#             self.a = a
# # # Объясните так реализовывать __init__ нельзя?
#
# print(' ----------------Задание №10-------------------')
# # # 11. Циклическая зависимость (стр. 39-44
class Node:
    def __init__(self, prev=None, next_=None):
        self.__prev = prev  # Class Node __скрытый параметр
        self.__next = next_  # Class Node

    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev

    def get_next(self):
        return Node

    def get_prev(self):
        return Node

    def get_value(self):
        pass

    def __str__(self):
        ...

    def __repr__(self):
        ...


class LinkedList:  # связанный список
    def __init__(self, node=None):
        if nodes is None:
            self.head = Node
            self.tail = Node
            self.__len = 0
        elif isinstance(nodes, list):
            self.head = nodes[0]
            self.tail = nodes[-1]
            self.linked_nodes(nodes)  # связываем пользовательский набор узлов

    def linked_nodes(self, nodes):  # нужно еще проверить если 1 значение
        # Установить ссылки для первого
        nodes[0].set_prev(nodes[-1])
        nodes[0].set_next(nodes[-1])
        # Установить ссылки для середины
        for i in range(1, len(nodes) - 1):
            nodes[i].set_prev((nodes[i - 1])
            nodes[i].set_next((nodes[i + 1])
            # Установить ссылки для конец
            nodes[-1].set_prev((nodes[i - 1])  # TODO Check when lenght of list
            nodes[-1].setr_next((nodes[i + 1])


def insert(self, node, index=0):
    '''
    Insert Node to any place of LinkedList -----вставить узел
    node - Node
    index - position of node
    '''

    # current_node = self.head
    # for i in range(index):
    #     current_node = current_node.get_next()
    # current_node.set_prev(node)

    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        self.tail.set_next(node)
        node.set_prev(self.tail)
        self.tail.set_next(self.head)
        self.head.set_prev(self.tail)

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def find(self, node):  # возврошаем индекс

    def remove(self, node):  # удаление по значению
        ...

    def delete(self, index):  # удаление по индексу
