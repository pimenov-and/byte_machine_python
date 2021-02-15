# coding: utf8
"""
ByteMachine
Состояние мыши.
"""
from __future__ import annotations
import unittest
import byte_machine_graphics_3 as bmg


class Mouse(object):
    """Состояние мыши."""

    def __init__(self):
        """Конструктор без параметров."""
        self.pos = bmg.Point()
        self.isLeftBtnDown = False
        self.isMiddleBtnDown = False
        self.isRightBtnDown = False

    def init(self, pos: bmg.Point, isLeftBtnDown: bool, isMiddleBtnDown: bool,
             isRightBtnDown: bool) -> None:
        """Функция инициализации."""
        assert isinstance(pos, bmg.Point)
        assert isinstance(isLeftBtnDown, bool)
        assert isinstance(isMiddleBtnDown, bool)
        assert isinstance(isRightBtnDown, bool)
        self.pos = pos
        self.isLeftBtnDown = isLeftBtnDown
        self.isMiddleBtnDown = isMiddleBtnDown
        self.isRightBtnDown = isRightBtnDown

    @staticmethod
    def create(pos: bmg.Point, isLeftBtnDown: bool, isMiddleBtnDown: bool,
               isRightBtnDown: bool) -> Mouse:
        """Функция создания."""
        assert isinstance(pos, bmg.Point)
        assert isinstance(isLeftBtnDown, bool)
        assert isinstance(isMiddleBtnDown, bool)
        assert isinstance(isRightBtnDown, bool)
        m = Mouse()
        m.init(pos, isLeftBtnDown, isMiddleBtnDown, isRightBtnDown)
        return m

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        # assert isinstance(byte_array, bytearray)
        return len(byte_array) == self.get_byte_array_len()

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        bap = byte_array[:8]
        self.pos.from_byte_array(bap)
        self.isLeftBtnDown = bmg.bmc.byte_array_to_bool([byte_array[8]])
        self.isMiddleBtnDown = bmg.bmc.byte_array_to_bool([byte_array[9]])
        self.isRightBtnDown = bmg.bmc.byte_array_to_bool([byte_array[10]])

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += self.pos.to_byte_array()
        ba += bmg.bmc.bool_to_byte_array(self.isLeftBtnDown)
        ba += bmg.bmc.bool_to_byte_array(self.isMiddleBtnDown)
        ba += bmg.bmc.bool_to_byte_array(self.isRightBtnDown)
        return ba

    def get_byte_array_len(self) -> int:
        """Получение длины массива байтов."""
        return 11

    def __eq__(self, other: Mouse) -> bool:
        """Оператор ==."""
        isPosEq = (self.pos == other.pos)
        isLeftBtnDownEq = (self.isLeftBtnDown == other.isLeftBtnDown)
        isMiddleBtnDownEq = (self.isMiddleBtnDown == other.isMiddleBtnDown)
        isRightBtnDownEq = (self.isRightBtnDown == other.isRightBtnDown)
        return isPosEq and isLeftBtnDownEq and isMiddleBtnDownEq \
            and isRightBtnDownEq

    def __ne__(self, other: Mouse) -> bool:
        """Оператор !=."""
        return not (self == other)

    def __str__(self) -> str:
        """Получение строкового представления."""
        return '{}, {}, {}, {}'.format(self.pos, self.isLeftBtnDown,
                                       self.isMiddleBtnDown,
                                       self.isRightBtnDown)


class TestMouse(unittest.TestCase):
    """Тестирование класса Mouse."""

    def test_constructor(self):
        """Тест конструктора класса Mouse."""
        m = Mouse()
        self.assertEqual(m.pos, bmg.Point())
        self.assertEqual(m.isLeftBtnDown, False)
        self.assertEqual(m.isMiddleBtnDown, False)
        self.assertEqual(m.isRightBtnDown, False)

    def test_init(self):
        """Тест функции init класса Mouse."""
        m = Mouse()
        m.init(bmg.Point(), True, False, False)
        self.assertEqual(m.pos, bmg.Point())
        self.assertEqual(m.isLeftBtnDown, True)
        self.assertEqual(m.isMiddleBtnDown, False)
        self.assertEqual(m.isRightBtnDown, False)

    def test_create(self):
        """Тест фукнции create класса Mouse."""
        pos = bmg.Point.create(110, 110)
        isLeftBtnDown = False
        isMiddleBtnDown = True
        isRightBtnDown = False
        m = Mouse.create(pos, isLeftBtnDown, isMiddleBtnDown, isRightBtnDown)
        self.assertEqual(m.pos, pos)
        self.assertEqual(m.isLeftBtnDown, isLeftBtnDown)
        self.assertEqual(m.isMiddleBtnDown, isMiddleBtnDown)
        self.assertEqual(m.isRightBtnDown, isRightBtnDown)

    def test_to_byte_array(self):
        """Тест функции to_byte_array класса Mouse."""
        m = Mouse()
        ba = m.to_byte_array()
        self.assertEqual(m.get_byte_array_len(), len(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array класса Mouse."""
        pos = bmg.Point.create(110, 110)
        isLeftBtnDown = False
        isMiddleBtnDown = True
        isRightBtnDown = False
        ba = bytearray()
        ba += pos.to_byte_array()
        ba += bmg.bmc.bool_to_byte_array(isLeftBtnDown)
        ba += bmg.bmc.bool_to_byte_array(isMiddleBtnDown)
        ba += bmg.bmc.bool_to_byte_array(isRightBtnDown)
        m = Mouse()
        m.from_byte_array(ba)
        self.assertEqual(m.pos, pos)
        self.assertEqual(m.isLeftBtnDown, isLeftBtnDown)
        self.assertEqual(m.isMiddleBtnDown, isMiddleBtnDown)
        self.assertEqual(m.isRightBtnDown, isRightBtnDown)

    def test_get_byte_list_len(self):
        """Тест функции get_byte_list_len класса Mouse."""
        m = Mouse()
        self.assertEqual(m.get_byte_array_len(), 11)

    def test_equal(self):
        """Тест функции == класса Mouse."""
        m1 = Mouse()
        self.assertTrue(m1 == m1)
        m2 = Mouse.create(bmg.Point(), False, True, False)
        self.assertFalse(m1 == m2)

    def test_not_equal(self):
        """Тест функции != класса Mouse."""
        pos = bmg.Point.create(100, 100)
        m1 = Mouse.create(pos, False, False, True)
        m2 = Mouse()
        self.assertTrue(m1 != m2)
        self.assertFalse(m1 != m1)


# Вызывается при загрузке модуля главным.
if __name__ == '__main__':
    unittest.main()
