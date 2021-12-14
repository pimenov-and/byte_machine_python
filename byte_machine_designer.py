"""
ByteMachine.

Состояние дизайнера.
"""
from __future__ import annotations


__author__ = "EnergyLabs"
__version__ = "0.9137"
__email__ = "energy.labs@yandex.ru"


import unittest
import byte_machine_graphics as bmg


class Designer:
    """Состояние дизайнера."""

    def __init__(self):
        """Конструктор без параметров."""
        self.size = bmg.Size()
        self.viewport_size = bmg.Size()
        self.horz_scroll_pos = 0
        self.vert_scroll_pos = 0

    def init(self, size: bmg.Size, viewport_size: bmg.Size,
             horz_scroll_pos: int, vert_scroll_pos: int) -> None:
        """Функция инициализации."""
        assert isinstance(size, bmg.Size)
        assert isinstance(viewport_size, bmg.Size)
        assert isinstance(horz_scroll_pos, int)
        assert isinstance(vert_scroll_pos, int)
        self.size = size
        self.viewport_size = viewport_size
        self.horz_scroll_pos = horz_scroll_pos
        self.vert_scroll_pos = vert_scroll_pos

    @staticmethod
    def create(size: bmg.Size, viewport_size: bmg.Size,
               horz_scroll_pos: int, vert_scroll_pos: int) -> Designer:
        """Функция создания."""
        assert isinstance(size, bmg.Size)
        assert isinstance(viewport_size, bmg.Size)
        assert isinstance(horz_scroll_pos, int)
        assert isinstance(vert_scroll_pos, int)
        d = Designer()
        d.init(size, viewport_size, horz_scroll_pos, vert_scroll_pos)
        return d

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        return True

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        ba_size = byte_array[:16]
        self.size.from_byte_array(ba_size)
        ba_viewport_size = byte_array[16:32]
        self.viewport_size.from_byte_array(ba_viewport_size)

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += self.size.to_byte_array()
        ba += self.viewport_size.to_byte_array()
        ba += bmg.bmc.int32_to_byte_array(self.horz_scroll_pos)
        ba += bmg.bmc.int32_to_byte_array(self.vert_scroll_pos)
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def get_byte_array_len(self) -> int:
        """Получение длины массива байтов."""
        return 25

    @staticmethod
    def s_get_byte_array_len() -> int:
        """Получение размера байтового массива."""
        return 25

    def __eq__(self, other: Designer) -> bool:
        """Оператор ==."""
        is_eq_size = (self.size == other.size)
        is_eq_viewport_size = (self.viewport_size == other.viewport_size)
        is_eq_horz_scroll_pos = (self.horz_scroll_pos == other.horz_scroll_pos)
        is_eq_vert_scroll_pos = (self.vert_scroll_pos == other.vert_scroll_pos)
        return is_eq_size and is_eq_viewport_size and is_eq_horz_scroll_pos \
            and is_eq_vert_scroll_pos

    def __ne__(self, other: Designer) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        size = self.size
        viewport_size = self.viewport_size
        horz_scroll_pos = self.horz_scroll_pos
        vert_scroll_pos = self.vert_scroll_pos
        return f"size: ({size}), "\
            f"viewport_size: ({viewport_size}), "\
            f"horz_scroll_pos: {horz_scroll_pos}, "\
            f"vert_scroll_pos: {vert_scroll_pos}"


class TestDesigner(unittest.TestCase):
    """Тестирование класса Designer."""

    def test_constructor(self):
        """Тестирование конструктора."""
        d = Designer()
        self.assertEqual(d.size, bmg.Size())
        self.assertEqual(d.viewport_size, bmg.Size())
        self.assertEqual(d.horz_scroll_pos, 0)
        self.assertEqual(d.vert_scroll_pos, 0)

    def test_init(self):
        """Тест функции init."""
        s = bmg.Size.create(1200, 800)
        vps = bmg.Size.create(1200, 800)
        hsp = 100
        vsp = 100
        d = Designer()
        d.init(s, vps, hsp, vsp)
        self.assertEqual(d.size, s)
        self.assertEqual(d.viewport_size, vps)
        self.assertEqual(d.horz_scroll_pos, hsp)
        self.assertEqual(d.vert_scroll_pos, vsp)

    def test_create(self):
        """Тест функции create."""
        s = bmg.Size.create(1200, 800)
        vps = bmg.Size.create(1200, 800)
        hsp = 100
        vsp = 100
        d = Designer.create(s, vps, hsp, vsp)
        self.assertEqual(d.size, s)
        self.assertEqual(d.viewport_size, vps)
        self.assertEqual(d.horz_scroll_pos, hsp)
        self.assertEqual(d.vert_scroll_pos, vsp)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        d = Designer()
        d.horz_scroll_pos = 1
        ba = d.to_byte_array()
        self.assertTrue(d.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        d = Designer()
        d.horz_scroll_pos = 1
        d.vert_scroll_pos = 2
        ba = d.to_byte_array()
        d.from_byte_array(ba)
        self.assertEqual(d.horz_scroll_pos, 1)
        self.assertEqual(d.vert_scroll_pos, 2)

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        d = Designer()
        ba = d.to_byte_array()
        self.assertTrue(d.check_byte_array(ba))

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        d = Designer()
        ba = d.to_byte_array()
        self.assertEqual(len(ba), d.get_byte_array_len())

    def test_s_get_byte_array_len(self):
        """Тест функции s_get_byte_array_len."""
        lenght = Designer.s_get_byte_array_len()
        d = Designer()
        self.assertEqual(lenght, d.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        d_1 = Designer()
        self.assertTrue(d_1 == d_1)
        d_2 = Designer()
        d_2.horz_scroll_pos = 1
        self.assertFalse(d_1 == d_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        d_1 = Designer()
        self.assertFalse(d_1 != d_1)
        d_2 = Designer()
        d_2.horz_scroll_pos = 1
        self.assertTrue(d_1 != d_2)


# Вызывается при загрузке модуля главным.
if __name__ == "__main__":
    unittest.main()
