"""
ByteMachine.

Контролы.
"""
from __future__ import annotations


__author__ = "EnergyLabs"
__version__ = "0.9122"


import unittest
import byte_machine_paint as bmp


class Button(object):
    """Класс кнопки."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.rect = bmp.bmg.Rect.create_2(0, 0, 75, 25)
        self.text = bmp.bmg.String.create("Button")
        self.color = bmp.bmg.Color.get_white()
        self.border_color = bmp.bmg.Color.get_black()
        self.click_handler = None

    def init(self, rect: bmp.bmg.Rect, text: bmp.bmg.String,
             color: bmp.bmg.Color = bmp.bmg.Color.get_white(),
             border_color: bmp.bmg.Color = bmp.bmg.Color.get_black()) -> None:
        """Функция инициализации."""
        assert isinstance(rect, bmp.bmg.Rect)
        assert isinstance(text, bmp.bmg.String)
        assert isinstance(color, bmp.bmg.Color)
        assert isinstance(border_color, bmp.bmg.Color)
        self.rect = rect
        self.text = text
        self.color = color
        self.border_color = border_color

    def create(rect: bmp.bmg.Rect, text: bmp.bmg.String,
               color: bmp.bmg.Color = bmp.bmg.Color.get_white(),
               borderColor: bmp.bmg.Color = bmp.bmg.Color.get_black()) -> Button:
        """Функция создания."""
        btn = Button()
        btn.init(rect, text, color, borderColor)
        return btn

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        return isinstance(byte_array, bytearray)

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += self.rect.to_byte_array()
        ba += self.text.to_byte_array()
        ba += self.color.to_byte_array()
        ba += self.borderColor.to_byte_array()
        return ba

    def from_byte_array(self, byte_list) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_array_len(self) -> bytearray:
        """Получение длины массива байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: Button) -> bool:
        """Оператор ==."""
        is_eq_rect = self.rect == other.rect
        is_eq_text = self.text == other.text
        is_eq_color = self.color == other.color
        is_eq_border_color = self.border_color == other.border_color
        return is_eq_rect and is_eq_text and is_eq_color and is_eq_border_color

    def __ne__(self, other: Button) -> bool:
        """Оператор !=."""
        return not self == other


class TestButton(unittest.TestCase):
    """Тестирование класса Button."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        btn = Button()
        self.assertEqual(btn.rect, bmp.bmg.Rect.create_2(0, 0, 75, 25))
        self.assertEqual(btn.text, bmp.bmg.String.create("Button"))
        self.assertEqual(btn.color, bmp.bmg.Color.get_white())
        self.assertEqual(btn.border_color, bmp.bmg.Color.get_black())

    def test_init(self):
        """Тест функции init."""
        btn = Button()
        rect = bmp.bmg.Rect.create_2(200, 200, 100, 50)
        text = bmp.bmg.String.create('Text')
        color = bmp.bmg.Color.get_white()
        border_color = bmp.bmg.Color.get_black()
        btn.init(rect, text, color, border_color)
        self.assertEqual(btn.rect, rect)
        self.assertEqual(btn.text, text)
        self.assertEqual(btn.color, color)
        self.assertEqual(btn.border_color, border_color)

    def test_create(self):
        """Тест функции create."""
        pass

    def test_equal(self):
        """Тест оператора ==."""
        btn = Button()
        self.assertTrue(btn == btn)

    def test_not_equal(self):
        """Тест оператора !=."""
        btn = Button()
        self.assertFalse(btn != btn)


# Вызывается при загрузке модуля главным
if __name__ == "__main__":
    unittest.main()
