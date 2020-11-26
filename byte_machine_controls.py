#coding: utf8
import unittest
from file_dump_paint import *


#----------------------------------------------------------------
# Класс кнопки
#----------------------------------------------------------------

class Button(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rect = Rect.create2(0, 0, 75, 25)
        self.text = String.create(u'Button')
        self.color = Color.get_white()
        self.borderColor = Color.get_black()

    def init(self, rect, text, color=Color.get_white(), borderColor=Color.get_black()):
        '''Функция инициализации.'''
        assert isinstance(rect, Rect)
        assert isinstance(text, String)
        assert isinstance(color, Color)
        assert isinstance(borderColor, Color)
        self.rect = rect
        self.text = text
        self.color = color
        self.borderColor = borderColor

    def create(rect, text, color=Color.get_white(), borderColor=Color.get_black()):
        '''Функция создания.'''
        assert isinstance(rect, Rect)
        assert isinstance(text, String)
        assert isinstance(color, Color)
        assert isinstance(borderColor, Color)
        btn = Button()
        btn.init(rect, text, color, borderColor)
        return btn

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += self.rect.to_byte_list()
        bl += self.text.to_byte_list()
        bl += self.color.to_byte_list()
        bl += self.borderColor.to_byte_list()
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из список байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def to_draw_ops(self):
        '''Получение в виде графических операций'''
        ops = []
        ops.append(SaveStateOp())
        ops.append(SetPenOp.create(self.borderColor()))
        ops.append(SetBrushOp.create(self.color()))
        ops.append(DrawRectOp.create(self.rect))
        ops.append(RestoreStateOp())
        return ops

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, Button)
        isEqRect = (self.rect == other.rect)
        isEqText = (self.text == other.text)
        isEqColor = (self.color == other.color)
        isEqColor = (self.borderColor == other.borderColor)
        return isEqRect and isEqText and isEqColor and isEqColor

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, Button)
        return not (self == other)


#----------------------------------------------------------------
# Тестирование класса кнопки
#----------------------------------------------------------------

class TestButton(unittest.TestCase):

    def test_constructor(self):
        btn = Button()
        self.assertEqual(btn.rect, Rect.create2(0, 0, 75, 25))
        self.assertEqual(btn.text, String.create(u'Button'))
        self.assertEqual(btn.color, Color.get_white())
        self.assertEqual(btn.borderColor, Color.get_black())

    def test_init(self):
        btn = Button()
        rect = Rect.create2(200, 200, 100, 50)
        text = String.create(u'Text')
        color = Color.get_white()
        borderColor = Color.get_black()
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


#----------------------------------------------------------------
# Вызывается при загрузке модуля главным
#----------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
