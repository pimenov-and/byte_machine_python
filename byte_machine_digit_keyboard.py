"""
ByteMachine.

Состояние цифровой клавиатуры.
"""
from __future__ import annotations
import unittest


class DigitKeyboard:
    """Состояние цифровой клавиатуры."""

    def __init__(self):
        """Конструктор без параметров."""
        self.keys = bytearray([0] * 10)

    def init(self, keys: bytearray()) -> None:
        """Функция инициализации."""
        assert DigitKeyboard.check_keys(keys)
        self.keys = keys

    @staticmethod
    def create(keys: bytearray) -> DigitKeyboard:
        """Функция создания."""
        assert DigitKeyboard.check_keys(keys)
        dk = DigitKeyboard()
        dk.init(keys)
        return dk

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        return DigitKeyboard.check_keys(byte_array)

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        return self.keys

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        self.keys = byte_array

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 10

    def __eq__(self, other: DigitKeyboard) -> bool:
        """Оператор ==."""
        return self.keys == other.keys

    def __ne__(self, other: DigitKeyboard) -> bool:
        """Оператор !=."""
        return not self.keys == other.keys

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.keys}"

    @staticmethod
    def check_keys(keys: bytearray) -> bool:
        """Проверка кодов клавиш."""
        if not isinstance(keys, bytearray):
            return False
        if not all(b in (0, 1) for b in keys):
            return False
        if len(keys) != 10:
            return False
        return True


class TestDigitKeyboard(unittest.TestCase):
    """Класс для тестирования."""

    def test_constructor(self):
        """Тест конструктора."""
        dk = DigitKeyboard()
        self.assertEqual(len(dk.keys), 10)
        self.assertEqual(dk.keys, bytearray([0] * 10))

    def test_init(self):
        """Тест функции init."""
        ba = bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        dk = DigitKeyboard()
        dk.init(ba)
        self.assertEqual(dk.keys, ba)

    def test_create(self):
        """Тест функции create."""
        ba = bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        dk = DigitKeyboard.create(ba)
        self.assertEqual(dk.keys, ba)

    def test_get_byte_list_len(self):
        """Тест функции get_byte_list_len."""
        dk = DigitKeyboard()
        self.assertEqual(dk.get_byte_array_len(), 10)

    def test_to_byte_list(self):
        """Тест функции to_byte_list."""
        dk = DigitKeyboard()
        ba = dk.to_byte_array()
        self.assertEqual(len(ba), 10)
        self.assertEqual(ba, bytearray([0] * 10))

    def test_from_byte_list(self):
        """Тест функции from_byte_list."""
        dk = DigitKeyboard()
        ba = bytearray([0] * 10)
        dk.from_byte_array(ba)
        self.assertEqual(dk.keys, ba)

    def test_equal(self):
        """Тест оператора ==."""
        dk1 = DigitKeyboard()
        self.assertTrue(dk1 == dk1)

    def test_not_equal(self):
        """Тест оператора !=."""
        dk1 = DigitKeyboard()
        ba = bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        dk2 = DigitKeyboard.create(ba)
        self.assertTrue(dk1 != dk2)


# Вызывается при загрузке модуля главным.
if __name__ == "__main__":
    unittest.main()
