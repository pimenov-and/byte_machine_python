"""
ByteMachine.

Отображение диапазонов.
"""
from __future__ import annotations


__author__ = "EnergyLabs"
__version__ = "0.9137"
__email__ = "energy.labs@yandex.ru"


import unittest
import byte_machine_graphics as bmg
import byte_machine_helper as bmh


class Coefs:
    """Пара коэффициентов."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.a = 0.0
        self.b = 0.0

    def init(self, a: float, b: float) -> None:
        """Функция инициализации."""
        assert isinstance(a, float)
        assert isinstance(b, float)
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
        if len(byte_array) < self.get_byte_array_len():
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Конвертация в массив байтов."""
        ba = bytearray()
        ba += bmg.bmc.double_to_byte_array(self.a)
        ba += bmg.bmc.double_to_byte_array(self.b)
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        ba_a = byte_array[:8]
        self.a = bmg.bmc.byte_array_to_double(ba_a)
        ba_b = byte_array[8:16]
        self.b = bmg.bmc.byte_array_to_double(ba_b)

    def get_byte_array_len(self) -> int:
        """Получение размера байтового массива."""
        return 16

    @staticmethod
    def s_get_byte_array_len() -> int:
        """Получение размера байтового массива."""
        return 16

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

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.diap_1 = bmg.DiapF()
        self.diap_2 = bmg.DiapF()
        self.coefs = Coefs()
        self.calc_coefs()

    def init(self, diap_1: bmg.DiapF, diap_2: bmg.DiapF) -> None:
        """Функция инициализации."""
        assert isinstance(diap_1, bmg.DiapF)
        assert isinstance(diap_2, bmg.DiapF)
        self.diap_1 = diap_1
        self.diap_2 = diap_2
        self.calc_coefs()

    @staticmethod
    def create(diap_1: bmg.DiapF, diap_2: bmg.DiapF) -> ReflDiap:
        """Функция создания."""
        rd = ReflDiap()
        rd.init(diap_1, diap_2)
        return rd

    def diap_1_to_diap_2(self, value: float) -> float:
        """Преобразования значения из диапазона 1 в диапазон 2."""
        assert isinstance(value, float)
        return (value - self.coefs.b) / self.coefs.a

    def diap_2_to_diap_1(self, value: float) -> float:
        """Преобразование значения из диапазона 2 в диапазон 1."""
        assert isinstance(value, float)
        return self.coefs.a * value + self.coefs.b

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 32:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Конвертация в массив байтов."""
        ba = bytearray()
        ba += self.diap_1.to_byte_array()
        ba += self.diap_2.to_byte_array()
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        self.diap_1.from_byte_array(byte_array)
        ba_diap_2 = byte_array[16:]
        self.diap_2.from_byte_array(ba_diap_2)

    def get_byte_array_len(self) -> int:
        """Получение размера байтового массива."""
        return 32

    @staticmethod
    def s_get_byte_array_len() -> int:
        """Получение размера байтового массива."""
        return 32

    def __eq__(self, other: ReflDiap) -> bool:
        """Оператор ==."""
        assert isinstance(other, ReflDiap)
        is_eq_diap_1 = self.diap_1 == other.diap_1
        is_eq_diap_2 = self.diap_2 == other.diap_2
        return is_eq_diap_1 and is_eq_diap_2

    def __ne__(self, other: ReflDiap) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        d_1 = self.diap_1
        d_2 = self.diap_2
        c = self.coefs
        return f"diap_1: ({d_1}), diap_2: ({d_2}), coefs: ({c})"

    def calc_coefs(self):
        """Расчёт коэффициентов."""
        d_1 = self.diap_1
        d_2 = self.diap_2
        c = self.coefs
        c.a = (d_1.begin - d_1.end) / (d_2.begin - d_2.end)
        c.b = d_1.begin - c.a * d_2.begin


class TestCoefs(unittest.TestCase):
    """Тест класса Coefs."""

    def test_constructor(self):
        """Тест конструктора."""
        c = Coefs()
        self.assertAlmostEqual(c.a, 0.0)
        self.assertAlmostEqual(c.b, 0.0)

    def test_init(self):
        """Тест функции init."""
        c = Coefs()
        c.init(-1.0, 1.0)
        self.assertAlmostEqual(c.a, -1.0)
        self.assertAlmostEqual(c.b, 1.0)

    def test_create(self):
        """Тест функции create."""
        c = Coefs.create(-2.0, 2.0)
        self.assertAlmostEqual(c.a, -2.0)
        self.assertAlmostEqual(c.b, 2.0)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        c = Coefs()
        ba = c.to_byte_array()
        self.assertTrue(c.check_byte_array(ba))

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        c = Coefs()
        ba = c.to_byte_array()
        self.assertTrue(c.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        a = -1.0
        b = 1.0
        c = Coefs.create(a, b)
        ba = c.to_byte_array()
        c.from_byte_array(ba)
        self.assertEqual(c.a, a)
        self.assertEqual(c.b, b)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        c = Coefs()
        ba = c.to_byte_array()
        self.assertEqual(len(ba), c.get_byte_array_len())

    def test_s_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        c = Coefs()
        self.assertEqual(Coefs.s_get_byte_array_len(), c.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        c_1 = Coefs()
        self.assertTrue(c_1 == c_1)

        c_2 = Coefs.create(-100.0, 200.0)
        self.assertFalse(c_1 == c_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        c_1 = Coefs()
        self.assertFalse(c_1 != c_1)

        c_2 = Coefs.create(-100.0, 200.0)
        self.assertTrue(c_1 != c_2)


class TestReflDiap(unittest.TestCase):
    """Тест класса ReflDiap."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        rd = ReflDiap()
        self.assertEqual(rd.diap_1, bmg.DiapF())
        self.assertEqual(rd.diap_2, bmg.DiapF())

    def test_init(self):
        """Тест функции init."""
        d_1 = bmg.DiapF.create(-100.0, 100.0)
        d_2 = bmg.DiapF.create(-200.0, 200.0)
        rd = ReflDiap()
        rd.init(d_1, d_2)
        self.assertEqual(rd.diap_1, d_1)
        self.assertEqual(rd.diap_2, d_2)

    def test_create(self):
        """Тест функции create."""
        d_1 = bmg.DiapF.create(-100.0, 100.0)
        d_2 = bmg.DiapF.create(-200.0, 200.0)
        rd = ReflDiap.create(d_1, d_2)
        self.assertEqual(rd.diap_1, d_1)
        self.assertEqual(rd.diap_2, d_2)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        rd = ReflDiap()
        ba = rd.to_byte_array()
        self.assertTrue(rd.check_byte_array(ba))

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        rd = ReflDiap()
        ba = rd.to_byte_array()
        self.assertTrue(rd.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        d_1 = bmg.DiapF.create(-100.0, 100.0)
        d_2 = bmg.DiapF.create(-200.0, 200.0)
        rd = ReflDiap.create(d_1, d_2)
        ba = rd.to_byte_array()
        rd.from_byte_array(ba)
        self.assertEqual(rd.diap_1, d_1)
        self.assertEqual(rd.diap_2, d_2)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        rd = ReflDiap()
        ba = rd.to_byte_array()
        self.assertEqual(len(ba), rd.get_byte_array_len())

    def test_s_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        rd = ReflDiap()
        self.assertEqual(ReflDiap.s_get_byte_array_len(),
                         rd.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        rd_1 = ReflDiap()
        self.assertTrue(rd_1 == rd_1)

        rd_2 = ReflDiap()
        rd_2.diap_1 = bmg.DiapF.create(-100.0, 200.0)
        self.assertFalse(rd_1 == rd_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        rd_1 = ReflDiap()
        self.assertFalse(rd_1 != rd_1)

        rd_2 = ReflDiap()
        rd_2.diap_1 = bmg.DiapF.create(-100.0, 200.0)
        self.assertTrue(rd_1 != rd_2)


# Вызывается при загрузке модуля главным.
if __name__ == "__main__":
    unittest.main()
