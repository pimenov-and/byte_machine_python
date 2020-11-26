# coding: utf8
import unittest
from file_dump_graphics import *


#----------------------------------------------------------------
#  Состояние мыши
#----------------------------------------------------------------

class Mouse(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.pos = Point()
        self.isLeftBtnDown = False
        self.isMiddleBtnDown = False
        self.isRightBtnDown = False

    def init(self, pos, isLeftBtnDown, isMiddleBtnDown, isRightBtnDown):
        '''Функция инициализации.'''
        assert isinstance(pos, Point)
        assert isinstance(isLeftBtnDown, bool)
        assert isinstance(isMiddleBtnDown, bool)
        assert isinstance(isRightBtnDown, bool)
        self.pos = pos
        self.isLeftBtnDown = isLeftBtnDown
        self.isMiddleBtnDown = isMiddleBtnDown
        self.isRightBtnDown = isRightBtnDown

    @staticmethod
    def create(pos, isLeftBtnDown, isMiddleBtnDown, isRightBtnDown):
        '''Функция создания.'''
        assert isinstance(pos, Point)
        assert isinstance(isLeftBtnDown, bool)
        assert isinstance(isMiddleBtnDown, bool)
        assert isinstance(isRightBtnDown, bool)
        m = Mouse()
        m.init(pos, isLeftBtnDown, isMiddleBtnDown, isRightBtnDown)
        return m

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) != 11:
            return False
        return True

    def from_byte_list(self, byte_list):
        '''Инициализация из список байтов.'''
        assert self.check_byte_list(byte_list)
        blp = byte_list[:8]
        self.pos.from_byte_list(blp)
        self.isLeftBtnDown = byte_list_to_bool([byte_list[8]])
        self.isMiddleBtnDown = byte_list_to_bool([byte_list[9]])
        self.isRightBtnDown = byte_list_to_bool([byte_list[10]])

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += self.pos.to_byte_list()
        bl += bool_to_byte_list(self.isLeftBtnDown)
        bl += bool_to_byte_list(self.isMiddleBtnDown)
        bl += bool_to_byte_list(self.isRightBtnDown)
        return bl

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 11

    def __eq__(self, other):
        '''Оператор ==.'''
        isPosEq = (self.pos == other.pos)
        isLeftBtnDownEq = (self.isLeftBtnDown == other.isLeftBtnDown)
        isMiddleBtnDownEq = (self.isMiddleBtnDown == other.isMiddleBtnDown)
        isRightBtnDownEq = (self.isRightBtnDown == other.isRightBtnDown)
        return isPosEq and isLeftBtnDownEq and isMiddleBtnDownEq and isRightBtnDownEq

    def __ne__(self, other):
        '''Оператор !=.'''
        return not self == other

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}, {}, {}, {}'.format(self.pos, self.isLeftBtnDown, self.isMiddleBtnDown, self.isRightBtnDown)


#----------------------------------------------------------------
# Тестирование класса Mouse
#----------------------------------------------------------------

class TestMouse(unittest.TestCase):

    def test_constructor(self):
        m = Mouse()
        self.assertEqual(m.pos, Point())
        self.assertEqual(m.isLeftBtnDown, False)
        self.assertEqual(m.isMiddleBtnDown, False)
        self.assertEqual(m.isRightBtnDown, False)

    def test_init(self):
        m = Mouse()
        m.init(Point(), True, False, False)
        self.assertEqual(m.pos, Point())
        self.assertEqual(m.isLeftBtnDown, True)
        self.assertEqual(m.isMiddleBtnDown, False)
        self.assertEqual(m.isRightBtnDown, False)

    def test_create(self):
        pos = Point.create(110, 110)
        isLeftBtnDown = False
        isMiddleBtnDown = True
        isRightBtnDown = False
        m = Mouse.create(pos, isLeftBtnDown, isMiddleBtnDown, isRightBtnDown)
        self.assertEqual(m.pos, pos)
        self.assertEqual(m.isLeftBtnDown, isLeftBtnDown)
        self.assertEqual(m.isMiddleBtnDown, isMiddleBtnDown)
        self.assertEqual(m.isRightBtnDown, isRightBtnDown)

    def test_to_byte_list(self):
        m = Mouse()
        bl = m.to_byte_list()
        self.assertEqual(m.get_byte_list_len(), len(bl))

    def test_from_byte_list(self):
        pos = Point.create(110, 110)
        isLeftBtnDown = False
        isMiddleBtnDown = True
        isRightBtnDown = False
        bl = []
        bl += pos.to_byte_list()
        bl += bool_to_byte_list(isLeftBtnDown)
        bl += bool_to_byte_list(isMiddleBtnDown)
        bl += bool_to_byte_list(isRightBtnDown)
        m = Mouse()
        m.from_byte_list(bl)
        self.assertEqual(m.pos, pos)
        self.assertEqual(m.isLeftBtnDown, isLeftBtnDown)
        self.assertEqual(m.isMiddleBtnDown, isMiddleBtnDown)
        self.assertEqual(m.isRightBtnDown, isRightBtnDown)

    def test_get_byte_list_len(self):
        m = Mouse()
        self.assertEqual(m.get_byte_list_len(), 11)

    def test_equal(self):
        m1 = Mouse()
        self.assertTrue(m1 == m1)
        m2 = Mouse.create(Point(), False, True, False)
        self.assertFalse(m1 == m2)

    def test_not_equal(self):
        pos = Point.create(100, 100)
        m1 = Mouse.create(pos, False, False, True)
        m2 = Mouse()
        self.assertTrue(m1 != m2)
        self.assertFalse(m1 != m1)


#----------------------------------------------------------------
# Вызывается при загрузке модуля главным
#----------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
