# coding: utf8
'''
ByteMachine
Контролы.
'''
from __future__ import annotations
import unittest
import byte_machine_paint_3 as bmp


class Button(object):
    '''
    Класс кнопки.
    '''

    def __init__(self):
        '''
        Конструктор без параметров.
        '''
        self.rect = bmp.bmg.Rect.create_2(0, 0, 75, 25)
        self.text = bmp.bmg.String.create('Button')
        self.color = bmp.bmg.Color.get_white()
        self.borderColor = bmp.bmg.Color.get_black()
        self.clickHandler = None

    def init(self, rect: bmp.bmg.Rect, text: bmp.bmg.String,
             color: bmp.bmg.Color = bmp.bmg.Color.get_white(),
             borderColor: bmp.bmg.Color = bmp.bmg.Color.get_black()) -> None:
        '''
        Функция инициализации.
        '''
        assert isinstance(rect, bmp.bmg.Rect)
        assert isinstance(text, bmp.bmg.String)
        assert isinstance(color, bmp.bmg.Color)
        assert isinstance(borderColor, bmp.bmg.Color)
        self.rect = rect
        self.text = text
        self.color = color
        self.borderColor = borderColor

    def create(rect: bmp.bmg.Rect, text: bmp.bmg.String,
               color: bmp.bmg.Color = bmp.bmg.Color.get_white(),
               borderColor: bmp.bmg.Color = bmp.bmg.Color.get_black()) -> Button:
        '''
        Функция создания.
        '''
        btn = Button()
        btn.init(rect, text, color, borderColor)
        return btn

    def check_byte_list(self, byte_array: bytearray) -> bool:
        '''
        Проверка корректности списка байтов для инициализации.
        '''
        return isinstance(byte_array, bytearray)

    def to_byte_array(self) -> bytearray:
        '''
        Получение в виде списка байтов.
        '''
        ba = bytearray()
        ba += self.rect.to_byte_array()
        ba += self.text.to_byte_array()
        ba += self.color.to_byte_array()
        ba += self.borderColor.to_byte_array()
        return ba

    def from_byte_array(self, byte_list) -> None:
        '''
        Инициализация из список байтов.
        '''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_array_len(self) -> bytearray:
        '''
        Получение длины списка байтов.
        '''
        return len(self.to_byte_list())

    def draw(self, painter: bmp.Painter) -> None:
        '''
        Получение в виде графических операций.
        '''
        pass

    def __eq__(self, other: Button) -> bool:
        '''
        Оператор ==.
        '''
        isEqRect = (self.rect == other.rect)
        isEqText = (self.text == other.text)
        isEqColor = (self.color == other.color)
        isEqColor = (self.borderColor == other.borderColor)
        return isEqRect and isEqText and isEqColor and isEqColor

    def __ne__(self, other: Button) -> bool:
        '''
        Оператор !=.
        '''
        return not (self == other)


class TestButton(unittest.TestCase):
    '''
    Тестирование класса Button.
    '''

    def test_constructor(self):
        btn = Button()
        self.assertEqual(btn.rect, bmp.bmg.Rect.create_2(0, 0, 75, 25))
        self.assertEqual(btn.text, bmp.bmg.String.create('Button'))
        self.assertEqual(btn.color, bmp.bmg.Color.get_white())
        self.assertEqual(btn.borderColor, bmp.bmg.Color.get_black())

    def test_init(self):
        btn = Button()
        rect = bmp.bmg.Rect.create_2(200, 200, 100, 50)
        text = bmp.bmg.String.create('Text')
        color = bmp.bmg.Color.get_white()
        borderColor = bmp.bmg.Color.get_black()
        btn.init(rect, text, color, borderColor)
        self.assertEqual(btn.rect, rect)
        self.assertEqual(btn.text, text)
        self.assertEqual(btn.color, color)
        self.assertEqual(btn.borderColor, borderColor)

    def test_create(self):
        pass

    def test_equal(self):
        btn = Button()
        self.assertTrue(btn == btn)

    def test_not_equal(self):
        btn = Button()
        self.assertFalse(btn != btn)


# Вызывается при загрузке модуля главным
if __name__ == '__main__':
    unittest.main()
