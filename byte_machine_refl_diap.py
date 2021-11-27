"""
ByteMachine.

Отображение диапазонов.
"""
from __future__ import annotations


__author__ = "EnergyLabs"
__version__ = "0.9129"


import unittest
import byte_machine_convert as bmc
import byte_machine_helper as bmh


class Coefs:
    """Пара коэффициентов."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.a = 0.0
        self.b = 0.0

    def init(self, a: float, b: float) -> None:
        """Функция инициализации."""
        self.a = a
        self.b = b

    @staticmethod
    def create(a: float, b: float) -> Coefs:
        """Функция создания."""
        c = Coefs()
        c.init(a, b)
        return c

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Конвертация в массив байтов."""
        ba = bytearray()
        ba += bmc.double_to_byte_array(self.a)
        ba += bmc.double_to_byte_array(self.b)
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        ba_a = byte_array[:8]
        self.a = bmc.byte_array_to_double(ba_a)
        ba_b = byte_array[8:16]
        self.b = bmc.byte_array_to_double(ba_b)

    def get_byte_array_len(self) -> int:
        """Получение размера байтового массива."""
        return 8

    def __eq__(self, other: Coefs) -> bool:
        """Оператор ==."""
        assert isinstance(other, Coefs)
        is_eq_a = bmh.float_equal(self.a, other.a)
        is_eq_b = bmh.float_equal(self.b, other.b)
        return is_eq_a and is_eq_b

    def __ne__(self, other: Coefs) -> bool:
        """Оператор !=."""
        assert isinstance(other, Coefs)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"a: {self.a}, b: {self.b}"


class ReflDiap:
    """Отображение диапазонов."""

    def __init__(self):
        """Конструктор без параметров."""
        self.coefs = Coefs()

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """."""
        pass

    def to_byte_array():
        """."""
        pass

    def from_byte_array():
        """."""
        pass

    def get_byte_array_len(self) -> int:
        """."""
        pass

    def __eq__(self, other: ReflDiap) -> bool:
        """Оператор ==."""
        assert isinstance(other, ReflDiap)
        return True

    def __ne__(self, other: ReflDiap) -> bool:
        """Оператор !=."""
        assert isinstance(other, ReflDiap)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f""


class TestCoefs(unittest.TestCase):
    """Тест класса Coefs."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        c = Coefs()

    def test_init(self):
        """Тест функции init."""
        pass

    def test_create(self):
        """Тест функции create."""
        pass

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        pass

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        pass

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        pass

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        pass

    def test_equal(self):
        """Тест оператора ==."""
        c = Coefs()
        self.assertTrue(c == c)

    def test_not_equal(self):
        """Тест оператора !=."""
        c = Coefs()
        self.assertFalse(c != c)


class TestReflDiap(unittest.TestCase):
    """Тест класса ReflDiap."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        pass

    def test_init(self):
        """Тест функции init."""
        pass

    def test_create(self):
        """Тест функции create."""
        pass

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        pass

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        pass

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        pass

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        pass

    def test_equal(self):
        """Тест оператора ==."""
        pass

    def test_not_equal(self):
        """Тест оператора !=."""
        pass


# Вызывается при загрузке модуля главным.
if __name__ == "__main__":
    unittest.main()
