# coding: utf8
"""
ByteMachine
Классы для графического вывода.
"""
from __future__ import annotations
# from enum import Enum
import math
import unittest
import byte_machine_helper_3 as bmh
import byte_machine_convert_3 as bmc


class Color(object):
    """Цвет."""

    def __init__(self):
        """Конструктор без параметров."""
        self.red = 0
        self.green = 0
        self.blue = 0
        self.alpha = 255

    def init(self, red: int, green: int, blue: int, alpha: int = 255) -> None:
        """Функция инициализации."""
        assert isinstance(red, int)
        assert 0 <= red <= 255
        assert isinstance(green, int)
        assert 0 <= green <= 255
        assert isinstance(blue, int)
        assert 0 <= blue <= 255
        assert isinstance(alpha, int)
        assert 0 <= alpha <= 255
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    @staticmethod
    def create(red: int, green: int, blue: int, alpha: int = 255) -> Color:
        """Функция создания с параметрами."""
        assert isinstance(red, int)
        assert 0 <= red <= 255
        assert isinstance(green, int)
        assert 0 <= green <= 255
        assert isinstance(blue, int)
        assert 0 <= blue <= 255
        assert isinstance(alpha, int)
        assert 0 <= alpha <= 255
        c = Color()
        c.init(red, green, blue, alpha)
        return c

    # Основные цвета.
    @staticmethod
    def get_black() -> Color:
        """Получение черного цвета."""
        return Color.create(0, 0, 0)

    @staticmethod
    def get_white() -> Color:
        """Получение белого цвета."""
        return Color.create(255, 255, 255)

    @staticmethod
    def get_red() -> Color:
        """Получение красного цвета."""
        return Color.create(255, 0, 0)

    @staticmethod
    def get_green() -> Color:
        """Получение зеленого цвета."""
        return Color.create(0, 128, 0)

    @staticmethod
    def get_blue() -> Color:
        """Получение синего цвета."""
        return Color.create(0, 0, 255)

    @staticmethod
    def get_gray() -> Color:
        """Получение серого цвета."""
        return Color.create(128, 128, 128)

    @staticmethod
    def get_yellow() -> Color:
        """Получение желтого цвета."""
        return Color.create(255, 255, 0)

    @staticmethod
    def get_transparent() -> Color:
        """Получение прозрачного цвета."""
        return Color.create(0, 0, 0, 0)

    # Красные тона.
    @staticmethod
    def get_indian_red() -> Color:
        """Получение цвета indian_red."""
        return Color.create(205, 92, 92)

    @staticmethod
    def get_light_coral() -> Color:
        """Получение цвета light_coral."""
        return Color.create(240, 128, 128)

    @staticmethod
    def get_dark_salmon() -> Color:
        """Получение цвета dark_salmon."""
        return Color.create(233, 150, 122)

    @staticmethod
    def get_light_salmon() -> Color:
        """Получение цвета light_salmon."""
        return Color.create(255, 160, 122)

    @staticmethod
    def get_crimson() -> Color:
        """Получение малинового цвета."""
        return Color.create(220, 20, 60)

    @staticmethod
    def get_fire_brick() -> Color:
        """Получение кирпичного цвета."""
        return Color.create(178, 34, 34)

    @staticmethod
    def get_dark_red() -> Color:
        """Получение тёмно-красного цвета."""
        return Color.create(139, 0, 0)

    # Розовые тона.
    @staticmethod
    def get_pink() -> Color:
        """Получение розового цвета."""
        return Color.create(255, 192, 203)

    @staticmethod
    def get_light_pink() -> Color:
        """Получение светло-розового цвета."""
        return Color.create(255, 182, 193)

    @staticmethod
    def get_hot_pink() -> Color:
        """Получение цвета HotPink."""
        return Color.create(255, 105, 180)

    @staticmethod
    def get_deep_pink() -> Color:
        """Получение цвета DeepPink."""
        return Color.create(255, 20, 147)

    @staticmethod
    def get_medium_violet_red() -> Color:
        """Получение цвета MediumVioletRed."""
        return Color.create(199, 21, 133)

    @staticmethod
    def get_pale_violet_red() -> Color:
        """Получение цвета PaleVioletRed."""
        return Color.create(219, 112, 147)

    # Оранжевые тона.
    @staticmethod
    def get_coral() -> Color:
        """Получение кораллового цвета."""
        return Color.create(255, 127, 80)

    @staticmethod
    def get_tomato() -> Color:
        """Получение томатного цвета."""
        return Color.create(255, 99, 71)

    @staticmethod
    def get_orange_red() -> Color:
        """Получение красно-оранжевого цвета."""
        return Color.create(255, 69, 0)

    @staticmethod
    def get_dark_orange() -> Color:
        """Получение темно-оранжевого цвета."""
        return Color.create(255, 140, 0)

    @staticmethod
    def get_orange() -> Color:
        """Получение оранжевого цвета."""
        return Color.create(255, 165, 0)

    # Желтые тона
    @staticmethod
    def get_gold() -> Color:
        """Получение золотого цвета."""
        return Color.create(255, 215, 0)

    @staticmethod
    def get_light_yellow() -> Color:
        """Получение светло-желтого цвета."""
        return Color.create(255, 255, 224)

    @staticmethod
    def get_lemon_chiffon() -> Color:
        """Получение цвета LemonChiffon."""
        return Color.create(255, 250, 205)

    @staticmethod
    def get_light_goldenrod_yellow() -> Color:
        """Получение цвета LightGoldenrodYellow."""
        return Color.create(250, 250, 210)

    @staticmethod
    def get_papaya_whip() -> Color:
        """Получение цвета PapayaWhip."""
        return Color.create(255, 239, 213)

    @staticmethod
    def get_moccasin() -> Color:
        """Получение цвета Moccasin."""
        return Color.create(255, 228, 181)

    @staticmethod
    def get_peach_puff() -> Color:
        """Получение цвета PeachPuff."""
        return Color.create(255, 218, 185)

    @staticmethod
    def get_pale_goldenrod() -> Color:
        """Получение цвета PaleGoldenrod."""
        return Color.create(238, 232, 170)

    @staticmethod
    def get_khaki() -> Color:
        """Получение цвета хаки."""
        return Color.create(240, 230, 140)

    @staticmethod
    def get_dark_khaki() -> Color:
        """Получение цвета темный хаки."""
        return Color.create(189, 183, 107)

    @staticmethod
    def get_navy() -> Color:
        """Получение цвета Navy."""
        return Color.create(0, 0, 128)

    @staticmethod
    def get_lime() -> Color:
        """Получение цвета Lime."""
        return Color.create(0, 255, 0)

    @staticmethod
    def get_teal() -> Color:
        """Получение цвета Teal."""
        return Color.create(0, 128, 128)

    @staticmethod
    def get_aqua() -> Color:
        """Получение цвета Aqua."""
        return Color.create(0, 255, 255)

    @staticmethod
    def get_olive() -> Color:
        """Получение цвета Olive."""
        return Color.create(128, 128, 0)

    @staticmethod
    def get_maroon() -> Color:
        """Получение цвета Maroon."""
        return Color.create(128, 0, 0)

    @staticmethod
    def get_purple() -> Color:
        """Получение пурпурного цвета."""
        return Color.create(128, 0, 128)

    @staticmethod
    def get_magenta() -> Color:
        """Получение цвета Маджента."""
        return Color.create(255, 0, 255)

    @staticmethod
    def get_silver() -> Color:
        """Получение цвета Silver."""
        return Color.create(192, 192, 192)

    @staticmethod
    def get_light_gray() -> Color:
        """Получение цвета LightGray."""
        return Color.create(211, 211, 211)

    @staticmethod
    def get_dark_gray() -> Color:
        """Получение цвета DarkGray."""
        return Color.create(169, 169, 169)

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        return len(byte_array) == self.get_byte_array_len()

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        return bytearray([self.red, self.green, self.blue, self.alpha])

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        self.init(byte_array[0], byte_array[1], byte_array[2], byte_array[3])

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 4

    def __eq__(self, other: Color) -> bool:
        """Проверка на равенство."""
        assert isinstance(other, Color)
        isEqRed = (self.red == other.red)
        isEqGreen = (self.green == other.green)
        isEqBlue = (self.blue == other.blue)
        isEqAlpha = (self.alpha == other.alpha)
        return isEqRed and isEqGreen and isEqBlue and isEqAlpha

    def __ne__(self, other: Color) -> bool:
        """Функция проверки на неравенство."""
        assert isinstance(other, Color)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return '{}, {}, {}, {}'.format(self.red, self.green,
                                       self.blue, self.alpha)


class String(object):
    """Строка."""

    def __init__(self):
        """Конструктор без параметров."""
        self.s = ''

    def init(self, s: str) -> None:
        """Функция инициализации."""
        assert isinstance(s, str)
        self.s = s

    @staticmethod
    def create(s: str) -> String:
        """Функция создания."""
        assert isinstance(s, str)
        st = String()
        st.init(s)
        return st

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        return len(byte_array) >= 4

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        sbl = bmc.str_to_byte_array(self.s)
        ba += bmc.int32_to_byte_array(len(sbl))
        ba += sbl
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        basz = byte_array[:4]
        sz = bmc.byte_array_to_int32(basz)
        assert sz == len(byte_array) - 4
        self.s = bmc.byte_array_to_str(byte_array[4:])

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: String) -> bool:
        """Оператор ==."""
        assert isinstance(other, String)
        return self.s == other.s

    def __ne__(self, other: String) -> bool:
        """Оператор !=."""
        assert isinstance(other, String)
        return not self == other

    def __lt__(self, other: String) -> bool:
        """Оператор <."""
        assert isinstance(other, String)
        return self.s < other.s

    def __le__(self, other: String) -> bool:
        """Оператор <=."""
        assert isinstance(other, String)
        return self.s <= other.s

    def __gt__(self, other: String) -> bool:
        """Оператор >."""
        assert isinstance(other, String)
        return self.s > other.s

    def __ge__(self, other: String) -> bool:
        """Оператор >=."""
        assert isinstance(other, String)
        return self.s >= other.s

    def __str__(self) -> str:
        """Получение строкового представления."""
        return self.s


class Point(object):
    """Точка с целочисленными координатами."""

    def __init__(self):
        """Конструктор без параметров."""
        self.x = 0
        self.y = 0

    def init(self, x: int, y: int) -> None:
        """Функция инициализации."""
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.x = x
        self.y = y

    @staticmethod
    def create(x: int, y: int) -> Point:
        """Функция создания с параметрами."""
        assert isinstance(x, int)
        assert isinstance(y, int)
        pt = Point()
        pt.init(x, y)
        return pt

    def is_null(self) -> bool:
        """Проверка координат на равенство 0."""
        return self.x == 0 and self.y == 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        return len(byte_array) == self.get_byte_array_len()

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        xbl = bmc.int32_to_byte_array(self.x)
        ybl = bmc.int32_to_byte_array(self.y)
        return bytearray(xbl + ybl)

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        vl = bmc.byte_array_to_int32_list(byte_array)
        self.init(vl[0], vl[1])

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 8

    def manhattan_len(self) -> int:
        """Манхэттенское расстояние."""
        return (int)(math.sqrt(self.x * self.x + self.y * self.y))

    def __add__(self, other: Point) -> Point:
        """Бинарный оператор +."""
        assert isinstance(other, Point)
        return Point.create(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: Point) -> Point:
        """Оператор +=."""
        assert isinstance(other, Point)
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: Point) -> Point:
        """Бинарный оператор -."""
        assert isinstance(other, Point)
        return Point.create(self.x - other.x, self.y - other.y)

    def __isub__(self, other: Point) -> Point:
        """Оператор -=."""
        assert isinstance(other, Point)
        self.x -= other.x
        self.y -= other.y
        return self

    def __neg__(self) -> Point:
        """Унарный оператор -."""
        return Point.create(-self.x, -self.y)

    def __eq__(self, other: Point) -> bool:
        """Оператор ==."""
        assert isinstance(other, Point)
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Point) -> bool:
        """Оператор !=."""
        assert isinstance(other, Point)
        return not (self == other)

    def __str__(self) -> str:
        """Получение строкового представления цвета."""
        return '{}, {}'.format(self.x, self.y)


class PointF(object):
    """Точка с дробными координатами."""

    def __init__(self):
        """Конструктор без параметров."""
        self.x = 0.0
        self.y = 0.0

    def init(self, x: float, y: float) -> None:
        """Функция инициализации."""
        assert isinstance(x, float)
        assert isinstance(y, float)
        self.x = x
        self.y = y

    @staticmethod
    def create(x: float, y: float) -> PointF:
        """Функция создания с параметрами."""
        assert isinstance(x, float)
        assert isinstance(y, float)
        pt = PointF()
        pt.init(x, y)
        return pt

    def is_null(self) -> bool:
        """Проверка координат на равенство 0."""
        return bmh.is_float_null(self.x) and bmh.is_float_null(self.y)

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        return len(byte_array) == self.get_byte_array_len()

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        xba = bmc.double_to_byte_array(self.x)
        yba = bmc.double_to_byte_array(self.y)
        return xba + yba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        vl = bmc.byte_array_to_double_list(byte_array)
        self.init(vl[0], vl[1])

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 16

    def manhattan_len(self) -> float:
        """Получение манхэттенского расстояния."""
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __add__(self, other: PointF) -> PointF:
        """Бинарный оператор +."""
        assert isinstance(other, PointF)
        return PointF.create(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: PointF) -> PointF:
        """Оператор +=."""
        assert isinstance(other, PointF)
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: PointF) -> PointF:
        """Бинарный оператор -."""
        assert isinstance(other, PointF)
        return PointF.create(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        """Оператор -=."""
        assert isinstance(other, PointF)
        self.x -= other.x
        self.y -= other.y
        return self

    def __neg__(self) -> PointF:
        """Унарный оператор -."""
        return Point.create(-self.x, -self.y)

    def __eq__(self, other: PointF) -> bool:
        """Оператор ==."""
        assert isinstance(other, PointF)
        isEqX = bmh.float_equal(self.x, other.x)
        isEqY = bmh.float_equal(self.y, other.y)
        return isEqX and isEqY

    def __ne__(self, other) -> bool:
        """Оператор !=."""
        assert isinstance(other, PointF)
        return not (self == other)

    def __str__(self) -> str:
        """Получение строкового представления."""
        return '{}, {}'.format(self.x, self.y)


class Size(object):
    """Размер с целочисленными координатами."""

    def __init__(self):
        """Конструктор без параметров."""
        self.width = 0
        self.height = 0

    def init(self, width: int, height: int) -> None:
        """Функция инициализации."""
        assert isinstance(width, int)
        assert isinstance(height, int)
        self.width = width
        self.height = height

    @staticmethod
    def create(width: int, height: int) -> Size:
        """Функция создания."""
        assert isinstance(width, int)
        assert isinstance(height, int)
        size = Size()
        size.init(width, height)
        return size

    def is_null(self):
        """Проверка ширины и высоты на 0."""
        return self.width == 0 and self.height == 0

    def is_valid(self):
        """Является ли размер валидным."""
        return self.width >= 0 and self.height >= 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        return len(byte_array) == self.get_byte_array_len()

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        bl = bmc.byte_array_to_int32_list(byte_array)
        self.width = bl[0]
        self.height = bl[1]

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        wbl = bmc.int32_to_byte_array(self.width)
        hbl = bmc.int32_to_byte_array(self.height)
        return wbl + hbl

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 8

    def __eq__(self, other: Size) -> bool:
        """Оператор ==."""
        assert isinstance(other, Size)
        isEqWidth = (self.width == other.width)
        isEqHeight = (self.height == other.height)
        return isEqWidth and isEqHeight

    def __ne__(self, other: Size) -> bool:
        """Оператор !=."""
        assert isinstance(other, Size)
        return not (self == other)

    def __mul__(self, other: Size) -> Size:
        """Оператор *."""
        assert isinstance(other, float)
        width = (int)(self.width * other)
        height = (int)(self.height * other)
        Size.init(width, height)
        return self

    def __imul__(self, other: Size) -> Size:
        """Оператор *=."""
        assert isinstance(other, float)
        self.width = (int)(self.width * other)
        self.height = (int)(self.height * other)
        return self

    def __str__(self) -> str:
        """Получение строкового представления."""
        return '{}, {}'.format(self.width, self.height)


class SizeF(object):
    """Размер с дробными координатами."""

    def __init__(self):
        """Конструктор без параметров."""
        self.width = 0.0
        self.height = 0.0

    def init(self, width: float, height: float) -> None:
        """Функция инициализации."""
        assert isinstance(width, float)
        assert isinstance(height, float)
        self.width = width
        self.height = height

    @staticmethod
    def create(width: float, height: float) -> SizeF:
        """Функция создания."""
        assert isinstance(width, float)
        assert isinstance(height, float)
        size = SizeF()
        size.init(width, height)
        return size

    def is_null(self) -> bool:
        """Проверка ширины и высоты на 0."""
        return bmh.is_float_null(self.width) and bmh.is_float_null(self.height)

    def is_valid(self) -> bool:
        """Является ли размер валидным."""
        return self.width >= 0 and self.height >= 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        return len(byte_array) == self.get_byte_array_len()

    def from_byte_list(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        self.width = bmc.byte_array_to_double(byte_array[:8])
        self.height = bmc.byte_array_to_double(byte_array[8:])

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        baw = bmc.double_to_byte_array(self.width)
        bah = bmc.double_to_byte_array(self.height)
        return baw + bah

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 16

    def __eq__(self, other) -> bool:
        """Оператор ==."""
        assert isinstance(other, SizeF)
        isEqWidth = bmh.float_equal(self.width, other.width)
        isEqHeight = bmh.float_equal(self.height, other.height)
        return isEqWidth and isEqHeight

    def __ne__(self, other) -> bool:
        """Оператор !=."""
        assert isinstance(other, SizeF)
        return not (self == other)

    def __mul__(self, other: float) -> SizeF:
        """Оператор *."""
        assert isinstance(other, float)
        return SizeF.create(self.width * other, self.height * other)

    def __imul__(self, other: float) -> SizeF:
        """Оператор *=."""
        assert isinstance(other, float)
        self.width *= other
        self.height *= other
        return self

    def __str__(self):
        """Получение строкового представления."""
        return '{}, {}'.format(self.width, self.height)


class Line(object):
    """Линия с целочисленными координатами."""

    def __init__(self):
        """Конструктор без параметров."""
        self.pt1 = Point()
        self.pt2 = Point()

    def init(self, pt1, pt2):
        """Функция инициализации."""
        assert isinstance(pt1, Point)
        assert isinstance(pt2, Point)
        self.pt1 = pt1
        self.pt2 = pt2

    def init2(self, x1, y1, x2, y2):
        """Функция инициализации."""
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
        """Функция инициализации 2."""
        assert isinstance(pt1, Point)
        assert isinstance(pt2, Point)
        line = Line()
        line.pt1 = pt1
        line.pt2 = pt2
        return line

    @staticmethod
    def create2(x1, y1, x2, y2):
        """Функция инициализации 2."""
        assert isinstance(x1, int)
        assert isinstance(y1, int)
        assert isinstance(x2, int)
        assert isinstance(y2, int)
        line = Line()
        line.pt1 = Point.create(x1, y1)
        line.pt2 = Point.create(x2, y2)
        return line

    def is_empty(self):
        """Проверка на линию нулевой длины."""
        return self.pt1 == self.pt2

    def check_byte_array(self, byte_list):
        """Проверка корректности списка байтов для инициализации."""
        return len(byte_list) == self.get_byte_array_len()

    def to_byte_array(self):
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += self.pt1.to_byte_array()
        ba += self.pt2.to_byte_array()
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        ba_pt1 = byte_array[:8]
        self.pt1.from_byte_array(ba_pt1)
        ba_pt2 = byte_array[8:]
        self.pt2.from_byte_array(ba_pt2)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 16

    def __eq__(self, other: Line) -> bool:
        """Оператор ==."""
        assert isinstance(other, Line)
        isEqPt1 = (self.pt1 == other.pt1)
        isEqPt2 = (self.pt2 == other.pt2)
        return isEqPt1 and isEqPt2

    def __ne__(self, other: Line) -> bool:
        """Оператор !=."""
        assert isinstance(other, Line)
        return not (self == other)

    def __str__(self) -> str:
        """Получение строкового представления объекта."""
        return '{}, {}'.format(self.pt1, self.pt2)


class LineF(object):
    """Линия с дробными координатами."""

    def __init__(self):
        """Конструктор без параметров."""
        self.pt1 = PointF()
        self.pt2 = PointF()

    def init(self, pt1: PointF, pt2: PointF) -> None:
        """Функция инициализации."""
        assert isinstance(pt1, PointF)
        assert isinstance(pt2, PointF)
        self.pt1 = pt1
        self.pt2 = pt2

    def init2(self, x1: float, y1: float, x2: float, y2: float) -> None:
        """Функция инициализации."""
        assert isinstance(x1, float)
        assert isinstance(y1, float)
        assert isinstance(x2, float)
        assert isinstance(y2, float)
        self.pt1 = PointF.create(x1, y1)
        self.pt2 = PointF.create(x2, y2)

    @staticmethod
    def create(pt1: PointF, pt2: PointF) -> LineF:
        """Функция инициализации 2."""
        assert isinstance(pt1, PointF)
        assert isinstance(pt2, PointF)
        line = LineF()
        line.pt1 = pt1
        line.pt2 = pt2
        return line

    @staticmethod
    def create2(x1: float, y1: float, x2: float, y2: float) -> LineF:
        """Функция инициализации 2."""
        assert isinstance(x1, float)
        assert isinstance(y1, float)
        assert isinstance(x2, float)
        assert isinstance(y2, float)
        line = LineF()
        line.pt1 = PointF.create(x1, y1)
        line.pt2 = PointF.create(x2, y2)
        return line

    def is_empty(self) -> bool:
        """Проверка на линию нулевой длины."""
        return self.pt1 == self.pt2

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        return len(byte_array) == self.get_byte_array_len()

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        bl = bytearray()
        bl += self.pt1.to_byte_array()
        bl += self.pt2.to_byte_array()
        return bl

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        bl_pt1 = byte_array[:16]
        self.pt1.from_byte_array(bl_pt1)
        bl_pt2 = byte_array[16:]
        self.pt2.from_byte_array(bl_pt2)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 32

    def __eq__(self, other: PointF) -> bool:
        """Оператор ==."""
        assert isinstance(other, LineF)
        isEqPt1 = (self.pt1 == other.pt1)
        isEqPt2 = (self.pt2 == other.pt2)
        return isEqPt1 and isEqPt2

    def __ne__(self, other: PointF) -> bool:
        """Оператор !=."""
        assert isinstance(other, LineF)
        return not (self == other)

    def __str__(self) -> str:
        """Получение строкового представления объекта."""
        return '{}, {}'.format(self.pt1, self.pt2)


class Polyline(object):
    """Ломаная линия с целыми координатами."""

    def __init__(self):
        """Конструктор без параметров."""
        self.points = []

    def init(self, points: list) -> None:
        """Функция инициализации."""
        assert Polyline._check_points(points)
        self.points = points

    @staticmethod
    def create(points: list) -> Polyline:
        """Функция создания."""
        assert Polyline._check_points(points)
        p = Polyline()
        p.init(points)
        return p

    def add_point(self, point: Point) -> None:
        """Добавление точки."""
        assert isinstance(point, Point)
        self.points.append(point)

    def get_point_count(self) -> int:
        """Получение количества точек."""
        return len(self.points)

    def is_empty(self) -> bool:
        """Проверка на отсутствие точек."""
        return len(self.points) == 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов."""
        return len(byte_array) >= 4

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmc.int32_to_byte_array(self.get_point_count())
        for pt in self.points:
            ba += pt.to_byte_array()
        return ba

    def from_byte_array(self, byte_array):
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        bac = byte_array[:4]
        count = bmc.byte_array_to_int32(bac)
        self.points = []
        for i in range(count):
            p = Point()
            bi = 4 + i * 8
            ei = bi + 8
            bap = byte_array[bi:ei]
            p.from_byte_list(bap)
            self.add_point(p)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: Polyline) -> bool:
        """Оператор ==."""
        assert isinstance(other, Polyline)
        return self.points == other.points

    def __ne__(self, other: Polyline) -> bool:
        """Оператор ==."""
        assert isinstance(other, Polyline)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления объекта."""
        return '{}'.format(self.points)

    @staticmethod
    def _check_points(points: list) -> bool:
        """Проверка списка точек."""
        if not isinstance(points, list):
            return False
        if not all(isinstance(pt, Point) for pt in points):
            return False
        return True


class PolylineF(object):
    """Ломаная линия с дробными координатами."""

    def __init__(self):
        """Конструктор без параметров."""
        self.points = []

    def init(self, points: list) -> None:
        """Функция инициализации."""
        assert PolylineF._check_points(points)
        self.points = points

    @staticmethod
    def create(points: list) -> PolylineF:
        """Функция создания."""
        assert PolylineF._check_points(points)
        p = PolylineF()
        p.init(points)
        return p

    def add_point(self, point: list) -> None:
        """Добавление точки."""
        assert isinstance(point, PointF)
        self.points.append(point)

    def get_point_count(self) -> int:
        """Получение количества точек."""
        return len(self.points)

    def is_empty(self):
        """Проверка на отсутствие точек."""
        return self.get_point_count() == 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов."""
        return len(byte_array) >= 4

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        count = self.get_point_count()
        ba += bmc.int32_to_byte_array(count)
        for pt in self.points:
            ba += pt.to_byte_array()
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_list(byte_array)
        basz = byte_array[:4]
        sz = bmc.byte_list_to_int32(basz)
        self.points = []
        for i in range(sz):
            pt = PointF()
            bi = 4 + i * 16
            ei = bi + 16
            bapt = byte_array[bi:ei]
            pt.from_byte_list(bapt)
            self.add_point(pt)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: PolylineF) -> bool:
        """Оператор ==."""
        assert isinstance(other, PolylineF)
        return self.points == other.points

    def __ne__(self, other: PolylineF) -> bool:
        """Оператор ==."""
        assert isinstance(other, PolylineF)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления объекта."""
        return '{}'.format(self.points)

    @staticmethod
    def _check_points(points: list) -> bool:
        """Проверка списка точек."""
        if not isinstance(points, list):
            return False
        if not all(isinstance(pt, PointF) for pt in points):
            return False
        return True


class Rect(object):
    """Прямоугольник с целочисленными координатами."""

    def __init__(self):
        """Конструктор без параметров."""
        self.leftTop = Point()
        self.size = Size()

    def init(self, leftTop: Point, size: Size) -> None:
        """Функция инициализации."""
        assert isinstance(leftTop, Point)
        assert isinstance(size, Size)
        self.leftTop = leftTop
        self.size = size

    def init2(self, left: int, top: int, width: int, height: int) -> None:
        """Функция инициализации 2."""
        assert isinstance(left, int)
        assert isinstance(top, int)
        assert isinstance(width, int)
        assert isinstance(height, int)
        self.leftTop = Point.create(left, top)
        self.size = Size.create(width, height)

    @staticmethod
    def create(leftTop: Point, size: Size) -> Rect:
        """Функция создания."""
        assert isinstance(leftTop, Point)
        assert isinstance(size, Size)
        rect = Rect()
        rect.init(leftTop, size)
        return rect

    @staticmethod
    def create2(left: int, top: int, width: int, height: int) -> Rect:
        """Функция создания 2."""
        assert isinstance(left, int)
        assert isinstance(top, int)
        assert isinstance(width, int)
        assert isinstance(height, int)
        rect = Rect()
        rect.init2(left, top, width, height)
        return rect

    def get_left(self) -> int:
        """Получение смещения слева."""
        return self.leftTop.x

    def set_left(self, left: int) -> None:
        """Задание смещения слева."""
        assert isinstance(left, int)
        self.leftTop.x = left

    def get_top(self) -> int:
        """Получение смещения слева."""
        return self.leftTop.y

    def set_top(self, top: int) -> None:
        """Задание смещения сверху."""
        assert isinstance(top, int)
        self.leftTop.y = top

    def get_width(self) -> int:
        """Получение ширины."""
        return self.size.width

    def set_width(self, width: int) -> None:
        """Задание ширины."""
        assert isinstance(width, int)
        self.size.width = width

    def get_height(self) -> int:
        """Получение высоты."""
        return self.size.height

    def set_height(self, height: int) -> None:
        """Задание высоты."""
        self.size.height = height

    def get_right(self) -> int:
        """Получение координаты правой стороны."""
        return self.get_left() + self.get_width()

    def get_bottom(self) -> int:
        """Получение координаты низа."""
        return self.get_top() + self.get_height()

    def get_center(self) -> Point:
        """Получение центра."""
        x = self.get_left() + self.get_width() // 2
        y = self.get_top() + self.get_height() // 2
        return Point.create(x, y)

    def is_valid(self) -> bool:
        """Является ли размер валидным."""
        return self.size.width >= 0 and self.size.height >= 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        return len(byte_array) == self.get_byte_list_len()

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        left = self.get_left()
        top = self.get_top()
        width = self.get_width()
        height = self.get_height()
        vl = [left, top, width, height]
        return bmc.int32_list_to_byte_array(vl)

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        vl = bmc.byte_array_to_int32_list(byte_array)
        self.init2(vl[0], vl[1], vl[2], vl[3])

    def get_byte_list_len(self):
        """Получение длины списка байтов."""
        return 16

    def __eq__(self, other: Rect) -> bool:
        """Оператор ==."""
        isEqLeftTop = (self.leftTop == other.leftTop)
        isEqSize = (self.size == other.size)
        return isEqLeftTop and isEqSize

    def __ne__(self, other: Rect) -> bool:
        """Оператор !=."""
        assert isinstance(other, Rect)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return '{}, {}'.format(self.leftTop, self.size)


class RectF(object):
    """Прямоугольник с дробными координатами."""

    def __init__(self):
        """Конструктор без параметров."""
        self.leftTop = PointF()
        self.size = SizeF()

    def init(self, leftTop: PointF, size: SizeF) -> None:
        """Функция инициализации."""
        assert isinstance(leftTop, PointF)
        assert isinstance(size, SizeF)
        self.leftTop = leftTop
        self.size = size

    def init2(self, left: float, top: float, width: float,
              height: float) -> None:
        """Функция инициализации 2."""
        assert isinstance(left, float)
        assert isinstance(top, float)
        assert isinstance(width, float)
        assert isinstance(height, float)
        self.leftTop = PointF.create(left, top)
        self.size = SizeF.create(width, height)

    @staticmethod
    def create(leftTop: PointF, size: SizeF) -> RectF:
        """Функция создания."""
        assert isinstance(leftTop, PointF)
        assert isinstance(size, SizeF)
        rect = RectF()
        rect.init(leftTop, size)
        return rect

    @staticmethod
    def create2(left: float, top: float, width: float,
                height: float) -> RectF:
        """Функция создания 2."""
        assert isinstance(left, float)
        assert isinstance(top, float)
        assert isinstance(width, float)
        assert isinstance(height, float)
        rect = RectF()
        rect.init2(left, top, width, height)
        return rect

    def get_left(self) -> float:
        """Получение смещения слева."""
        return self.leftTop.x

    def set_left(self, left: float) -> None:
        """Задание смещения слева."""
        assert isinstance(left, float)
        self.topLeft.x = left

    def get_top(self) -> float:
        """Получение смещения сверху."""
        return self.leftTop.y

    def set_top(self, top: float) -> None:
        """Задание смещения сверху."""
        assert isinstance(top, float)
        self.topLeft.y = top

    def get_width(self) -> float:
        """Получение ширины."""
        return self.size.width

    def get_height(self) -> float:
        """Получение высоты."""
        return self.size.height

    def get_right(self):
        """Получение координаты правой стороны."""
        return self.get_left() + self.get_width()

    def get_bottom(self) -> float:
        """Получение координаты низа."""
        return self.get_top() + self.get_height()

    def get_center(self) -> PointF:
        """Получение центра."""
        x = self.get_left() + self.get_width() / 2
        y = self.get_top() + self.get_height() / 2
        return PointF.create(x, y)

    def is_valid(self) -> bool:
        """Является ли размер валидным."""
        return self.size.width >= 0.0 and self.size.height >= 0.0

    def check_byte_array(self, byte_array) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        return len(byte_array) == self.get_byte_array_len()

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        left = self.get_left()
        top = self.get_top()
        width = self.get_width()
        height = self.get_height()
        vl = [left, top, width, height]
        return bmc.double_list_to_byte_array(vl)

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        vl = bmc.byte_array_to_double_list(byte_array)
        self.init2(vl[0], vl[1], vl[2], vl[3])

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 32

    def __eq__(self, other: RectF) -> bool:
        """Оператор ==."""
        isEqLeftTop = (self.leftTop == other.leftTop)
        isEqSize = (self.size == other.size)
        return isEqLeftTop and isEqSize

    def __ne__(self, other: RectF) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления объекта."""
        return '{}, {}'.format(self.leftTop, self.size)


class RoundRect(object):
    """Прямоугольник со сглажененными углами с целыми координатами."""

    def __init__(self):
        """Конструктор без параметров."""
        self.rect = Rect()
        self.radiusX = 0
        self.radiusY = 0

    def init(self, rect: Rect, radiusX: int, radiusY: int) -> None:
        """Функция инициализации."""
        assert isinstance(rect, Rect)
        assert isinstance(radiusX, int)
        assert isinstance(radiusY, int)
        self.rect = rect
        self.radiusX = RoundRect._correctRadius(radiusX)
        self.radiusY = RoundRect._correctRadius(radiusY)

    @staticmethod
    def create(rect: Rect, radiusX: int, radiusY: int) -> RoundRect:
        """Функция создания."""
        assert isinstance(rect, Rect)
        assert isinstance(radiusX, int)
        assert isinstance(radiusY, int)
        r = RoundRect()
        r.init(rect, radiusX, radiusY)
        return r

    def get_center(self) -> Point:
        """Получение центра."""
        return self.rect.get_center()

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов."""
        return len(byte_array) == self.get_byte_array_len()

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        bar = self.rect.to_byte_array()
        barx = bmc.int32_to_byte_list(self.radiusX)
        bary = bmc.int32_to_byte_list(self.radiusY)
        return bar + barx + bary

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        bar = byte_array[:16]
        self.rect.from_byte_array(bar)
        barx = byte_array[16:24]
        self.radiusX = bmc.byte_array_to_int32(barx)
        bary = byte_array[24:32]
        self.radiusY = bmc.byte_array_to_int32(bary)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 32

    def __eq__(self, other: RoundRect) -> bool:
        """Оператор ==."""
        isEqRect = (self.rect == other.rect)
        isEqRadiusX = (self.radiusX == other.radiusX)
        isEqRadiusY = (self.radiusY == other.radiusY)
        return isEqRect and isEqRadiusX and isEqRadiusY

    def __ne__(self, other: RoundRect) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления объекта."""
        return '{}, {}, {}'.format(self.rect, self.radiusX, self.radiusY)

    @staticmethod
    def _correctRadius(radius: int) -> int:
        """Корректировка радиуса."""
        if radius < 0:
            return 0
        elif radius > 100:
            return 100
        else:
            return radius


class RoundRectF(object):
    """Прямоугольник со сглажененными углами с дробными координатами."""

    def __init__(self):
        """Конструктор без параметров."""
        self.rect = RectF()
        self.radiusX = 0
        self.radiusY = 0

    def init(self, rect: RectF, radiusX: int, radiusY: int) -> None:
        """Функция инициализации."""
        assert isinstance(rect, RectF)
        assert isinstance(radiusX, int)
        assert isinstance(radiusY, int)
        self.rect = rect
        self.radiusX = RoundRectF._correctRadius(radiusX)
        self.radiusY = RoundRectF._correctRadius(radiusY)

    @staticmethod
    def create(rect: RectF, radiusX: int, radiusY: int) -> RoundRectF:
        """Функция создания."""
        assert isinstance(rect, RectF)
        assert isinstance(radiusX, float)
        assert isinstance(radiusY, float)
        r = RoundRectF()
        r.init(rect, radiusX, radiusY)
        return r

    def get_center(self) -> PointF:
        """Получение центра."""
        return self.rect.get_center()

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов."""
        return len(byte_array) == self.get_byte_array_len()

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        bar = self.rect.to_byte_array()
        barx = bmc.int_to_byte_list(self.radiusX)
        bary = bmc.int_to_byte_list(self.radiusY)
        return bar + barx + bary

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        bar = byte_array[:32]
        self.rect.from_byte_array(bar)
        barx = byte_array[32:36]
        self.radiusX = bmc.byte_array_to_int(barx)
        bary = byte_array[36:40]
        self.radiusY = bmc.byte_array_to_int(bary)

    def get_byte_array_len(self):
        """Получение длины списка байтов."""
        return 40

    def __eq__(self, other: RoundRectF) -> bool:
        """Оператор ==."""
        isEqRect = (self.rect == other.rect)
        isEqRadiusX = self.radiusX == other.radiusX
        isEqRadiusY = self.radiusY == other.radiusY
        return isEqRect and isEqRadiusX and isEqRadiusY

    def __ne__(self, other: RoundRectF) -> bool:
        """Оператор !=."""
        return not (self == other)

    def __str__(self) -> str:
        """Получение строкового представления объекта."""
        return '{}, {}, {}'.format(self.rect, self.radiusX, self.radiusY)

    @staticmethod
    def _correctRadius(radius: int) -> int:
        """Корректировка радиуса."""
        if radius < 0:
            return 0
        elif radius > 100:
            return 100
        else:
            return radius


class Polygon(object):
    """Полигон с точками с целочисленными координатами."""

    def __init__(self):
        """Конструктор без параметров."""
        self.points = []

    def init(self, points: list) -> None:
        """Функция инициализации."""
        assert Polygon._check_points(points)
        self.points = points

    @staticmethod
    def create(points: list) -> Polygon:
        """Функция создания."""
        assert Polygon._check_points(points)
        p = Polygon()
        p.init(points)
        return p

    def add_point(self, point: Point) -> None:
        """Добавление точки."""
        assert isinstance(point, Point)
        self.points.append(point)

    def get_point_count(self) -> int:
        """Получение количества точек."""
        return len(self.points)

    def is_empty(self):
        """Получение признака отсутствия точек."""
        return len(self.points) == 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка списка байтов."""
        return len(byte_array) >= 4

    def to_byte_list(self):
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmc.int32_to_byte_array(self.get_point_count())
        for pt in self.points:
            ba += pt.to_byte_array()
        return ba

    def from_byte_list(self, byte_list):
        """Инициализация из списка байтов."""
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: Polygon) -> bool:
        """Оператор ==."""
        return self.points == other.points

    def __ne__(self, other: Polygon) -> bool:
        """Оператор !=."""
        return not (self == other)

    def __str__(self) -> str:
        """Получение строкового представления."""
        return '{}'.format(self.points)

    @staticmethod
    def _check_points(points):
        """Проверка списка точек."""
        if not isinstance(points, list):
            return False
        if not all(isinstance(pt, Point) for pt in points):
            return False
        return True


class PolygonF(object):
    """Полигон с точками с дробными координатами."""

    def __init__(self):
        """Конструктор без параметров."""
        self.points = []

    def init(self, points):
        """Функция инициализации."""
        assert isinstance(points, list)
        self.points = points

    @staticmethod
    def create(points):
        """Функция создания."""
        assert isinstance(points, list)
        p = PolygonF()
        p.init(points)
        return p

    def add_point(self, point: Point) -> None:
        """Функция добавления точки."""
        assert isinstance(point, PointF)
        self.points.append(point)

    def get_point_count(self):
        """Получение количества точек."""
        return len(self.points)

    def is_empty(self) -> bool:
        """Получение признака отсутствия точек."""
        return self.get_point_count() == 0

    def check_byte_list(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов."""
        return len(byte_array) >= self.get_byte_array_len()

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        count = self.get_point_count()
        ba += bmc.int32_to_byte_array(count)
        for pt in self.points:
            ba += pt.to_byte_list()
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_list(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_list())

    def __eq__(self, other: PolygonF) -> bool:
        """Оператор ==."""
        return self.points == other.points

    def __ne__(self, other: list) -> bool:
        """Оператор !=."""
        return not (self == other)

    @staticmethod
    def _check_points(points: list) -> bool:
        """Проверка списка точек."""
        if not isinstance(points, list):
            return False
        if not all(isinstance(pt, PointF) for pt in points):
            return False
        return True


class PenStyle(object):
    """Стиль пера."""

    @staticmethod
    def style_to_str(style: int) -> str:
        """Перевод стиля в строку."""
        assert isinstance(style, int)
        if style == PenStyle.NO_PEN:
            return 'NO_PEN'
        elif style == PenStyle.DASH_LINE:
            return 'DASH_LINE'
        elif style == PenStyle.DOT_LINE:
            return 'DOT_LINE'
        elif style == PenStyle.DASH_DOT_LINE:
            return 'DASH_DOT_LINE'
        elif style == PenStyle.DASH_DOT_DOT_LINE:
            return 'DASH_DOT_DOT_LINE'
        else:
            return 'SOLID_LINE'

    NO_PEN = 0
    SOLID_LINE = 1
    DASH_LINE = 2
    DOT_LINE = 3
    DASH_DOT_LINE = 4
    DASH_DOT_DOT_LINE = 5


class PenJoinStyle(object):
    """Стиль соединения линий для пера."""

    @staticmethod
    def style_to_str(style: int) -> str:
        """Перевод стиля в строку."""
        assert isinstance(style, int)
        if style == PenJoinStyle.MITER_JOIN:
            return 'MITER_JOIN'
        elif style == PenJoinStyle.BEVEL_JOIN:
            return 'BEVEL_JOIN'
        elif style == PenJoinStyle.ROUND_JOIN:
            return 'ROUND_JOIN'
        else:
            return 'MITER_JOIN'

    MITER_JOIN = 0x00
    BEVEL_JOIN = 0x40
    ROUND_JOIN = 0x80


class PenCapStyle(object):
    """Стиль окончания пера."""

    @staticmethod
    def style_to_str(style: int) -> str:
        """Перевод стиля в строку."""
        assert isinstance(style, int)
        if style == PenCapStyle.SQUARE_CAP:
            return 'SQUARE_CAP'
        elif style == PenCapStyle.ROUND_CAP:
            return 'ROUND_CAP'
        else:
            return 'FLAT_CAP'

    FLAT_CAP = 0x00
    SQUARE_CAP = 0x10
    ROUND_CAP = 0x20


class Pen(object):
    """Перо."""

    def __init__(self):
        """Конструктор без параметров."""
        self.color = Color()
        self.width = 1
        self.style = PenStyle.SOLID_LINE
        self.join_style = PenJoinStyle.MITER_JOIN
        self.cap_style = PenCapStyle.FLAT_CAP

    def init(self, color: Color, width: int,
             style: int = PenStyle.SOLID_LINE,
             join_style: int = PenJoinStyle.MITER_JOIN,
             cap_style: int = PenCapStyle.FLAT_CAP) -> None:
        """Функция инициализации."""
        assert isinstance(color, Color)
        assert isinstance(width, int)
        assert width >= 0 and width <= 100
        assert isinstance(style, int)
        assert isinstance(join_style, int)
        assert isinstance(cap_style, int)
        self.color = color
        self.width = width
        self.style = style
        self.join_style = join_style
        self.cap_style = cap_style

    @staticmethod
    def create(color: Color, width: int,
               style: int = PenStyle.SOLID_LINE,
               join_style: int = PenJoinStyle.MITER_JOIN,
               cap_style: int = PenCapStyle.FLAT_CAP) -> Pen:
        """Функция создания."""
        assert isinstance(color, Color)
        assert isinstance(width, int)
        assert width >= 0 and width <= 100
        assert isinstance(style, int)
        assert isinstance(join_style, int)
        assert isinstance(cap_style, int)
        pen = Pen()
        pen.init(color, width, style, join_style, cap_style)
        return pen

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        assert isinstance(byte_array, bytearray)
        return len(byte_array) == self.get_byte_array_len()

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += self.color.to_byte_array()
        ba += bmc.int32_to_byte_array(self.width)
        ba += bmc.int8_to_byte_array(self.style)
        ba += bmc.int8_to_byte_array(self.join_style)
        ba += bmc.int8_to_byte_array(self.cap_style)
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        bac = byte_array[:4]
        self.color.from_byte_array(bac)
        baw = byte_array[4:8]
        self.width = bmc.byte_array_to_int32(baw)
        sbl = byte_array[8:9]
        self.style = bmc.byte_array_to_int8(sbl)
        jsbl = byte_array[9:10]
        self.join_style = bmc.byte_array_to_int8(jsbl)
        cpbl = byte_array[10:11]
        self.cap_style = bmc.byte_array_to_int8(cpbl)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 11

    def __eq__(self, other: Pen) -> bool:
        """Оператор ==."""
        isEqColor = (self.color == other.color)
        isEqWidth = (self.width == other.width)
        isEqStyle = (self.style == other.style)
        isEqJoinStyle = (self.join_style == other.join_style)
        isEqCapStyle = (self.cap_style == other.cap_style)
        return isEqColor and isEqWidth and isEqStyle \
            and isEqJoinStyle and isEqCapStyle

    def __ne__(self, other: Pen) -> bool:
        """Оператор !=."""
        assert isinstance(other, Pen)
        return not (self == other)

    def __str__(self) -> str:
        """Получение строкового представления."""
        return '{}, {}, {}, {}, {}'.format(self.color, self.width,
                                           self.style, self.join_style,
                                           self.cap_style)


class BrushStyle(object):
    """Стиль кисти."""

    @staticmethod
    def style_to_str(style: int) -> str:
        """Перевод стиля в строку."""
        if style == BrushStyle.NO_BRUSH:
            return 'NO_BRUSH'
        elif style == BrushStyle.DENSE1_PATTERN:
            return 'DENSE1_PATTERN'
        elif style == BrushStyle.DENSE2_PATTERN:
            return 'DENSE2_PATTERN'
        elif style == BrushStyle.DENSE3_PATTERN:
            return 'DENSE3_PATTERN'
        elif style == BrushStyle.DENSE4_PATTERN:
            return 'DENSE4_PATTERN'
        elif style == BrushStyle.DENSE5_PATTERN:
            return 'DENSE5_PATTERN'
        elif style == BrushStyle.DENSE6_PATTERN:
            return 'DENSE6_PATTERN'
        elif style == BrushStyle.DENSE7_PATTERN:
            return 'DENSE7_PATTERN'
        elif style == BrushStyle.HOR_PATTERN:
            return 'HOR_PATTERN'
        elif style == BrushStyle.VER_PATTERN:
            return 'VER_PATTERN'
        elif style == BrushStyle.CROSS_PATTERN:
            return 'CROSS_PATTERN'
        elif style == BrushStyle.BDIAG_PATTERN:
            return 'BDIAG_PATTERN'
        elif style == BrushStyle.FDIAG_PATTERN:
            return 'FDIAG_PATTERN'
        else:
            return 'SOLID_PATTERN'

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


class Brush(object):
    """Кисть."""

    def __init__(self):
        """Конструктор без параметров."""
        self.color = Color()
        self.style = BrushStyle.SOLID_PATTERN

    def init(self, color: Color, style: int) -> None:
        """Функция инициализации."""
        assert isinstance(color, Color)
        assert isinstance(style, int)
        self.color = color
        self.style = style

    @staticmethod
    def create(color: Color(), style: int) -> Brush:
        """Функция создания."""
        assert isinstance(color, Color)
        assert isinstance(style, int)
        brush = Brush()
        brush.init(color, style)
        return brush

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        return len(byte_array) == 5

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += self.color.to_byte_array()
        ba += bmc.int8_to_byte_array(self.style)
        return ba

    def from_byte_array(self, byte_array) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        bac = byte_array[:4]
        self.color.from_byte_array(bac)
        bas = byte_array[4:]
        self.style = bmc.byte_array_to_int8(bas)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 5

    def __eq__(self, other: Brush) -> bool:
        """Оператор ==."""
        return self.color == other.color

    def __ne__(self, other: Brush) -> bool:
        """Оператор !=."""
        return not (self == other)

    def __str__(self) -> str:
        """Получение строкового представления."""
        return '{}'.format(self.color)


class Font(object):
    """Шрифт."""

    def __init__(self):
        """Конструктор без параметров."""
        self.family = String.create('Arial')
        self.size = 12
        self.is_bold = False

    def init(self, family: String, size: int, is_bold: bool = False):
        """Функция инициализации."""
        assert isinstance(family, String)
        assert isinstance(size, int)
        assert isinstance(is_bold, bool)
        self.family = family
        self.size = size
        self.is_bold = is_bold

    @staticmethod
    def create(family: String, size: int, is_bold: bool = False) -> Font:
        """Функция создания."""
        assert isinstance(family, String)
        assert isinstance(size, int)
        assert isinstance(is_bold, bool)
        font = Font()
        font.init(family, size, is_bold)
        return font

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        return len(byte_array) >= 10

    def from_byte_list(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        sz = len(byte_array)
        fbl = byte_array[:sz-5]
        self.family.from_byte_array(fbl)
        bas = byte_array[sz-5:sz-5+4]
        self.size = bmc.byte_array_to_int32(bas)
        bab = byte_array[-1:]
        self.is_bold = bmc.byte_array_to_bool(bab)

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += self.family.to_byte_array()
        ba += bmc.int32_to_byte_array(self.size)
        ba += bmc.bool_to_byte_array(self.is_bold)
        return ba

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: Font) -> bool:
        """Оператор ==."""
        isEqFamily = (self.family == other.family)
        isEqSize = (self.size == other.size)
        isEqBold = (self.is_bold == other.is_bold)
        return isEqFamily and isEqSize and isEqBold

    def __ne__(self, other: Font) -> bool:
        """Оператор !=."""
        return not (self == other)

    def __str__(self) -> str:
        """Получение строкового представления."""
        return '{}, {}, {}'.format(self.family, self.size, self.is_bold)


class TestColor(unittest.TestCase):
    """Тестирование класса Color."""

    def test_contructor(self):
        """Тест конструктора."""
        c = Color()
        self.assertEqual(c.red, 0)
        self.assertEqual(c.green, 0)
        self.assertEqual(c.blue, 0)
        self.assertEqual(c.alpha, 255)

    def test_init(self):
        """Тест функции init."""
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
        """Тест функции create."""
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
        """Тест функции get_red."""
        c = Color.get_red()
        c_red = Color.create(255, 0, 0)
        self.assertEqual(c, c_red)

    def test_get_green(self):
        """Тест функции get_green."""
        c = Color.get_green()
        c_green = Color.create(0, 128, 0)
        self.assertEqual(c, c_green)

    def test_get_blue(self):
        """Тест функции get_blue."""
        c = Color.get_blue()
        c_blue = Color.create(0, 0, 255)
        self.assertEqual(c, c_blue)

    def test_get_white(self):
        """Тест функции get_blue."""
        c = Color.get_white()
        c_white = Color.create(255, 255, 255)
        self.assertEqual(c, c_white)

    def test_get_black(self):
        """Тест функции get_black."""
        c = Color.get_black()
        c_black = Color.create(0, 0, 0)
        self.assertEqual(c, c_black)

    def test_get_transparent(self):
        """Тест функции get_transparent."""
        c = Color.get_transparent()
        self.assertEqual(c.red, 0)
        self.assertEqual(c.green, 0)
        self.assertEqual(c.blue, 0)
        self.assertEqual(c.alpha, 0)

    def test_from_byte_array(self):
        """Тест функции to_byte_array."""
        ba = bytearray([0, 0, 0, 255])
        c = Color()
        c.from_byte_array(ba)
        self.assertEqual(c, Color.get_black())

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        c = Color()
        ba = c.to_byte_array()
        self.assertTrue(c.check_byte_array(ba))

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        c = Color()
        ba = c.to_byte_array()
        self.assertEqual(c.get_byte_array_len(), len(ba))

    def test_equal(self):
        """Тест оператора ==."""
        c1 = Color()
        self.assertTrue(c1 == c1)
        c2 = Color.create(200, 200, 200)
        self.assertFalse(c1 == c2)

    def test_not_equal(self):
        """Тест оператора !=."""
        c1 = Color()
        self.assertFalse(c1 != c1)


class TestString(unittest.TestCase):
    """Тестирование класса String."""

    def test_constructor(self):
        """Тест конструктора."""
        s = String()
        s.s = '123'

    def test_init(self):
        """Тест функции init."""
        s = String()
        s.init('123')
        self.assertEqual(s.s, '123')

    def test_create(self):
        """Тест функции create."""
        s = String.create('123')
        self.assertEqual(s.s, '123')

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        s = String.create('123')
        ba = s.to_byte_array()
        self.assertTrue(s.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        s = String.create('123')
        ba = s.to_byte_array()
        s.from_byte_array(ba)
        self.assertEqual(s.s, '123')

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        s = String()
        ba = s.to_byte_array()
        self.assertEqual(s.get_byte_array_len(), len(ba))

    def test_equal(self):
        """Тест оператора ==."""
        s1 = String()
        self.assertTrue(s1 == s1)
        s2 = String.create('123')
        self.assertFalse(s1 == s2)

    def test_not_equal(self):
        """Тест оператора !=."""
        s1 = String()
        self.assertFalse(s1 != s1)
        s2 = String.create('123')
        self.assertTrue(s1 != s2)


class TestPoint(unittest.TestCase):
    """Тестирование класса Point."""

    def test_constructor(self):
        """Тест конструктора."""
        pt = Point()
        self.assertEqual(pt.x, 0)
        self.assertEqual(pt.y, 0)

    def test_init(self):
        """Тест функции init."""
        pt = Point()
        pt.init(100, 100)
        self.assertEqual(pt.x, 100)
        self.assertEqual(pt.y, 100)

    def test_create(self):
        """Тест функции create."""
        pt = Point.create(50, 50)
        self.assertEqual(pt.x, 50)
        self.assertEqual(pt.y, 50)

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        pt = Point()
        ba = pt.to_byte_array()
        self.assertTrue(pt.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        ba = bytearray([0, 0, 0, 0, 0, 0, 0, 0])
        pt = Point()
        pt.from_byte_array(ba)
        self.assertTrue(pt == Point())

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        pt = Point()
        ba = pt.to_byte_array()
        self.assertEqual(pt.get_byte_array_len(), len(ba))

    def test_add(self):
        """Тест оператора +."""
        pt1 = Point.create(200, 200)
        pt2 = Point.create(100, 100)
        self.assertEqual(pt1 + pt2, Point.create(300, 300))

    def test_iadd(self):
        """Тест оператора +=."""
        pt1 = Point.create(200, 200)
        pt2 = Point.create(100, 100)
        pt1 += pt2
        self.assertEqual(pt1, Point.create(300, 300))

    def test_sub(self):
        """Тест оператора -."""
        pt1 = Point.create(200, 200)
        pt2 = Point.create(100, 100)
        self.assertEqual(pt1 - pt2, Point.create(100, 100))

    def test_isub(self):
        """Тест оператора -=."""
        pt1 = Point.create(200, 200)
        pt2 = Point.create(100, 100)
        pt1 -= pt2
        self.assertEqual(pt1, Point.create(100, 100))

    def test_equal(self):
        """Тест оператора ==."""
        pt1 = Point()
        self.assertTrue(pt1 == pt1)
        pt2 = Point.create(100, 100)
        self.assertFalse(pt1 == pt2)

    def test_not_equal(self):
        """Тест оператора !=."""
        pt1 = Point()
        self.assertFalse(pt1 != pt1)
        pt2 = Point.create(100, 100)
        self.assertTrue(pt1 != pt2)


class TestPointF(unittest.TestCase):
    """Тестирование класса PointF."""

    def test_constructor(self):
        """."""
        pt = PointF()
        self.assertAlmostEqual(pt.x, 0.0)
        self.assertAlmostEqual(pt.y, 0.0)

    def test_init(self):
        """."""
        pt = PointF()
        pt.init(100.0, 100.0)
        self.assertAlmostEqual(pt.x, 100.0)
        self.assertAlmostEqual(pt.y, 100.0)

    def test_create(self):
        """."""
        pt = PointF.create(100.0, 100.0)
        self.assertAlmostEqual(pt.x, 100.0)
        self.assertAlmostEqual(pt.y, 100.0)

    def test_to_byte_array(self):
        """."""
        pt = PointF()
        ba = pt.to_byte_array()
        self.assertTrue(pt.check_byte_array(ba))

    def test_from_byte_array(self):
        """."""
        pt = PointF()
        ba = bmc.double_list_to_byte_array([0.0, 0.0])
        pt.from_byte_array(ba)
        self.assertEqual(pt, PointF())

    def test_get_byte_array_len(self):
        """."""
        pt = PointF()
        bl = pt.to_byte_array()
        self.assertEqual(pt.get_byte_array_len(), len(bl))

    def test_add(self):
        """."""
        pt1 = PointF.create(200.0, 200.0)
        pt2 = PointF.create(100.0, 100.0)
        self.assertEqual(pt1 + pt2, PointF.create(300.0, 300.0))

    def test_iadd(self):
        """."""
        pt1 = PointF.create(200.0, 200.0)
        pt2 = PointF.create(100.0, 100.0)
        pt1 += pt2
        self.assertEqual(pt1, PointF.create(300.0, 300.0))

    def test_sub(self):
        """."""
        pt1 = PointF.create(200.0, 200.0)
        pt2 = PointF.create(100.0, 100.0)
        self.assertEqual(pt1 - pt2, PointF.create(100.0, 100.0))

    def test_isub(self):
        """."""
        pt1 = PointF.create(200.0, 200.0)
        pt2 = PointF.create(100.0, 100.0)
        pt1 -= pt2
        self.assertEqual(pt1, PointF.create(100.0, 100.0))

    def test_equal(self):
        """."""
        pt1 = PointF()
        self.assertTrue(pt1 == pt1)
        pt2 = PointF.create(100.0, 100.0)
        self.assertFalse(pt1 == pt2)

    def test_not_equal(self):
        """."""
        pt1 = PointF()
        self.assertFalse(pt1 != pt1)
        pt2 = PointF.create(100.0, 100.0)
        self.assertTrue(pt1 != pt2)


class TestSize(unittest.TestCase):
    """Тестирование класса Size."""

    def test_contructor(self):
        """."""
        sz = Size()
        self.assertEqual(sz.width, 0)
        self.assertEqual(sz.height, 0)

    def test_init(self):
        """."""
        sz = Size()
        sz.init(100, 100)
        self.assertEqual(sz.width, 100)
        self.assertEqual(sz.height, 100)

    def test_create(self):
        """."""
        sz = Size.create(100, 100)
        self.assertEqual(sz.width, 100)
        self.assertEqual(sz.height, 100)

    def test_is_null(self):
        """."""
        sz = Size()
        self.assertTrue(sz.is_null())

    def test_to_byte_array(self):
        """."""
        sz = Size.create(100, 100)
        ba = sz.to_byte_array()
        self.assertTrue(sz.check_byte_array(ba))

    def from_byte_array(self):
        """."""
        sz = Size.create(100, 100)
        ba = bmc.int32_list_to_byte_array([100, 100])
        sz.from_byte_list(ba)
        self.assertEqual(sz.width, 100)
        self.assertEqual(sz.height, 100)

    def test_equal(self):
        """."""
        sz1 = Size()
        self.assertTrue(sz1 == sz1)
        sz2 = Size.create(100, 100)
        self.assertFalse(sz1 == sz2)

    def test_not_equal(self):
        """."""
        sz1 = Size()
        self.assertFalse(sz1 != sz1)
        sz2 = Size.create(100, 100)
        self.assertTrue(sz1 != sz2)


class TestSizeF(unittest.TestCase):
    """Тестирование класса SizeF."""

    def test_contructor(self):
        """."""
        sz = SizeF()
        self.assertAlmostEqual(sz.width, 0.0)
        self.assertAlmostEqual(sz.height, 0.0)

    def test_init(self):
        """."""
        sz = SizeF()
        sz.init(100.0, 100.0)
        self.assertAlmostEqual(sz.width, 100.0)
        self.assertAlmostEqual(sz.height, 100.0)

    def test_create(self):
        """."""
        sz = SizeF.create(100.0, 100.0)
        self.assertAlmostEqual(sz.width, 100.0)
        self.assertAlmostEqual(sz.height, 100.0)

    def test_is_null(self):
        """."""
        sz = Size()
        self.assertTrue(sz.is_null())

    def test_to_byte_array(self):
        """."""
        sz = SizeF.create(100.0, 100.0)
        ba = sz.to_byte_array()
        self.assertTrue(sz.check_byte_array(ba))

    def from_byte_list(self):
        """."""
        sz = SizeF.create(100.0, 100.0)
        ba = bmc.double_list_to_byte_array([100.0, 100.0])
        sz.from_byte_array(ba)
        self.assertAlmostEqual(sz.width, 100.0)
        self.assertAlmostEqual(sz.height, 100.0)

    def test_get_byte_array_len(self):
        """."""
        sz = SizeF()
        self.assertEqual(sz.get_byte_array_len(), len(sz.to_byte_array()))

    def test_equal(self):
        """."""
        sz1 = SizeF()
        self.assertTrue(sz1 == sz1)
        sz2 = SizeF.create(100.0, 100.0)
        self.assertFalse(sz1 == sz2)

    def test_not_equal(self):
        """."""
        sz1 = SizeF()
        self.assertFalse(sz1 != sz1)
        sz2 = SizeF.create(100.0, 100.0)
        self.assertTrue(sz1 != sz2)


class TestLine(unittest.TestCase):
    """Тестирование класса Line."""

    def test_contructor(self):
        """."""
        line = Line()
        self.assertEqual(line.pt1, Point())
        self.assertEqual(line.pt2, Point())

    def test_init(self):
        """."""
        line = Line()
        pt1 = Point()
        pt2 = Point.create(100, 100)
        line.init(pt1, pt2)
        self.assertEqual(line.pt1, pt1)
        self.assertEqual(line.pt2, pt2)

    def test_init2(self):
        """."""
        line = Line()
        line.init2(10, 10, 100, 100)
        self.assertEqual(line.pt1.x, 10)
        self.assertEqual(line.pt1.y, 10)
        self.assertEqual(line.pt2.x, 100)
        self.assertEqual(line.pt2.y, 100)

    def test_create(self):
        """."""
        pt1 = Point()
        pt2 = Point.create(100, 100)
        line = Line.create(pt1, pt2)
        self.assertEqual(line.pt1, pt1)
        self.assertEqual(line.pt2, pt2)

    def test_create2(self):
        """."""
        line = Line.create2(10, 10, 100, 100)
        self.assertEqual(line.pt1.x, 10)
        self.assertEqual(line.pt1.y, 10)
        self.assertEqual(line.pt2.x, 100)
        self.assertEqual(line.pt2.y, 100)

    def test_to_byte_array(self):
        """."""
        line = Line.create2(10, 10, 100, 100)
        ba = line.to_byte_array()
        self.assertTrue(line.check_byte_array(ba))

    def test_from_byte_array(self):
        """."""
        bl = bmc.int32_list_to_byte_array([0, 0, 0, 0])
        line = Line()
        line.from_byte_array(bl)
        self.assertEqual(line.pt1, Point())
        self.assertEqual(line.pt2, Point())

    def test_get_byte_array_len(self):
        """."""
        line = Line()
        self.assertEqual(line.get_byte_array_len(), len(line.to_byte_array()))

    def test_equal(self):
        """."""
        line1 = Line()
        self.assertTrue(line1 == line1)
        line2 = Line.create2(0, 0, 100, 100)
        self.assertFalse(line1 == line2)

    def test_not_equal(self):
        """."""
        line1 = Line()
        self.assertFalse(line1 != line1)
        line2 = Line.create2(0, 0, 100, 100)
        self.assertTrue(line1 != line2)


class TestLineF(unittest.TestCase):
    """Тест класса LineF."""

    def test_contructor(self):
        """."""
        line = LineF()
        self.assertEqual(line.pt1, PointF())
        self.assertEqual(line.pt2, PointF())

    def test_init(self):
        """."""
        line = LineF()
        pt1 = PointF()
        pt2 = PointF.create(100.0, 100.0)
        line.init(pt1, pt2)
        self.assertEqual(line.pt1, pt1)
        self.assertEqual(line.pt2, pt2)

    def test_init2(self):
        """."""
        line = LineF()
        x1 = 100.0
        y1 = 100.0
        x2 = 200.0
        y2 = 200.0
        line.init2(x1, y1, x2, y2)
        self.assertAlmostEqual(line.pt1.x, x1)
        self.assertAlmostEqual(line.pt1.y, y1)
        self.assertAlmostEqual(line.pt2.x, x2)
        self.assertAlmostEqual(line.pt2.y, y2)

    def test_create(self):
        """."""
        pt1 = PointF()
        pt2 = PointF.create(100.0, 100.0)
        line = LineF.create(pt1, pt2)
        self.assertEqual(line.pt1, pt1)
        self.assertEqual(line.pt2, pt2)

    def test_create2(self):
        """."""
        x1 = 100.0
        y1 = 100.0
        x2 = 200.0
        y2 = 200.0
        line = LineF.create2(x1, y1, x2, y2)
        self.assertAlmostEqual(line.pt1.x, 100.0)
        self.assertAlmostEqual(line.pt1.y, 100.0)
        self.assertAlmostEqual(line.pt2.x, 200.0)
        self.assertAlmostEqual(line.pt2.y, 200.0)

    def test_from_byte_array(self):
        """."""
        line = LineF.create2(100.0, 100.0, 200.0, 200.0)
        ba = line.to_byte_array()
        line.from_byte_array(ba)
        self.assertAlmostEqual(line.pt1.x, 100.0)
        self.assertAlmostEqual(line.pt1.y, 100.0)
        self.assertAlmostEqual(line.pt2.x, 200.0)
        self.assertAlmostEqual(line.pt2.y, 200.0)

    def test_get_byte_array_len(self):
        """."""
        line = Line()
        self.assertEqual(line.get_byte_array_len(), len(line.to_byte_array()))

    def test_equal(self):
        """."""
        line1 = LineF()
        self.assertTrue(line1 == line1)
        line2 = LineF.create2(0.0, 0.0, 100.0, 100.0)
        self.assertFalse(line1 == line2)

    def test_not_equal(self):
        """."""
        line1 = LineF()
        self.assertFalse(line1 != line1)
        line2 = LineF.create2(0.0, 0.0, 100.0, 100.0)
        self.assertTrue(line1 != line2)


class TestPolyline(unittest.TestCase):
    """Тестирование класса Polyline."""

    def test_contructor(self):
        """Тест конструктора."""
        p = Polyline()
        self.assertTrue(p.is_empty())
        self.assertEqual(p.get_point_count(), 0)

    def test_init(self):
        """Тест функции init."""
        p = Polyline()
        points = [Point().create(100, 100)]
        p.init(points)
        self.assertFalse(p.is_empty())
        self.assertEqual(p.get_point_count(), 1)

    def test_create(self):
        """Тест функции create."""
        points = [Point().create(100, 100)]
        p = Polyline.create(points)
        self.assertFalse(p.is_empty())
        self.assertEqual(p.points, points)
        self.assertEqual(p.get_point_count(), 1)

    def test_add_point(self):
        """Тест функции add_point."""
        pt = Point().create(100, 100)
        p = Polyline()
        p.add_point(pt)
        self.assertFalse(p.is_empty())
        self.assertEqual(p.get_point_count(), 1)

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        p = Polyline()
        ba = p.to_byte_array()
        self.assertTrue(p.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        p = Polyline()
        ba = p.to_byte_array()
        p.from_byte_array(ba)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        p = Polyline()
        self.assertEqual(p.get_byte_array_len(), len(p.to_byte_array()))

    def test_equal(self):
        """Тест оператора ==."""
        p1 = Polyline()
        self.assertTrue(p1 == p1)
        points = [Point().create(100, 100)]
        p2 = Polyline.create(points)
        self.assertFalse(p1 == p2)

    def test_not_equal(self):
        """Тест оператора !=."""
        p1 = Polyline()
        self.assertFalse(p1 != p1)
        points = [Point().create(100, 100)]
        p2 = Polyline.create(points)
        self.assertTrue(p1 != p2)


class TestPolylineF(unittest.TestCase):
    """Тест класса PolylineF."""

    def test_contructor(self):
        """."""
        p = PolylineF()
        self.assertTrue(p.is_empty())
        self.assertEqual(p.get_point_count(), 0)

    def test_init(self):
        """."""
        p = PolylineF()
        points = [PointF().create(200.0, 200.0)]
        p.init(points)
        self.assertFalse(p.is_empty())
        self.assertEqual(p.get_point_count(), 1)

    def test_create(self):
        """."""
        points = [PointF(), PointF().create(200.0, 200.0)]
        p = PolylineF().create(points)
        self.assertFalse(p.is_empty())

    def test_add_point(self):
        """."""
        pt = PointF().create(100.0, 100.0)
        p = PolylineF()
        p.add_point(pt)
        self.assertFalse(p.is_empty())
        self.assertEqual(p.get_point_count(), 1)

    def test_to_byte_array(self):
        """."""
        p = PolylineF()
        ba = p.to_byte_array()
        self.assertTrue(p.check_byte_array(ba))

    def test_from_byte_array(self):
        """."""
        pass

    def test_get_byte_array_len(self):
        """."""
        p = PolylineF()
        self.assertEqual(p.get_byte_array_len(), len(p.to_byte_array()))

    def test_equal(self):
        """."""
        p1 = PolylineF()
        self.assertTrue(p1 == p1)
        points = [PointF().create(100.0, 100.0)]
        p2 = PolylineF.create(points)
        self.assertFalse(p1 == p2)

    def test_not_equal(self):
        """."""
        p1 = PolylineF()
        self.assertFalse(p1 != p1)
        points = [PointF().create(100.0, 100.0)]
        p2 = PolylineF.create(points)
        self.assertTrue(p1 != p2)


class TestRect(unittest.TestCase):
    """Тестирование класса Rect."""

    def test_contructor(self):
        """Тест конструктора."""
        rect = Rect()
        self.assertEqual(rect.get_left(), 0)
        self.assertEqual(rect.get_top(), 0)
        self.assertEqual(rect.get_width(), 0)
        self.assertEqual(rect.get_height(), 0)

    def test_init(self):
        """Тест функции init."""
        rect = Rect()
        lt = Point()
        s = Size.create(100, 100)
        rect.init(lt, s)
        self.assertEqual(rect.get_left(), 0)
        self.assertEqual(rect.get_top(), 0)
        self.assertEqual(rect.get_width(), 100)
        self.assertEqual(rect.get_height(), 100)

    def test_init2(self):
        """Тест функции init2."""
        rect = Rect()
        rect.init2(100, 100, 200, 200)
        self.assertEqual(rect.get_left(), 100)
        self.assertEqual(rect.get_top(), 100)
        self.assertEqual(rect.get_width(), 200)
        self.assertEqual(rect.get_height(), 200)

    def test_create(self):
        """Тест функции create."""
        leftTop = Point.create(10, 10)
        size = Size.create(100, 100)
        rect = Rect.create(leftTop, size)
        self.assertEqual(rect.leftTop, leftTop)
        self.assertEqual(rect.size, size)

    def test_create2(self):
        """Тест функции create2."""
        rect = Rect.create2(50, 50, 300, 300)
        self.assertEqual(rect.get_left(), 50)
        self.assertEqual(rect.get_top(), 50)
        self.assertEqual(rect.get_width(), 300)
        self.assertEqual(rect.get_height(), 300)

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        rect = Rect()
        bl = rect.to_byte_array()
        self.assertTrue(rect.check_byte_array(bl))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        coords = [100, 100, 200, 200]
        ba = bmc.int32_list_to_byte_array(coords)
        rect = Rect()
        rect.from_byte_array(ba)
        self.assertEqual(rect.get_left(), 100)
        self.assertEqual(rect.get_top(), 100)
        self.assertEqual(rect.get_width(), 200)
        self.assertEqual(rect.get_height(), 200)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        line = Line()
        self.assertEqual(line.get_byte_array_len(), len(line.to_byte_array()))

    def test_equal(self):
        """Тест оператора ==."""
        rect1 = Rect()
        self.assertTrue(rect1 == rect1)
        rect_2 = Rect.create2(0, 0, 200, 200)
        self.assertFalse(rect1 == rect_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        rect1 = Rect()
        self.assertFalse(rect1 != rect1)
        rect2 = Rect.create2(100, 100, 200, 200)
        self.assertTrue(rect1 != rect2)


class TestRectF(unittest.TestCase):
    """Тест класса RectF."""

    def test_constructor(self):
        """Тест конструктора."""
        rect = RectF()
        self.assertEqual(rect.leftTop, PointF())
        self.assertEqual(rect.size, SizeF())

    def test_init(self):
        """Тест функции init."""
        leftTop = PointF.create(100.0, 100.0)
        size = SizeF.create(200.0, 200.0)
        rect = RectF()
        rect.init(leftTop, size)
        self.assertEqual(rect.leftTop, leftTop)
        self.assertEqual(rect.size, size)

    def test_init2(self):
        """Тест функции init2."""
        rect = RectF()
        rect.init2(100.0, 100.0, 200.0, 200.0)
        self.assertAlmostEqual(rect.get_left(), 100.0)
        self.assertAlmostEqual(rect.get_top(), 100.0)
        self.assertAlmostEqual(rect.get_width(), 200.0)
        self.assertAlmostEqual(rect.get_height(), 200.0)

    def test_create(self):
        """Тест функции create класса RectF."""
        leftTop = PointF.create(100.0, 100.0)
        size = SizeF.create(200.0, 200.0)
        rect = RectF.create(leftTop, size)
        self.assertEqual(rect.leftTop, leftTop)
        self.assertEqual(rect.size, size)

    def test_create2(self):
        """Тест функции create2 класса RectF."""
        rect = RectF.create2(100.0, 100.0, 200.0, 200.0)
        self.assertAlmostEqual(rect.get_left(), 100.0)
        self.assertAlmostEqual(rect.get_top(), 100.0)
        self.assertAlmostEqual(rect.get_width(), 200.0)
        self.assertAlmostEqual(rect.get_height(), 200.0)

    def test_to_byte_array(self):
        """Тест функции to_byte_array класса RectF."""
        rect = RectF()
        ba = rect.to_byte_array()
        self.assertTrue(rect.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array класса RectF."""
        coords = [100.0, 100.0, 200.0, 200.0]
        bl = bmc.double_list_to_byte_array(coords)
        rect = RectF()
        rect.from_byte_array(bl)
        self.assertAlmostEqual(rect.get_left(), 100.0)
        self.assertAlmostEqual(rect.get_top(), 100.0)
        self.assertAlmostEqual(rect.get_width(), 200.0)
        self.assertAlmostEqual(rect.get_height(), 200.0)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len класса RectF."""
        line = Line()
        self.assertEqual(line.get_byte_array_len(), len(line.to_byte_array()))

    def test_equal(self):
        """Тест operator == класса RectF."""
        rect1 = RectF()
        self.assertTrue(rect1 == rect1)
        rect2 = RectF.create2(100.0, 100.0, 200.0, 200.0)
        self.assertFalse(rect1 == rect2)

    def test_not_equal(self):
        """Тест operator !=."""
        rect1 = RectF()
        self.assertTrue(rect1 == rect1)
        rect2 = RectF.create2(10.0, 10.0, 100.0, 100.0)
        self.assertFalse(rect1 == rect2)


class TestRoundRect(unittest.TestCase):
    """Тест класса RoundRect."""

    pass

#     def test_constructor(self):
#         rrect = RoundRect()
#         self.assertEqual(rrect.rect, Rect())
#         self.assertTrue(is_float_null(rrect.radiusX))
#         self.assertTrue(is_float_null(rrect.radiusY))

#     def test_init(self):
#         rrect = RoundRect()
#         rect = Rect.create2(0, 0, 100, 100)
#         radiusX = 1.0
#         radiusY = 1.0
#         rrect.init(rect, radiusX, radiusY)
#         self.assertEqual(rrect.rect, rect)
#         self.assertTrue(float_equal(rrect.radiusX, radiusX))
#         self.assertTrue(float_equal(rrect.radiusY, radiusY))

#     def test_create(self):
#         rect = Rect.create2(0, 0, 100, 100)
#         radiusX = 1.0
#         radiusY = 1.0
#         rrect = RoundRect.create(rect, radiusX, radiusY)
#         self.assertEqual(rrect.rect, rect)
#         self.assertTrue(float_equal(rrect.radiusX, radiusX))
#         self.assertTrue(float_equal(rrect.radiusY, radiusY))

#     def test_to_byte_list(self):
#         rrect = RoundRect()
#         bl = rrect.to_byte_list()
#         self.assertTrue(rrect.check_byte_list(bl))

#     def test_from_byte_list(self):
#         rrect = RoundRect()
#         bl = rrect.to_byte_list()
#         rrect.from_byte_list(bl)

#     def test_get_byte_list_len(self):
#         rrect = RoundRect()
#         self.assertEqual(rrect.get_byte_list_len(),
#             len(rrect.to_byte_list()))

#     def test_equal(self):
#         rrect1 = RoundRect()
#         self.assertTrue(rrect1 == rrect1)
#         rrect2 = RoundRect.create(Rect.create2(0, 0, 100, 100), 10.0, 10.0)
#         self.assertFalse(rrect1 == rrect2)

#     def test_not_equal(self):
#         rect1 = RoundRect()
#         self.assertFalse(rect1 != rect1)
#         rect2 = RoundRect.create(Rect.create2(0, 0, 100, 100), 10.0, 10.0)
#         self.assertTrue(rect1 != rect2)


class TestRoundRectF(unittest.TestCase):
    """Тест класса RoundRectF."""

    pass


#     def test_constructor(self):
#         rrect = RoundRectF()
#         self.assertEqual(rrect.rect, RectF())
#         self.assertEqual(rrect.radiusX, 0.0)
#         self.assertEqual(rrect.radiusY, 0.0)

#     def test_init(self):
#         rrect = RoundRectF()
#         rect = RectF()
#         radiusX = 0.0
#         radiusY = 0.0
#         rrect.init(rect, radiusX, radiusY)
#         self.assertEqual(rrect.rect, rect)
#         self.assertEqual(rrect.radiusX, radiusX)
#         self.assertEqual(rrect.radiusY, radiusY)

#     def test_create(self):
#         rect = RectF.create2(0.0, 0.0, 100.0, 100.0)
#         radiusX = 1.0
#         radiusY = 1.0
#         rrect = RoundRectF.create(rect, radiusX, radiusY)
#         self.assertEqual(rrect.rect, rect)
#         self.assertEqual(rrect.radiusX, radiusX)
#         self.assertEqual(rrect.radiusY, radiusY)

#     def test_to_byte_list(self):
#         rrect = RoundRectF()
#         bl = rrect.to_byte_list()
#         self.assertTrue(rrect.check_byte_list(bl))

#     def test_from_byte_list(self):
#         rect = RectF.create2(100.0, 100.0, 200.0, 200.0)
#         radiusX = 1.0
#         radiusY = 1.0
#         bl = rect.to_byte_list() + double_to_byte_list(radiusX) +
#             double_to_byte_list(radiusY)
#         rrect = RoundRectF()
#         rrect.from_byte_list(bl)

#     def test_get_byte_list_len(self):
#         rrect = RoundRectF()

#     def test_equal(self):
#         rect1 = RoundRectF()
#         self.assertTrue(rect1 == rect1)
#         rect2 = RoundRectF.create(RectF.create2(0.0, 0.0, 100.0, 100.0),
#             10.0, 10.0)
#         self.assertFalse(rect1 == rect2)

#     def test_not_equal(self):
#         rect1 = RoundRectF()
#         self.assertFalse(rect1 != rect1)
#         rect2 = RoundRectF.create(RectF.create2(0.0, 0.0, 100.0, 100.0),
#             10.0, 10.0)
#         self.assertTrue(rect1 != rect2)


class TestPenStyle(unittest.TestCase):
    """Тест класса PenStyle."""

    pass


class TestPenJoinStyle(unittest.TestCase):
    """Тест класса PenJoinStyle."""

    pass


class TestPenCapStyle(unittest.TestCase):
    """Тест класса PenCapStyle."""

    pass


class TestPen(unittest.TestCase):
    """Тест класса Pen."""

    def test_constructor(self):
        """Тест конструктора."""
        pen = Pen()
        self.assertEqual(pen.color, Color())
        self.assertTrue(pen.width == 1)

    def test_init(self):
        """Тест функции init."""
        pen = Pen()
        pen.init(Color.get_red(), 2)
        self.assertEqual(pen.color, Color.get_red())
        self.assertTrue(pen.width == 2)

    def test_create(self):
        """Тест функции create."""
        pen = Pen.create(Color.get_red(), 2)
        self.assertEqual(pen.color, Color.get_red())
        self.assertTrue(pen.width == 2)

    def test_to_byte_list(self):
        """Тест функции to_bte_list."""
        pen = Pen()
        ba = pen.to_byte_array()
        self.assertTrue(pen.check_byte_array(ba))

#     def test_from_byte_list(self):
#         pen = Pen()
#         c = Color.get_blue()
#         w = 3
#         cbl = c.to_byte_list()
#         wbl = int32_to_byte_list(w)
#         sbl = int8_to_byte_list(PenStype.SOLID_LINE)
#         jsbl = int8_to_byte_list(PenJoinStyle.MITER_JOIN)
#         bl = cbl + wbl + sbl + jsbl + [0]
#         pen.from_byte_list(bl)
#         self.assertEqual(pen.color, c)
#         self.assertEqual(pen.width, w)

    def test_get_byte_list_len(self):
        """Тест функции get_byte_list_len."""
        pen = Pen()
        self.assertEqual(pen.get_byte_array_len(), len(pen.to_byte_array()))

    def test_equal(self):
        """Тест оператора ==."""
        pen1 = Pen()
        self.assertTrue(pen1 == pen1)
        pen2 = Pen.create(Color.get_red(), 2)
        self.assertFalse(pen1 == pen2)

    def test_not_equal(self):
        """Тест оператора !=."""
        pen1 = Pen()
        self.assertFalse(pen1 != pen1)
        pen2 = Pen.create(Color.get_red(), 2)
        self.assertTrue(pen1 != pen2)


class TestBrushStyle(unittest.TestCase):
    """Тест класса BrushStyle."""

    pass


class TestBrush(unittest.TestCase):
    """Тест класса Brush."""

    def test_constructor(self):
        """Тест конструктора."""
        brush = Brush()
        self.assertEqual(brush.color, Color())
        self.assertEqual(brush.style, BrushStyle.SOLID_PATTERN)

    def test_init(self):
        """Тест функции init."""
        brush = Brush()
        brush.init(Color.get_green(), BrushStyle.BDIAG_PATTERN)
        self.assertEqual(brush.color, Color.get_green())
        self.assertEqual(brush.style, BrushStyle.BDIAG_PATTERN)

    def test_create(self):
        """Тест функции create."""
        brush = Brush.create(Color.get_red(), BrushStyle.DENSE1_PATTERN)
        self.assertEqual(brush.color, Color.get_red())
        self.assertEqual(brush.style, BrushStyle.DENSE1_PATTERN)

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        brush = Brush()
        ba = brush.to_byte_array()
        self.assertTrue(brush.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        c = Color.get_gold()
        s = BrushStyle.FDIAG_PATTERN
        ba = bytearray()
        ba += c.to_byte_array()
        ba += bmc.int8_to_byte_array(s)
        brush = Brush()
        brush.from_byte_array(ba)
        self.assertEqual(brush.color, c)
        self.assertEqual(brush.style, s)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        brush = Brush()
        self.assertEqual(brush.get_byte_array_len(),
                         len(brush.to_byte_array()))

    def test_equal(self):
        """Тест оператора ==."""
        brush1 = Brush()
        self.assertTrue(brush1 == brush1)
        brush2 = Brush.create(Color.get_blue(), BrushStyle.SOLID_PATTERN)
        self.assertFalse(brush1 == brush2)

    def test_not_equal(self):
        """Тест оператора !=."""
        brush1 = Brush()
        self.assertFalse(brush1 != brush1)
        brush2 = Brush.create(Color.get_blue(), BrushStyle.SOLID_PATTERN)
        self.assertTrue(brush1 != brush2)


class TestFont(unittest.TestCase):
    """Тест класса Font."""

    def test_constructor(self):
        """Тест конструктора."""
        font = Font()
        self.assertEqual(font.family, String.create('Arial'))
        self.assertEqual(font.size, 12)
        self.assertEqual(font.is_bold, False)

    def test_init(self):
        """Тест функции init."""
        family = String.create('Courier New')
        size = 14
        is_bold = True
        font = Font()
        font.init(family, size, is_bold)
        self.assertEqual(font.family, family)
        self.assertEqual(font.size, size)
        self.assertEqual(font.is_bold, is_bold)

    def test_create(self):
        """Тест функции create."""
        family = String.create('Courier New')
        size = 16
        is_bold = True
        font = Font.create(family, size, is_bold)
        self.assertEqual(font.family, family)
        self.assertEqual(font.size, size)
        self.assertEqual(font.is_bold, is_bold)

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        font = Font()
        ba = font.to_byte_array()
        self.assertTrue(font.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        font = Font()
        family = String.create('Courier New')
        size = 16
        is_bold = True
        ba = bytearray()
        ba += family.to_byte_array()
        ba += bmc.int32_to_byte_array(size)
        ba += bmc.bool_to_byte_array(is_bold)
        font.from_byte_list(ba)
        self.assertEqual(font.family, family)
        self.assertEqual(font.size, size)
        self.assertEqual(font.is_bold, is_bold)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        line = Line()
        self.assertEqual(line.get_byte_array_len(), len(line.to_byte_array()))

    def test_equal(self):
        """Тест оператора ==."""
        font1 = Font()
        self.assertTrue(font1 == font1)
        family = String.create('Courier New')
        size = 14
        is_bold = True
        font2 = Font.create(family, size, is_bold)
        self.assertFalse(font1 == font2)

    def test_not_equal(self):
        """Тест оператора !=."""
        font1 = Font()
        self.assertFalse(font1 != font1)
        family = String.create('Courier New')
        size = 14
        is_bold = True
        font2 = Font.create(family, size, is_bold)
        self.assertTrue(font1 != font2)


# Вызывается при загрузке модуля главным
if __name__ == '__main__':
    unittest.main()
