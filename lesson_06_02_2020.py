#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re


class Date:
    '''
    input data format ->'1970-01-01'
    '''             # 0  1   2   3   4   5   6   7   8   9   10  11
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # невисокосный год
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  # високосный год
    # not_leap_year = DAY_OF_MONTH[0]  # невисокосный год
    # leap_year = DAY_OF_MONTH[1]  # високосный год
    #
    # data_input = re.compile("\d\d\d\d-\d\d-\d\d") #format ->'1970-01-01'
    # # print(type(data_input))
    # def __init__(self, *args):
    # 2 вариант передаем int
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day #при присвоений свойство  переопределяется day становится day

    @staticmethod
    def is_leap_year(year):
        if year % 4 == 0 and year % 100 != 0 or year == 0:  # .....год является високос-ным, если он делится на 4,
            return f'{year} -This leap years '  # но не делится на 100, исключая то,что делящиеся на 400 годы тоже являются високосными
        else:
            return f'{year}-This years not leap'

    @classmethod
    def get_max_day(cls, year, month):
        leap_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month-1]

    @property
    def date(self):  #должны проверять является строка или int
        return f'{self.day}.{self.month}.{self.year}'
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError('Date must be str')
        value = value.split('.')
        if len(value) != 3:
            raise ValueError('Invalid date format')

        try:
            day = int(value[0])
            month = int(value[1])
            year = int(value[2])
            self.is_valid_date(year, month, day)
        except ValueError:
            raise ValueError('Invalid date format')
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f' {self.date}'

    def __repr__(self):
        return f'Date: {self.date}'

    @classmethod
    def is_valid_date(cls, year, month, day):
        if not isinstance(year, int):
            raise TypeError('year must be int')
        if not isinstance(month, int):
            raise TypeError('month must be int')
        if not isinstance(day, int):
            raise TypeError('day must be int')

        if not 0 < month <= 12:
            raise ValueError('month must be 0 < month <= 12')

        if not 0 < day <= cls.get_max_day(year, month):
            raise ValueError('invalid day for this month and year')

    @property
    def day(self):
        return self._day
    @property
    def month(self):
        return self._month
    @property
    def year(self):
        return self._year

    def add_day(self, day):
        return self.day += _day

    def add_month(self, month):
        return self.month += _month

    def add_year(self, year):
        return self.year += _year

    @staticmethod
    def date2_date1(date2, date1):
        return date2 - date1

    # перезагрузка метода
    # def date_to_int(data):
    @year.setter
    def year(self, value):
        self._year = value

    @month.setter
    def month(self, value):
        self._month = value

    @day.setter
    def day(self, value):
        self._day = value
    @day.setter
    def day(self, value):
        self._day = value


if __name__ == "__main__":
    # Примеры:
    date = Date(2018, 11, 23)
    # print(date)  # 23.11.2018
    # repr(date)  # Date(2018, 11, 23)
    # print(Date.get_max_day(2021, 10))

    date.date = '31.11.2018'
    print(date.date) # '31.11.2018'
    # date.day   = 31 # Запрет
    # print(date.day)
    # date.month = 50 #
    # date.month = 11 # 02 -> 01.03
    # date.year       # на след. месяц
