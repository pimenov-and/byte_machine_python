# coding: utf8
import unittest

#----------------------------------------------------------------
# Состояние клавиатуры (только цифровые клавиши)
#----------------------------------------------------------------

class DigitKeyboard(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.keys = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def init(self, keys):
        '''Функция инициализации.'''
        assert DigitKeyboard.check_keys(keys)
        self.keys = keys

    @staticmethod
    def create(keys):
        '''Функция создания.'''
        assert DigitKeyboard.check_keys(keys)
        dk = DigitKeyboard()
        dk.init(keys)
        return dk

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        return DigitKeyboard.check_keys(byte_list)

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        return self.keys

    def from_byte_list(self, byte_list):
        assert self.check_byte_list(byte_list)
        self.keys = byte_list

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 10

    def __eq__(self, other):
        '''Оператор ==.'''
        return self.keys == other.keys

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self.keys == other.keys)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.keys)

    @staticmethod
    def check_keys(keys):
        '''Проверка кодов клавиш.'''
        if not isinstance(keys, list):
            return False
        if not all(b in [0, 1] for b in keys):
            return False
        if len(keys) != 10:
            return False
        return True


#----------------------------------------------------------------
# Тестирование класса DigitKeyboard
#----------------------------------------------------------------

class TestDigitKeyboard(unittest.TestCase):

    def test_constructor(self):
        dk = DigitKeyboard()
        self.assertEqual(len(dk.keys), 10)
        self.assertEqual(dk.keys, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_init(self):
        bl = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        dk = DigitKeyboard()
        dk.init(bl)
        self.assertEqual(dk.keys, bl)

    def test_create(self):
        bl = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        dk = DigitKeyboard.create(bl)
        self.assertEqual(dk.keys, bl)

    def test_get_byte_list_len(self):
        dk = DigitKeyboard()
        self.assertEqual(dk.get_byte_list_len(), 10)

    def test_to_byte_list(self):
        dk = DigitKeyboard()
        bl = dk.to_byte_list()
        self.assertEqual(len(bl), 10)
        self.assertEqual(bl, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_from_byte_list(self):
        dk = DigitKeyboard()
        bl = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dk.from_byte_list(bl)
        self.assertEqual(dk.keys, bl)

    def test_equal(self):
        dk1 = DigitKeyboard()
        self.assertTrue(dk1 == dk1)

    def test_not_equal(self):
        dk1 = DigitKeyboard()
        bl = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        dk2 = DigitKeyboard.create(bl)
        self.assertTrue(dk1 != dk2)


#----------------------------------------------------------------
# Вызывается при загрузке модуля главным
#----------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
