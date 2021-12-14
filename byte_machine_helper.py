"""
ByteMachine.

Вспомогательные функции.
"""
__author__ = "EnergyLabs"
__version__ = "0.9137"
__email__ = "energy.labs@yandex.ru"


import sys
import unittest


# Функции сравнения для float.

def float_equal(value_1: float, value_2: float) -> bool:
    """Функция проверки на равенство для float."""
    eps = sys.float_info.epsilon
    return abs(value_1 - value_2) < eps


def float_not_equal(value_1: float, value_2: float) -> bool:
    """Функция проверки на неравенство для float."""
    return not float_equal(value_1, value_2)


def is_float_null(value: float) -> bool:
    """Функция проверки float на равенство 0."""
    return float_equal(value, 0.0)


class Test(unittest.TestCase):
    """Класс для тестирования."""

    def test_float_equal(self):
        """Тест функции float_equal."""
        v_1 = 0.0
        v_2 = 1.0
        self.assertTrue(float_equal(v_1, v_1))
        self.assertFalse(float_equal(v_1, v_2))

    def test_not_equal(self):
        """Тест функции float_not_equal."""
        v_1 = 0.0
        v_2 = 1.0
        self.assertTrue(float_not_equal(v_1, v_2))
        self.assertFalse(float_not_equal(v_1, v_1))

    def test_is_float_null(self):
        """Тест функции is_float_null."""
        self.assertTrue(is_float_null(0.0))
        self.assertFalse(is_float_null(1.0))


# Вызывается при загрузке модуля главным.
if __name__ == "__main__":
    unittest.main()
