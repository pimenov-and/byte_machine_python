# coding: utf8
'''
ByteMachine
Вспомогательные функции.
'''
import sys
import unittest


# Функции сравнения для float
def float_equal(value1: float, value2: float) -> bool:
    '''Функция проверки на равенство для float.'''
    eps = sys.float_info.epsilon
    return abs(value1 - value2) < eps


def float_not_equal(value1: float, value2: float) -> bool:
    '''Функция проверки на неравенство для float.'''
    return not float_equal(value1, value2)


def is_float_null(value: float) -> bool:
    '''Функция проверки float на равенство 0.'''
    return float_equal(value, 0.0)


class Test(unittest.TestCase):
    '''
    Класс для тестирования.
    '''

    def test_float_equal(self):
        v1 = 0.0
        v2 = 1.0
        self.assertTrue(float_equal(v1, v1))
        self.assertFalse(float_equal(v1, v2))

    def test_not_equal(self):
        v1 = 0.0
        v2 = 1.0
        self.assertTrue(float_not_equal(v1, v2))
        self.assertFalse(float_not_equal(v1, v1))

    def test_is_float_null(self):
        self.assertTrue(is_float_null(0.0))
        self.assertFalse(is_float_null(1.0))


# Вызывается при загрузке модуля главным
if __name__ == '__main__':
    unittest.main()
