# coding: utf8
import math
import unittest
from file_dump_convert import *


#----------------------------------------------------------------
# Функции
#----------------------------------------------------------------

def check_byte_list(byte_list):
    '''Проверка корректности списка байтов.'''
    if not isinstance(byte_list, list):
        return False
    if not all(0 <= b <= 255 for b in byte_list):
        return False
    return True


#----------------------------------------------------------------
# Цвет
#----------------------------------------------------------------

class Color(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.red = 0
        self.green = 0
        self.blue = 0
        self.alpha = 255

    def init(self, red, green, blue, alpha=255):
        '''Функция инициализации.'''
        assert 0 <= red <= 255
        assert 0 <= green <= 255
        assert 0 <= blue <= 255
        assert 0 <= alpha <= 255
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    @staticmethod
    def create(red, green, blue, alpha=255):
        '''Функция создания с параметрами.'''
        assert 0 <= red <= 255
        assert 0 <= green <= 255
        assert 0 <= blue <= 255
        assert 0 <= alpha <= 255
        c = Color()
        c.init(red, green, blue, alpha)
        return c
    
    # Основные цвета.
    @staticmethod
    def get_black():
        '''Получение черного цвета.'''
        return Color.create(0, 0, 0)

    @staticmethod
    def get_white():
        '''Получение белого цвета.'''
        return Color.create(255, 255, 255)
    
    @staticmethod
    def get_red():
        '''Получение красного цвета.'''
        return Color.create(255, 0, 0)

    @staticmethod
    def get_green():
        '''Получение зеленого цвета.'''
        return Color.create(0, 128, 0)

    @staticmethod
    def get_blue():
        '''Получение синего цвета.'''
        return Color.create(0, 0, 255)

    @staticmethod
    def get_gray():
        '''Получение серого цвета.'''
        return Color.create(128, 128, 128)

    @staticmethod
    def get_yellow():
        '''Получение желтого цвета.'''
        return Color.create(255, 255, 0)

    @staticmethod
    def get_transparent():
        '''Получение прозрачного цвета.'''
        return Color.create(0, 0, 0, 0)

    # Красные тона.
    @staticmethod
    def get_indian_red():
        '''Получение цвета indian_red.'''
        return Color.create(205, 92, 92)

    @staticmethod
    def get_light_coral():
        '''Получение цвета light_coral.'''
        return Color.create(240, 128, 128)

    @staticmethod
    def get_dark_salmon():
        '''Получение цвета dark_salmon.'''
        return Color.create(233, 150, 122)

    @staticmethod
    def get_light_salmon():
        '''Получение цвета light_salmon.'''
        return Color.create(255, 160, 122)

    @staticmethod
    def get_crimson():
        '''Получение малинового цвета.'''
        return Color.create(220, 20, 60)

    @staticmethod
    def get_fire_brick():
        '''Получение кирпичного цвета.'''
        return Color.create(178, 34, 34)

    @staticmethod
    def get_dark_red():
        '''Получение тёмно-красного цвета.'''
        return Color.create(139, 0, 0)

    # Розовые тона.
    @staticmethod
    def get_pink():
        '''Получение розового цвета.'''
        return Color.create(255, 192, 203)

    @staticmethod
    def get_light_pink():
        '''Получение светло-розового цвета.'''
        return Color.create(255, 182, 193)

    @staticmethod
    def get_hot_pink():
        '''Получение цвета HotPink.'''
        return Color.create(255, 105, 180)

    @staticmethod
    def get_deep_pink():
        '''Получение цвета DeepPink.'''
        return Color.create(255, 20, 147)

    @staticmethod   
    def get_medium_violet_red():
        '''Получение цвета MediumVioletRed.'''
        return Color.create(199, 21, 133)

    @staticmethod
    def get_pale_violet_red():
        '''Получение цвета PaleVioletRed.'''
        return Color.create(219, 112, 147)

    # Оранжевые тона.    
    @staticmethod
    def get_coral():
        '''Получение цвета Coral.'''
        return Color.create(255, 127, 80)
    
    @staticmethod
    def get_tomato():
        '''Получение томатного цвета.'''
        return Color.create(255, 99, 71)

    @staticmethod
    def get_orange_red():
        '''Получение красно-оранжевого цвета.'''
        return Color.create(255, 69, 0)

    @staticmethod
    def get_dark_orange():
        '''Получение темно-оранжевого цвета.'''
        return Color.create(255, 140, 0)
    
    @staticmethod
    def get_orange():
        '''Получение оранжевого цвета.'''
        return Color.create(255, 165, 0)

    # Желтые тона
    @staticmethod
    def get_gold():
        '''Получение золотого цвета.'''
        return Color.create(255, 215, 0)

    @staticmethod
    def get_light_yellow():
        '''Получение светло-желтого цвета.'''
        return Color.create(255, 255, 224)

    @staticmethod
    def get_lemon_chiffon():
        '''Получение цвета LemonChiffon.'''
        return Color.create(255, 250, 205)

    @staticmethod
    def get_light_goldenrod_yellow():
        '''Получение цвета LightGoldenrodYellow.'''
        return Color.create(250, 250, 210)

    @staticmethod
    def get_papaya_whip():
        '''Получение цвета PapayaWhip.'''
        return Color.create(255, 239, 213)

    @staticmethod
    def get_moccasin():
        '''Получение цвета Moccasin.'''
        return Color.create(255, 228, 181)

    @staticmethod
    def get_peach_puff():
        '''Получение цвета PeachPuff.'''
        return Color.create(255, 218, 185)

    @staticmethod
    def get_pale_goldenrod():
        '''Получение цвета PaleGoldenrod.'''
        return Color.create(238, 232, 170)

    @staticmethod
    def get_khaki():
        '''Получение цвета хаки.'''
        return Color.create(240, 230, 140)

    @staticmethod
    def get_dark_khaki():
        '''Получение цвета темный хаки.'''
        return Color.create(189, 183, 107)

    @staticmethod
    def get_navy():
        '''Получение цвета Navy.'''
        return Color.create(0, 0, 128)

    @staticmethod
    def get_lime():
        '''Получение цвета Lime.'''
        return Color.create(0, 255, 0)

    @staticmethod
    def get_teal():
        '''Получение цвета Teal.'''
        return Color.create(0, 128, 128)

    @staticmethod
    def get_aqua():
        '''Получение цвета Aqua.'''
        return Color.create(0, 255, 255)

    @staticmethod
    def get_olive():
        '''Получение цвета Olive.'''
        return Color.create(128, 128, 0)    

    @staticmethod
    def get_maroon():
        '''Получение цвета Maroon.'''
        return Color.create(128, 0, 0)

    @staticmethod
    def get_purple():
        '''Получение пурпурного цвета.'''
        return Color.create(128, 0, 128)

    @staticmethod
    def get_magenta():
        '''Получение цвета "Маджента".'''
        return Color.create(255, 0, 255)

    @staticmethod
    def get_silver():
        '''Получение цвета Silver.'''
        return Color.create(192, 192, 192)

    @staticmethod
    def get_light_gray():
        '''Получение цвета LightGray.'''
        return Color.create(211, 211, 211)

    @staticmethod
    def get_dark_gray():
        '''Получение цвета DarkGray.'''
        return Color.create(169, 169, 169)

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) != 4:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        return [self.red, self.green, self.blue, self.alpha]

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        self.init(byte_list[0], byte_list[1], byte_list[2], byte_list[3])

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 4

    def __eq__(self, other):
        '''Проверка на равенство.'''
        assert isinstance(other, Color)
        isEqRed = (self.red == other.red)
        isEqGreen = (self.green == other.green)
        isEqBlue = (self.blue == other.blue)
        isEqAlpha = (self.alpha == other.alpha)
        return isEqRed and isEqGreen and isEqBlue and isEqAlpha

    def __ne__(self, other):
        '''Функция проверки на неравенство.'''
        assert isinstance(other, Color)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления цвета.'''
        return '{}, {}, {}, {}'.format(self.red, self.green, self.blue, self.alpha)


#----------------------------------------------------------------
# Строка
#----------------------------------------------------------------

class String(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.s = u''

    def init(self, s):
        '''Функция инициализации.'''
        assert isinstance(s, unicode)
        self.s = s

    @staticmethod
    def create(s):
        '''Функция создания.'''
        assert isinstance(s, unicode)
        st = String()
        st.init(s)
        return st

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < 4:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        sbl = unicode_to_byte_list(self.s)
        bl += int32_to_byte_list(len(sbl))
        bl += sbl
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        sbl = byte_list[:4]
        sz = byte_list_to_int32(sbl)
        self.s = byte_list_to_unicode(byte_list[4:])

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, String)
        return self.s == other.s

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, String)
        return not (self == other)

    def __lt__(self, other):
        '''Оператор <.'''
        assert isinstance(other, String)
        return self.s < other.s

    def __le__(self, other):
        '''Оператор <=.'''
        assert isinstance(other, String)
        return self.s <= other.s

    def __gt__(self, other):
        '''Оператор >.'''
        assert isinstance(other, String)
        return self.s > other.s

    def __ge__(self, other):
        '''Оператор >=.'''
        assert isinstance(other, String)
        return self.s >= other.s

    def __str__(self):
        '''Получение строкового представления цвета.'''
        return self.s


#----------------------------------------------------------------
# Точка с целочисленными координатами
#----------------------------------------------------------------

class Point(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.x = 0
        self.y = 0

    def init(self, x, y):
        '''Функция иницилизации.'''
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.x = x
        self.y = y

    @staticmethod
    def create(x, y):
        '''Функция создания с параметрами.'''
        assert isinstance(x, int)
        assert isinstance(y, int)
        pt = Point()
        pt.init(x, y)
        return pt

    def is_null(self):
        '''Проверка координат на равенство 0.'''
        return (self.x == 0) and (self.y == 0)

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) != 8:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        xbl = int32_to_byte_list(self.x)
        ybl = int32_to_byte_list(self.y)
        return xbl + ybl
    
    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        vl = byte_list_to_int32_list(byte_list)
        self.init(vl[0], vl[1])

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 8

    def manhattan_len(self):
        '''Манхэттенское расстояние.'''
        return (int)(math.sqrt(self.x * self.x + self.y * self.y))

    def __add__(self, other):
        '''Бинарный оператор +.'''
        assert isinstance(other, Point)
        return Point.create(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        '''Оператор +=.'''
        assert isinstance(other, Point)
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        '''Бинарный оператор -.'''
        assert isinstance(other, Point)
        return Point.create(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        '''Оператор -=.'''
        assert isinstance(other, Point)
        self.x -= other.x
        self.y -= other.y
        return self

    def __neg__(self):
        '''Унарный оператор -.'''
        assert isinstance(other, Point)
        return Point.create(-self.x, -self.y)

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, Point)
        isEqX = (self.x == other.x)
        isEqY = (self.y == other.y)
        return isEqX and isEqY

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, Point)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления цвета.'''
        return '{}, {}'.format(self.x, self.y)


#----------------------------------------------------------------
# Точка с дробными координатами
#----------------------------------------------------------------

class PointF(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.x = 0.0
        self.y = 0.0

    def init(self, x, y):
        '''Функция инициализации.'''
        assert isinstance(x, float)
        assert isinstance(y, float)
        self.x = x
        self.y = y

    @staticmethod
    def create(x, y):
        '''Функция создания с параметрами.'''
        assert isinstance(x, float)
        assert isinstance(y, float)
        pt = PointF()
        pt.init(x, y)
        return pt

    def is_null(self):
        '''Проверка координат на равенство 0.'''
        return float_equal(self.x, 0.0) and float_equal(self.y, 0.0)

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) != self.get_byte_list_len():
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        xbl = double_to_byte_list(self.x)
        ybl = double_to_byte_list(self.y)
        return xbl + ybl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        vl = byte_list_to_double_list(byte_list)
        self.init(vl[0], vl[1])

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 16

    def manhattan_len(self):
        '''Манхэттенское расстояние.'''
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __add__(self, other):
        '''Бинарный оператор +.'''
        assert isinstance(other, PointF)
        return PointF.create(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        '''Оператор +=.'''
        assert isinstance(other, PointF)
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        '''Бинарный оператор -.'''
        assert isinstance(other, PointF)
        return PointF.create(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        '''Оператор -=.'''
        assert isinstance(other, PointF)
        self.x -= other.x
        self.y -= other.y
        return self

    def __neg__(self):
        '''Унарный оператор -.'''
        assert isinstance(other, PointF)
        return Point.create(-self.x, -self.y)

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, PointF)
        isEqX = float_equal(self.x, other.x)
        isEqY = float_equal(self.y, other.y)
        return isEqX and isEqY

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, PointF)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}, {}'.format(self.x, self.y)


#----------------------------------------------------------------
# Размер с целочисленными координатами
#----------------------------------------------------------------

class Size(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.width = 0
        self.height = 0

    def init(self, width, height):
        '''Функция инициализации.'''
        assert isinstance(width, int)
        assert isinstance(height, int)
        self.width = width
        self.height = height

    @staticmethod
    def create(width, height):
        '''Функция создания.'''
        assert isinstance(width, int)
        assert isinstance(height, int)
        size = Size()
        size.init(width, height)
        return size

    def is_null(self):
        '''Проверка ширины и высоты на 0.'''
        return (self.width == 0) and (self.height == 0)

    def is_valid(self):
        '''Является ли размер валидным.'''
        return (self.width >= 0) and (self.height >= 0)

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) != 8:
            return False
        return True

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        bl = byte_list_to_int32_list(byte_list)
        self.width = bl[0]
        self.height = bl[1]

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        wbl = int32_to_byte_list(self.width)
        hbl = int32_to_byte_list(self.height)
        return wbl + hbl

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 8

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, Size)
        isEqWidth = (self.width == other.width)
        isEqHeight = (self.height == other.height)
        return isEqWidth and isEqHeight

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, Size)
        return not (self == other)

    def __mul__(self, other):
        '''Оператор *.'''
        assert isinstance(other, float)
        width = (int)(self.width * other)
        height = (int)(self.height * other)
        return Size.init(width, height)

    def __imul__(self, other):
        '''Оператор *=.'''
        assert isinstance(other, float)
        self.width = (int)(self.width * other)
        self.height = (int)(self.height * other)
        return self

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}, {}'.format(self.width, self.height)


#----------------------------------------------------------------
# Размер с дробными координатами
#----------------------------------------------------------------

class SizeF(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.width = 0.0
        self.height = 0.0

    def init(self, width, height):
        '''Функция инициализации.'''
        assert isinstance(width, float)
        assert isinstance(height, float)
        self.width = width
        self.height = height

    @staticmethod
    def create(width, height):
        '''Функция создания.'''
        assert isinstance(width, float)
        assert isinstance(height, float)
        size = SizeF()
        size.init(width, height)
        return size

    def is_null(self):
        '''Проверка ширины и высоты на 0.'''
        return float_equal(self.width, 0.0) and float_equal(self.height, 0.0)

    def is_valid(self):
        '''Является ли размер валидным.'''
        return (self.width >= 0.0) and (self.height >= 0.0)

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) != self.get_byte_list_len():
            return False
        return True

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        self.width = byte_list_to_double(byte_list[:8])
        self.height = byte_list_to_double(byte_list[8:])

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        return double_to_byte_list(self.width) + double_to_byte_list(self.height)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 16

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, SizeF)
        isEqWidth = float_equal(self.width, other.width)
        isEqHeight = float_equal(self.height, other.height)
        return isEqWidth and isEqHeight

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, SizeF)
        return not (self == other)

    def __mul__(self, other):
        '''Оператор *.'''
        assert isinstance(other, float)
        return Size.init(self.width * other, self.height * other)

    def __imul__(self, other):
        '''Оператор *=.'''
        assert isinstance(other, float)
        self.width *= other
        self.height *= other
        return self

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}, {}'.format(self.width, self.height)


#----------------------------------------------------------------
# Линия с целочисленными координатами
#----------------------------------------------------------------

class Line(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.pt1 = Point()
        self.pt2 = Point()

    def init(self, pt1, pt2):
        '''Функция инициализации.'''
        assert isinstance(pt1, Point)
        assert isinstance(pt2, Point)
        self.pt1 = pt1
        self.pt2 = pt2

    def init2(self, x1, y1, x2, y2):
        '''Функция инициализации.'''
        assert isinstance(x1, int)
        assert isinstance(y1, int)
        assert isinstance(x2, int)
        assert isinstance(y2, int)
        self.pt1.x = x1
        self.pt1.y = y1
        self.pt2.x = x2
        self.pt2.y = y2

    @staticmethod
    def create(pt1, pt2):
        '''Функция инициализации 2.'''
        assert isinstance(pt1, Point)
        assert isinstance(pt2, Point)
        line = Line()
        line.pt1 = pt1
        line.pt2 = pt2
        return line

    @staticmethod
    def create2(x1, y1, x2, y2):
        '''Функция инициализации 2.'''
        assert isinstance(x1, int)
        assert isinstance(y1, int)
        assert isinstance(x2, int)
        assert isinstance(y2, int)
        line = Line()
        line.pt1 = Point.create(x1, y1)
        line.pt2 = Point.create(x2, y2)
        return line

    def is_empty(self):
        '''Проверка на линию нулевой длины.'''
        return self.pt1 == self.pt2

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) != 16:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += self.pt1.to_byte_list()
        bl += self.pt2.to_byte_list()
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        bl_pt1 = byte_list[:8]
        self.pt1.from_byte_list(bl_pt1)
        bl_pt2 = byte_list[8:]
        self.pt2.from_byte_list(bl_pt2)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 16
    
    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, Line)
        isEqPt1 = (self.pt1 == other.pt1)
        isEqPt2 = (self.pt2 == other.pt2)
        return isEqPt1 and isEqPt2

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, Line)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления объекта.'''
        return '{}, {}'.format(self.pt1, self.pt2)


#----------------------------------------------------------------
# Линия с дробными координатами
#----------------------------------------------------------------

class LineF(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.pt1 = PointF()
        self.pt2 = PointF()

    def init(self, pt1, pt2):
        '''Функция инициализации.'''
        assert isinstance(pt1, PointF)
        assert isinstance(pt2, PointF)
        self.pt1 = pt1
        self.pt2 = pt2

    def init2(self, x1, y1, x2, y2):
        '''Функция инициализации.'''
        assert isinstance(x1, float)
        assert isinstance(y1, float)
        assert isinstance(x2, float)
        assert isinstance(y2, float)
        self.pt1 = PointF.create(x1, y1)
        self.pt2 = PointF.create(x2, y2)

    @staticmethod
    def create(pt1, pt2):
        '''Функция инициализации 2.'''
        assert isinstance(pt1, PointF)
        assert isinstance(pt2, PointF)
        line = LineF()
        line.pt1 = pt1
        line.pt2 = pt2
        return line

    @staticmethod
    def create2(x1, y1, x2, y2):
        '''Функция инициализации 2.'''
        assert isinstance(x1, float)
        assert isinstance(y1, float)
        assert isinstance(x2, float)
        assert isinstance(y2, float)
        line = LineF()
        line.pt1 = PointF.create(x1, y1)
        line.pt2 = PointF.create(x2, y2)
        return line

    def is_empty(self):
        '''Проверка на линию нулевой длины.'''
        return self.pt1 == self.pt2

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) != 32:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += self.pt1.to_byte_list()
        bl += self.pt2.to_byte_list()
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        bl_pt1 = byte_list[:16]
        self.pt1.from_byte_list(bl_pt1)
        bl_pt2 = byte_list[16:]
        self.pt2.from_byte_list(bl_pt2)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 32

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, LineF)
        isEqPt1 = (self.pt1 == other.pt1)
        isEqPt2 = (self.pt2 == other.pt2)
        return isEqPt1 and isEqPt2

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, LineF)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления объекта.'''
        return '{}, {}'.format(self.pt1, self.pt2)


#----------------------------------------------------------------
# Ломаная линия с целыми координатами
#----------------------------------------------------------------

class Polyline(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.points = []

    def init(self, points):
        '''Функция инициализации.'''
        assert Polyline._check_points(points)
        self.points = points

    @staticmethod
    def create(points):
        '''Функция создания.'''
        assert Polyline._check_points(points)
        p = Polyline()
        p.init(points)
        return p

    def add_point(self, point):
        '''Добавление точки.'''
        assert isinstance(point, Point)
        self.points.append(point)

    def get_point_count(self):
        '''Получение количества точек.'''
        return len(self.points)

    def is_empty(self):
        '''Проверка на отсутствие точек.'''
        return self.get_point_count() == 0

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < 4:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int32_to_byte_list(self.get_point_count())
        for pt in self.points:
            bl += pt.to_byte_list()
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        cbl = byte_line[:4]
        count = byte_list_to_int32(cbl)
        self.points = []
        for i in range(count):
            p = Point()
            bi = 4 + i * 8
            ei = bi + 8
            pbl = byte_list[bi:ei]
            p.from_byte_list(pbl)
            self.add_point(p)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, Polyline)
        return self.points == other.points

    def __ne__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, Polyline)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления объекта.'''
        return '{}'.format(self.points)

    @staticmethod
    def _check_points(points):
        '''Проверка списка точек.'''
        if not isinstance(points, list):
            return False
        if not all(isinstance(pt, Point) for pt in points):
            return False
        return True


#----------------------------------------------------------------
# Ломаная линия с дробными координатами
#----------------------------------------------------------------

class PolylineF(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.points = []

    def init(self, points):
        '''Функция инициализации.'''
        assert PolylineF._check_points(points)
        self.points = points

    @staticmethod
    def create(points):
        '''Функция создания.'''
        assert PolylineF._check_points(points)
        p = PolylineF()
        p.init(points)
        return p

    def add_point(self, point):
        '''Добавление точки.'''
        assert isinstance(point, PointF)
        self.points.append(point)

    def get_point_count(self):
        '''Получение количества точек.'''
        return len(self.points)

    def is_empty(self):
        '''Проверка на отсутствие точек.'''
        return self.get_point_count() == 0

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < 4:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        count = self.get_point_count()
        bl += int32_to_byte_list(count)
        for pt in self.points:
            bl += pt.to_byte_list()
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        cbl = byte_list[:4]
        count = byte_list_to_int32(cbl)
        self.points = []
        for i in range(count):
            p = PointF()
            bi = 4 + i * 16
            ei = bi + 16
            pbl = byte_list[bi:ei]
            p.from_byte_list(pbl)
            self.add_point(p)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, PolylineF)
        return self.points == other.points

    def __ne__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, PolylineF)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления объекта.'''
        return '{}'.format(self.points)

    @staticmethod
    def _check_points(points):
        '''Проверка списка точек.'''
        if not isinstance(points, list):
            return False
        if not all(isinstance(pt, PointF) for pt in points):
            return False
        return True


#----------------------------------------------------------------
# Прямоугольник с целочисленными координатами
#----------------------------------------------------------------

class Rect(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.leftTop = Point()
        self.size = Size()

    def init(self, leftTop, size):
        '''Функция инициализации.'''
        assert isinstance(leftTop, Point)
        assert isinstance(size, Size)
        self.leftTop = leftTop
        self.size = size

    def init2(self, left, top, width, height):
        '''Функция инициализации 2.'''
        assert isinstance(left, int)
        assert isinstance(top, int)
        assert isinstance(width, int)
        assert isinstance(height, int)
        self.leftTop = Point.create(left, top)
        self.size = Size.create(width, height)

    @staticmethod
    def create(leftTop, size):
        '''Функция создания.'''
        assert isinstance(leftTop, Point)
        assert isinstance(size, Size)
        rect = Rect()
        rect.init(leftTop, size)
        return rect

    @staticmethod
    def create2(left, top, width, height):
        '''Функция создания 2.'''
        assert isinstance(left, int)
        assert isinstance(top, int)
        assert isinstance(width, int)
        assert isinstance(height, int)
        rect = Rect()
        rect.init2(left, top, width, height)
        return rect

    def get_left(self):
        '''Получение смещения слева.'''
        return self.leftTop.x

    def set_left(self, left):
        '''Задание смещения слева.'''
        assert isinstance(left, int)
        self.leftTop.x = left

    def get_top(self):
        '''Получение смещения слева.'''
        return self.leftTop.y

    def set_top(self, top):
        '''Задание смещения сверху.'''
        assert isinstance(top, int)
        self.leftTop.y = top

    def get_width(self):
        '''Получение ширины.'''
        return self.size.width

    def set_width(self, width):
        '''Задание ширины.'''
        assert isinstance(width, int)
        self.size.width = width
    
    def get_height(self):
        '''Получение высоты.'''
        return self.size.height

    def set_height(self, height):
        '''Задание высоты.'''
        self.size.height = height

    def get_right(self):
        '''Получение координаты правой стороны.'''
        return self.get_left() + self.get_width()

    def get_bottom(self):
        '''Получение координаты низа.'''
        return self.get_top() + self.get_height()

    def get_center(self):
        '''Получение центра.'''
        x = self.get_left() + self.get_width() / 2
        y = self.get_top() + self.get_height() / 2
        return Point.create(x, y)

    def is_valid(self):
        '''Является ли размер валидным.'''
        return self.size.width >= 0 and self.size.height >= 0

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) != 16:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        l = self.get_left()
        t = self.get_top()
        w = self.get_width()
        h = self.get_height()
        vl = [l, t, w, h]
        return int32_list_to_byte_list(vl)

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        vl = byte_list_to_int32_list(byte_list)
        self.init2(vl[0], vl[1], vl[2], vl[3])

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 16

    def __eq__(self, other):
        '''Оператор ==.'''
        isEqLeftTop = (self.leftTop == other.leftTop)
        isEqSize = (self.size == other.size)
        return isEqLeftTop and isEqSize

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}, {}'.format(self.leftTop, self.size)


#----------------------------------------------------------------
# Прямоугольник с дробными координатами
#----------------------------------------------------------------

class RectF(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.leftTop = PointF()
        self.size = SizeF()

    def init(self, leftTop, size):
        '''Функция инициализации.'''
        assert isinstance(leftTop, PointF)
        assert isinstance(size, SizeF)
        self.leftTop = leftTop
        self.size = size

    def init2(self, left, top, width, height):
        '''Функция инициализации 2.'''
        assert isinstance(left, float)
        assert isinstance(top, float)
        assert isinstance(width, float)
        assert isinstance(height, float)
        self.leftTop = PointF.create(left, top)
        self.size = SizeF.create(width, height)

    @staticmethod
    def create(leftTop, size):
        '''Функция создания.'''
        assert isinstance(leftTop, PointF)
        assert isinstance(size, SizeF)
        rect = RectF()
        rect.init(leftTop, size)
        return rect

    @staticmethod
    def create2(left, top, width, height):
        '''Функция создания 2.'''
        assert isinstance(left, float)
        assert isinstance(top, float)
        assert isinstance(width, float)
        assert isinstance(height, float)
        rect = RectF()
        rect.init2(left, top, width, height)
        return rect

    def get_left(self):
        '''Получение смещения слева.'''
        return self.leftTop.x

    def set_left(self, left):
        '''Задание смещения слева.'''
        assert isinstance(left, float)
        self.topLeft.x = left

    def get_top(self):
        '''Получение смещения сверху.'''
        return self.leftTop.y

    def set_top(self, top):
        '''Задание смещения сверху.'''
        assert isinstance(top, float)
        self.topLeft.y = top

    def get_width(self):
        '''Получение ширины.'''
        return self.size.width

    def get_height(self):
        '''Получение высоты.'''
        return self.size.height

    def get_right(self):
        '''Получение координаты правой стороны.'''
        return self.get_left() + self.get_width()

    def get_bottom(self):
        '''Получение координаты низа.'''
        return self.get_top() + self.get_height()

    def get_center(self):
        '''Получение центра.'''
        x = self.get_left() + self.get_width() / 2
        y = self.get_top() + self.get_height() / 2
        return Point.create(x, y)

    def is_valid(self):
        '''Является ли размер валидным.'''
        return self.size.width >= 0.0 and self.size.height >= 0.0

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) != 32:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        l = self.get_left()
        t = self.get_top()
        w = self.get_width()
        h = self.get_height()
        vl = [l, t, w, h]
        return double_list_to_byte_list(vl)

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        vl = byte_list_to_double_list(byte_list)
        self.init2(vl[0], vl[1], vl[2], vl[3]) 

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 32

    def __eq__(self, other):
        '''Оператор ==.'''
        isEqLeftTop = (self.leftTop == other.leftTop)
        isEqSize = (self.size == other.size)
        return isEqLeftTop and isEqSize

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления объекта.'''
        return '{}, {}'.format(self.leftTop, self.size)


#----------------------------------------------------------------
# Прямоугольник со сглажененными углами с целыми координатами
#----------------------------------------------------------------

class RoundRect(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rect = Rect()
        self.radiusX = 0.0
        self.radiusY = 0.0

    def init(self, rect, radiusX, radiusY):
        '''Функция инициализации.'''
        assert isinstance(rect, Rect)
        assert isinstance(radiusX, float)
        assert isinstance(radiusY, float)
        self.rect = rect
        self.radiusX = RoundRect._correctRadius(radiusX)
        self.radiusY = RoundRect._correctRadius(radiusY)

    @staticmethod
    def create(rect, radiusX, radiusY):
        '''Функция создания.'''
        assert isinstance(rect, Rect)
        assert isinstance(radiusX, float)
        assert isinstance(radiusY, float)
        r = RoundRect()
        r.init(rect, radiusX, radiusY)
        return r

    def get_center(self):
        '''Получение центра.'''
        return self.rect.get_center()

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) != 32:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        rbl = self.rect.to_byte_list()
        rxbl = double_to_byte_list(self.radiusX)
        rybl = double_to_byte_list(self.radiusY)
        return rbl + rxbl + rybl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        rbl = byte_list[:16]
        self.rect.from_byte_list(rbl)
        xbl = byte_list[16:24]
        self.radiusX = byte_list_to_double(xbl)
        ybl = byte_list[24:32]
        self.radiusY = byte_list_to_double(ybl)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 32

    def __eq__(self, other):
        '''Оператор ==.'''
        isEqRect = (self.rect == other.rect)
        isEqRadiusX = (self.radiusX == other.radiusX)
        isEqRadiusY = (self.radiusY == other.radiusY)
        return isEqRect and isEqRadiusX and isEqRadiusY

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления объекта.'''
        return '{}, {}, {}'.format(self.rect, self.radiusX, self.radiusY)

    @staticmethod
    def _correctRadius(radius):
        '''Корректировка радиуса.'''
        if radius < 0.0:
            return 0.0
        elif radius > 100.0:
            return 100.0
        else:
            return radius


#----------------------------------------------------------------
# Прямоугольник со сглажененными углами с дробными координатами
#----------------------------------------------------------------

class RoundRectF(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rect = RectF()
        self.radiusX = 0.0
        self.radiusY = 0.0

    def init(self, rect, radiusX, radiusY):
        '''Функция инициализации.'''
        assert isinstance(rect, RectF)
        assert isinstance(radiusX, float)
        assert isinstance(radiusY, float)
        self.rect = rect
        self.radiusX = RoundRectF._correctRadius(radiusX)
        self.radiusY = RoundRectF._correctRadius(radiusY)

    @staticmethod
    def create(rect, radiusX, radiusY):
        '''Функция создания.'''
        assert isinstance(rect, RectF)
        assert isinstance(radiusX, float)
        assert isinstance(radiusY, float)
        r = RoundRectF()
        r.init(rect, radiusX, radiusY)
        return r

    def get_center(self):
        '''Получение центра.'''
        return self.rect.get_center()

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) != 48:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        rbl = self.rect.to_byte_list()
        rxbl = double_to_byte_list(self.radiusX)
        rybl = double_to_byte_list(self.radiusY)
        return rbl + rxbl + rybl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        rbl = byte_list[:32]
        self.rect.from_byte_list(rbl)
        xbl = byte_list[32:40]
        self.radiusX = byte_list_to_double(xbl)
        ybl = byte_list[40:48]
        self.radiusY = byte_list_to_double(ybl)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 48

    def __eq__(self, other):
        '''Оператор ==.'''
        isEqRect = (self.rect == other.rect)
        isEqRadiusX = float_equal(self.radiusX, other.radiusX)
        isEqRadiusY = float_equal(self.radiusY, other.radiusY)
        return isEqRect and isEqRadiusX and isEqRadiusY

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления объекта.'''
        return '{}, {}, {}'.format(self.rect, self.radiusX, self.radiusY)

    @staticmethod
    def _correctRadius(radius):
        '''Корректировка радиуса.'''
        if radius < 0.0:
            return 0.0
        elif radius > 100.0:
            return 100.0
        else:
            return radius


#----------------------------------------------------------------
# Полигон с точками с целочисленными координатами
#----------------------------------------------------------------

class Polygon(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.points = []

    def init(self, points):
        '''Функция инициализации.'''
        assert Polygon._check_points(points)
        self.points = points

    @staticmethod
    def create(points):
        '''Функция создания.'''
        assert Polygon._check_points(points)
        p = Polygon()
        p.init(points)
        return p

    def add_point(self, point):
        '''Добавление точки.'''
        assert isinstance(point, Point)
        self.points.append(point)

    def get_point_count(self):
        '''Получение количества точек.'''
        return len(self.points)

    def is_empty(self):
        return self.get_point_count() == 0

    def check_byte_list(self, byte_list):
        '''Проверка списка байтов.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < 4:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int32_to_byte_list(self.get_point_count())
        for pt in self.points:
            bl += pt.to_byte_list()
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        return self.points == other.points

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.points)

    @staticmethod
    def _check_points(points):
        '''Проверка списка точек.'''
        if not isinstance(points, list):
            return False
        if not all(isinstance(pt, Point) for pt in points):
            return False
        return True


#----------------------------------------------------------------
# Полигон с точками с дробными координатами
#----------------------------------------------------------------

class PolygonF(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.points = []

    def init(self, points):
        '''Функция инициализации.'''
        assert isinstance(points, list)
        self.points = points

    @staticmethod
    def create(points):
        '''Функция создания.'''
        assert isinstance(points, list)
        p = PolygonF()
        p.init(points)
        return p

    def add_point(point):
        assert isinstance(point, PointF)
        points.append(point)

    def get_point_count(self):
        '''Получение количества точек.'''
        return len(self.points)

    def is_empty(self):
        return self.get_point_count() == 0

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < 4:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        count = self.get_point_count()
        bl += int32_to_byte_list(count)
        for pt in self.points:
            bl += pt.to_byte_list()
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        return self.points == other.points

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    @staticmethod
    def _check_points(points):
        '''Проверка списка точек.'''
        if not isinstance(points, list):
            return False
        if not all(isinstance(pt, PointF) for pt in points):
            return False
        return True


#----------------------------------------------------------------
# Стиль пера
#----------------------------------------------------------------

class PenStype(object):

    NO_PEN = 0
    SOLID_LINE = 1
    DASH_LINE = 2
    DOT_LINE = 3
    DASH_DOT_LINE = 4
    DASH_DOT_DOT_LINE = 5


#----------------------------------------------------------------
# Стиль соединения линий для пера
#----------------------------------------------------------------

class PenJoinStyle(object):

    MITER_JOIN = 0x00
    BEVEL_JOIN = 0x40
    ROUND_JOIN = 0x80


#----------------------------------------------------------------
# Стиль окончания пера
#----------------------------------------------------------------

class PenCapStyle(object):

    FLAT_CAP = 0x00
    SQUARE_CAP = 0x10
    ROUND_CAP = 0x20


#----------------------------------------------------------------
# Перо
#----------------------------------------------------------------

class Pen(object):

    def __init__(self):
        '''Конструктор без параметров'''
        self.color = Color()
        self.width = 1
        self.style = PenStype.SOLID_LINE
        self.join_style = PenJoinStyle.MITER_JOIN
        self.cap_style = PenCapStyle.FLAT_CAP

    def init(self, color, width, style=PenStype.SOLID_LINE, join_style=PenJoinStyle.MITER_JOIN, cap_style=PenCapStyle.FLAT_CAP):
        '''Функция инициализации.'''
        assert isinstance(color, Color)
        assert isinstance(width, int)
        assert width >= 0 and width <= 100
        self.color = color
        self.width = width
        self.style = style
        self.join_style = join_style
        self.cap_style = cap_style

    @staticmethod
    def create(color, width, style=PenStype.SOLID_LINE, join_style=PenJoinStyle.MITER_JOIN, cap_style=PenCapStyle.FLAT_CAP):
        '''Функция создания.'''
        assert isinstance(color, Color)
        assert isinstance(width, int)
        assert width >= 0
        pen = Pen()
        pen.init(color, width, style, join_style, cap_style)
        return pen

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) != 11:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += self.color.to_byte_list()
        bl += int32_to_byte_list(self.width)
        bl += int8_to_byte_list(self.style)
        bl += int8_to_byte_list(self.join_style)
        bl += int8_to_byte_list(self.cap_style)
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        blc = byte_list[:4]
        self.color.from_byte_list(blc)
        blw = byte_list[4:8]
        self.width = byte_list_to_int32(blw)
        sbl = byte_list[8:9]
        self.style = byte_list_to_int8(sbl)
        jsbl = byte_list[9:10]
        self.join_style = byte_list_to_int8(jsbl)
        cpbl = byte_list[10:11]
        self.cap_style = byte_list_to_int8(cpbl)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 11

    def __eq__(self, other):
        '''Оператор ==.'''
        isEqColor = (self.color == other.color)
        isEqWidth = (self.width == other.width)
        isEqStyle = (self.style == other.style)
        isEqJoinStyle = (self.join_style == other.join_style)
        isEqCapStyle = (self.cap_style == other.cap_style)
        return isEqColor and isEqWidth and isEqStyle and isEqJoinStyle and isEqCapStyle

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}, {}, {}, {}, {}'.format(self.color, self.width, self.style, self.join_style, self.cap_style)


#----------------------------------------------------------------
# Стиль кисти
#----------------------------------------------------------------

class BrushStyle(object):

    NO_BRUSH = 0
    SOLID_PATTERN = 1
    DENSE1_PATTERN = 2
    DENSE2_PATTERN = 3
    DENSE3_PATTERN = 4
    DENSE4_PATTERN = 5
    DENSE5_PATTERN = 6
    DENSE6_PATTERN = 7
    DENSE7_PATTERN = 8
    HOR_PATTERN = 9
    VER_PATTERN = 10
    CROSS_PATTERN = 11
    BDIAG_PATTERN = 12
    FDIAG_PATTERN = 13


#----------------------------------------------------------------
# Кисть
#----------------------------------------------------------------

class Brush(object):

    def __init__(self):
        '''Конструктор без параметров'''
        self.color = Color()
        self.style = BrushStyle.SOLID_PATTERN

    def init(self, color):
        '''Функция инициализации.'''
        assert isinstance(color, Color)
        self.color = color
        self.style = BrushStyle.SOLID_PATTERN

    @staticmethod
    def create(color):
        '''Функция создания.'''
        assert isinstance(color, Color)
        brush = Brush()
        brush.init(color)
        return brush

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) != 5:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += self.color.to_byte_list()
        bl += int8_to_byte_list(self.style)
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        cbl = byte_list[:4]
        self.color.from_byte_list(cbl)
        sbl = byte_list[4:]
        self.style = byte_list_to_int8(sbl)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 5

    def __eq__(self, other):
        '''Оператор ==.'''
        return self.color == other.color

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.color)


#----------------------------------------------------------------
# Шрифт
#----------------------------------------------------------------

class Font(object):

    def __init__(self):
        '''Конструктор без параметров'''
        self.family = String.create(u'Arial')
        self.size = 12
        self.is_bold = False

    def init(self, family, size, is_bold=False):
        '''Функция инициализации.'''
        assert isinstance(family, String)
        assert isinstance(size, int)
        self.family = family
        self.size = size
        self.is_bold = is_bold

    @staticmethod
    def create(family, size, is_bold=False):
        '''Функция создания.'''
        assert isinstance(family, String)
        assert isinstance(size, int)
        font = Font()
        font.init(family, size, is_bold)
        return font

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < 10:
            return False
        return True

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        s = len(byte_list)
        fbl = byte_list[:s-5]
        self.family.from_byte_list(fbl)
        sbl = byte_list[s-5:s-5+4]
        self.size = byte_list_to_int32(sbl)
        bbl = byte_list[-1:]
        self.is_bold = byte_list_to_bool(bbl)

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += self.family.to_byte_list()
        bl += int32_to_byte_list(self.size)
        bl += bool_to_byte_list(self.is_bold)
        return bl

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        isEqFamily = (self.family == other.family)
        isEqSize = (self.size == other.size)
        isEqBold = (self.is_bold == other.is_bold)
        return isEqFamily and isEqSize and isEqBold

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}, {}'.format(self.family, self.size)



#----------------------------------------------------------------
# Тестирование класса Color
#----------------------------------------------------------------

class TestColor(unittest.TestCase):

    def test_contructor(self):
        c = Color()
        self.assertEqual(c.red, 0)
        self.assertEqual(c.green, 0)
        self.assertEqual(c.blue, 0)
        self.assertEqual(c.alpha, 255)

    def test_init(self):
        c = Color()
        c.init(200, 200, 200)
        self.assertEqual(c.red, 200)
        self.assertEqual(c.green, 200)
        self.assertEqual(c.blue, 200)
        self.assertEqual(c.alpha, 255)

        c.init(100, 100, 100, 100)
        self.assertEqual(c.red, 100)
        self.assertEqual(c.green, 100)
        self.assertEqual(c.blue, 100)
        self.assertEqual(c.alpha, 100)

    def test_create(self):
        c = Color.create(50, 50, 50)
        self.assertTrue(isinstance(c, Color))
        self.assertEqual(c.red, 50)
        self.assertEqual(c.green, 50)
        self.assertEqual(c.blue, 50)
        self.assertEqual(c.alpha, 255)

        c = Color.create(40, 40, 40, 40)
        self.assertEqual(c.red, 40)
        self.assertEqual(c.green, 40)
        self.assertEqual(c.blue, 40)
        self.assertEqual(c.alpha, 40)

    def test_get_red(self):
        c = Color.get_red()
        c_red = Color.create(255, 0, 0)
        self.assertEqual(c, c_red)

    def test_get_green(self):
        c = Color.get_green()
        c_green = Color.create(0, 128, 0)
        self.assertEqual(c, c_green)

    def test_get_blue(self):
        c = Color.get_blue()
        c_blue = Color.create(0, 0, 255)
        self.assertEqual(c, c_blue)

    def test_get_white(self):
        c = Color.get_white()
        c_white = Color.create(255, 255, 255)
        self.assertEqual(c, c_white) 

    def test_get_black(self):
        c = Color.get_black()
        c_black = Color.create(0, 0, 0)
        self.assertEqual(c, c_black) 

    def test_get_transparent(self):
        c = Color.get_transparent()
        self.assertEqual(c.red, 0)
        self.assertEqual(c.green, 0)
        self.assertEqual(c.blue, 0)
        self.assertEqual(c.alpha, 0)

    def test_from_byte_list(self):
        bl = [0, 0, 0, 255]
        c = Color()
        c.from_byte_list(bl)
        self.assertEqual(c, Color.get_black())

    def test_to_byte_list(self):
        c = Color()
        bl = c.to_byte_list()
        self.assertTrue(c.check_byte_list(bl))

    def test_get_byte_list_len(self):
        c = Color()
        bl = c.to_byte_list()
        self.assertEqual(c.get_byte_list_len(), len(bl))

    def test_equal(self):
        c1 = Color()
        self.assertTrue(c1 == c1)
        c2 = Color.create(200, 200, 200)
        self.assertFalse(c1 == c2)

    def test_not_equal(self):
        c1 = Color()
        self.assertFalse(c1 != c1)


#----------------------------------------------------------------
# Тестирование класса String
#----------------------------------------------------------------

class TestString(unittest.TestCase):

    def test_constructor(self):
        s = String()
        s.s = u'123'

    def test_init(self):
        s = String()
        s.init(u'123')
        self.assertEqual(s.s, u'123')

    def test_create(self):
        s = String.create(u'123')
        self.assertEqual(s.s, u'123')

    def test_to_byte_list(self):
        s = String.create(u'123')
        bl = s.to_byte_list()
        self.assertTrue(s.check_byte_list(bl))

    def test_from_byte_list(self):
        s = String.create(u'123')
        bl = s.to_byte_list()
        s.from_byte_list(bl)
        self.assertEqual(s.s, u'123')

    def test_get_byte_list_len(self):
        s = String()
        bl = s.to_byte_list()
        self.assertEqual(s.get_byte_list_len(), len(bl))

    def test_equal(self):
        s1 = String()
        self.assertTrue(s1 == s1)
        s2 = String.create(u'123')
        self.assertFalse(s1 == s2)

    def test_not_equal(self):
        s1 = String()
        self.assertFalse(s1 != s1)
        s2 = String.create(u'123')
        self.assertTrue(s1 != s2)


#----------------------------------------------------------------
# Тестирование класса Point
#----------------------------------------------------------------

class TestPoint(unittest.TestCase):

    def test_constructor(self):
        pt = Point()
        self.assertEqual(pt.x, 0)
        self.assertEqual(pt.y, 0)

    def test_init(self):
        pt = Point()
        pt.init(100, 100)
        self.assertEqual(pt.x, 100)
        self.assertEqual(pt.y, 100)

    def test_create(self):
        pt = Point.create(50, 50)
        self.assertTrue(isinstance(pt, Point))
        self.assertEqual(pt.x, 50)
        self.assertEqual(pt.y, 50)

    def test_to_byte_list(self):
        pt = Point()
        bl = pt.to_byte_list()
        self.assertTrue(pt.check_byte_list(bl))

    def test_from_byte_list(self):
        bl = generate(8)
        pt = Point()
        pt.from_byte_list(bl)
        self.assertTrue(pt == Point())

    def test_get_byte_list_len(self):
        pt = Point()
        bl = pt.to_byte_list()
        self.assertEqual(pt.get_byte_list_len(), len(bl))

    def test_add(self):
        pt1 = Point.create(200, 200)
        pt2 = Point.create(100, 100)
        self.assertEqual(pt1 + pt2, Point.create(300, 300))

    def test_iadd(self):
        pt1 = Point.create(200, 200)
        pt2 = Point.create(100, 100)
        pt1 += pt2
        self.assertEqual(pt1, Point.create(300, 300))

    def test_sub(self):
        pt1 = Point.create(200, 200)
        pt2 = Point.create(100, 100)
        self.assertEqual(pt1 - pt2, Point.create(100, 100))

    def test_isub(self):
        pt1 = Point.create(200, 200)
        pt2 = Point.create(100, 100)
        pt1 -= pt2
        self.assertEqual(pt1, Point.create(100, 100))

    def test_equal(self):
        pt1 = Point()
        self.assertTrue(pt1 == pt1)
        pt2 = Point.create(100, 100)
        self.assertFalse(pt1 == pt2)

    def test_not_equal(self):
        pt1 = Point()
        self.assertFalse(pt1 != pt1)
        pt2 = Point.create(100, 100)
        self.assertTrue(pt1 != pt2)


#----------------------------------------------------------------
# Тестирование класса PointF
#----------------------------------------------------------------

class TestPointF(unittest.TestCase):

    def test_constructor(self):
        pt = PointF()
        self.assertEqual(pt.x, 0.0)
        self.assertEqual(pt.y, 0.0)

    def test_init(self):
        pt = PointF()
        pt.init(100.0, 100.0)
        self.assertEqual(pt.x, 100.0)
        self.assertEqual(pt.y, 100.0)

    def test_create(self):
        pt = PointF.create(100.0, 100.0)
        self.assertEqual(pt.x, 100.0)
        self.assertEqual(pt.y, 100.0)

    def test_to_byte_list(self):
        pt = PointF()
        bl = pt.to_byte_list()
        self.assertTrue(pt.check_byte_list(bl))

    def test_from_byte_list(self):
        pt = PointF()
        bl = generate(16)
        pt.from_byte_list(bl)
        self.assertEqual(pt, PointF())

    def test_get_byte_list_len(self):
        pt = PointF()
        bl = pt.to_byte_list()
        self.assertEqual(pt.get_byte_list_len(), len(bl))

    def test_add(self):
        pt1 = PointF.create(200.0, 200.0)
        pt2 = PointF.create(100.0, 100.0)
        self.assertEqual(pt1 + pt2, PointF.create(300.0, 300.0))

    def test_iadd(self):
        pt1 = PointF.create(200.0, 200.0)
        pt2 = PointF.create(100.0, 100.0)
        pt1 += pt2
        self.assertEqual(pt1, PointF.create(300.0, 300.0))

    def test_sub(self):
        pt1 = PointF.create(200.0, 200.0)
        pt2 = PointF.create(100.0, 100.0)
        self.assertEqual(pt1 - pt2, PointF.create(100.0, 100.0))

    def test_isub(self):
        pt1 = PointF.create(200.0, 200.0)
        pt2 = PointF.create(100.0, 100.0)
        pt1 -= pt2
        self.assertEqual(pt1, PointF.create(100.0, 100.0))

    def test_equal(self):
        pt1 = PointF()
        self.assertTrue(pt1 == pt1)
        pt2 = PointF.create(100.0, 100.0)
        self.assertFalse(pt1 == pt2)

    def test_not_equal(self):
        pt1 = PointF()
        self.assertFalse(pt1 != pt1)
        pt2 = PointF.create(100.0, 100.0)
        self.assertTrue(pt1 != pt2)


#----------------------------------------------------------------
# Тестирование класса Size
#----------------------------------------------------------------

class TestSize(unittest.TestCase):

    def test_contructor(self):
        size = Size()
        self.assertEqual(size.width, 0)
        self.assertEqual(size.height, 0)

    def test_init(self):
        size = Size()
        size.init(100, 100)
        self.assertEqual(size.width, 100)
        self.assertEqual(size.height, 100)

    def test_create(self):
        size = Size.create(100, 100)
        self.assertEqual(size.width, 100)
        self.assertEqual(size.height, 100)

    def test_is_null(self):
        size = Size()
        self.assertTrue(size.is_null())

    def test_to_byte_list(self):
        size = Size.create(100, 100)
        bl = size.to_byte_list()
        self.assertTrue(size.check_byte_list(bl))

    def from_byte_list(self):
        size = Size.create(100, 100)
        bl = int32_list_to_byte_list([100, 100])
        size.from_byte_list(bl)
        self.assertEqual(size.width, 100)
        self.assertEqual(size.height, 100)

    def test_equal(self):
        size1 = Size()
        self.assertTrue(size1 == size1)
        size2 = Size.create(100, 100)
        self.assertFalse(size1 == size2)
        
    def test_not_equal(self):
        size1 = Size()
        self.assertFalse(size1 != size1)
        size2 = Size.create(100, 100)
        self.assertTrue(size1 != size2)


#----------------------------------------------------------------
# Тестирование класса SizeF
#----------------------------------------------------------------

class TestSizeF(unittest.TestCase):

    def test_contructor(self):
        size = SizeF()
        self.assertTrue(float_equal(size.width, 0.0))
        self.assertTrue(float_equal(size.height, 0.0))

    def test_init(self):
        size = SizeF()
        size.init(100.0, 100.0)
        self.assertTrue(float_equal(size.width, 100.0))
        self.assertTrue(float_equal(size.height, 100.0))        

    def test_create(self):
        size = SizeF.create(100.0, 100.0)
        self.assertTrue(float_equal(size.width, 100.0))
        self.assertTrue(float_equal(size.height, 100.0))

    def test_is_null(self):
        size = Size()
        self.assertTrue(size.is_null())

    def test_to_byte_list(self):
        size = SizeF.create(100.0, 100.0)
        bl = size.to_byte_list()
        self.assertTrue(size.check_byte_list(bl))

    def from_byte_list(self):
        size = SizeF.create(100.0, 100.0)
        bl = double_list_to_byte_list([100.0, 100.0])
        size.from_byte_list(bl)
        self.assertEqual(float_equal(size.width, 100.0))
        self.assertEqual(float_equal(size.height, 100.0))

    def test_get_byte_list_len(self):
        line = Line()
        self.assertEqual(line.get_byte_list_len(), len(line.to_byte_list()))

    def test_equal(self):
        size1 = SizeF()
        self.assertTrue(size1 == size1)
        size2 = SizeF.create(100.0, 100.0)
        self.assertFalse(size1 == size2)

    def test_not_equal(self):
        size1 = SizeF()
        self.assertFalse(size1 != size1)
        size2 = SizeF.create(100.0, 100.0)
        self.assertTrue(size1 != size2)


#----------------------------------------------------------------
# Тестирование класса Line
#----------------------------------------------------------------

class TestLine(unittest.TestCase):

    def test_contructor(self):
        line = Line()
        self.assertEqual(line.pt1, Point())
        self.assertEqual(line.pt2, Point())

    def test_init(self):
        line = Line()
        pt1 = Point()
        pt2 = Point.create(100, 100)
        line.init(pt1, pt2)
        self.assertEqual(line.pt1, pt1)
        self.assertEqual(line.pt2, pt2)

    def test_init2(self):
        line = Line()
        line.init2(10, 10, 100, 100)
        self.assertEqual(line.pt1.x, 10)
        self.assertEqual(line.pt1.y, 10)
        self.assertEqual(line.pt2.x, 100)
        self.assertEqual(line.pt2.y, 100)

    def test_create(self):
        pt1 = Point()
        pt2 = Point.create(100, 100)
        line = Line.create(pt1, pt2)
        self.assertEqual(line.pt1, pt1)
        self.assertEqual(line.pt2, pt2)

    def test_create2(self):
        line = Line.create2(10, 10, 100, 100)
        self.assertEqual(line.pt1.x, 10)
        self.assertEqual(line.pt1.y, 10)
        self.assertEqual(line.pt2.x, 100)
        self.assertEqual(line.pt2.y, 100)

    def test_to_byte_list(self):
        line = Line.create2(10, 10, 100, 100)
        bl = line.to_byte_list()
        self.assertTrue(line.check_byte_list(bl))

    def test_from_byte_list(self):
        bl = generate(16)
        line = Line()
        line.from_byte_list(bl)
        self.assertEqual(line.pt1, Point())
        self.assertEqual(line.pt2, Point())

    def test_get_byte_list_len(self):
        line = Line()
        self.assertEqual(line.get_byte_list_len(), len(line.to_byte_list()))

    def test_equal(self):
        line1 = Line()
        self.assertTrue(line1 == line1)
        line2 = Line.create2(0, 0, 100, 100)
        self.assertFalse(line1 == line2)

    def test_not_equal(self):
        line1 = Line()
        self.assertFalse(line1 != line1)
        line2 = Line.create2(0, 0, 100, 100)
        self.assertTrue(line1 != line2)


#----------------------------------------------------------------
# Тестирование класса LineF
#----------------------------------------------------------------

class TestLineF(unittest.TestCase):

    def test_contructor(self):
        line = LineF()
        self.assertEqual(line.pt1, PointF())
        self.assertEqual(line.pt2, PointF())

    def test_init(self):
        line = LineF()
        pt1 = PointF()
        pt2 = PointF.create(100.0, 100.0)
        line.init(pt1, pt2)
        self.assertEqual(line.pt1, pt1)
        self.assertEqual(line.pt2, pt2)

    def test_init2(self):
        line = LineF()
        x1 = 100.0
        y1 = 100.0
        x2 = 200.0
        y2 = 200.0
        line.init2(x1, y1, x2, y2)
        self.assertTrue(float_equal(line.pt1.x, x1))
        self.assertTrue(float_equal(line.pt1.y, y1))
        self.assertTrue(float_equal(line.pt2.x, x2))
        self.assertTrue(float_equal(line.pt2.y, y2))

    def test_create(self):
        pt1 = PointF()
        pt2 = PointF.create(100.0, 100.0)
        line = LineF.create(pt1, pt2)

    def test_create2(self):
        x1 = 100.0
        y1 = 100.0
        x2 = 200.0
        y2 = 200.0
        line = LineF.create2(x1, y1, x2, y2)
        self.assertTrue(float_equal(line.pt1.x, 100.0))
        self.assertTrue(float_equal(line.pt1.y, 100.0))
        self.assertTrue(float_equal(line.pt2.x, 200.0))
        self.assertTrue(float_equal(line.pt2.y, 200.0))

    def test_get_byte_list_len(self):
        line = LineF()
        self.assertEqual(line.get_byte_list_len(), len(line.to_byte_list()))

    def test_from_byte_list(self):
        line = LineF.create2(100.0, 100.0, 200.0, 200.0)
        bl = line.to_byte_list()
        line.from_byte_list(bl)
        self.assertTrue(float_equal(line.pt1.x, 100.0))
        self.assertTrue(float_equal(line.pt1.y, 100.0))
        self.assertTrue(float_equal(line.pt2.x, 200.0))
        self.assertTrue(float_equal(line.pt2.y, 200.0))

    def test_get_byte_list_len(self):
        line = Line()
        self.assertEqual(line.get_byte_list_len(), len(line.to_byte_list()))

    def test_equal(self):
        line1 = LineF()
        self.assertTrue(line1 == line1)
        line2 = LineF.create2(0.0, 0.0, 100.0, 100.0)
        self.assertFalse(line1 == line2)

    def test_not_equal(self):
        line1 = LineF()
        self.assertFalse(line1 != line1)
        line2 = LineF.create2(0.0, 0.0, 100.0, 100.0)
        self.assertTrue(line1 != line2)


#----------------------------------------------------------------
# Тестирование класса Polyline
#----------------------------------------------------------------

class TestPolyline(unittest.TestCase):

    def test_contructor(self):
        p = Polyline()
        self.assertTrue(p.is_empty())
        self.assertEqual(p.get_point_count(), 0)

    def test_init(self):
        p = Polyline()
        points = [Point().create(100, 100)]
        p.init(points)
        self.assertFalse(p.is_empty())
        self.assertEqual(p.get_point_count(), 1)

    def test_create(self):
        points = [Point().create(100, 100)]
        p = Polyline.create(points)
        self.assertFalse(p.is_empty())
        self.assertEqual(p.points, points)
        self.assertEqual(p.get_point_count(), 1)

    def test_add_point(self):
        pt = Point().create(100, 100)
        p = Polyline()
        p.add_point(pt)
        self.assertFalse(p.is_empty())
        self.assertEqual(p.get_point_count(), 1)

    def test_to_byte_list(self):
        p = Polyline()
        bl = p.to_byte_list()
        self.assertTrue(p.check_byte_list(bl))

    def test_from_byte_list(self):
        pass

    def test_get_byte_list_len(self):
        p = Polyline()
        self.assertEqual(p.get_byte_list_len(), len(p.to_byte_list()))

    def test_equal(self):
        p1 = Polyline()
        self.assertTrue(p1 == p1)
        points = [Point().create(100, 100)]
        p2 = Polyline.create(points)
        self.assertFalse(p1 == p2)

    def test_not_equal(self):
        p1 = Polyline()
        self.assertFalse(p1 != p1)
        points = [Point().create(100, 100)]
        p2 = Polyline.create(points)
        self.assertTrue(p1 != p2)
        

#----------------------------------------------------------------
# Тестирование класса PolylineF
#----------------------------------------------------------------

class TestPolylineF(unittest.TestCase):

    def test_contructor(self):
        p = PolylineF()
        self.assertTrue(p.is_empty())
        self.assertEqual(p.get_point_count(), 0)

    def test_init(self):
        p = PolylineF()
        points = [PointF().create(200.0, 200.0)]
        p.init(points)
        self.assertFalse(p.is_empty())
        self.assertEqual(p.get_point_count(), 1)

    def test_create(self):
        points = [PointF(), PointF().create(200.0, 200.0)]
        p = PolylineF().create(points)
        self.assertFalse(p.is_empty())

    def test_add_point(self):
        pt = PointF().create(100.0, 100.0)
        p = PolylineF()
        p.add_point(pt)
        self.assertFalse(p.is_empty())
        self.assertEqual(p.get_point_count(), 1)

    def test_to_byte_list(self):
        p = PolylineF()
        bl = p.to_byte_list()
        self.assertTrue(p.check_byte_list(bl))

    def test_from_byte_list(self):
        pass

    def test_get_byte_list_len(self):
        p = PolylineF()
        self.assertEqual(p.get_byte_list_len(), len(p.to_byte_list()))

    def test_equal(self):
        p1 = PolylineF()
        self.assertTrue(p1 == p1)
        points = [PointF().create(100.0, 100.0)]
        p2 = PolylineF.create(points)
        self.assertFalse(p1 == p2)

    def test_not_equal(self):
        p1 = PolylineF()
        self.assertFalse(p1 != p1)
        points = [PointF().create(100.0, 100.0)]
        p2 = PolylineF.create(points)
        self.assertTrue(p1 != p2)


#----------------------------------------------------------------
# Тестирование класса Rect
#----------------------------------------------------------------

class TestRect(unittest.TestCase):

    def test_contructor(self):
        rect = Rect()
        self.assertEqual(rect.get_left(), 0)
        self.assertEqual(rect.get_top(), 0)
        self.assertEqual(rect.get_width(), 0)
        self.assertEqual(rect.get_height(), 0)

    def test_init(self):
        rect = Rect()
        lt = Point()
        s = Size.create(100, 100)
        rect.init(lt, s)
        self.assertEqual(rect.get_left(), 0)
        self.assertEqual(rect.get_top(), 0)
        self.assertEqual(rect.get_width(), 100)
        self.assertEqual(rect.get_height(), 100)

    def test_init2(self):
        rect = Rect()
        rect.init2(100, 100, 200, 200)
        self.assertEqual(rect.get_left(), 100)
        self.assertEqual(rect.get_top(), 100)
        self.assertEqual(rect.get_width(), 200)
        self.assertEqual(rect.get_height(), 200)

    def test_create(self):
        leftTop = Point.create(10, 10)
        size = Size.create(100, 100)
        rect = Rect.create(leftTop, size)
        self.assertEqual(rect.leftTop, leftTop)
        self.assertEqual(rect.size, size)

    def test_create2(self):
        rect = Rect.create2(50, 50, 300, 300)
        self.assertEqual(rect.get_left(), 50)
        self.assertEqual(rect.get_top(), 50)
        self.assertEqual(rect.get_width(), 300)
        self.assertEqual(rect.get_height(), 300)

    def test_to_byte_list(self):
        rect = Rect()
        bl = rect.to_byte_list()
        self.assertTrue(rect.check_byte_list(bl))

    def test_from_byte_list(self):
        coords = [100, 100, 200, 200]
        bl = int32_list_to_byte_list(coords)
        rect = Rect()
        rect.from_byte_list(bl)
        self.assertEqual(rect.get_left(), 100)
        self.assertEqual(rect.get_top(), 100)
        self.assertEqual(rect.get_width(), 200)
        self.assertEqual(rect.get_height(), 200)

    def test_get_byte_list_len(self):
        line = Line()
        self.assertEqual(line.get_byte_list_len(), len(line.to_byte_list()))

    def test_equal(self):
        rect1 = Rect()
        self.assertTrue(rect1 == rect1)
        rect2 = Rect.create2(0, 0, 200, 200)
        self.assertFalse(rect1 == rect2)

    def test_not_equal(self):
        rect1 = Rect()
        self.assertFalse(rect1 != rect1)
        rect2 = Rect.create2(100, 100, 200, 200)
        self.assertTrue(rect1 != rect2)


#----------------------------------------------------------------
# Тестирование класса RectF
#----------------------------------------------------------------

class TestRectF(unittest.TestCase):

    def test_constructor(self):
        rect = RectF()
        self.assertEqual(rect.leftTop, PointF())
        self.assertEqual(rect.size, SizeF())

    def test_init(self):
        leftTop = PointF.create(100.0, 100.0)
        size = SizeF.create(200.0, 200.0)
        rect = RectF()
        rect.init(leftTop, size)
        self.assertEqual(rect.leftTop, leftTop)
        self.assertEqual(rect.size, size)

    def test_init2(self):
        rect = RectF()
        rect.init2(100.0, 100.0, 200.0, 200.0)
        self.assertTrue(float_equal(rect.get_left(), 100.0))
        self.assertTrue(float_equal(rect.get_top(), 100.0))
        self.assertTrue(float_equal(rect.get_width(), 200.0))
        self.assertTrue(float_equal(rect.get_height(), 200.0))

    def test_create(self):
        leftTop = PointF.create(100.0, 100.0)
        size = SizeF.create(200.0, 200.0)
        rect = RectF.create(leftTop, size)
        self.assertEqual(rect.leftTop, leftTop)
        self.assertEqual(rect.size, size)

    def test_create2(self):
        rect = RectF.create2(100.0, 100.0, 200.0, 200.0)
        self.assertTrue(float_equal(rect.get_left(), 100.0))
        self.assertTrue(float_equal(rect.get_top(), 100.0))
        self.assertTrue(float_equal(rect.get_width(), 200.0))
        self.assertTrue(float_equal(rect.get_height(), 200.0))

    def test_to_byte_list(self):
        rect = RectF()
        bl = rect.to_byte_list()
        self.assertTrue(rect.check_byte_list(bl))

    def test_from_byte_list(self):
        coords = [100.0, 100.0, 200.0, 200.0]
        bl = double_list_to_byte_list(coords)
        rect = RectF()
        rect.from_byte_list(bl)
        self.assertTrue(float_equal(rect.get_left(), 100.0))
        self.assertTrue(float_equal(rect.get_top(), 100.0))
        self.assertTrue(float_equal(rect.get_width(), 200.0))
        self.assertTrue(float_equal(rect.get_height(), 200.0))

    def test_get_byte_list_len(self):
        line = Line()
        self.assertEqual(line.get_byte_list_len(), len(line.to_byte_list()))

    def test_equal(self):
        rect1 = RectF()
        self.assertTrue(rect1 == rect1)
        rect2 = RectF.create2(100.0, 100.0, 200.0, 200.0)
        self.assertFalse(rect1 == rect2)

    def test_not_equal(self):
        rect1 = RectF()
        self.assertTrue(rect1 == rect1)
        rect2 = RectF.create2(10.0, 10.0, 100.0, 100.0)
        self.assertFalse(rect1 == rect2)


#----------------------------------------------------------------
# Тестирование класса RoundRect
#----------------------------------------------------------------

class TestRoundRect(unittest.TestCase):

    def test_constructor(self):
        rrect = RoundRect()
        self.assertEqual(rrect.rect, Rect())
        self.assertTrue(is_float_null(rrect.radiusX))
        self.assertTrue(is_float_null(rrect.radiusY))

    def test_init(self):
        rrect = RoundRect()
        rect = Rect.create2(0, 0, 100, 100)
        radiusX = 1.0
        radiusY = 1.0
        rrect.init(rect, radiusX, radiusY)
        self.assertEqual(rrect.rect, rect)
        self.assertTrue(float_equal(rrect.radiusX, radiusX))
        self.assertTrue(float_equal(rrect.radiusY, radiusY))

    def test_create(self):
        rect = Rect.create2(0, 0, 100, 100)
        radiusX = 1.0
        radiusY = 1.0
        rrect = RoundRect.create(rect, radiusX, radiusY)
        self.assertEqual(rrect.rect, rect)
        self.assertTrue(float_equal(rrect.radiusX, radiusX))
        self.assertTrue(float_equal(rrect.radiusY, radiusY))

    def test_to_byte_list(self):
        rrect = RoundRect()
        bl = rrect.to_byte_list()
        self.assertTrue(rrect.check_byte_list(bl))

    def test_from_byte_list(self):
        rrect = RoundRect()
        bl = rrect.to_byte_list()
        rrect.from_byte_list(bl)

    def test_get_byte_list_len(self):
        rrect = RoundRect()
        self.assertEqual(rrect.get_byte_list_len(), len(rrect.to_byte_list()))

    def test_equal(self):
        rrect1 = RoundRect()
        self.assertTrue(rrect1 == rrect1)
        rrect2 = RoundRect.create(Rect.create2(0, 0, 100, 100), 10.0, 10.0)
        self.assertFalse(rrect1 == rrect2)

    def test_not_equal(self):
        rect1 = RoundRect()
        self.assertFalse(rect1 != rect1)
        rect2 = RoundRect.create(Rect.create2(0, 0, 100, 100), 10.0, 10.0)
        self.assertTrue(rect1 != rect2)


#----------------------------------------------------------------
# Тестирование класса RoundRectF
#----------------------------------------------------------------

class TestRoundRectF(unittest.TestCase):

    def test_constructor(self):
        rrect = RoundRectF()
        self.assertEqual(rrect.rect, RectF())
        self.assertEqual(rrect.radiusX, 0.0)
        self.assertEqual(rrect.radiusY, 0.0)

    def test_init(self):
        rrect = RoundRectF()
        rect = RectF()
        radiusX = 0.0
        radiusY = 0.0
        rrect.init(rect, radiusX, radiusY)
        self.assertEqual(rrect.rect, rect)
        self.assertEqual(rrect.radiusX, radiusX)
        self.assertEqual(rrect.radiusY, radiusY)

    def test_create(self):
        rect = RectF.create2(0.0, 0.0, 100.0, 100.0)
        radiusX = 1.0
        radiusY = 1.0
        rrect = RoundRectF.create(rect, radiusX, radiusY)
        self.assertEqual(rrect.rect, rect)
        self.assertEqual(rrect.radiusX, radiusX)
        self.assertEqual(rrect.radiusY, radiusY)

    def test_to_byte_list(self):
        rrect = RoundRectF()
        bl = rrect.to_byte_list()
        self.assertTrue(rrect.check_byte_list(bl))

    def test_from_byte_list(self):
        rect = RectF.create2(100.0, 100.0, 200.0, 200.0)
        radiusX = 1.0
        radiusY = 1.0
        bl = rect.to_byte_list() + double_to_byte_list(radiusX) + double_to_byte_list(radiusY)
        rrect = RoundRectF()
        rrect.from_byte_list(bl)

    def test_get_byte_list_len(self):
        rrect = RoundRectF()

    def test_equal(self):
        rect1 = RoundRectF()
        self.assertTrue(rect1 == rect1)
        rect2 = RoundRectF.create(RectF.create2(0.0, 0.0, 100.0, 100.0), 10.0, 10.0)
        self.assertFalse(rect1 == rect2)

    def test_not_equal(self):
        rect1 = RoundRectF()
        self.assertFalse(rect1 != rect1)
        rect2 = RoundRectF.create(RectF.create2(0.0, 0.0, 100.0, 100.0), 10.0, 10.0)
        self.assertTrue(rect1 != rect2)


#----------------------------------------------------------------
# Тестирование класса Pen
#----------------------------------------------------------------

class TestPen(unittest.TestCase):

    def test_constructor(self):
        pen = Pen()
        self.assertEqual(pen.color, Color())
        self.assertTrue(pen.width == 1)

    def test_init(self):
        pen = Pen()
        pen.init(Color.get_red(), 2)
        self.assertEqual(pen.color, Color.get_red())
        self.assertTrue(pen.width == 2)

    def test_create(self):
        pen = Pen.create(Color.get_red(), 2)
        self.assertEqual(pen.color, Color.get_red())
        self.assertTrue(pen.width == 2)

    def test_to_byte_list(self):
        pen = Pen()
        bl = pen.to_byte_list()
        self.assertTrue(pen.check_byte_list(bl))

    def test_from_byte_list(self):
        pen = Pen()
        c = Color.get_blue()
        w = 3
        cbl = c.to_byte_list()
        wbl = int32_to_byte_list(w)
        sbl = int8_to_byte_list(PenStype.SOLID_LINE)
        jsbl = int8_to_byte_list(PenJoinStyle.MITER_JOIN)
        bl = cbl + wbl + sbl + jsbl + [0]
        pen.from_byte_list(bl)
        self.assertEqual(pen.color, c)
        self.assertEqual(pen.width, w)

    def test_get_byte_list_len(self):
        line = Line()
        self.assertEqual(line.get_byte_list_len(), len(line.to_byte_list()))

    def test_equal(self):
        pen1 = Pen()
        self.assertTrue(pen1 == pen1)
        pen2 = Pen.create(Color.get_red(), 2)
        self.assertFalse(pen1 == pen2)

    def test_not_equal(self):
        pen1 = Pen()
        self.assertFalse(pen1 != pen1)
        pen2 = Pen.create(Color.get_red(), 2)
        self.assertTrue(pen1 != pen2)


#----------------------------------------------------------------
# Тестирование класса Brush
#----------------------------------------------------------------

class TestBrush(unittest.TestCase):

    def test_constructor(self):
        brush = Brush()
        self.assertEqual(brush.color, Color())

    def test_init(self):
        brush = Brush()
        brush.init(Color.get_green())
        self.assertEqual(brush.color, Color.get_green())

    def test_create(self):
        brush = Brush.create(Color.get_green())
        self.assertEqual(brush.color, Color.get_green())

    def test_to_byte_list(self):
        brush = Brush()
        bl = brush.to_byte_list()
        self.assertTrue(brush.check_byte_list(bl))

    def test_from_byte_list(self):
        c = Color.get_gold()
        brush = Brush.create(c)
        cbl = c.to_byte_list()
        self.assertEqual(brush.color, c)

    def test_get_byte_list_len(self):
        brush = Brush()
        self.assertEqual(brush.get_byte_list_len(), len(brush.to_byte_list()))

    def test_equal(self):
        brush1 = Brush()
        self.assertTrue(brush1 == brush1)
        brush2 = Brush.create(Color.get_blue())
        self.assertFalse(brush1 == brush2)

    def test_not_equal(self):
        brush1 = Brush()
        self.assertFalse(brush1 != brush1)
        brush2 = Brush.create(Color.get_blue())
        self.assertTrue(brush1 != brush2)


#----------------------------------------------------------------
# Тестирование класса Font
#----------------------------------------------------------------

class TestFont(unittest.TestCase):

    def test_constructor(self):
        font = Font()
        self.assertEqual(font.family, String.create(u'Arial'))
        self.assertEqual(font.size, 12)
        self.assertEqual(font.is_bold, False)

    def test_init(self):
        family = String.create(u'Courier New')
        size = 14
        is_bold = True
        font = Font()
        font.init(family, size, is_bold)
        self.assertEqual(font.family, family)
        self.assertEqual(font.size, size)
        self.assertEqual(font.is_bold, is_bold)

    def test_create(self):
        family = String.create(u'Courier New')
        size = 16
        is_bold = True
        font = Font.create(family, size, is_bold)
        self.assertEqual(font.family, family)
        self.assertEqual(font.size, size)
        self.assertEqual(font.is_bold, is_bold)

    def test_to_byte_list(self):
        font = Font()
        bl = font.to_byte_list()
        self.assertTrue(font.check_byte_list(bl))

    def test_from_byte_list(self):
        font = Font()
        family = String.create(u'Courier New')
        size = 16
        is_bold = True
        bl = []
        bl += family.to_byte_list()
        bl += int32_to_byte_list(size)
        bl += bool_to_byte_list(is_bold)
        font.from_byte_list(bl)
        self.assertEqual(font.family, family)
        self.assertEqual(font.size, size)
        self.assertEqual(font.is_bold, is_bold)

    def test_get_byte_list_len(self):
        line = Line()
        self.assertEqual(line.get_byte_list_len(), len(line.to_byte_list()))

    def test_equal(self):
        font1 = Font()
        self.assertTrue(font1 == font1)
        family = String.create(u'Courier New')
        size = 14
        is_bold = True
        font2 = Font.create(family, size, is_bold)
        self.assertFalse(font1 == font2)

    def test_not_equal(self):
        font1 = Font()
        self.assertFalse(font1 != font1)
        family = String.create(u'Courier New')
        size = 14
        is_bold = True
        font2 = Font.create(family, size, is_bold)
        self.assertTrue(font1 != font2)


#----------------------------------------------------------------
# Вызывается при загрузке модуля главным
#----------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
