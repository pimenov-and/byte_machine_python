# coding: utf8
import math
import unittest
from file_dump_graphics import *


#----------------------------------------------------------------
# Коды операций
#----------------------------------------------------------------

class DrawOpCodes(object):

    UNKNOWN = -1
    SAVE_STATE = 0
    RESTORE_STATE = 1
    SET_CLIP_RECT = 2
    TRANFORM_TRANSLATE = 3
    TRANFORM_ROTATE = 4
    TRANFORM_SCALE = 5
    SET_PEN = 6
    SET_BRUSH = 7
    SET_FONT = 8
    SET_ANTIALIASING = 9
    DRAW_POINT = 10
    DRAW_POINTS = 11
    DRAW_POINTF = 12
    DRAW_POINTSF = 13
    DRAW_LINE = 14
    DRAW_LINES = 15
    DRAW_LINEF = 16
    DRAW_LINESF = 17
    DRAW_POLYLINE = 18
    DRAW_POLYLINEF = 19
    DRAW_ARC = 20
    DRAW_ARCF = 21
    DRAW_RECT = 22
    DRAW_RECTS = 23
    DRAW_RECTF = 24
    DRAW_RECTSF = 25
    DRAW_ROUND_RECT = 26
    DRAW_ROUND_RECTS = 27
    DRAW_ROUND_RECTF = 28
    DRAW_ROUND_RECTSF = 29
    DRAW_ELLIPSE = 30
    DRAW_ELLIPSES = 31
    DRAW_ELLIPSEF = 32
    DRAW_ELLIPSESF = 33
    DRAW_POLYGON = 34
    DRAW_POLYGONF = 35
    DRAW_IMAGE = 36
    DRAW_TEXT = 37
    COUNT = 38


#----------------------------------------------------------------
# Флаги выравнивания (объединяются через ИЛИ)
#----------------------------------------------------------------

class AlignmentFlags(object):

    ALIGN_UNKNOWN = 0x00
    ALIGN_LEFT = 0x01
    ALIGN_RIGHT = 0x02
    ALIGN_HCENTER = 0x04
    ALIGN_TOP = 0x20
    ALIGN_BOTTOM = 0x40
    ALIGN_VCENTER = 0x80


#----------------------------------------------------------------
# Операция "Сохранения состояния"
#----------------------------------------------------------------

class SaveStateOp(object):

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.SAVE_STATE:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.SAVE_STATE)
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 3

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, SaveStateOp)
        return True

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, SaveStateOp)
        return not (self == other)


#----------------------------------------------------------------
# Операция "Восстановление состояния"
#----------------------------------------------------------------

class RestoreStateOp(object):

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.RESTORE_STATE:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.RESTORE_STATE)
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 3

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, RestoreStateOp)
        return True

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, RestoreStateOp)
        return not self == other


#----------------------------------------------------------------
# Операция "Задание прямоугольника отсечения"
#----------------------------------------------------------------

class SetClipRectOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rect = Rect()

    def init(self, rect):
        '''Функция инициализации.'''
        assert isinstance(rect, Rect)
        self.rect = rect

    @staticmethod
    def create(rect):
        '''Функция создания.'''
        assert isinstance(rect, Rect)
        op = SetClipRectOp()
        op.init(rect)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.SET_CLIP_RECT:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.SET_CLIP_RECT)
        bl += self.rect.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        rbl = byte_list[2:18]
        self.rect.from_byte_list(rbl)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 19

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, SetClipRectOp)
        return self.rect == other.rect

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, SetClipRectOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.rect)


#----------------------------------------------------------------
# Операция "Трансформация - перенос"
#----------------------------------------------------------------

class TransformTranslateOp(object):
    
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
        '''Функция создания.'''
        assert isinstance(x, float)
        assert isinstance(y, float)
        op = TransformTranslateOp()
        op.init(x, y)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.TRANFORM_TRANSLATE:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.TRANFORM_TRANSLATE)
        bl += double_to_byte_list(self.x)
        bl += double_to_byte_list(self.y)
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        bl = byte_list[2:18]
        data = byte_list_to_double_list(bl)
        self.x = data[0]
        self.y = data[1]

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 19

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, TransformTranslateOp)
        isEqX = float_equal(self.x, other.x)
        isEqY = float_equal(self.y, other.y)
        return isEqX and isEqY

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, TransformTranslateOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}, {}'.format(self.x, self.y)


#----------------------------------------------------------------
# Операция "Трансформация - поворот"
#----------------------------------------------------------------

class TransformRotateOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.angle = 0.0

    def init(self, angle):
        '''Функция инициализации.'''
        assert isinstance(angle, float)
        self.angle = angle

    @staticmethod
    def create(angle):
        '''Функция создания.'''
        assert isinstance(angle, float)
        op = TransformRotateOp()
        op.init(angle)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.TRANFORM_ROTATE:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.TRANFORM_ROTATE)
        bl += double_to_byte_list(self.angle)
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        ba = byte_list[2:10]
        self.angle = byte_list_to_double(ba)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 11

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, TransformRotateOp)
        return float_equal(self.angle, other.angle)

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, TransformRotateOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.angle)


#----------------------------------------------------------------
# Операция "Трансформация - масштабирование"
#----------------------------------------------------------------

class TransformScaleOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.x = 1.0
        self.y = 1.0

    def init(self, x, y):
        '''Функция инициалиазации.'''
        assert isinstance(x, float)
        assert isinstance(y, float)
        self.x = x
        self.y = y

    @staticmethod
    def create(x, y):
        '''Функция создания.'''
        assert isinstance(x, float)
        assert isinstance(y, float)
        op = TransformScaleOp()
        op.init(x, y)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.TRANFORM_SCALE:
            return False
        return True
        
    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.TRANFORM_SCALE)
        bl += double_to_byte_list(self.x)
        bl += double_to_byte_list(self.y)
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        assert self.check_byte_list(byte_list)
        bl = byte_list[2:18]
        bc = double_list_to_byte_list(bl)
        self.x = bc[0]
        self.y = bc[1]

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 19

    def __eq__(self, other):
        '''Функция проверки на равенство.'''
        assert isinstance(other, TransformScaleOp)
        isEqX = float_equal(self.x, other.x)
        isEqY = float_equal(self.y, other.y)
        return isEqX and isEqY

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, TransformScaleOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}, {}'.format(self.x, self.y)


#----------------------------------------------------------------
# Операция "Задание сглаживания"
#----------------------------------------------------------------

class SetAntialiasingOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.antialiasing = False

    def init(self, antialiasing):
        '''Функция инициализации.'''
        assert isinstance(antialiasing, bool)
        self.antialiasing = antialiasing

    @staticmethod
    def create(antialiasing):
        '''Функция создания.'''
        assert isinstance(antialiasing, bool)
        op = SetAntialiasingOp()
        op.init(antialiasing)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.SET_ANTIALIASING:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.SET_ANTIALIASING)
        bl += bool_to_byte_list(self.antialiasing)
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        ba = byte_list[2:3]
        self.antialiasing = byte_list_to_bool(ba)
        
    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 4

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, SetAntialiasingOp)
        return self.antialiasing == other.antialiasing

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, SetAntialiasingOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.antialiasing)


#----------------------------------------------------------------
# Операция "Задать перо"
#----------------------------------------------------------------

class SetPenOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.pen = Pen()

    def init(self, pen):
        '''Функция инициализации'''
        assert isinstance(pen, Pen)
        self.pen = pen

    @staticmethod
    def create(pen):
        '''Функция создания.'''
        assert isinstance(pen, Pen)
        op = SetPenOp()
        op.pen = pen
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.SET_PEN:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.SET_PEN)
        bl += self.pen.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        bp = byte_list[2:13]
        self.pen.from_byte_list(bp)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 14

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, SetPenOp)
        return self.pen == other.pen

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, SetPenOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления объекта.'''
        return '{}'.format(self.pen)


#----------------------------------------------------------------
# Операция "Задать кисть"
#----------------------------------------------------------------

class SetBrushOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.brush = Brush()

    def init(self, brush):
        '''Функция инициализации.'''
        assert isinstance(brush, Brush)
        self.brush = brush

    @staticmethod
    def create(brush):
        '''Функция создания.'''
        assert isinstance(brush, Brush)
        op = SetBrushOp()
        op.init(brush)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.SET_BRUSH:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.SET_BRUSH)
        bl += self.brush.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        bb = byte_list[2:7]
        self.brush.from_byte_list(bb)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 8

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, SetBrushOp)
        return self.brush == other.brush

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, SetBrushOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления объекта.'''
        return '{}'.format(self.brush)


#----------------------------------------------------------------
# Операция "Задание шрифта"
#----------------------------------------------------------------

class SetFontOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.font = Font()

    def init(self, font):
        '''Функция инициализации.'''
        assert isinstance(font, Font)
        self.font = font

    @staticmethod
    def create(font):
        '''Функция создания.'''
        op = SetFontOp()
        op.init(font)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.SET_FONT:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.SET_FONT)
        bl += self.font.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, SetFontOp)
        return self.font == other.font

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, SetFontOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления объекта.'''
        return '{}'.format(self.brush)


#----------------------------------------------------------------
# Операция "Нарисовать точку с целочисленными координатами"
#----------------------------------------------------------------

class DrawPointOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.point = Point()

    def init(self, point):
        '''Функция ицнициализации.'''
        assert isinstance(s, Point)
        self.point = point

    @staticmethod
    def create(point):
        '''Функция создания.'''
        assert isinstance(s, Point)
        op = DarwPointOp()
        op.init(point)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_POINT:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_POINT)
        bl += self.point.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert check_byte_list(byte_list)
        pbl = byte_list[2:10]
        self.point.from_byte_list(pbl)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 11

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawPointOp)
        return self.point == other.point

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawPointOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.point)


#----------------------------------------------------------------
# Операция "Нарисовать точки с целочисленными координатами"
#----------------------------------------------------------------

class DrawPointsOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.points = []

    def init(self, points):
        '''Функция ицнициализации.'''
        self.points = points

    @staticmethod
    def create(points):
        '''Функция создания.'''
        assert isinstance(points, list)
        op = DrawPointsOp()
        op.init(points)
        return op
        
    def add_point(point):
        '''Функция добавления точки.'''
        assert isinstance(s, Point)
        self.points.append(point)

    def get_point_count():
        '''Получение количества точек.'''
        return len(self.points)

    def is_empty(self):
        '''Получение признака отсутствия точек.'''
        return self.get_point_count() == 0

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_POINTS:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_POINTS)
        bl += int32_to_byte_list(self.get_point_count())
        for p in self.points:
            bl += p.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert check_byte_list(byte_list)
        cbl = byte_list[2:6]
        count = byte_list_to_int32(cbl)
        point_len = Point().get_byte_list_len()
        offset = 6
        self.points = []
        for i in range(count):
            p = Point()
            pbl = byte_list[offset:offset + point_len]
            p.from_byte_list(pbl)
            self.add_point(p)
            offset += pl

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawPointsOp)
        return self.points == other.points

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawPointsOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.points)


#----------------------------------------------------------------
# Операция "Нарисовать точку с дробными координатами"
#----------------------------------------------------------------

class DrawPointfOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.point = PointF()

    def init(self, point):
        '''Функция инициализации.'''
        assert isinstance(point, Point)
        self.point = point

    @staticmethod
    def create(point):
        '''Функция создания.'''
        assert isinstance(point, Point)
        op = DrawPointfOp()
        op.init(point)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_POINTF:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_POINTF)
        bl += self.point.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert check_byte_list(byte_list)
        pbl = byte_list[2:18]
        self.point.from_byte_list(pbl)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 19

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawPointfOp)
        return self.point == other.point

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawPointfOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.point)


#----------------------------------------------------------------
# Операция "Нарисовать точки с дробными координатами"
#----------------------------------------------------------------

class DrawPointsfOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.points = []

    def init(self, points):
        '''Функция ицнициализации.'''
        assert isinstance(points, list)
        self.points = points

    @staticmethod
    def create(points):
        '''Функция создания.'''
        assert isinstance(points, list)
        op = DrawPointsfOp()
        op.init(points)
        return op

    def get_point_count(self):
        '''Получение количества точек.'''
        return len(self.points)

    def add_point(self, point):
        '''Добавление точки.'''
        assert isinstance(points, PointF)
        self.points.append(point)

    def is_empty(self):
        '''Получение признака отсутствия точек.'''
        return len(self.points) == 0

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_POINTSF:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_POINTSF)
        bl += int32_to_byte_list(self.get_point_count())
        for p in self.points:
            bl += p.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация из списка байтов.'''
        assert self.check_byte_list(byte_list)
        cbl = byte_list[2:6]
        count = byte_list_to_int32(cbl)
        point_len = PointF().get_byte_list_len()
        offset = 6
        self.points = []
        for i in range(count):
            p = PointF()
            pbl = byte_list[offset:offset + point_len]
            p.from_byte_list(pbl)
            self.add_point(p)
            offset += pl

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawPointsfOp)
        return self.points == other.points

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawPointsfOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.points)


#----------------------------------------------------------------
# Операция "Нарисовать линию с целочисленными коордиинатами"
#----------------------------------------------------------------

class DrawLineOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.line = Line()

    def init(self, line):
        '''Функция инициализации.'''
        assert isinstance(line, Line)
        self.line = line

    def init2(self, pt1, pt2):
        '''Функция инициализации.'''
        assert isinstance(pt1, Point)
        assert isinstance(pt2, Point)
        self.line = Line.create(pt1, pt2)

    def init3(self, x1, y1, x2, y2):
        '''Функция инициализации.'''
        assert isinstance(x1, int)
        assert isinstance(y1, int)
        assert isinstance(x2, int)
        assert isinstance(y2, int)
        self.line = Line.create2(x1, y1, x2, y2)

    @staticmethod
    def create(line):
        '''Функция создания.'''
        assert isinstance(line, Line)
        op = DrawLineOp()
        op.init(line)
        return op

    @staticmethod
    def create2(pt1, pt2):
        '''Функция создания.'''
        assert isinstance(pt1, Point)
        assert isinstance(pt2, Point)
        op = DrawLineOp()
        op.init2(pt1, pt2)
        return op

    @staticmethod
    def create3(x1, y1, x2, y2):
        '''Функция создания.'''
        assert isinstance(x1, int)
        assert isinstance(y1, int)
        assert isinstance(x2, int)
        assert isinstance(y2, int)
        op = DrawLineOp()
        op.init3(x1, y1, x2, y2)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_LINE:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_LINE)
        bl += self.line.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        bl = byte_list[2:18]
        self.line.from_byte_list(bl)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 19

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawLineOp)
        return self.line == other.line

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawLineOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.line)


#----------------------------------------------------------------
# Операция "Нарисовать линии с целыми координатами"
#----------------------------------------------------------------

class DrawLinesOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.lines = []

    def init(self, lines):
        '''Функция инициализации.'''
        assert check_lines(lines)
        self.lines = lines

    def create(lines):
        '''Функция создания.'''
        assert check_lines(lines)
        op = DrawLinesOp()
        op.init(lines)
        return op

    def add_line(self, line):
        '''Функция добавления линий.'''
        assert isinstance(line, Line)
        self.lines.append(line)

    def get_line_count(self):
        '''Получение количества линий.'''
        return len(self.lines)

    def is_empty(self):
        '''Получение признака отсуствия линий.'''
        return self.get_line_count() == 0

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < 6:
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_LINES:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_LINES)
        bl += int32_to_byte_list(self.get_line_count())
        for line in self.lines:
            bl += line.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert check_byte_list(byte_list)
        cbl = byte_list[2:6]
        count = byte_list_to_int32(cbl)
        line_len = Line().get_byte_list_len()
        self.lines = []
        offset = 6
        for i in range(count):
            line = Line()
            lbl = byte_list[offset:offset + line_len]
            line.from_byte_list(lbl)
            self.add_point(line)
            offet += line_len

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawLinesOp)
        return self.lines == other.lines

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawLinesOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.lines)

    @staticmethod
    def check_lines(lines):
        '''Проверка списка точек.'''
        if not isinstance(lines, list):
            return False
        if not all([isinstance(line, Line) for line in lines]):
            return False
        return True


#----------------------------------------------------------------
# Операция "Нарисовать линию с дробными координатами"
#----------------------------------------------------------------

class DrawLinefOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.line = LineF()

    def init(self, line):
        '''Функция инициализации.'''
        assert isinstance(line, LineF)
        self.line = line

    def init2(self, pt1, pt2):
        '''Функция инициализации.'''
        assert isinstance(pt1, PointF)
        assert isinstance(pt2, PointF)
        self.line = LineF.create(pt1, pt2)

    def init3(self, x1, y1, x2, y2):
        '''Функция инициализации.'''
        assert isinstance(x1, float)
        assert isinstance(y1, float)
        assert isinstance(x2, float)
        assert isinstance(y2, float)
        self.line = LineF.create2(x1, y1, x2, y2)

    @staticmethod
    def create(line):
        '''Функция создания.'''
        assert isinstance(line, LineF)
        op = DrawLinefOp()
        op.init(line)
        return op

    @staticmethod
    def create2(pt1, pt2):
        '''Функция создания.'''
        assert isinstance(line, LineF)
        op = DrawLinefOp()
        op.init2(pt1, pt2)
        return op

    @staticmethod
    def create3(x1, y1, x2, y2):
        '''Функция создания.'''
        assert isinstance(x1, float)
        assert isinstance(y1, float)
        assert isinstance(x2, float)
        assert isinstance(y2, float)
        op = DrawLinefOp()
        op.init3(x1, y1, x2, y2)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_LINEF:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_LINEF)
        bl += self.line.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        bl = byte_list[2:34]
        self.line.from_byte_list(bl)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 35

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawLinefOp)
        return self.line == other.line

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawLinefOp)
        return not (self == other)
    
    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.line)


#----------------------------------------------------------------
# Операция "Нарисовать линии с дробными координатами"
#----------------------------------------------------------------

class DrawLinesfOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.lines = []

    def init(self, lines):
        '''Функция инициализации.'''
        assert check_lines(lines)
        self.lines = lines

    @staticmethod
    def create(lines):
        '''Функция создания.'''
        assert check_lines(lines)
        op = DrawLinesfOp()
        op.init(lines)
        return op

    def add_line(self, line):
        '''Добавление линии.'''
        assert isinstance(line, PointF)
        self.lines.append(line)

    def get_line_count(self):
        '''Получение количества линий.'''
        return len(self.lines)

    def is_empty(self):
        '''Получение признака отсуствия линий.'''
        return self.get_line_count() == 0

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < 6:
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_LINEF:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_LINESF)
        bl += int32_to_byte_list(self.get_line_count())
        for line in self.lines:
            bl += line.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert check_byte_list(byte_list)
        cbl = byte_list[2:6]
        count = byte_list_to_int32(cbl)
        self.lines = []
        line_len = LineF().get_byte_list_len()
        offset = 6
        for i in range(count):
            line = Line()
            lbl = byte_list[offset:offset + line_len]
            line.from_byte_list(lbl)
            self.add_line(line)
            offset += line_len

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawLinesfOp)
        return self.lines == other.lines

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawLinesfOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.lines)

    @staticmethod
    def check_lines(lines):
        '''Проверка списка точек.'''
        if not isinstance(lines, list):
            return False
        if not all([isinstance(line, LineF) for line in lines]):
            return False
        return True


#----------------------------------------------------------------
# Операция "Нарисовать ломаную линию с целочисленными координатами"
#----------------------------------------------------------------

class DrawPolylineOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.polyline = Polyline()

    def init(self, polyline):
        '''Функция инициализации.'''
        assert isinstance(polyline, Polyline)
        self.polyline = polyline

    @staticmethod
    def create(polyline):
        '''Функция создания.'''
        assert isinstance(polyline, Polyline)
        op = DrawPolylineOp()
        op.init(polyline)
        return op

    def add_point(self, point):
        '''Функция добавления линий.'''
        assert isinstance(point, Point)
        self.polyline.add_point(point)

    def get_point_count(self):
        '''Получение количества линий.'''
        return self.polyline.get_point_count()

    def is_empty(self):
        '''Получение признака отсуствия линий.'''
        return self.polyline.is_empty()

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < 6:
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_POLYLINE:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_POLYLINE)
        bl += self.polyline.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
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
        assert isinstance(other, DrawPolylineOp)
        return self.polyline == other.polyline

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawPolylineOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.polyline)


#----------------------------------------------------------------
# Операция "Нарисовать ломаную линию с дробными координатами"
#----------------------------------------------------------------

class DrawPolylinefOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.polyline = PolylineF()

    def init(self, polyline):
        '''Функция инициализации.'''
        assert isinstance(polyline, PolylineF)
        self.polyline = polyline

    @staticmethod
    def create(polyline):
        '''Функция создания.'''
        assert isinstance(polyline, PolylineF)
        op = DrawPolylinefOp()
        op.init(polyline)
        return op

    def add_point(self, point):
        '''Функция добавления линий.'''
        assert isinstance(point, PointF)
        self.polyline.add_point(point)

    def is_empty(self):
        '''Получение признака отсутствия точек.'''
        return self.polyline.is_empty()

    def get_point_count(self):
        '''Получение количества точек.'''
        return self.polyline.get_point_count()

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_POLYLINEF)
        bl += self.polyline.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
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
        assert isinstance(other, DrawPolylinefOp)
        return self.polyline == other.polyline

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawPolylinefOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.polyline)


#----------------------------------------------------------------
# Операция "Нарисовать прямоугольник"
#----------------------------------------------------------------

class DrawRectOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rect = Rect()

    def init(self, rect):
        '''Функция инициализации.'''
        assert isinstance(rect, Rect)
        self.rect = rect

    @staticmethod
    def create(rect):
        '''Функция создания.'''
        assert isinstance(rect, Rect)
        op = DrawRectOp()
        op.init(rect)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_RECT:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_RECT)
        bl += self.rect.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 18

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawRectOp)
        return self.rect == other.rect

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawRectOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.rect)


#----------------------------------------------------------------
# Операция "Нарисовать прямоугольники с целочисленными координатами"
#----------------------------------------------------------------

class DrawRectsOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rects = []

    def init(self, rects):
        '''Функция инициализации.'''
        assert isinstance(rects, list)
        self.rects = rects

    @staticmethod
    def create(rects):
        '''Функция создания.'''
        assert isinstance(rects, list)
        op = DrawRectsOp()
        op.init(rects)
        return op

    def add_rect(self, rect):
        '''Добавление точки.'''
        self.rects.append(rect)

    def get_rect_count(self):
        '''Получение количества прямоугольников.'''
        return len(self.rects)

    def is_empty(self):
        '''Получение признака отсутствия прямоугольников.'''
        return self.get_rect_count() == 0

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_RECTS:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_RECTS)
        bl += int32_to_byte_list(self.get_rect_count())
        for rect in self.rects:
            bl += rect.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        return self.rects == other.rects

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.rects)

    @staticmethod
    def check_lines(rects):
        '''Проверка списка прямоугольников.'''
        if not isinstance(rects, list):
            return False
        if not all([isinstance(rect, Rect) for rect in rects]):
            return False
        return True


#----------------------------------------------------------------
# Операция "Нарисовать прямоугольник с координатами с плавающей точкой"
#----------------------------------------------------------------

class DrawRectfOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rect = RectF()

    def init(self, rect):
        '''Функция инициализации.'''
        assert isinstance(rect, RectF)
        self.rect = rect

    @staticmethod
    def create(rect):
        '''Функция создания.'''
        assert isinstance(rect, RectF)
        op = DrawRectfOp()
        op.init(rect)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_RECTF:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_RECTF)
        bl += self.rect.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 34

    def __eq__(self, other):
        '''Оператор ==.'''
        return self.rect == other.rect

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.rect)


#----------------------------------------------------------------
# Операция "Нарисовать прямоугольники с дробными координатами"
#----------------------------------------------------------------

class DrawRectsfOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rects = []

    def init(self, rects):
        '''Функция инициализации.'''
        assert isinstance(rects, list)
        self.rects = rects

    @staticmethod
    def create(rects):
        '''Функция создания.'''
        assert isinstance(rects, list)
        op = DrawRectsfOp()
        op.init(rects)
        return op

    def add_rect(self, rect):
        '''Добавление прямоугольника.'''
        assert isinstance(rect, RectF)
        self.rects.append(rect)

    def get_rect_count(self):
        '''Получение количества прямоугольников.'''
        return len(self.rects)

    def is_empty(self):
        '''Получение признака отсутствия прямоугольников.'''
        return self.get_rect_count() == 0

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_RECTSF:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_RECTSF)
        bl += int32_to_byte_list(self.get_rect_count())
        for rect in self.rects:
            bl += rect.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawRectsfOp)
        return self.rects == other.rects

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawRectsfOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.rects)

    @staticmethod
    def check_lines(rects):
        '''Проверка списка прямоугольников.'''
        if not isinstance(rects, list):
            return False
        if not all([isinstance(rect, RectF) for rect in rects]):
            return False
        return True


#----------------------------------------------------------------
# Операция "Нарисовать эллипс с целочисленными координатами"
#----------------------------------------------------------------

class DrawEllipseOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rect = Rect()

    def init(self, rect):
        '''Функция инициализации.'''
        assert isinstance(rect, Rect)
        self.rect = rect

    @staticmethod
    def create(rect):
        '''Функция создания.'''
        assert isinstance(rect, Rect)
        op = DrawEllipseOp()
        op.init(rect)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_ELLIPSE:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_ELLIPSE)
        bl += self.rect.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        bl = byte_list[2:]
        self.rect.from_byte_list(bl)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 18

    def __eq__(self, other):
        '''Оператор ==.'''
        return self.rect == other.rect

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.rect)


#----------------------------------------------------------------
# Операция "Нарисовать эллипсы с целочисленными координатами"
#----------------------------------------------------------------

class DrawEllipsesOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rects = []

    def init(self, rects):
        '''Функция инициализации.'''
        assert isinstance(rects, list)
        self.rects = rects

    @staticmethod
    def create(rects):
        '''Функция создания.'''
        assert isinstance(rects, list)
        op = DrawEllipsesOp()
        op.init(rects)
        return op

    def add_rect(self, rect):
        '''Добавление точки.'''
        assert isinstance(rects, Rect)
        self.rects.append(rect)

    def get_rect_count(self):
        '''Получение количества точек.'''
        return len(self.rects)

    def is_empty(self):
        '''Получение признака отсутствия прямоугольников.'''
        return self.get_rect_count() == 0

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_ELLIPSES:
            return False
        return True

    def to_byte_list(self):
        '''Получение списка байтов.'''
        bl = []
        bl += int32_to_byte_list(self.get_rect_count())
        for r in self.rects:
            bl += r.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        pass
    
    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawEllipsesOp)
        return self.rects == other.rects

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawEllipsesOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.rects)

    @staticmethod
    def check_lines(rects):
        '''Проверка списка прямоугольников.'''
        if not isinstance(rects, list):
            return False
        if not all([isinstance(rect, Rect) for rect in rects]):
            return False
        return True


#----------------------------------------------------------------
# Операция "Нарисовать эллипс с дробными координатами"
#----------------------------------------------------------------

class DrawEllipsefOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rect = RectF()

    def init(self, rect):
        '''Функция инициализации.'''
        assert isinstance(rect, RectF)
        self.rect = rect

    @staticmethod
    def create(rect):
        '''Функция создания.'''
        assert isinstance(rect, RectF)
        op = DrawEllipsefOp()
        op.init(rect)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < 34:
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_ELLIPSEF:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_ELLIPSEF)
        bl += self.rect.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 34

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawEllipsefOp)
        return self.rect == other.rect

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawEllipsefOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.rect)


#----------------------------------------------------------------
# Операция "Нарисовать эллипсы с дробными координатами"
#----------------------------------------------------------------

class DrawEllipsesfOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rects = []

    def init(self, rects):
        '''Функция инициализации.'''
        assert isinstance(rects, list)
        self.rects = rects

    @staticmethod
    def create(rects):
        '''Функция создания.'''
        assert isinstance(rects, list)
        op = DrawEllipsesfOp()
        op.init(rects)
        return op

    def add_rect(self, rect):
        '''Добавление прямоугольника.'''
        assert isinstance(rect, RectF)
        self.rects.append(rect)

    def get_rect_count(self):
        '''Получение количество прямоугольников.'''
        return len(self.rects)

    def is_empty(self):
        '''Получение признака изменений.'''
        return self.get_rect_count() == 0

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_ELLIPSESF:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_ELLIPSESF)
        bl += int32_to_byte_list(self.get_rect_count())
        for rect in self.rects:
            bl += rect.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        cbl = byte_list[2:6]
        count = byte_list_to_int32(cbl)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawEllipsesfOp)
        return self.rects == other.rects

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawEllipsesfOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.rects)

    @staticmethod
    def check_lines(rects):
        '''Проверка списка прямоугольников.'''
        if not isinstance(rects, list):
            return False
        if not all([isinstance(rect, RectF) for rect in rects]):
            return False
        return True


#----------------------------------------------------------------
# Операция "Вывод прямоугольника с целочисленными координатами
# со сглаженными углами"
#----------------------------------------------------------------

class DrawRoundRectOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rect = RoundRect()

    def init(self, rect):
        '''Функция инициализации.'''
        assert isinstance(rect, RoundRect)
        self.rect = rect

    @staticmethod
    def create(rect):
        '''Функция создания.'''
        assert isinstance(rect, RoundRect)
        op = DrawRoundRectOp()
        op.init(rect)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_ROUND_RECT:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_ROUND_RECT)
        bl += self.rect.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        rbl = byte_list[2:26]
        rect.from_byte_list(rbl)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 27

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawRoundRectOp)
        return self.rect == other.rect

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawRoundRectOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.rect)


#----------------------------------------------------------------
# Операция "Вывод прямоугольников с целочисленными координатами
# со сглаженными углами"
#----------------------------------------------------------------

class DrawRoundRectsOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rects = []

    def init(self, rects):
        '''Функция инициализации.'''
        assert check_lines(rects)
        self.rects = rects

    @staticmethod
    def create(rects):
        '''Функция создания.'''
        assert check_lines(rects)
        op = DrawRoundRectsOp()
        op.init(rects)
        return op

    def add_rect(self, rect):
        '''Добавление прямоугольника.'''
        assert isinstance(rect, RoundRect)
        self.rects.append(rect)

    def is_empty(self):
        '''Получение признака отсутствия прямоугольников.'''
        return self.get_rect_count() == 0

    def get_rect_count(self):
        '''Получение количества прямоугольников.'''
        return len(self.rects)

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_ROUND_RECTS:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_ROUND_RECTS)
        bl += int32_to_byte_list(self.get_rect_count())
        for rect in self.rects:
            bl += rect.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        cbl = byte_list[2:6]
        count = byte_list_to_int32(byte_list)
        for i in range(count):
            rect = RoundRect()
            rs = rect.get_byte_list_len()
            bbegin = 6 + i * rs
            bend = bbegin + rs
            rbl = byte_list[bbegin:bend]
            rect.from_byte_list(rbl)
            self.add_rect(rect)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawRoundRectsOp)
        return self.rects == other.rects

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawRoundRectsOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.rects)

    @staticmethod
    def check_lines(rects):
        '''Проверка списка прямоугольников.'''
        if not isinstance(rects, list):
            return False
        if not all([isinstance(rect, RoundRect) for rect in rects]):
            return False
        return True
        

#----------------------------------------------------------------
# Операция "Вывод прямоугольника с дробными координатами
# со сглаженными углами"
#----------------------------------------------------------------

class DrawRoundRectfOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rect = RoundRectF()

    def init(self, rect):
        '''Функция инициализации.'''
        assert isinstance(rect, RoundRectF)
        self.rect = rect

    @staticmethod
    def create(rect):
        '''Функция создания.'''
        assert isinstance(rect, RoundRectF)
        op = DrawRoundRectfOp()
        op.init(rect)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_ROUND_RECTF:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_ROUND_RECTF)
        bl += self.rect.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        rbl = byte_list[2:50]
        self.rect.from_byte_list(rbl)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 51

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawRoundRectfOp)
        return self.rect == other.rect

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawRoundRectfOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.rect)


#----------------------------------------------------------------
# Операция "Вывод прямоугольников с дробными координатами
# со сглаженными углами"
#----------------------------------------------------------------

class DrawRoundRectsfOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rects = []

    def init(self, rects):
        '''Функция инициализации.'''
        assert check_lines(rects)
        self.rects = rects

    @staticmethod
    def create(rects):
        '''Функция создания.'''
        assert check_lines(rects)
        op = DrawRoundRectsfOp()
        op.init(rects)
        return op

    def is_empty(self):
        '''Получение признака отсутствия прямоугольников.'''
        return self.get_rect_count() == 0

    def add_rect(self, rect):
        '''Добавление прямоугольника.'''
        assert isinstance(rect, RoundRectF)
        self.rects.append(rect)

    def get_rect_count(self):
        '''Получение количества прямоугольников.'''
        return len(self.rects)

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_ROUND_RECTSF:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_ROUND_RECTSF)
        bl += int32_to_byte_list(self.get_rect_count())
        for rect in self.rects:
            bl += rect.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        assert isinstance(other, DrawRoundRectsfOp)
        return self.rects == other.rects

    def __ne__(self, other):
        '''Оператор !=.'''
        assert isinstance(other, DrawRoundRectsfOp)
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.rects)

    @staticmethod
    def check_lines(rects):
        '''Проверка списка прямоугольников.'''
        if not isinstance(rects, list):
            return False
        if not all([isinstance(rect, RoundRectF) for rect in rects]):
            return False
        return True


#----------------------------------------------------------------
# Операция "Вывод текста"
#----------------------------------------------------------------

class DrawTextOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.text = String()
        self.point = PointF()

    def init(self, text, point):
        '''Функция инициализации.'''
        assert isinstance(text, String)
        assert isinstance(point, PointF)
        self.text = text
        self.point = point

    @staticmethod
    def create(text):
        '''Функция создания.'''
        assert isinstance(text, String)
        assert isinstance(point, PointF)
        op = DrawTextOp()
        op.init(text)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_TEXT:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_TEXT)
        bl += self.text.to_byte_list()
        bl += self.point.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        isEqText = (self.text == other.text)
        isEqPoint = (self.point == other.point)
        return isEqText and isEqPoint

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return self.text


#----------------------------------------------------------------
# Операция "Вывод изображения"
#----------------------------------------------------------------

class DrawImageOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.path = String()
        self.point = PointF()
        self.align = AlignmentFlags.ALIGN_LEFT | AlignmentFlags.ALIGN_TOP

    def init(self, path, point, align):
        '''Функция инициализации.'''
        assert isinstance(path, String)
        assert isinstance(point, PointF)
        assert isinstance(align, int)
        self.path = path
        self.point = point
        self.align = align

    @staticmethod
    def create(path, point, align):
        '''Функция создания.'''
        assert isinstance(path, String)
        assert isinstance(point, PointF)
        assert isinstance(align, int)
        op = DrawImageOp()
        op.init(path, point, align)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < 12:
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_IMAGE:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_IMAGE)
        bl += self.path.to_byte_list()
        bl += self.point.to_byte_list()
        bl += int32_to_byte_list(self.align)
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        # Получение пути
        size_path_bl = byte_list[2:6]
        path_size = byte_list_to_int32(size_path_bl)
        path_begin = 2
        path_end = 6 + path_size
        path_bl = byte_list[path_begin:path_end]
        self.path.from_byte_list(path_bl)
        # Получение точки
        point_begin = path_end
        point_end = point_begin + 16
        point_bl = byte_list[point_begin:point_end]
        self.point.from_byte_list(point_bl)
        # Получение выравнивания
        align_begin = point_end
        align_end = align_begin + 4
        align_bl = byte_list[align_begin:align_end]
        self.align = byte_list_to_int32(align_bl)

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        isEqPath = (self.path == other.path)
        isEqPoint = (self.point == other.point)
        isEqAlign = (self.align == other.align)
        return isEqPath and isEqPoint and isEqAlign

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}, {}'.format(self.path, self.point)


#----------------------------------------------------------------
# Операция "Вывод дуги с целочисленными координатами"
#----------------------------------------------------------------

class DrawArcOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rect = Rect()
        self.startAngle = 0
        self.spanAngle = 0
        
    def init(self, rect, startAngle, spanAngle):
        '''Функция инициализации.'''
        assert isinstance(rect, Rect)
        assert isinstance(startAngle, int)
        assert isinstance(spanAngle, int)
        self.rect = rect
        self.startAngle = startAngle
        self.spanAngle = spanAngle

    @staticmethod
    def create(rect, startAngle, spanAngle):
        '''Функция создания.'''
        assert isinstance(rect, Rect)
        assert isinstance(startAngle, int)
        assert isinstance(spanAngle, int)
        op = DrawArcOp()
        op.init(rect, startAngle, spanAngle)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < 24:
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_ARC:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_ARC)
        bl += rect.to_byte_list()
        bl += int32_to_byte_list(self.startAngle)
        bl += int32_to_byte_list(self.spanAngle)
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert check_byte_list(byte_list)
        pass

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 24

    def __eq__(self, other):
        '''Оператор ==.'''
        isEqRect = (self.rect == other.rect)
        isEqStartAngle = (self.startAngle == other.startAngle)
        isEqSpanAngle= (self.spanAngle == other.spanAngle)
        return isEqRect and isEqStartAngle and isEqSpanAngle

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}, {}, {}'.format(self.rect, self.startAngle, self.spanAngle)


#----------------------------------------------------------------
# Операция "Вывод дуги с дробными координатами"
#----------------------------------------------------------------

class DrawArcfOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.rect = RectF()
        self.startAngle = 0
        self.spanAngle = 0

    def init(self, rect, startAngle, spanAngle):
        '''Функция инициализации.'''
        assert isinstance(rect, RectF)
        assert isinstance(startAngle, int)
        assert isinstance(spanAngle, int)
        self.rect = rect
        self.startAngle = startAngle
        self.spanAngle = spanAngle

    @staticmethod
    def create(rect, startAngle, spanAngle):
        '''Функция создания.'''
        assert isinstance(rect, RectF)
        assert isinstance(startAngle, int)
        assert isinstance(spanAngle, int)
        op = DrawArcfOp()
        op.init(rect, startAngle, spanAngle)
        return op

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < 40:
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_ARCF:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_ARCF)
        bl += rect.to_byte_list()
        bl += int32_to_byte_list(self.startAngle)
        bl += int32_to_byte_list(self.spanAngle)
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return 40

    def __eq__(self, other):
        '''Оператор ==.'''
        isEqRect = (self.rect == other.rect)
        isEqStartAngle = (self.startAngle == other.startAngle)
        isEqSpanAngle= (self.spanAngle == other.spanAngle)
        return isEqRect and isEqStartAngle and isEqSpanAngle

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}, {}, {}'.format(self.rect, self.startAngle, self.spanAngle)


#----------------------------------------------------------------
# Операция "Вывод полигона с целыми координатами"
#----------------------------------------------------------------

class DrawPolygonOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.polygon = Polygon()

    def init(self, polygon):
        '''Функция инициализации.'''
        assert isinstance(polygon, Polygon)
        self.polygon = polygon

    @staticmethod
    def create(polygon):
        '''Функция создания.'''
        assert isinstance(polygon, Polygon)
        op = DrawPolygonOp()
        op.init(polygon)
        return op

    def add_point(self, point):
        '''Добавление точки.'''
        assert isinstance(point, Point)
        self.polygon.add_point(point)

    def get_point_count(self):
        '''Получение количества точек.'''
        return self.polygon.get_point_count()

    def is_empty(self):
        '''Проверка полигона на пустоту.'''
        return self.polygon.is_empty()

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < 6:
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_POLYGON:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_POLYGON)
        bl += self.polygon.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        return self.polygon == other.polygon

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.polygon)


#----------------------------------------------------------------
# Операция "Вывод полигона с дробными координатами"
#----------------------------------------------------------------

class DrawPolygonfOp(object):

    def __init__(self):
        '''Конструктор без параметров.'''
        self.polygon = PolygonF()

    def init(self, polygon):
        '''Функция инициализации.'''
        assert isinstance(polygon, PolygonF)
        self.polygon = polygon

    @staticmethod
    def create(polygon):
        '''Функция создания.'''
        assert isinstance(polygon, PolygonF)
        op = DrawPolygonfOp()
        op.init(polygon)
        return op

    def add_point(self, point):
        '''Добавление точки.'''
        assert isinstance(point, PointF)
        self.polygon.add_point(point)

    def get_point_count(self):
        '''Получение количества точек.'''
        return self.polygon.get_point_count()

    def is_empty(self):
        '''Проверка полигона на пустоту.'''
        return self.polygon.is_empty()

    def check_byte_list(self, byte_list):
        '''Проверка корректности списка байтов для инициализации.'''
        if not check_byte_list(byte_list):
            return False
        if len(byte_list) < 6:
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_POLYGONF:
            return False
        return True

    def to_byte_list(self):
        '''Получение в виде списка байтов.'''
        bl = []
        bl += int16_to_byte_list(DrawOpCodes.DRAW_POLYGONF)
        bl += self.polygon.to_byte_list()
        bl += uint8_to_byte_list(0) # резерв
        return bl

    def from_byte_list(self, byte_list):
        '''Инициализация через список байтов.'''
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self):
        '''Получение длины списка байтов.'''
        return len(self.to_byte_list())

    def __eq__(self, other):
        '''Оператор ==.'''
        return self.polygon == other.polygon

    def __ne__(self, other):
        '''Оператор !=.'''
        return not (self == other)

    def __str__(self):
        '''Получение строкового представления.'''
        return '{}'.format(self.polygon)


#----------------------------------------------------------------
# Функции
#----------------------------------------------------------------

def draw_ops_to_byte_list(operations):
    '''Преобразование последовательности операций в список байтов.'''
    bl = []
    for op in operations:
        bl += op.to_byte_list()
    return bl


def byte_list_to_draw_ops(byte_list):
    '''Преобразование списка байтов в последовательность операций.'''
    ops = []
    while len(byte_list) > 0:
        code = get_draw_op_code(byte_list)
        op = create_draw_op(code)
        op.from_byte_list(byte_list)
        ops.append(op)
        l = op.get_byte_list_len()
        assert l > 0
        byte_list = byte_list[l:]
    return ops


def create_draw_op(code):
    '''Создание операции по коду.'''
    if code == DrawOpCodes.SAVE_STATE:
        return SaveStateOp()
    elif code == DrawOpCodes.RESTORE_STATE:
        return RestoreStateOp()
    elif code == DrawOpCodes.SET_CLIP_RECT:
        return SetClipRectOp()
    elif code == DrawOpCodes.TRANFORM_TRANSLATE:
        return TransformTranslateOp()
    elif code == DrawOpCodes.TRANFORM_ROTATE:
        return TransformRotateOp()
    elif code == DrawOpCodes.TRANFORM_SCALE:
        return TransformScaleOp()
    elif code == DrawOpCodes.SET_PEN:
        return SetPenOp()
    elif code == DrawOpCodes.SET_BRUSH:
        return SetBrushOp()
    elif code == DrawOpCodes.SET_FONT:
        return SetFontOp()
    elif code == DrawOpCodes.SET_ANTIALIASING:
        return SetAntialiasingOp()
    elif code == DrawOpCodes.DRAW_POINT:
        return DrawPointOp()
    elif code == DrawOpCodes.DRAW_POINTS:
        return DrawPointsOp()
    elif code == DrawOpCodes.DRAW_POINTF:
        return DrawPointfOp
    elif code == DrawOpCodes.DRAW_POINTSF:
        return DrawPointsfOp()
    elif code == DrawOpCodes.DRAW_LINE:
        return DrawLineOp()
    elif code == DrawOpCodes.DRAW_LINE:
        return DrawLinesOp()
    elif code == DrawOpCodes.DRAW_LINEF:
        return DrawLinefOp()
    elif code == DrawOpCodes.DRAW_LINESF:
        return DrawLinesfOp()
    elif code == DrawOpCodes.DRAW_POLYLINE:
        return DrawPolylineOp()
    elif code == DrawOpCodes.DRAW_POLYLINEF:
        return DrawPolylinefOp()
    elif code == DrawOpCodes.DRAW_ARC:
        return DrawArcOp()
    elif code == DrawOpCodes.DRAW_ARCF:
        return DrawArcfOp()
    elif code == DrawOpCodes.DRAW_RECT:
        return DrawRectOp()
    elif code == DrawOpCodes.DRAW_RECTS:
        return DarwRectsOp()
    elif code == DrawOpCodes.DRAW_RECTF:
        return DrawRectfOp()
    elif code == DrawOpCodes.DRAW_RECTSF:
        return DrawRectsfOp()
    elif code == DrawOpCodes.DRAW_ROUND_RECT:
        return DrawRoundRectOp()
    elif code == DrawOpCodes.DRAW_ROUND_RECTS:
        return DrawRoundRectsOp()
    elif code == DrawOpCodes.DRAW_ROUND_RECTF:
        return DrawRoundRectfOp()
    elif code == DrawOpCodes.DRAW_ROUND_RECTSF:
        return DrawRoundRectsfOp()
    elif code == DrawOpCodes.DRAW_ELLIPSE:
        return DrawEllipseOp()
    elif code == DrawOpCodes.DRAW_ELLIPSES:
        return DrawEllipsesOp()
    elif code == DrawOpCodes.DRAW_ELLIPSEF:
        return DrawEllipsefOp()
    elif code == DrawOpCodes.DRAW_ELLIPSESF:
        return DrawEllipsesfOp()
    elif code == DrawOpCodes.DRAW_POLYGON:
        return DrawPolygonOp()
    elif code == DrawOpCodes.DRAW_POLYGONF:
        return DrawPolygonfOp()
    elif code == DrawOpCodes.DRAW_IMAGE:
        return DrawImageOp()
    elif code == DrawOpCodes.DRAW_TEXT:
        return DrawTextOp()
    else:
        raise Exception('Bad operation code')


def get_draw_op_code(byte_list):
    '''Получение кода операции из списка байтов.'''
    assert len(byte_list) >= 2
    bc = byte_list[:2]
    code = byte_list_to_int16(bc)
    if 0 <= code < DrawOpCodes.COUNT:
        return code
    else:
        return DrawOpCodes.UNKNOWN


#----------------------------------------------------------------
# Тестирование класса SaveStateOp
#----------------------------------------------------------------

class TestSaveStateOp(object):

    def test_to_byte_list(self):
        op = SaveStateOp()
        bl = op.to_byte_list()
        self.assertTrue(op.is_correct_byte_list(bl))

    def test_from_byte_list(self):
        bl = int16_to_byte_list(DrawOpCodes.SAVE_STATE)
        op = SaveStateOp()
        op.from_byte_list(bl)

    def test_get_byte_list_len(self):
        op = SaveStateOp()
        bl = op.to_byte_list()
        self.assertEqual(op.test_get_byte_list_len(), len(bl))

    def test_equal(self):
        op1 = SaveStateOp()
        self.assertTrue(op1 == op1)

    def test_not_equal(self):
        op1 = SaveStateOp()
        self.assertFalse(op1 != op1)


#----------------------------------------------------------------
# Тестирование класса RestoreStateOp
#----------------------------------------------------------------

class TestRestoreStateOp(object):

    def test_to_byte_list(self):
        op = RestoreStateOp()
        bl = op.to_byte_list()
        self.assertTrue(op.is_correct_byte_list(bl))

    def test_from_byte_list(self):
        bl = int16_to_byte_list(DrawOpCodes.RESTORE_STATE)
        op = RestoreStateOp()
        op.from_byte_list(bl)

    def test_get_byte_list_len(self):
        op = RestoreStateOp()
        bl = op.to_byte_list()
        self.assertEqual(op.get_byte_list_len(), len(bl))

    def test_equal(self):
        op1 = RestoreStateOp()
        self.assertTrue(op1 == op1)
        op2 = RestoreStateOp()
        self.assertTrue(op1 == op2)

    def test_not_equal(self):
        op1 = RestoreStateOp()
        self.assertFalse(op1 != op1)


#----------------------------------------------------------------
# Тестирование класса SetAntialiasingOp
#----------------------------------------------------------------

class TestSetAntialiasingOp(unittest.TestCase):

    def test_constructor(self):
        op = SetAntialiasingOp()
        self.assertFalse(op.antialiasing)

    def test_init(self):
        op = SetAntialiasingOp()
        op.antialiasing = True
        self.assertTrue(op.antialiasing)

    def test_create(self):
        op = SetAntialiasingOp.create(True)
        self.assertTrue(op.antialiasing)

    def test_to_byte_list(self):
        op = SetAntialiasingOp()
        bl = op.to_byte_list()
        self.assertTrue(op.check_byte_list(bl))

    def test_from_byte_list(self):
        op = SetAntialiasingOp()
        bl = op.to_byte_list()
        op.from_byte_list(bl)

    def test_get_byte_list_len(self):
        op = SetAntialiasingOp()
        bl = op.to_byte_list()
        self.assertEqual(op.get_byte_list_len(), len(bl))

    def test_equal(self):
        op1 = SetAntialiasingOp()
        self.assertTrue(op1 == op1)
        op2 = SetAntialiasingOp.create(True)
        self.assertFalse(op1 == op2)

    def test_not_equal(self):
        op1 = SetAntialiasingOp()
        self.assertFalse(op1 != op1)
        op2 = SetAntialiasingOp.create(True)
        self.assertTrue(op1 != op2)


#----------------------------------------------------------------
# Тестирование класса TransformTranslateOp
#----------------------------------------------------------------

class TestTransformTranslateOp(unittest.TestCase):

    def test_constructor(self):
        op = TransformTranslateOp()
        self.assertTrue(float_equal(op.x, 0.0))
        self.assertTrue(float_equal(op.y, 0.0))

    def test_init(self):
        op = TransformTranslateOp()
        op.init(100.0, 100.0)
        self.assertTrue(float_equal(op.x, 100.0))
        self.assertTrue(float_equal(op.y, 100.0))

    def test_create(self):
        op = TransformTranslateOp.create(100.0, 100.0)
        self.assertTrue(float_equal(op.x, 100.0))
        self.assertTrue(float_equal(op.y, 100.0))

    def test_to_byte_list(self):
        op = TransformTranslateOp()
        bl = op.to_byte_list()
        self.assertTrue(op.check_byte_list(bl))

    def test_from_byte_list(self):
        op = TransformTranslateOp()
        op.x = op.y = 1.0
        bl = op.to_byte_list()
        op.from_byte_list(bl)
        self.assertTrue(float_equal(op.x, 1.0))
        self.assertTrue(float_equal(op.y, 1.0))

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        op1 = TransformTranslateOp()
        self.assertTrue(op1 == op1)
        op2 = TransformTranslateOp.create(100.0, 100.0)
        self.assertFalse(op1 == op2)

    def test_not_equal(self):
        op1 = TransformTranslateOp()
        self.assertFalse(op1 != op1)
        op2 = TransformTranslateOp.create(100.0, 100.0)
        self.assertTrue(op1 != op2)


#----------------------------------------------------------------
# Тестирование класса TransformRotateOp
#----------------------------------------------------------------

class TestTransformRotateOp(unittest.TestCase):

    def test_constructor(self):
        op = TransformRotateOp()
        self.assertTrue(float_equal(op.angle, 0.0))

    def test_init(self):
        op = TransformRotateOp()
        op.init(1.5)
        self.assertTrue(float_equal(op.angle, 1.5))

    def test_create(self):
        op = TransformRotateOp.create(1.5)
        self.assertTrue(float_equal(op.angle, 1.5))

    def test_to_byte_list(self):
        op = TransformRotateOp()
        bl = op.to_byte_list()
        self.assertTrue(op.check_byte_list(bl))

    def test_from_byte_list(self):
        op = TransformRotateOp()
        op.angle = 1.0
        bl = op.to_byte_list()
        op.from_byte_list(bl)
        self.assertTrue(float_equal(op.angle, 1.0))

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        op1 = TransformRotateOp()
        self.assertTrue(op1 == op1)
        op2 = TransformRotateOp.create(1.0)
        self.assertFalse(op1 == op2)

    def test_not_equal(self):
        op1 = TransformRotateOp()
        op2 = TransformRotateOp.create(1.0)
        self.assertTrue(op1 != op2)


#----------------------------------------------------------------
# Тестирование класса TransformScaleOp
#----------------------------------------------------------------

class TestTransformScaleOp(unittest.TestCase):

    def test_constructor(self):
        op = TransformScaleOp()
        self.assertTrue(float_equal(op.x, 1.0))
        self.assertTrue(float_equal(op.y, 1.0))

    def test_init(self):
        op = TransformScaleOp()
        op.init(2.0, 2.0)
        self.assertTrue(float_equal(op.x, 2.0))
        self.assertTrue(float_equal(op.y, 2.0))

    def test_create(self):
        op = TransformScaleOp.create(2.0, 2.0)
        self.assertTrue(float_equal(op.x, 2.0))
        self.assertTrue(float_equal(op.y, 2.0))

    def test_to_byte_list(self):
        op = TransformScaleOp()
        bl = op.to_byte_list()
        self.assertTrue(op.check_byte_list(bl))

    def test_from_byte_list(self):
        op = TransformScaleOp()

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        op1 = TransformScaleOp()
        self.assertTrue(op1 == op1)
        op2 = TransformScaleOp.create(2.0, 2.0)
        self.assertFalse(op1 == op2)

    def test_not_equal(self):
        op1 = TransformScaleOp()
        op2 = TransformScaleOp.create(2.0, 2.0)
        self.assertTrue(op1 != op2)


#----------------------------------------------------------------
# Тестирование класса SetFontOp
#----------------------------------------------------------------

class TestSetFontOp(object):

    def test_constructor(self):
        op = SetFontOp()

    def test_init(self):
        op = SetFontOp()

    def test_create(self):
        op = SetFontOp()

    def test_to_byte_list(self):
        op = SetFontOp()
        bl = op.to_byte_list()
        self.assertTrue(op.check_byte_list(bl))

    def test_from_byte_list(self):
        op = SetFontOp()

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        op = SetFontOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        op = SetFontOp()
        self.assertFalse(op != op)


#----------------------------------------------------------------
# Тестирование класса DrawLineOp
#----------------------------------------------------------------

class TestDrawLineOp(unittest.TestCase):

    def test_constructor(self):
        op = DrawLineOp()
        self.assertEqual(op.line, Line())

    def test_init(self):
        op = DrawLineOp()

    def test_init2(self):
        op = DrawLineOp()

    def test_init3(self):
        op = DrawLineOp()

    def test_create(self):
        pass

    def test_create2(self):
        pass

    def test_create3(self):
        pass

    def test_to_byte_list(self):
        op = DrawLineOp()
        bl = op.to_byte_list()
        self.assertTrue(op.check_byte_list(bl))

    def test_from_byte_list(self):
        pass

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        op1 = DrawLineOp()
        self.assertTrue(op1 == op1)
        op2 = DrawLineOp.create3(10, 10, 200, 200)
        self.assertFalse(op1 == op2)

    def test_not_equal(self):
        op1 = DrawLineOp()
        self.assertFalse(op1 != op1)
        op2 = DrawLineOp.create3(10, 10, 200, 200)
        self.assertTrue(op1 != op2)


#----------------------------------------------------------------
# Тестирование класса DrawLinefOp
#----------------------------------------------------------------

class TestDrawLinefOp(unittest.TestCase):

    def test_constructor(self):
        op = DrawLinefOp()

    def test_init(self):
        op = DrawLinefOp()

    def test_init2(self):
        op = DrawLinefOp()

    def test_init3(self):
        op = DrawLinefOp()

    def test_create(self):
        pass

    def test_create2(self):
        pass

    def test_create3(self):
        pass

    def test_to_byte_list(self):
        op = DrawLinefOp()
        bl = op.to_byte_list()
        self.assertTrue(op.check_byte_list(bl))

    def test_from_byte_list(self):
        pass

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        op1 = DrawLinefOp()
        self.assertTrue(op1 == op1)
        op2 = DrawLinefOp.create3(10.0, 10.0, 200.0, 200.0)
        self.assertFalse(op1 == op2)

    def test_not_equal(self):
        op1 = DrawLinefOp()
        self.assertFalse(op1 != op1)
        op2 = DrawLinefOp.create3(10.0, 10.0, 200.0, 200.0)
        self.assertTrue(op1 != op2)


#----------------------------------------------------------------
# Тестирование класса DrawRectOp
#----------------------------------------------------------------

class TestDrawRectOp(unittest.TestCase):

    def test_constructor(self):
        op = DrawRectOp()

    def test_init(self):
        op = DrawRectOp()        

    def test_create(self):
        rect = Rect.create2(10, 10, 300, 300)
        op = DrawRectOp.create(rect)
        self.assertEqual(op.rect, rect)

    def test_to_byte_list(self):
        op = DrawRectOp()
        bl = op.to_byte_list()
        self.assertTrue(op.check_byte_list(bl))

    def test_from_byte_list(self):
        pass

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        op1 = DrawRectOp()
        self.assertTrue(op1 == op1)
        rect = Rect.create2(10, 10, 300, 300)
        op2 = DrawRectOp.create(rect)
        self.assertFalse(op1 == op2)

    def test_not_equal(self):
        op1 = DrawRectOp()
        self.assertFalse(op1 != op1)
        rect = Rect.create2(10, 10, 300, 300)
        op2 = DrawRectOp.create(rect)
        self.assertTrue(op1 != op2)


#----------------------------------------------------------------
# Тестирование класса DrawRectsOp
#----------------------------------------------------------------

class TestDrawRectsOp(unittest.TestCase):

    def test_constructor(self):
        op = DrawRectsOp()

    def test_init(self):
        op = DrawRectsOp()

    def test_create(self):
        rects = [Rect(), Rect(), Rect()]
        op = DrawRectsOp.create(rects)
        self.assertEqual(op.rects, rects)

    def test_to_byte_list(self):
        op = DrawRectsOp()
        bl = op.to_byte_list()
        self.assertTrue(op.check_byte_list(bl))

    def test_from_byte_list(self):
        pass

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        pass

    def test_not_equal(self):
        pass


#----------------------------------------------------------------
# Тестирование класса DrawRectfOp
#----------------------------------------------------------------

class TestDrawRectfOp(unittest.TestCase):

    def test_constructor(self):
        op = DrawRectfOp()
        self.assertEqual(op.rect, RectF())

    def test_init(self):
        op = DrawRectfOp()
        rect = RectF.create2(0.0, 0.0, 200.0, 200.0)
        op.init(rect)
        self.assertEqual(op.rect, rect)

    def test_create(self):
        op = DrawRectfOp()

    def test_to_byte_list(self):
        op = DrawRectfOp()

    def test_from_byte_list(self):
        op = DrawRectfOp()

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        rect1 = RectF.create2(0.0, 0.0, 200.0, 200.0)
        op1 = DrawRectfOp.create(rect1)
        self.assertTrue(op1 == op1)
        rect2 = RectF.create2(10.0, 10.0, 200.0, 200.0)
        op2 = DrawRectfOp.create(rect2)
        self.assertFalse(op1 == op2)

    def test_not_equal(self):
        rect1 = RectF.create2(0.0, 0.0, 200.0, 200.0)
        op1 = DrawRectfOp.create(rect1)
        self.assertFalse(op1 != op1)
        rect2 = RectF.create2(10.0, 10.0, 300.0, 300.0)
        op2 = DrawRectfOp.create(rect2)
        self.assertTrue(op1 != op2)


#----------------------------------------------------------------
# Тестирование класса DrawRectsfOp
#----------------------------------------------------------------

class TestDrawRectsfOp(unittest.TestCase):

    def test_constructor(self):
        op = DrawRectsfOp()
        self.assertEqual(op.rects, [])
        self.assertTrue(op.is_empty())

    def test_init(self):
        op = DrawRectsfOp()

    def test_create(self):
        pass

    def test_to_byte_list(self):
        pass

    def test_from_byte_list(self):
        pass

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        DrawRectsfOp()

    def test_not_equal(self):
        pass


#----------------------------------------------------------------
# Тестирование класса DrawEllipseOp
#----------------------------------------------------------------

class TestDrawEllipseOp(unittest.TestCase):

    def test_constructor(self):
        op = DrawEllipseOp()
        self.assertEqual(op.rect, Rect())

    def test_init(self):
        op = DrawEllipseOp()

    def test_create(self):
        op = DrawEllipseOp()

    def test_to_byte_list(self):
        op = DrawEllipseOp()

    def test_from_byte_list(self):
        op = DrawEllipseOp()

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        op1 = DrawEllipseOp()
        self.assertTrue(op1 == op1)
        rect = Rect.create2(100, 100, 200, 200)
        op2 = DrawEllipseOp.create(rect)
        self.assertFalse(op1 == op2)

    def test_not_equal(self):
        op1 = DrawEllipseOp()
        self.assertFalse(op1 != op1)
        rect = Rect.create2(100, 100, 200, 200)
        op2 = DrawEllipseOp.create(rect)
        self.assertTrue(op1 != op2)


#----------------------------------------------------------------
# Тестирование класса DrawEllipsesOp
#----------------------------------------------------------------

class TestDrawEllipsesOp(unittest.TestCase):

    def test_constructor(self):
        op = DrawEllipsesOp()
        self.assertTrue(op.is_empty())
        self.assertEqual(op.get_rect_count(), 0)

    def test_init(self):
        rects = [Rect(), Rect(), Rect()]
        op = DrawEllipsesOp()

    def test_create(self):
        op = DrawEllipsesOp()

    def test_to_byte_list(self):
        op = DrawEllipsesOp()

    def test_from_byte_list(self):
        op = DrawEllipsesOp()

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        op = DrawEllipsesOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        op = DrawEllipsesOp()
        self.assertFalse(op != op)
    

#----------------------------------------------------------------
# Тестирование класса DrawEllipsefOp
#----------------------------------------------------------------

class TestDrawEllipsefOp(unittest.TestCase):

    def test_constructor(self):
        op = DrawEllipsefOp()
        self.assertEqual(op.rect, RectF())

    def test_init(self):
        op = DrawEllipsefOp()
        rect = RectF.create2(100.0, 100.0, 200.0, 200.0)
        op.init(rect)
        self.assertEqual(op.rect, rect)

    def test_create(self):
        rect = RectF.create2(100.0, 100.0, 200.0, 200.0)
        op = DrawEllipsefOp.create(rect)
        self.assertEqual(op.rect, rect)

    def test_to_byte_list(self):
        op = DrawEllipsefOp()
        bl = op.to_byte_list()
        self.assertTrue(op.check_byte_list(bl))

    def test_from_byte_list(self):
        op = DrawEllipsefOp()

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        op1 = DrawEllipsefOp()
        self.assertTrue(op1 == op1)
        rect = RectF.create2(100.0, 100.0, 200.0, 200.0)
        op2 = DrawEllipsefOp.create(rect)
        self.assertFalse(op1 == op2)

    def test_not_equal(self):
        op1 = DrawEllipsefOp()
        self.assertFalse(op1 != op1)
        rect = RectF.create2(100.0, 100.0, 200.0, 200.0)
        op2 = DrawEllipsefOp.create(rect)
        self.assertTrue(op1 != op2)


#----------------------------------------------------------------
# Тестирование класса DrawEllipsesfOp
#----------------------------------------------------------------

class TestDrawEllipsesfOp(unittest.TestCase):

    def test_constructor(self):
        op = DrawEllipsesfOp()
        self.assertTrue(op.is_empty())

    def test_init(self):
        op = DrawEllipsesfOp()
        rects = [RectF(), RectF(), RectF()]
        op.init(rects)
        self.assertEqual(op.get_rect_count(), len(rects))

    def test_create(self):
        rects = [RectF(), RectF(), RectF()]
        op = DrawEllipsesfOp.create(rects)
        self.assertEqual(op.get_rect_count(), len(rects))

    def test_to_byte_list(self):
        op = DrawEllipsesfOp()
        rects = [RectF(), RectF(), RectF()]
        op.init(rects)
        bl = op.to_byte_list()
        self.assertTrue(op.check_byte_list(bl))

    def test_from_byte_list(self):
        op = DrawEllipsesfOp()

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        op = DrawEllipsesfOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        op = DrawEllipsesfOp()
        self.assertFalse(op != op)


#----------------------------------------------------------------
# Тестирование класса DrawPolylineOp
#----------------------------------------------------------------

class TestDrawPolylineOp(unittest.TestCase):

    def test_constructor(self):
        op = DrawPolylineOp()
        self.assertEqual(op.polyline, Polyline())

    def init(self):
        polyline = Polyline.create([Point()])
        op = DrawPolylineOp()
        op.init(polyline)
        self.assertFalse(op.is_empty())
        self.assertEqual(op.get_point_count(), 1)

    def test_create(self):
        polyline = Polyline.create([Point()])
        op = DrawPolylineOp.create(polyline)
        self.assertFalse(op.is_empty())
        self.assertEqual(op.get_point_count(), 1)

    def test_to_byte_list(self):
        op = DrawPolylineOp()
        bl = op.to_byte_list()
        self.assertTrue(op.check_byte_list(bl))

    def test_from_byte_list(self):
        pass

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        op = DrawPolylineOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        op = DrawPolylineOp()
        self.assertFalse(op != op)


#----------------------------------------------------------------
# Тестирование класса DrawPolylinefOp 
#----------------------------------------------------------------

class TestDrawPolylinefOp(unittest.TestCase):

    def test_constructor(self):
        op = DrawPolylinefOp()
        self.assertEqual(op.polyline, PolylineF())

    def init(self):
        polyline = PolylineF.create([PointF()])
        op = DrawPolylinefOp()
        op.init(polyline)
        self.assertFalse(op.is_empty())
        self.assertEqual(op.get_point_count(), 1)

    def test_create(self):
        polyline = PolylineF.create([PointF()])
        op = DrawPolylinefOp.create(polyline)

    def test_to_byte_list(self):
        pass

    def test_from_byte_list(self):
        pass

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        op = DrawPolylinefOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        op = DrawPolylinefOp()
        self.assertFalse(op != op)


#----------------------------------------------------------------
# Тестирование класса DrawPolygonOp 
#----------------------------------------------------------------

class TestDrawPolygonOp(unittest.TestCase):

    def test_constructor(self):
        op = DrawPolygonOp()
        self.assertEqual(op.polygon, Polygon())

    def init(self):
        polygon = Polygon.create([Point()])
        op = DrawPolygonOp()
        op.init(polygon)
        self.assertEqual(op.polygon, polygon)

    def test_create(self):
        pass

    def test_to_byte_list(self):
        pass

    def test_from_byte_list(self):
        pass

    def test_get_byte_list_len(self):
        pass

    def test_equal(self):
        op = DrawPolygonOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        op = DrawPolygonOp()
        self.assertFalse(op != op)


#----------------------------------------------------------------
# Тестирование класса DrawPolygonfOp 
#----------------------------------------------------------------

class TestDrawPolygonfOp(unittest.TestCase):

    def test_constructor(self):
        op = DrawPolygonfOp()
        self.assertEqual(op.polygon, PolygonF())

    def test_init(self):
        polygon = PolygonF.create([PointF()])
        op = DrawPolygonfOp()
        op.init(polygon)
        self.assertEqual(op.polygon, polygon)

    def test_create(self):
        polygon = PolygonF.create([PointF()])
        op = DrawPolygonfOp.create(polygon)
        self.assertEqual(op.polygon, polygon)

    def test_to_byte_list(self):
        polygon = PolygonF.create([PointF()])
        op = DrawPolygonfOp.create(polygon)
        bl = op.to_byte_list()
        self.assertTrue(op.check_byte_list(bl))
        
    def test_from_byte_list(self):
        pass

    def test_get_byte_list_len(self):
        op = DrawPolygonfOp()

    def test_equal(self):
        op = DrawPolygonfOp()
        self.assertTrue(op == op)
        points = [Point()]

    def test_not_equal(self):
        op = DrawPolygonfOp()
        self.assertFalse(op != op)


#----------------------------------------------------------------
# Вызывается при загрузке модуля главным
#----------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
