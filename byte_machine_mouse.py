"""
ByteMachine.

Состояние мыши.
"""
from __future__ import annotations
import unittest
import byte_machine_graphics as bmg

class Mouse:
    """Состояние мыши."""

    def __init__(self):
        """Конструктор без параметров."""
        self.pos = bmg.Point()
        self.is_left_btn_down = False
        self.is_middle_btn_down = False
        self.is_right_btn_down = False

    def init(self, pos: bmg.Point, is_left_btn_down: bool, is_middle_btn_down: bool,
             is_right_btn_down: bool) -> None:
        """Функция инициализации."""
        assert isinstance(pos, bmg.Point)
        assert isinstance(is_left_btn_down, bool)
        assert isinstance(is_middle_btn_down, bool)
        assert isinstance(is_right_btn_down, bool)
        self.pos = pos
        self.is_left_btn_down = is_left_btn_down
        self.is_middle_btn_down = is_middle_btn_down
        self.is_right_btn_down = is_right_btn_down

    @staticmethod
    def create(pos: bmg.Point, is_left_btn_down: bool, is_middle_btn_down: bool,
               is_right_btn_down: bool) -> Mouse:
        """Функция создания."""
        assert isinstance(pos, bmg.Point)
        assert isinstance(is_left_btn_down, bool)
        assert isinstance(is_middle_btn_down, bool)
        assert isinstance(is_right_btn_down, bool)
        m = Mouse()
        m.init(pos, is_left_btn_down, is_middle_btn_down, is_right_btn_down)
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
        self.is_left_btn_down = bmg.bmc.byte_array_to_bool([byte_array[8]])
        self.is_middle_btn_down = bmg.bmc.byte_array_to_bool([byte_array[9]])
        self.is_right_btn_down = bmg.bmc.byte_array_to_bool([byte_array[10]])

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += self.pos.to_byte_array()
        ba += bmg.bmc.bool_to_byte_array(self.is_left_btn_down)
        ba += bmg.bmc.bool_to_byte_array(self.is_middle_btn_down)
        ba += bmg.bmc.bool_to_byte_array(self.is_right_btn_down)
        return ba

    def get_byte_array_len(self) -> int:
        """Получение длины массива байтов."""
        return 11

    def __eq__(self, other: Mouse) -> bool:
        """Оператор ==."""
        is_pos_eq = (self.pos == other.pos)
        is_left_btn_down_eq = (self.is_left_btn_down == other.is_left_btn_down)
        is_middle_btn_down_eq = (self.is_middle_btn_down == other.is_middle_btn_down)
        is_right_btn_down_eq = (self.is_right_btn_down == other.is_right_btn_down)
        return is_pos_eq and is_left_btn_down_eq and is_middle_btn_down_eq \
            and is_right_btn_down_eq

    def __ne__(self, other: Mouse) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.pos}, {self.is_left_btn_down}, \
            {self.is_middle_btn_down}, {self.is_right_btn_down}"


class TestMouse(unittest.TestCase):
    """Тестирование класса Mouse."""

    def test_constructor(self):
        """Тест конструктора."""
        m = Mouse()
        self.assertEqual(m.pos, bmg.Point())
        self.assertEqual(m.is_left_btn_down, False)
        self.assertEqual(m.is_middle_btn_down, False)
        self.assertEqual(m.is_right_btn_down, False)

    def test_init(self):
        """Тест функции init."""
        m = Mouse()
        m.init(bmg.Point(), True, False, False)
        self.assertEqual(m.pos, bmg.Point())
        self.assertEqual(m.is_left_btn_down, True)
        self.assertEqual(m.is_middle_btn_down, False)
        self.assertEqual(m.is_right_btn_down, False)

    def test_create(self):
        """Тест фукнции create."""
        pos = bmg.Point.create(110, 110)
        is_left_btn_down = False
        is_middle_btn_down = True
        is_right_btn_down = False
        m = Mouse.create(pos, is_left_btn_down, is_middle_btn_down, is_right_btn_down)
        self.assertEqual(m.pos, pos)
        self.assertEqual(m.is_left_btn_down, is_left_btn_down)
        self.assertEqual(m.is_middle_btn_down, is_middle_btn_down)
        self.assertEqual(m.is_right_btn_down, is_right_btn_down)

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        m = Mouse()
        ba = m.to_byte_array()
        self.assertEqual(m.get_byte_array_len(), len(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        pos = bmg.Point.create(110, 110)
        is_left_btn_down = False
        is_middle_btn_down = True
        is_right_btn_down = False
        ba = bytearray()
        ba += pos.to_byte_array()
        ba += bmg.bmc.bool_to_byte_array(is_left_btn_down)
        ba += bmg.bmc.bool_to_byte_array(is_middle_btn_down)
        ba += bmg.bmc.bool_to_byte_array(is_right_btn_down)
        m = Mouse()
        m.from_byte_array(ba)
        self.assertEqual(m.pos, pos)
        self.assertEqual(m.is_left_btn_down, is_left_btn_down)
        self.assertEqual(m.is_middle_btn_down, is_middle_btn_down)
        self.assertEqual(m.is_right_btn_down, is_right_btn_down)

    def test_get_byte_list_len(self):
        """Тест функции get_byte_list_len."""
        m = Mouse()
        self.assertEqual(m.get_byte_array_len(), 11)

    def test_equal(self):
        """Тест оператора ==."""
        m1 = Mouse()
        self.assertTrue(m1 == m1)
        m2 = Mouse.create(bmg.Point(), False, True, False)
        self.assertFalse(m1 == m2)

    def test_not_equal(self):
        """Тест оператора !=."""
        pos = bmg.Point.create(100, 100)
        m1 = Mouse.create(pos, False, False, True)
        m2 = Mouse()
        self.assertTrue(m1 != m2)
        self.assertFalse(m1 != m1)


# Вызывается при загрузке модуля главным.
if __name__ == "__main__":
    unittest.main()
