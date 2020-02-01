#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from task1_Glass import Glass

class MyTestCase(unittest.TestCase):
    def test_init(self): #все тесты начинаются с test
        self.assertRaises(TypeError,Glass,'st',10)
        self.assertRaises(TypeError, Glass, 10, 'st')

if __name__ == '__main__':
    unittest.main()