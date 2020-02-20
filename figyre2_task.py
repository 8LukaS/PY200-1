import os

import sys
# Подключаем модули QApplication и QLabel
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtCore import Qt, QPoint

from abc import abstractclassmethod
class Figure:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @abstractmethod
    def perimeter(self):
        ...

    def square(self):
        ...
    @property
    def width(self):
        return 0.0

    def height(self):
        return 0.0


class Rectangle(Figure):
    def __init__(self, x=0, y=0, w=0, h=0):
        self.__x = x
        self.__y = y
        self.w = w
        self.h = h

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def perimeter(self):
        return 2 * (self.w + self.h)

    def square(self):
        return self.w * self.h

    def width(self):
        return self.w

    def height(self):
        return self.h

