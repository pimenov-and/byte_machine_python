"""
ByteMachine.

Операции рисования.
"""
from __future__ import annotations


__author__ = "EnergyLabs"
__version__ = "0.9129"


import unittest
import byte_machine_helper as bmh
import byte_machine_graphics as bmg


class DrawOpCodes:
    """Коды операций рисования."""

    @staticmethod
    def code_to_str(code: int) -> str:
        """Конвертация кода в строку."""
        if code == DrawOpCodes.SAVE_STATE:
            return "SAVE_STATE"
        elif code == DrawOpCodes.RESTORE_STATE:
            return "RESTORE_STATE"
        elif code == DrawOpCodes.SET_CLIP_RECT:
            return "SET_CLIP_RECT"
        elif code == DrawOpCodes.TRANSFORM_TRANSLATE:
            return "TRANSFORM_TRANSLATE"
        elif code == DrawOpCodes.TRANSFORM_ROTATE:
            return "TRANSFORM_ROTATE"
        elif code == DrawOpCodes.TRANSFORM_SCALE:
            return "TRANSFORM_SCALE"
        elif code == DrawOpCodes.SET_PEN:
            return "SET_PEN"
        elif code == DrawOpCodes.SET_BRUSH:
            return "SET_BRUSH"
        elif code == DrawOpCodes.SET_FONT:
            return "SET_FONT"
        elif code == DrawOpCodes.SET_ANTIALIASING:
            return "SET_ANTIALIASING"
        elif code == DrawOpCodes.DRAW_POINT:
            return "DRAW_POINT"
        elif code == DrawOpCodes.DRAW_POINTS:
            return "DRAW_POINTS"
        elif code == DrawOpCodes.DRAW_POINTF:
            return "DRAW_POINTF"
        elif code == DrawOpCodes.DRAW_POINTSF:
            return "DRAW_POINTSF"
        elif code == DrawOpCodes.DRAW_LINE:
            return "DRAW_LINE"
        elif code == DrawOpCodes.DRAW_LINES:
            return "DRAW_LINES"
        elif code == DrawOpCodes.DRAW_LINESF:
            return "DRAW_LINESF"
        elif code == DrawOpCodes.DRAW_LINESF:
            return "DRAW_LINESF"
        elif code == DrawOpCodes.DRAW_POLYLINE:
            return "DRAW_POLYLINE"
        elif code == DrawOpCodes.DRAW_POLYLINEF:
            return "DRAW_POLYLINEF"
        elif code == DrawOpCodes.DRAW_ARC:
            return "DRAW_ARC"
        elif code == DrawOpCodes.DRAW_ARCF:
            return "DRAW_ARCF"
        elif code == DrawOpCodes.DRAW_RECT:
            return "DRAW_RECT"
        elif code == DrawOpCodes.DRAW_RECTS:
            return "DRAW_RECTS"
        elif code == DrawOpCodes.DRAW_RECTF:
            return "DRAW_RECTF"
        elif code == DrawOpCodes.DRAW_RECTSF:
            return "DRAW_RECTSF"
        elif code == DrawOpCodes.DRAW_ROUND_RECT:
            return "DRAW_ROUND_RECT"
        elif code == DrawOpCodes.DRAW_ROUND_RECTS:
            return "DRAW_ROUND_RECTS"
        elif code == DrawOpCodes.DRAW_ROUND_RECTF:
            return "DRAW_ROUND_RECTF"
        elif code == DrawOpCodes.DRAW_ROUND_RECTSF:
            return "DRAW_ROUND_RECTSF"
        elif code == DrawOpCodes.DRAW_ELLIPSE:
            return "DRAW_ELLIPSE"
        elif code == DrawOpCodes.DRAW_ELLIPSES:
            return "DRAW_ELLIPSES"
        elif code == DrawOpCodes.DRAW_ELLIPSEF:
            return "DRAW_ELLIPSEF"
        elif code == DrawOpCodes.DRAW_ELLIPSESF:
            return "DRAW_ELLIPSESF"
        elif code == DrawOpCodes.DRAW_POLYGON:
            return "DRAW_POLYGON"
        elif code == DrawOpCodes.DRAW_POLYGONF:
            return "DRAW_POLYGONF"
        elif code == DrawOpCodes.DRAW_IMAGE:
            return "DRAW_IMAGE"
        elif code == DrawOpCodes.DRAW_TEXT:
            return "DRAW_TEXT"
        else:
            return "UNKNOWN"

    @staticmethod
    def str_to_code(s: str) -> int:
        """Конвертация строки в код."""
        if s == "SAVE_STATE":
            return DrawOpCodes.SAVE_STATE
        elif s == "RESTORE_STATE":
            return DrawOpCodes.RESTORE_STATE
        elif s == "SET_CLIP_RECT":
            return DrawOpCodes.SET_CLIP_RECT
        elif s == "TRANSFORM_TRANSLATE":
            return DrawOpCodes.TRANSFORM_TRANSLATE
        elif s == "TRANSFORM_ROTATE":
            return DrawOpCodes.TRANSFORM_ROTATE
        elif s == "TRANSFORM_SCALE":
            return DrawOpCodes.TRANSFORM_SCALE
        elif s == "SET_PEN":
            return DrawOpCodes.SET_PEN
        elif s == "SET_BRUSH":
            return DrawOpCodes.SET_BRUSH
        elif s == "SET_FONT":
            return DrawOpCodes.SET_FONT
        elif s == "SET_ANTIALIASING":
            return DrawOpCodes.SET_ANTIALIASING
        elif s == "DRAW_POINT":
            return DrawOpCodes.DRAW_POINT
        elif s == "DRAW_POINTS":
            return DrawOpCodes.DRAW_POINTS
        elif s == "DRAW_POINTF":
            return DrawOpCodes.DRAW_POINTF
        elif s == "DRAW_POINTSF":
            return DrawOpCodes.DRAW_POINTSF
        elif s == "DRAW_LINE":
            return DrawOpCodes.DRAW_LINE
        elif s == "DRAW_LINES":
            return DrawOpCodes.DRAW_LINES
        elif s == "DRAW_LINEF":
            return DrawOpCodes.DRAW_LINEF
        elif s == "DRAW_LINESF":
            return DrawOpCodes.DRAW_LINESF
        elif s == "DRAW_POLYLINE":
            return DrawOpCodes.DRAW_POLYLINE
        elif s == "DRAW_POLYLINEF":
            return DrawOpCodes.DRAW_POLYLINEF
        elif s == "DRAW_ARC":
            return DrawOpCodes.DRAW_ARC
        elif s == "DRAW_ARCF":
            return DrawOpCodes.DRAW_ARCF
        elif s == "DRAW_RECT":
            return DrawOpCodes.DRAW_RECT
        elif s == "DRAW_RECTS":
            return DrawOpCodes.DRAW_RECTS
        elif s == "DRAW_RECTF":
            return DrawOpCodes.DRAW_RECTF
        elif s == "DRAW_RECTS":
            return DrawOpCodes.DRAW_RECTS
        elif s == "DRAW_ROUND_RECT":
            return DrawOpCodes.DRAW_ROUND_RECT
        elif s == "DRAW_ROUND_RECTS":
            return DrawOpCodes.DRAW_ROUND_RECTS
        elif s == "DRAW_ROUND_RECTF":
            return DrawOpCodes.DRAW_ROUND_RECTF
        elif s == "DRAW_ROUND_RECTSF":
            return DrawOpCodes.DRAW_ROUND_RECTSF
        elif s == "DRAW_ELLIPSE":
            return DrawOpCodes.DRAW_ELLIPSE
        elif s == "DRAW_ELLIPSES":
            return DrawOpCodes.DRAW_ELLIPSES
        elif s == "DRAW_ELLIPSEF":
            return DrawOpCodes.DRAW_ELLIPSEF
        elif s == "DRAW_ELLIPSESF":
            return DrawOpCodes.DRAW_ELLIPSESF
        elif s == "DRAW_POLYGON":
            return DrawOpCodes.DRAW_POLYGON
        elif s == "DRAW_POLYGONF":
            return DrawOpCodes.DRAW_POLYGONF
        elif s == "DRAW_IMAGE":
            return DrawOpCodes.DRAW_IMAGE
        elif s == "DRAW_TEXT":
            return DrawOpCodes.DRAW_TEXT
        else:
            return DrawOpCodes.UNKNOWN

    @staticmethod
    def get_values() -> tuple:
        """Получение набора значений в виде кортежа."""
        return (DrawOpCodes.UNKNOWN,
                DrawOpCodes.RESTORE_STATE,
                DrawOpCodes.SET_CLIP_RECT,
                DrawOpCodes.TRANSFORM_TRANSLATE,
                DrawOpCodes.TRANSFORM_ROTATE,
                DrawOpCodes.TRANSFORM_SCALE,
                DrawOpCodes.SET_PEN,
                DrawOpCodes.SET_BRUSH,
                DrawOpCodes.SET_FONT,
                DrawOpCodes.SET_ANTIALIASING,
                DrawOpCodes.DRAW_POINT,
                DrawOpCodes.DRAW_POINTS,
                DrawOpCodes.DRAW_POINTF,
                DrawOpCodes.DRAW_POINTSF,
                DrawOpCodes.DRAW_LINE,
                DrawOpCodes.DRAW_LINES,
                DrawOpCodes.DRAW_LINEF,
                DrawOpCodes.DRAW_LINESF,
                DrawOpCodes.DRAW_POLYLINE,
                DrawOpCodes.DRAW_POLYLINEF,
                DrawOpCodes.DRAW_ARC,
                DrawOpCodes.DRAW_ARCF,
                DrawOpCodes.DRAW_RECT,
                DrawOpCodes.DRAW_RECTS,
                DrawOpCodes.DRAW_RECTF,
                DrawOpCodes.DRAW_RECTSF,
                DrawOpCodes.DRAW_ROUND_RECT,
                DrawOpCodes.DRAW_ROUND_RECTS,
                DrawOpCodes.DRAW_ROUND_RECTF,
                DrawOpCodes.DRAW_ROUND_RECTSF,
                DrawOpCodes.DRAW_ELLIPSE,
                DrawOpCodes.DRAW_ELLIPSES,
                DrawOpCodes.DRAW_ELLIPSEF,
                DrawOpCodes.DRAW_ELLIPSESF,
                DrawOpCodes.DRAW_POLYGON,
                DrawOpCodes.DRAW_POLYGONF,
                DrawOpCodes.DRAW_IMAGE,
                DrawOpCodes.DRAW_TEXT)

    @staticmethod
    def is_correct_value(value: int) -> bool:
        """Проверка корректности значения."""
        assert isinstance(value, int)
        return value in DrawOpCodes.get_values()

    @staticmethod
    def get_count() -> int:
        """Получение количества значений."""
        return 38

    UNKNOWN = -1
    SAVE_STATE = 0
    RESTORE_STATE = 1
    SET_CLIP_RECT = 2
    TRANSFORM_TRANSLATE = 3
    TRANSFORM_ROTATE = 4
    TRANSFORM_SCALE = 5
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


class HorzAlignFlags:
    """Горизонтальные флаги выравнивания."""

    @staticmethod
    def flag_to_str(flag: int) -> str:
        """Конвертация флага в строку."""
        if flag == HorzAlignFlags.LEFT:
            return "LEFT"
        elif flag == HorzAlignFlags.CENTER:
            return "CENTER"
        elif flag == HorzAlignFlags.RIGHT:
            return "RIGHT"
        else:
            return "UNKNOWN"

    @staticmethod
    def str_to_flag(s: str) -> int:
        """Конвертация строки во флаг."""
        if s == "LEFT":
            return HorzAlignFlags.LEFT
        elif s == "CENTER":
            return HorzAlignFlags.CENTER
        elif s == "RIGHT":
            return HorzAlignFlags.RIGHT
        else:
            return HorzAlignFlags.UNKNOWN

    @staticmethod
    def get_values() -> tuple:
        """Получение набора значений в виде кортежа."""
        return (HorzAlignFlags.UNKNOWN, HorzAlignFlags.LEFT,
                HorzAlignFlags.CENTER, HorzAlignFlags.RIGHT)

    @staticmethod
    def is_correct_value(value: int) -> bool:
        """Проверка корректности значения."""
        assert isinstance(value, int)
        return value in HorzAlignFlags.get_values()

    @staticmethod
    def get_count() -> int:
        """Получение количества значений."""
        return 4

    UNKNOWN = -1
    LEFT = 0
    CENTER = 1
    RIGHT = 2


class VertAlignFlags:
    """Вертикальные флаги выравнивания."""

    @staticmethod
    def flag_to_str(flag: int) -> str:
        """Конвертация флага в строку."""
        if flag == VertAlignFlags.TOP:
            return "TOP"
        elif flag == VertAlignFlags.CENTER:
            return "CENTER"
        elif flag == VertAlignFlags.BOTTOM:
            return "BOTTOM"
        else:
            return "UNKNOWN"

    @staticmethod
    def str_to_flag(s: str) -> int:
        """Конвертация строки во флаг."""
        if s == "TOP":
            return VertAlignFlags.TOP
        elif s == "CENTER":
            return VertAlignFlags.CENTER
        elif s == "BOTTOM":
            return VertAlignFlags.BOTTOM
        else:
            return VertAlignFlags.UNKNOWN

    @staticmethod
    def get_values() -> tuple:
        """Получение набора значений в виде кортежа."""
        return (VertAlignFlags.UNKNOWN, VertAlignFlags.TOP,
                VertAlignFlags.CENTER, VertAlignFlags.BOTTOM)

    @staticmethod
    def is_correct_value(value: int) -> bool:
        """Проверка корректности значения."""
        assert isinstance(value, int)
        return value in VertAlignFlags.get_values()

    @staticmethod
    def get_count() -> int:
        """Получение количества значений."""
        return 4

    UNKNOWN = -1
    TOP = 0
    CENTER = 1
    BOTTOM = 2


class AlignFlags:
    """Флаги выравнивания."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.horz_align = HorzAlignFlags.LEFT
        self.vert_align = VertAlignFlags.TOP

    def init(self, horz_align: int, vert_align: int) -> None:
        """Функция инициализации."""
        assert isinstance(horz_align, int)
        assert isinstance(vert_align, int)
        self.horz_align = horz_align
        self.vert_align = vert_align

    @staticmethod
    def create(horz_align: int, vert_align: int) -> AlignFlags:
        """Функция создания."""
        flags = AlignFlags()
        flags.init(horz_align, vert_align)
        return flags

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 2:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int8_to_byte_array(self.horz_align)
        ba += bmg.bmc.int8_to_byte_array(self.vert_align)
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        self.horz_align = byte_array[0]
        self.vert_align = byte_array[1]

    def get_byte_array_len(self) -> int:
        """Получение длины массива байтов."""
        return 2

    def __eq__(self, other: AlignFlags) -> bool:
        """Оператор ==."""
        assert isinstance(other, AlignFlags)
        is_eq_horz_align = self.horz_align == other.horz_align
        is_eq_vert_align = self.vert_align == other.vert_align
        return is_eq_horz_align and is_eq_vert_align

    def __ne__(self, other: AlignFlags) -> bool:
        """Оператор !=."""
        assert isinstance(other, AlignFlags)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        str_horz_align = HorzAlignFlags.flag_to_str(self.horz_align)
        str_vert_align = VertAlignFlags.flag_to_str(self.vert_align)
        return str_horz_align + "|" + str_vert_align


class SaveStateOp:
    """Операция "Сохранения состояния"."""

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.SAVE_STATE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.SAVE_STATE)
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        #  reserve = byte_array[2:3]

    def get_byte_array_len(self) -> int:
        """Получение длины массива байтов."""
        return 3

    def __eq__(self, other: SaveStateOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, SaveStateOp)
        return True

    def __ne__(self, other: SaveStateOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, SaveStateOp)
        return False


class RestoreStateOp:
    """Операция "Восстановление состояния"."""

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.RESTORE_STATE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.RESTORE_STATE)
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        #  reserve = byte_array[2:3]

    def get_byte_array_len(self) -> int:
        """Получение длины массива байтов."""
        return 3

    def __eq__(self, other: RestoreStateOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, RestoreStateOp)
        return True

    def __ne__(self, other: RestoreStateOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, RestoreStateOp)
        return False


class SetClipRectOp:
    """Операция "Задание прямоугольника отсечения"."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.rect = bmg.Rect()

    def init(self, rect: bmg.Rect) -> None:
        """Функция инициализации."""
        assert isinstance(rect, bmg.Rect)
        self.rect = rect

    @staticmethod
    def create(rect: bmg.Rect) -> SetClipRectOp:
        """Функция создания."""
        assert isinstance(rect, bmg.Rect)
        op = SetClipRectOp()
        op.init(rect)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.SET_CLIP_RECT:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.int16_to_byte_array(DrawOpCodes.SET_CLIP_RECT)
        ba += self.rect.to_byte_array()
        ba += bmg.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        bar = byte_array[2:18]
        self.rect.from_byte_array(bar)
        #  reverse = byte_array[18:19]

    def get_byte_array_len(self) -> int:
        """Получение длины массива байтов."""
        return 19

    def __eq__(self, other: SetClipRectOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, SetClipRectOp)
        return self.rect == other.rect

    def __ne__(self, other: SetClipRectOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, SetClipRectOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.rect}"


class TransformTranslateOp:
    """Операция "Трансформация - перенос"."""

    def __init__(self) -> None:
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
    def create(x: float, y: float) -> TransformTranslateOp:
        """Функция создания."""
        assert isinstance(x, float)
        assert isinstance(y, float)
        op = TransformTranslateOp()
        op.init(x, y)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.TRANSFORM_TRANSLATE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.TRANSFORM_TRANSLATE)
        ba += bmg.bmc.double_to_byte_array(self.x)
        ba += bmg.bmc.double_to_byte_array(self.y)
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        ba = byte_array[2:18]
        data = bmg.bmc.byte_array_to_double_list(ba)
        self.x = data[0]
        self.y = data[1]
        #  reverse = byte_array[18:19]

    def get_byte_array_len(self) -> int:
        """Получение длины массива байтов."""
        return 19

    def __eq__(self, other: TransformTranslateOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, TransformTranslateOp)
        is_eq_x = bmh.float_equal(self.x, other.x)
        is_eq_y = bmh.float_equal(self.y, other.y)
        return is_eq_x and is_eq_y

    def __ne__(self, other: TransformTranslateOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, TransformTranslateOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.x}, {self.y}"


class TransformRotateOp:
    """Операция "Трансформация - поворот"."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.angle = 0.0

    def init(self, angle: float) -> None:
        """Функция инициализации."""
        assert isinstance(angle, float)
        self.angle = angle

    @staticmethod
    def create(angle: float) -> TransformRotateOp:
        """Функция создания."""
        assert isinstance(angle, float)
        op = TransformRotateOp()
        op.init(angle)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.TRANSFORM_ROTATE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.TRANSFORM_ROTATE)
        ba += bmg.bmc.double_to_byte_array(self.angle)
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        ba = byte_array[2:10]
        self.angle = bmg.bmc.byte_array_to_double(ba)
        #  reserve = byte_array[10:11]

    def get_byte_array_len(self) -> int:
        """Получение длины массива байтов."""
        return 11

    def __eq__(self, other: TransformRotateOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, TransformRotateOp)
        return bmh.float_equal(self.angle, other.angle)

    def __ne__(self, other: TransformRotateOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, TransformRotateOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.angle}"


class TransformScaleOp:
    """Операция "Трансформация - масштабирование"."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.x = 1.0
        self.y = 1.0

    def init(self, x: float, y: float) -> None:
        """Функция инициализации."""
        assert isinstance(x, float)
        assert isinstance(y, float)
        self.x = x
        self.y = y

    @staticmethod
    def create(x, y):
        """Функция создания."""
        assert isinstance(x, float)
        assert isinstance(y, float)
        op = TransformScaleOp()
        op.init(x, y)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.TRANSFORM_SCALE:
            return False
        return True

    def to_byte_array(self):
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.TRANSFORM_SCALE)
        ba += bmg.bmc.double_to_byte_array(self.x)
        ba += bmg.bmc.double_to_byte_array(self.y)
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализации через список байтов."""
        assert self.check_byte_array(byte_array)
        ba = byte_array[2:18]
        bc = bmg.bmc.byte_array_to_double_list(ba)
        self.x = bc[0]
        self.y = bc[1]
        #  reserve = byte_array[18:19]

    def get_byte_array_len(self):
        """Получение длины списка байтов."""
        return 19

    def __eq__(self, other) -> bool:
        """Функция проверки на равенство."""
        assert isinstance(other, TransformScaleOp)
        is_eq_x = bmh.float_equal(self.x, other.x)
        is_eq_y = bmh.float_equal(self.y, other.y)
        return is_eq_x and is_eq_y

    def __ne__(self, other) -> bool:
        """Оператор !=."""
        assert isinstance(other, TransformScaleOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.x}, {self.y}"


class SetAntialiasingOp:
    """Операция "Задание сглаживания"."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.antialiasing = False

    def init(self, antialiasing: bool) -> None:
        """Функция инициализации."""
        assert isinstance(antialiasing, bool)
        self.antialiasing = antialiasing

    @staticmethod
    def create(antialiasing: bool) -> SetAntialiasingOp:
        """Функция создания."""
        assert isinstance(antialiasing, bool)
        op = SetAntialiasingOp()
        op.init(antialiasing)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.SET_ANTIALIASING:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.SET_ANTIALIASING)
        ba += bmg.bmc.bool_to_byte_array(self.antialiasing)
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        ba = byte_array[2:3]
        self.antialiasing = bmg.bmc.byte_array_to_bool(ba)
        #  reverse = byte_array[3:4]

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 4

    def __eq__(self, other: SetAntialiasingOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, SetAntialiasingOp)
        return self.antialiasing == other.antialiasing

    def __ne__(self, other: SetAntialiasingOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, SetAntialiasingOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.antialiasing}"


class SetPenOp:
    """Операция "Задать перо"."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.pen = bmg.Pen()

    def init(self, pen: bmg.Pen) -> None:
        """Функция инициализации."""
        assert isinstance(pen, bmg.Pen)
        self.pen = pen

    @staticmethod
    def create(pen: bmg.Pen) -> SetPenOp:
        """Функция создания."""
        assert isinstance(pen, bmg.Pen)
        op = SetPenOp()
        op.pen = pen
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.SET_PEN:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.SET_PEN)
        ba += self.pen.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через массив байтов."""
        assert self.check_byte_array(byte_array)
        bap = byte_array[2:13]
        self.pen.from_byte_array(bap)
        #  reverse = byte_array[13:14]

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 14

    def __eq__(self, other: SetPenOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, SetPenOp)
        return self.pen == other.pen

    def __ne__(self, other: SetPenOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, SetPenOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления объекта."""
        return f"{self.pen}"


class SetBrushOp:
    """Операция "Задать кисть"."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.brush = bmg.Brush()

    def init(self, brush: bmg.Brush) -> None:
        """Функция инициализации."""
        assert isinstance(brush, bmg.Brush)
        self.brush = brush

    @staticmethod
    def create(brush: bmg.Brush) -> SetBrushOp:
        """Функция создания."""
        assert isinstance(brush, bmg.Brush)
        op = SetBrushOp()
        op.init(brush)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.SET_BRUSH:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.SET_BRUSH)
        ba += self.brush.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        bb = byte_array[2:7]
        self.brush.from_byte_array(bb)
        #  reverse = byte_array[7:8]

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 8

    def __eq__(self, other: SetBrushOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, SetBrushOp)
        return self.brush == other.brush

    def __ne__(self, other: SetBrushOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, SetBrushOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления объекта."""
        return f"{self.brush}"


class SetFontOp:
    """Операция "Задание шрифта"."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.font = bmg.Font()

    def init(self, font: bmg.Font) -> None:
        """Функция инициализации."""
        assert isinstance(font, bmg.Font)
        self.font = font

    @staticmethod
    def create(font: bmg.Font) -> SetFontOp:
        """Функция создания."""
        op = SetFontOp()
        op.init(font)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 2:
            return False
        if get_op_code(byte_array) != DrawOpCodes.SET_FONT:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.SET_FONT)
        ba += self.font.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        baf = byte_array[2:]
        self.font.from_byte_array(baf)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: SetFontOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, SetFontOp)
        return self.font == other.font

    def __ne__(self, other: SetFontOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, SetFontOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления объекта."""
        return f"{self.brush}"


class DrawPointOp:
    """Операция "Нарисовать точку с целочисленными координатами"."""

    def __init__(self):
        """Конструктор без параметров."""
        self.point = bmg.Point()

    def init(self, point: bmg.Point) -> None:
        """Функция ицнициализации."""
        assert isinstance(point, bmg.Point)
        self.point = point

    @staticmethod
    def create(point: bmg.Point) -> DrawPointOp:
        """Функция создания."""
        assert isinstance(point, bmg.Point)
        op = DrawPointOp()
        op.init(point)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_POINT:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_POINT)
        ba += self.point.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        bap = byte_array[2:10]
        self.point.from_byte_array(bap)
        #  reserve = byte_array[10:11]

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 11

    def __eq__(self, other: DrawPointOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawPointOp)
        return self.point == other.point

    def __ne__(self, other: DrawPointOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawPointOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.point}"


class DrawPointsOp:
    """Операция "Нарисовать набор точек с целочисленными координатами"."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.points = []

    def init(self, points) -> None:
        """Функция ицнициализации."""
        self.points = points

    @staticmethod
    def create(points: list) -> DrawPointsOp:
        """Функция создания."""
        assert isinstance(points, list)
        op = DrawPointsOp()
        op.init(points)
        return op

    def add_point(self, point: bmg.Point) -> None:
        """Функция добавления точки."""
        assert isinstance(point, bmg.Point)
        self.points.append(point)

    def get_point_count(self) -> int:
        """Получение количества точек."""
        return len(self.points)

    def is_empty(self) -> bool:
        """Получение признака отсутствия точек."""
        return self.get_point_count() == 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_POINTS:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_POINTS)
        ba += bmg.bmc.int32_to_byte_array(self.get_point_count())
        for p in self.points:
            ba += p.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        cbl = byte_array[2:6]
        count = bmg.bmc.byte_array_to_int32(cbl)
        point_len = bmg.Point().get_byte_array_len()
        offset = 6
        self.points = []
        for i in range(count):
            p = bmg.Point()
            pbl = byte_array[offset:offset + point_len]
            p.from_byte_array(pbl)
            self.add_point(p)
            offset += point_len

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: DrawPointsOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawPointsOp)
        return self.points == other.points

    def __ne__(self, other: DrawPointsOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawPointsOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.points}"


class DrawPointfOp:
    """Операция "Нарисовать точку с дробными координатами"."""

    def __init__(self):
        """Конструктор без параметров."""
        self.point = bmg.PointF()

    def init(self, point: bmg.PointF) -> None:
        """Функция инициализации."""
        assert isinstance(point, bmg.PointF)
        self.point = point

    @staticmethod
    def create(point: bmg.PointF) -> DrawPointfOp:
        """Функция создания."""
        assert isinstance(point, bmg.PointF)
        op = DrawPointfOp()
        op.init(point)
        return op

    def check_byte_array(self, byte_array):
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_POINTF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_POINTF)
        ba += self.point.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        bap = byte_array[2:18]
        self.point.from_byte_array(bap)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 19

    def __eq__(self, other: DrawPointfOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawPointfOp)
        return self.point == other.point

    def __ne__(self, other: DrawPointfOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawPointfOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.point}"


class DrawPointsfOp:
    """Операция "Нарисовать точки с дробными координатами"."""

    def __init__(self):
        """Конструктор по умолчанию."""
        self.points = []

    def init(self, points: list) -> None:
        """Функция ицнициализации."""
        assert isinstance(points, list)
        self.points = points

    @staticmethod
    def create(points: list) -> DrawPointsfOp:
        """Функция создания."""
        assert isinstance(points, list)
        op = DrawPointsfOp()
        op.init(points)
        return op

    def get_point_count(self):
        """Получение количества точек."""
        return len(self.points)

    def add_point(self, point: bmg.PointF) -> None:
        """Добавление точки."""
        assert isinstance(point, bmg.PointF)
        self.points.append(point)

    def is_empty(self) -> bool:
        """Получение признака отсутствия точек."""
        return len(self.points) == 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_POINTSF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_POINTSF)
        ba += bmg.bmc.int32_to_byte_array(self.get_point_count())
        for p in self.points:
            ba += p.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        cbl = byte_array[2:6]
        count = bmg.bmc.byte_array_to_int32(cbl)
        point_len = bmg.PointF().get_byte_array_len()
        offset = 6
        self.points = []
        for i in range(count):
            p = bmg.PointF()
            pbl = byte_array[offset:offset + point_len]
            p.from_byte_array(pbl)
            self.add_point(p)
            offset += point_len

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: DrawPointsfOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawPointsfOp)
        return self.points == other.points

    def __ne__(self, other: DrawPointsfOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawPointsfOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.points}"


class DrawLineOp:
    """Операция "Нарисовать линию с целочисленными коордиинатами"."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.line = bmg.Line()

    def init(self, line: bmg.Line) -> None:
        """Функция инициализации."""
        assert isinstance(line, bmg.Line)
        self.line = line

    def init_2(self, pt_1: bmg.Line, pt_2: bmg.Line) -> None:
        """Функция инициализации."""
        assert isinstance(pt_1, bmg.Point)
        assert isinstance(pt_2, bmg.Point)
        self.line = bmg.Line.create(pt_1, pt_2)

    def init_3(self, x_1: int, y_1: int, x_2: int, y_2: int) -> None:
        """Функция инициализации."""
        assert isinstance(x_1, int)
        assert isinstance(y_1, int)
        assert isinstance(x_2, int)
        assert isinstance(y_2, int)
        self.line = bmg.Line.create_2(x_1, y_1, x_2, y_2)

    @staticmethod
    def create(line: bmg.Line) -> DrawLineOp:
        """Функция создания."""
        assert isinstance(line, bmg.Line)
        op = DrawLineOp()
        op.init(line)
        return op

    @staticmethod
    def create_2(pt_1: bmg.Point, pt_2: bmg.Point) -> DrawLineOp:
        """Функция создания."""
        assert isinstance(pt_1, bmg.Point)
        assert isinstance(pt_2, bmg.Point)
        op = DrawLineOp()
        op.init_2(pt_1, pt_2)
        return op

    @staticmethod
    def create_3(x1: int, y1: int, x2: int, y2: int) -> DrawLineOp:
        """Функция создания."""
        assert isinstance(x1, int)
        assert isinstance(y1, int)
        assert isinstance(x2, int)
        assert isinstance(y2, int)
        op = DrawLineOp()
        op.init_3(x1, y1, x2, y2)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_LINE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_LINE)
        ba += self.line.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        ba = byte_array[2:18]
        self.line.from_byte_array(ba)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 19

    def __eq__(self, other: DrawLineOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawLineOp)
        return self.line == other.line

    def __ne__(self, other: DrawLineOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawLineOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.line}"


class DrawLinesOp:
    """Операция "Нарисовать линии с целыми координатами"."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.lines = []

    def init(self, lines: list) -> None:
        """Функция инициализации."""
        assert DrawLinesOp._check_lines(lines)
        self.lines = lines

    def create(lines: list) -> DrawLinesOp:
        """Функция создания."""
        assert DrawLinesOp._check_lines(lines)
        op = DrawLinesOp()
        op.init(lines)
        return op

    def add_line(self, line: bmg.Line):
        """Функция добавления линий."""
        assert isinstance(line, bmg.Line)
        self.lines.append(line)

    def get_line_count(self):
        """Получение количества линий."""
        return len(self.lines)

    def is_empty(self):
        """Получение признака отсуствия линий."""
        return self.get_line_count() == 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 6:
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_LINES:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_LINES)
        ba += bmg.bmc.int32_to_byte_array(self.get_line_count())
        for line in self.lines:
            ba += line.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        basz = byte_array[2:6]
        sz = bmg.bmc.byte_array_to_int32(basz)
        line_len = bmg.Line().get_byte_array_len()
        self.lines = []
        offset = 6
        for i in range(sz):
            line = bmg.Line()
            lbl = byte_array[offset:offset + line_len]
            line.from_byte_array(lbl)
            self.add_point(line)
            offset += line_len

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: DrawLinesOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawLinesOp)
        return self.lines == other.lines

    def __ne__(self, other: DrawLinesOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawLinesOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.lines}"

    @staticmethod
    def _check_lines(lines):
        """Проверка списка точек."""
        if not isinstance(lines, list):
            return False
        if not all([isinstance(line, bmg.Line) for line in lines]):
            return False
        return True


class DrawLinefOp:
    """Операция "Нарисовать линию с дробными координатами"."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.line = bmg.LineF()

    def init(self, line: bmg.LineF) -> None:
        """Функция инициализации."""
        assert isinstance(line, bmg.LineF)
        self.line = line

    def init_2(self, pt_1: bmg.PointF, pt_2: bmg.PointF) -> None:
        """Функция инициализации 2."""
        assert isinstance(pt_1, bmg.PointF)
        assert isinstance(pt_2, bmg.PointF)
        self.line = bmg.LineF.create(pt_1, pt_2)

    def init_3(self, x_1: float, y_1: float, x_2: float, y_2: float) -> None:
        """Функция инициализации 3."""
        assert isinstance(x_1, float)
        assert isinstance(y_1, float)
        assert isinstance(x_2, float)
        assert isinstance(y_2, float)
        self.line = bmg.LineF.create_2(x_1, y_1, x_2, y_2)

    @staticmethod
    def create(line: bmg.LineF) -> DrawLinefOp:
        """Функция создания."""
        assert isinstance(line, bmg.LineF)
        op = DrawLinefOp()
        op.init(line)
        return op

    @staticmethod
    def create_2(pt_1: bmg.PointF, pt_2: bmg.PointF) -> DrawLinefOp:
        """Функция создания 2."""
        assert isinstance(pt_1, bmg.PointF)
        assert isinstance(pt_2, bmg.PointF)
        op = DrawLinefOp()
        op.init_2(pt_1, pt_2)
        return op

    @staticmethod
    def create_3(x_1: float, y_1: float, x_2: float, y_2: float) -> DrawLinefOp:
        """Функция создания 3."""
        assert isinstance(x_1, float)
        assert isinstance(y_1, float)
        assert isinstance(x_2, float)
        assert isinstance(y_2, float)
        op = DrawLinefOp()
        op.init_3(x_1, y_1, x_2, y_2)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_LINEF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_LINEF)
        ba += self.line.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        ba = byte_array[2:34]
        self.line.from_byte_array(ba)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 35

    def __eq__(self, other: DrawLinefOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawLinefOp)
        return self.line == other.line

    def __ne__(self, other: DrawLinefOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawLinefOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.line}"


class DrawLinesfOp:
    """Операция "Нарисовать линии с дробными координатами"."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.lines = []

    def init(self, lines: list) -> None:
        """Функция инициализации."""
        assert DrawLinesfOp._check_lines(lines)
        self.lines = lines

    @staticmethod
    def create(lines: list) -> DrawLinesfOp:
        """Функция создания."""
        assert DrawLinesfOp._check_lines(lines)
        op = DrawLinesfOp()
        op.init(lines)
        return op

    def add_line(self, line: bmg.LineF) -> None:
        """Добавление линии."""
        assert isinstance(line, bmg.LineF)
        self.lines.append(line)

    def get_line_count(self) -> int:
        """Получение количества линий."""
        return len(self.lines)

    def is_empty(self) -> bool:
        """Получение признака отсуствия линий."""
        return self.get_line_count() == 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 6:
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_LINEF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_LINESF)
        ba += bmg.bmc.int32_to_byte_array(self.get_line_count())
        for line in self.lines:
            ba += line.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert DrawLinesfOp.check_byte_array(byte_array)
        basz = byte_array[2:6]
        sz = bmg.bmc.byte_array_to_int32(basz)
        self.lines = []
        line_len = bmg.LineF().get_byte_array_len()
        offset = 6
        for i in range(sz):
            line = bmg.Line()
            lbl = byte_array[offset:offset + line_len]
            line.from_byte_array(lbl)
            self.add_line(line)
            offset += line_len

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: DrawLinesfOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawLinesfOp)
        return self.lines == other.lines

    def __ne__(self, other: DrawLinesfOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawLinesfOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.lines}"

    @staticmethod
    def _check_lines(lines: list) -> bool:
        """Проверка списка точек."""
        if not isinstance(lines, list):
            return False
        if not all([isinstance(line, bmg.LineF) for line in lines]):
            return False
        return True


class DrawPolylineOp:
    """Операция "Нарисовать ломаную линию с целочисленными координатами"."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.polyline = bmg.Polyline()

    def init(self, polyline: bmg.Polyline) -> None:
        """Функция инициализации."""
        assert isinstance(polyline, bmg.Polyline)
        self.polyline = polyline

    @staticmethod
    def create(polyline: bmg.Polyline) -> DrawPolylineOp:
        """Функция создания."""
        assert isinstance(polyline, bmg.Polyline)
        op = DrawPolylineOp()
        op.init(polyline)
        return op

    def add_point(self, point: bmg.Point) -> None:
        """Функция добавления линий."""
        assert isinstance(point, bmg.Point)
        self.polyline.add_point(point)

    def get_point_count(self) -> int:
        """Получение количества линий."""
        return self.polyline.get_point_count()

    def is_empty(self) -> bool:
        """Получение признака отсуствия линий."""
        return self.polyline.is_empty()

    def check_byte_array(self, byte_array):
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 6:
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_POLYLINE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_POLYLINE)
        ba += self.polyline.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawPolylineOp)
        return self.polyline == other.polyline

    def __ne__(self, other) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawPolylineOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.polyline}"


class DrawPolylinefOp:
    """Операция "Нарисовать ломаную линию с дробными координатами"."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.polyline = bmg.PolylineF()

    def init(self, polyline: bmg.PolylineF) -> None:
        """Функция инициализации."""
        assert isinstance(polyline, bmg.PolylineF)
        self.polyline = polyline

    @staticmethod
    def create(polyline: bmg.Polyline) -> DrawPolylinefOp:
        """Функция создания."""
        assert isinstance(polyline, bmg.PolylineF)
        op = DrawPolylinefOp()
        op.init(polyline)
        return op

    def add_point(self, point: bmg.PointF) -> None:
        """Функция добавления линий."""
        assert isinstance(point, bmg.PointF)
        self.polyline.add_point(point)

    def is_empty(self) -> bool:
        """Получение признака отсутствия точек."""
        return self.polyline.is_empty()

    def get_point_count(self) -> int:
        """Получение количества точек."""
        return self.polyline.get_point_count()

    def check_byte_array(self, byte_array):
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 6:
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_POLYLINE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_POLYLINEF)
        ba += self.polyline.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        bapl = byte_array[:2]
        self.polyline.from_byte_array(bapl)

    def get_byte_array_len(self):
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: DrawPolylinefOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawPolylinefOp)
        return self.polyline == other.polyline

    def __ne__(self, other: DrawPolylinefOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawPolylinefOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.polyline}"


class DrawRectOp:
    """Операция "Нарисовать прямоугольник"."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.rect = bmg.Rect()

    def init(self, rect: bmg.Rect) -> None:
        """Функция инициализации."""
        assert isinstance(rect, bmg.Rect)
        self.rect = rect

    @staticmethod
    def create(rect: bmg.Rect) -> DrawRectOp:
        """Функция создания."""
        assert isinstance(rect, bmg.Rect)
        op = DrawRectOp()
        op.init(rect)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_RECT:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_RECT)
        ba += self.rect.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 19

    def __eq__(self, other: DrawRectOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawRectOp)
        return self.rect == other.rect

    def __ne__(self, other: DrawRectOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawRectOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.rect}"


class DrawRectsOp:
    """Операция "Нарисовать прямоугольники с целочисленными координатами"."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.rects = []

    def init(self, rects: list) -> None:
        """Функция инициализации."""
        assert DrawRectsOp._check_lines(rects)
        self.rects = rects

    @staticmethod
    def create(rects: list) -> DrawRectsOp:
        """Функция создания."""
        assert DrawRectsOp._check_lines(rects)
        op = DrawRectsOp()
        op.init(rects)
        return op

    def add_rect(self, rect) -> None:
        """Добавление точки."""
        self.rects.append(rect)

    def get_rect_count(self):
        """Получение количества прямоугольников."""
        return len(self.rects)

    def is_empty(self) -> bool:
        """Получение признака отсутствия прямоугольников."""
        return len(self.rects) == 0

    def check_byte_array(self, byte_array):
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_RECTS:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_RECTS)
        ba += bmg.bmc.int32_to_byte_array(self.get_rect_count())
        for rect in self.rects:
            ba += rect.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: DrawRectsOp) -> bool:
        """Оператор ==."""
        return self.rects == other.rects

    def __ne__(self, other: DrawRectsOp) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.rects}"

    @staticmethod
    def _check_lines(rects):
        """Проверка списка прямоугольников."""
        if not isinstance(rects, list):
            return False
        if not all([isinstance(rect, bmg.Rect) for rect in rects]):
            return False
        return True


class DrawRectfOp:
    """Операция "Нарисовать прямоугольник с координатами с плавающей точкой"."""

    def __init__(self):
        """Конструктор без параметров."""
        self.rect = bmg.RectF()

    def init(self, rect: bmg.RectF) -> None:
        """Функция инициализации."""
        assert isinstance(rect, bmg.RectF)
        self.rect = rect

    @staticmethod
    def create(rect: bmg.RectF) -> DrawRectfOp:
        """Функция создания."""
        assert isinstance(rect, bmg.RectF)
        op = DrawRectfOp()
        op.init(rect)
        return op

    def check_byte_array(self, byte_array: bmg.RectF):
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_RECTF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_RECTF)
        ba += self.rect.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 35

    def __eq__(self, other: DrawRectfOp) -> bool:
        """Оператор ==."""
        return self.rect == other.rect

    def __ne__(self, other: DrawRectfOp) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.rect}"


class DrawRectsfOp:
    """Операция "Нарисовать прямоугольники с дробными координатами"."""

    def __init__(self):
        """Конструктор по умолчанию."""
        self.rects = []

    def init(self, rects):
        """Функция инициализации."""
        assert DrawRectsfOp._check_lines(rects)
        self.rects = rects

    @staticmethod
    def create(rects):
        """Функция создания."""
        assert DrawRectsfOp._check_lines(rects)
        op = DrawRectsfOp()
        op.init(rects)
        return op

    def add_rect(self, rect):
        """Добавление прямоугольника."""
        assert isinstance(rect, bmg.RectF)
        self.rects.append(rect)

    def get_rect_count(self):
        """Получение количества прямоугольников."""
        return len(self.rects)

    def is_empty(self):
        """Получение признака отсутствия прямоугольников."""
        return len(self.rects) == 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_RECTSF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_RECTSF)
        ba += bmg.bmc.int32_to_byte_array(self.get_rect_count())
        for rect in self.rects:
            ba += rect.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через массив байтов."""
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: DrawRectsfOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawRectsfOp)
        return self.rects == other.rects

    def __ne__(self, other: DrawRectsfOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawRectsfOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return '{}'.format(self.rects)

    @staticmethod
    def _check_lines(rects):
        """Проверка списка прямоугольников."""
        if not isinstance(rects, list):
            return False
        if not all([isinstance(rect, bmg.RectF) for rect in rects]):
            return False
        return True


class DrawEllipseOp:
    """Операция "Нарисовать эллипс с целочисленными координатами"."""

    def __init__(self):
        """Конструктор без параметров."""
        self.rect = bmg.Rect()

    def init(self, rect: bmg.Rect) -> None:
        """Функция инициализации."""
        assert isinstance(rect, bmg.Rect)
        self.rect = rect

    @staticmethod
    def create(rect: bmg.Rect) -> DrawEllipseOp:
        """Функция создания."""
        assert isinstance(rect, bmg.Rect)
        op = DrawEllipseOp()
        op.init(rect)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_ELLIPSE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_ELLIPSE)
        ba += self.rect.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через массив байтов."""
        assert self.check_byte_array(byte_array)
        ba = byte_array[2:]
        self.rect.from_byte_array(ba)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 19

    def __eq__(self, other: DrawEllipseOp) -> bool:
        """Оператор ==."""
        return self.rect == other.rect

    def __ne__(self, other: DrawEllipseOp) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.rect}"


class DrawEllipsesOp:
    """Операция "Нарисовать эллипсы с целочисленными координатами"."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.rects = []

    def init(self, rects: list) -> None:
        """Функция инициализации."""
        assert DrawEllipsesOp._check_lines(rects)
        self.rects = rects

    @staticmethod
    def create(rects) -> DrawEllipsesOp:
        """Функция создания."""
        assert DrawEllipsesOp._check_lines(rects)
        op = DrawEllipsesOp()
        op.init(rects)
        return op

    def add_rect(self, rect: bmg.Rect) -> None:
        """Добавление эллипса."""
        assert isinstance(rect, bmg.Rect)
        self.rects.append(rect)

    def get_rect_count(self) -> int:
        """Получение количества эллипсов."""
        return len(self.rects)

    def is_empty(self) -> bool:
        """Получение признака отсутствия эллипсов."""
        return self.get_rect_count() == 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 7:
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_ELLIPSES:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_ELLIPSES)
        ba += bmg.bmc.int32_to_byte_array(self.get_rect_count())
        for r in self.rects:
            ba += r.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через массив байтов."""
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: DrawEllipsesOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawEllipsesOp)
        return self.rects == other.rects

    def __ne__(self, other: DrawEllipsesOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawEllipsesOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.rects}"

    @staticmethod
    def _check_lines(rects):
        """Проверка списка прямоугольников."""
        if not isinstance(rects, list):
            return False
        if not all([isinstance(rect, bmg.Rect) for rect in rects]):
            return False
        return True


class DrawEllipsefOp:
    """Операция "Нарисовать эллипс с дробными координатами"."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.rect = bmg.RectF()

    def init(self, rect):
        """Функция инициализации."""
        assert isinstance(rect, bmg.RectF)
        self.rect = rect

    @staticmethod
    def create(rect: bmg.RectF) -> DrawEllipsefOp:
        """Функция создания."""
        assert isinstance(rect, bmg.RectF)
        op = DrawEllipsefOp()
        op.init(rect)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_ELLIPSEF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_ELLIPSEF)
        ba += self.rect.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 35

    def __eq__(self, other: DrawEllipsefOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawEllipsefOp)
        return self.rect == other.rect

    def __ne__(self, other: DrawEllipsefOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawEllipsefOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.rect}"


class DrawEllipsesfOp:
    """Операция "Нарисовать эллипсы с дробными координатами"."""

    def __init__(self):
        """Конструктор без параметров."""
        self.rects = []

    def init(self, rects):
        """Функция инициализации."""
        assert DrawEllipsesfOp._check_rects(rects)
        self.rects = rects

    @staticmethod
    def create(rects):
        """Функция создания."""
        assert isinstance(rects, list)
        op = DrawEllipsesfOp()
        op.init(rects)
        return op

    def add_rect(self, rect: bmg.Rect) -> None:
        """Добавление эллипса."""
        assert isinstance(rect, bmg.RectF)
        self.rects.append(rect)

    def get_rect_count(self) -> int:
        """Получение количество эллипсов."""
        return len(self.rects)

    def is_empty(self) -> bool:
        """Получение признака отсутствия эллипсов."""
        return len(self.rects) == 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 7:
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_ELLIPSESF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_ELLIPSESF)
        ba += bmg.bmc.int32_to_byte_array(self.get_rect_count())
        for rect in self.rects:
            ba += rect.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array):
        """Инициализация через массив байтов."""
        assert self.check_byte_array(byte_array)
        ba_sz = byte_array[2:6]
        sz = bmg.bmc.byte_array_to_int32(ba_sz)
        rects = []
        for i in range(sz):
            r = bmg.Rect()
            rs = r.get_byte_array_len()
            rbi = 2 + 4 + i * rs
            ba_r = byte_array[rbi:]
            r.from_byte_array(ba_r)
        self.rects = rects

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: DrawEllipsesfOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawEllipsesfOp)
        return self.rects == other.rects

    def __ne__(self, other: DrawEllipsesfOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawEllipsesfOp)
        return not self == other

    def __str__(self):
        """Получение строкового представления."""
        return f"{self.rects}"

    @staticmethod
    def _check_rects(rects: list) -> bool:
        """Проверка списка прямоугольников."""
        if not isinstance(rects, list):
            return False
        if not all([isinstance(rect, bmg.RectF) for rect in rects]):
            return False
        return True


class DrawRoundRectOp:
    """Операция "Вывод прямоугольника с целочисленными координатами со сглаженными углами"."""

    def __init__(self):
        """Конструктор по умолчанию."""
        self.rect = bmg.RoundRect()

    def init(self, rect: bmg.RoundRect) -> None:
        """Функция инициализации."""
        assert isinstance(rect, bmg.RoundRect)
        self.rect = rect

    @staticmethod
    def create(rect: bmg.RoundRect) -> DrawRoundRectOp:
        """Функция создания."""
        assert isinstance(rect, bmg.RoundRect)
        op = DrawRoundRectOp()
        op.init(rect)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_ROUND_RECT:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_ROUND_RECT)
        ba += self.rect.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через массив байтов."""
        assert self.check_byte_array(byte_array)
        bar = byte_array[2:26]
        self.rect.from_byte_array(bar)

    def get_byte_array_len(self):
        """Получение длины списка байтов."""
        return 27

    def __eq__(self, other: DrawRoundRectOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawRoundRectOp)
        return self.rect == other.rect

    def __ne__(self, other: DrawRoundRectOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawRoundRectOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.rect}"


class DrawRoundRectsOp:
    """Операция "Вывод прямоугольников с целочисленными координатами со сглаженными углами"."""

    def __init__(self):
        """Конструктор по умолчанию."""
        self.rects = []

    def init(self, rects: list) -> None:
        """Функция инициализации."""
        assert DrawRoundRectsOp._check_lines(rects)
        self.rects = rects

    @staticmethod
    def create(rects: list) -> DrawRoundRectsOp:
        """Функция создания."""
        assert DrawRoundRectsOp.check_lines(rects)
        op = DrawRoundRectsOp()
        op.init(rects)
        return op

    def add_rect(self, rect):
        """Добавление прямоугольника."""
        assert isinstance(rect, bmg.RoundRect)
        self.rects.append(rect)

    def is_empty(self) -> bool:
        """Получение признака отсутствия прямоугольников."""
        return self.get_rect_count() == 0

    def get_rect_count(self) -> int:
        """Получение количества прямоугольников."""
        return len(self.rects)

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_ROUND_RECTS:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_ROUND_RECTS)
        ba += bmg.bmc.int32_to_byte_array(self.get_rect_count())
        for rect in self.rects:
            ba += rect.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через массив байтов."""
        assert self.check_byte_array(byte_array)
        basz = byte_array[2:6]
        sz = bmg.bmc.byte_array_to_int32(basz)
        for i in range(sz):
            rect = bmg.RoundRect()
            rs = rect.get_byte_array_len()
            bbegin = 6 + i * rs
            bend = bbegin + rs
            rbl = byte_array[bbegin:bend]
            rect.from_byte_array(rbl)
            self.add_rect(rect)

    def get_byte_array_len(self) -> int:
        """Получение длины массива байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: DrawRoundRectsOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawRoundRectsOp)
        return self.rects == other.rects

    def __ne__(self, other: DrawRoundRectsOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawRoundRectsOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.rects}"

    @staticmethod
    def _check_lines(rects):
        """Проверка списка прямоугольников."""
        if not isinstance(rects, list):
            return False
        if not all([isinstance(rect, bmg.RoundRect) for rect in rects]):
            return False
        return True


class DrawRoundRectfOp:
    """Операция "Вывод прямоугольника с дробными координатами со сглаженными углами"."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.rect = bmg.RoundRectF()

    def init(self, rect) -> None:
        """Функция инициализации."""
        assert isinstance(rect, bmg.RoundRectF)
        self.rect = rect

    @staticmethod
    def create(rect) -> DrawRoundRectfOp:
        """Функция создания."""
        assert isinstance(rect, bmg.RoundRectF)
        op = DrawRoundRectfOp()
        op.init(rect)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_ROUND_RECTF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_ROUND_RECTF)
        ba += self.rect.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray):
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        rbl = byte_array[2:50]
        self.rect.from_byte_array(rbl)

    def get_byte_array_len(self):
        """Получение длины списка байтов."""
        return 51

    def __eq__(self, other: DrawRoundRectfOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawRoundRectfOp)
        return self.rect == other.rect

    def __ne__(self, other: DrawRoundRectfOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawRoundRectfOp)
        return not self == other

    def __str__(self):
        """Получение строкового представления."""
        return f"{self.rect}"


class DrawRoundRectsfOp:
    """Операция "Вывод прямоугольников с дробными координатами со сглаженными углами"."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.rects = []

    def init(self, rects: list) -> None:
        """Функция инициализации."""
        assert DrawRoundRectsfOp._check_rects(rects)
        self.rects = rects

    @staticmethod
    def create(rects: list) -> DrawRoundRectsfOp:
        """Функция создания."""
        assert DrawRoundRectsfOp._check_rects(rects)
        op = DrawRoundRectsfOp()
        op.init(rects)
        return op

    def is_empty(self) -> bool:
        """Получение признака отсутствия прямоугольников."""
        return self.get_rect_count() == 0

    def add_rect(self, rect: bmg.RoundRectF) -> None:
        """Добавление прямоугольника."""
        assert isinstance(rect, bmg.RoundRectF)
        self.rects.append(rect)

    def get_rect_count(self):
        """Получение количества прямоугольников."""
        return len(self.rects)

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_ROUND_RECTSF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_ROUND_RECTSF)
        ba += bmg.bmc.int32_to_byte_array(self.get_rect_count())
        for rect in self.rects:
            ba += rect.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_list):
        """Инициализация через список байтов."""
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawRoundRectsfOp)
        return self.rects == other.rects

    def __ne__(self, other) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawRoundRectsfOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.rects}"

    @staticmethod
    def _check_rects(rects) -> bool:
        """Проверка списка прямоугольников."""
        if not isinstance(rects, list):
            return False
        if not all([isinstance(rect, bmg.RoundRectF) for rect in rects]):
            return False
        return True


class DrawTextOp:
    """Операция "Вывод текста"."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.text = bmg.String()
        self.point = bmg.PointF()
        self.align = AlignFlags()

    def init(self, text: bmg.String, point: bmg.PointF, align: AlignFlags) -> None:
        """Функция инициализации."""
        assert isinstance(text, bmg.String)
        assert isinstance(point, bmg.PointF)
        assert isinstance(align, AlignFlags)
        self.text = text
        self.point = point
        self.align = align

    @staticmethod
    def create(text: bmg.String, point: bmg.PointF, align: AlignFlags) -> DrawTextOp:
        """Функция создания."""
        assert isinstance(text, bmg.String)
        assert isinstance(point, bmg.PointF)
        assert isinstance(align, AlignFlags)
        op = DrawTextOp()
        op.init(text, point, align)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_TEXT:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_TEXT)
        ba += self.text.to_byte_array()
        ba += self.point.to_byte_array()
        ba += self.align.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        ba_data = byte_array[2:]  # отсечение кода операции
        self.text.from_byte_array(ba_data)
        ba_data = ba_data[self.text.get_byte_array_len():]
        self.point.from_byte_array(ba_data)
        ba_data = ba_data[self.point.get_byte_array_len():]
        self.align.from_byte_array(ba_data)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other) -> bool:
        """Оператор ==."""
        is_eq_text = self.text == other.text
        is_eq_point = self.point == other.point
        is_eq_align = self.align == other.align
        return is_eq_text and is_eq_point and is_eq_align

    def __ne__(self, other) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.text}, {self.pos}, {self.align}"


class DrawImageOp:
    """Операция "Вывод изображения"."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.path = bmg.String()
        self.point = bmg.PointF()
        self.align = AlignFlags()

    def init(self, path: str, point: bmg.PointF, align: AlignFlags) -> None:
        """Функция инициализации."""
        assert isinstance(path, bmg.String)
        assert isinstance(point, bmg.PointF)
        assert isinstance(align, AlignFlags)
        self.path = path
        self.point = point
        self.align = align

    @staticmethod
    def create(path: str, point: bmg.PointF, align: AlignFlags) -> DrawImageOp:
        """Функция создания."""
        assert isinstance(path, bmg.String)
        assert isinstance(point, bmg.PointF)
        assert isinstance(align, AlignFlags)
        op = DrawImageOp()
        op.init(path, point, align)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_IMAGE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_IMAGE)
        ba += self.path.to_byte_array()
        ba += self.point.to_byte_array()
        ba += self.align.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        # Получение пути
        size_path_ba = byte_array[2:6]
        path_size = bmg.bmc.byte_array_to_int32(size_path_ba)
        path_begin = 2
        path_end = 6 + path_size
        ba_path = byte_array[path_begin:path_end]
        self.path.from_byte_array(ba_path)
        # Получение точки
        point_begin = path_end
        point_end = point_begin + 16
        ba_point = byte_array[point_begin:point_end]
        self.point.from_byte_array(ba_point)
        # Получение выравнивания
        align_begin = point_end
        align_end = align_begin + 2
        ba_align = byte_array[align_begin:align_end]
        self.align.from_byte_array(ba_align)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: DrawImageOp) -> bool:
        """Оператор ==."""
        is_eq_path = (self.path == other.path)
        is_eq_point = (self.point == other.point)
        is_eq_align = (self.align == other.align)
        return is_eq_path and is_eq_point and is_eq_align

    def __ne__(self, other: DrawImageOp) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.path}, {self.point}, {self.align}"


class DrawArcOp:
    """Операция "Вывод дуги с целочисленными координатами"."""

    def __init__(self):
        """Конструктор по умолчанию."""
        self.rect = bmg.Rect()
        self.start_angle = 0
        self.span_angle = 0

    def init(self, rect: bmg.Rect, start_angle: int, span_angle: int) -> None:
        """Функция инициализации."""
        assert isinstance(rect, bmg.Rect)
        assert isinstance(start_angle, int)
        assert isinstance(span_angle, int)
        self.rect = rect
        self.start_angle = start_angle
        self.span_angle = span_angle

    @staticmethod
    def create(rect: bmg.Rect, startAngle: int, spanAngle: int) -> DrawArcOp:
        """Функция создания."""
        assert isinstance(rect, bmg.Rect)
        assert isinstance(startAngle, int)
        assert isinstance(spanAngle, int)
        op = DrawArcOp()
        op.init(rect, startAngle, spanAngle)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 24:
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_ARC:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массив байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_ARC)
        ba += self.rect.to_byte_array()
        ba += bmg.bmc.int32_to_byte_array(self.start_angle)
        ba += bmg.bmc.int32_to_byte_array(self.span_angle)
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через массив байтов."""
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 24

    def __eq__(self, other: DrawArcOp) -> bool:
        """Оператор ==."""
        is_eq_rect = (self.rect == other.rect)
        is_eq_start_angle = (self.start_angle == other.start_angle)
        is_eq_span_angle = (self.span_angle == other.span_angle)
        return is_eq_rect and is_eq_start_angle and is_eq_span_angle

    def __ne__(self, other: DrawArcOp) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.rect}, {self.startAngle}, {self.spanAngle}"


class DrawArcfOp:
    """Операция "Вывод дуги с дробными координатами"."""

    def __init__(self):
        """Конструктор по умолчанию."""
        self.rect = bmg.RectF()
        self.start_angle = 0
        self.span_angle = 0

    def init(self, rect: bmg.RectF, start_angle: int, span_angle: int) -> None:
        """Функция инициализации."""
        assert isinstance(rect, bmg.RectF)
        assert isinstance(start_angle, int)
        assert isinstance(span_angle, int)
        self.rect = rect
        self.start_angle = start_angle
        self.span_angle = span_angle

    @staticmethod
    def create(rect: bmg.RectF, startAngle: int, spanAngle: int) -> DrawArcfOp:
        """Функция создания."""
        assert isinstance(rect, bmg.RectF)
        assert isinstance(startAngle, int)
        assert isinstance(spanAngle, int)
        op = DrawArcfOp()
        op.init(rect, startAngle, spanAngle)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 40:
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_ARCF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = []
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_ARCF)
        ba += self.rect.to_byte_array()
        ba += bmg.bmc.int32_to_byte_array(self.startAngle)
        ba += bmg.bmc.int32_to_byte_array(self.spanAngle)
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_list(self, byte_list):
        """Инициализация через список байтов."""
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 40

    def __eq__(self, other: DrawArcfOp) -> bool:
        """Оператор ==."""
        is_eq_rect = (self.rect == other.rect)
        is_eq_start_angle = (self.start_angle == other.start_angle)
        is_eq_span_angle = (self.span_angle == other.span_angle)
        return is_eq_rect and is_eq_start_angle and is_eq_span_angle

    def __ne__(self, other: DrawArcfOp) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.rect}, {self.start_angle}, {self.span_angle}"


class DrawPolygonOp:
    """Операция "Вывод полигона с целыми координатами"."""

    def __init__(self):
        """Конструктор по умолчанию."""
        self.polygon = bmg.Polygon()

    def init(self, polygon):
        """Функция инициализации."""
        assert isinstance(polygon, bmg.Polygon)
        self.polygon = polygon

    @staticmethod
    def create(polygon: bmg.Polygon):
        """Функция создания."""
        assert isinstance(polygon, bmg.Polygon)
        op = DrawPolygonOp()
        op.init(polygon)
        return op

    def add_point(self, point: bmg.Point):
        """Добавление точки."""
        assert isinstance(point, bmg.Point)
        self.polygon.add_point(point)

    def get_point_count(self) -> int:
        """Получение количества точек."""
        return self.polygon.get_point_count()

    def is_empty(self) -> bool:
        """Проверка на то, что полигон не содержит точек."""
        return self.polygon.is_empty()

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 6:
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_POLYGON:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_POLYGON)
        ba += self.polygon.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: DrawPolygonOp) -> bool:
        """Оператор ==."""
        return self.polygon == other.polygon

    def __ne__(self, other: DrawPolygonOp) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.polygon}"


class DrawPolygonfOp:
    """Операция "Вывод полигона с дробными координатами"."""

    def __init__(self):
        """Конструктор по умолчанию."""
        self.polygon = bmg.PolygonF()

    def init(self, polygon: bmg.PolygonF) -> None:
        """Функция инициализации."""
        assert isinstance(polygon, bmg.PolygonF)
        self.polygon = polygon

    @staticmethod
    def create(polygon: bmg.PolygonF) -> DrawPolygonfOp:
        """Функция создания."""
        assert isinstance(polygon, bmg.PolygonF)
        op = DrawPolygonfOp()
        op.init(polygon)
        return op

    def add_point(self, point: bmg.PointF) -> None:
        """Добавление точки."""
        assert isinstance(point, bmg.PointF)
        self.polygon.add_point(point)

    def get_point_count(self):
        """Получение количества точек."""
        return self.polygon.get_point_count()

    def is_empty(self) -> bool:
        """Проверка полигона на пустоту."""
        return self.polygon.is_empty()

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 6:
            return False
        if get_op_code(byte_array) != DrawOpCodes.DRAW_POLYGONF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_POLYGONF)
        ba += self.polygon.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: DrawPolygonfOp) -> bool:
        """Оператор ==."""
        return self.polygon == other.polygon

    def __ne__(self, other: DrawPolygonfOp) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.polygon}"


def ops_to_byte_array(ops: list) -> bytearray:
    """Преобразование последовательности операций в список байтов."""
    ba = bytearray()
    for op in ops:
        ba += op.to_byte_array()
    return ba


def byte_array_to_ops(byte_array: bytearray) -> list:
    """Преобразование списка байтов в последовательность операций."""
    ops = []
    while len(byte_array) > 0:
        code = get_op_code(byte_array)
        op = create_op(code)
        op.from_byte_array(byte_array)
        ops.append(op)
        sz = op.get_byte_array_len()
        assert sz > 0
        byte_array = byte_array[sz:]
    return ops


def create_op(code: int):
    """Создание операции по ее коду."""
    if code == DrawOpCodes.SAVE_STATE:
        return SaveStateOp()
    elif code == DrawOpCodes.RESTORE_STATE:
        return RestoreStateOp()
    elif code == DrawOpCodes.SET_CLIP_RECT:
        return SetClipRectOp()
    elif code == DrawOpCodes.TRANSFORM_TRANSLATE:
        return TransformTranslateOp()
    elif code == DrawOpCodes.TRANSFORM_ROTATE:
        return TransformRotateOp()
    elif code == DrawOpCodes.TRANSFORM_SCALE:
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
        return DrawRectsOp()
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
        raise Exception("Bad operation code")


def create_op_from_bytes(byte_array: bytearray):
    """Создание операции из байтового массива."""
    assert len(byte_array) >= 2
    code = byte_array[:2]
    op = create_op(code)
    op.from_byte_array(byte_array)
    return op


def get_op_code(byte_array: bytearray) -> int:
    """Получение кода операции из списка байтов."""
    assert len(byte_array) >= 2
    bac = byte_array[:2]
    code = bmg.bmc.byte_array_to_int16(bac)
    if 0 <= code < DrawOpCodes.get_count():
        return code
    else:
        return DrawOpCodes.UNKNOWN


class TestDrawOpCodes(unittest.TestCase):
    """Тест класса DrawOpCodes."""

    def test_code_to_str(self):
        """Тест функции code_to_str."""
        pass

    def test_str_to_code(self):
        """Тест функции str_to_code."""
        pass

    def test_get_values(self):
        """Тест функции get_values."""
        pass

    def test_is_correct_value(self):
        """Тест функции is_correct_value."""
        pass

    def test_get_count(self):
        """Тест функции get_count."""
        pass


class TestSaveStateOp(unittest.TestCase):
    """Тест для класса SaveStateOp."""

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        op = SaveStateOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = SaveStateOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_from_byte_list(self):
        """Тест функции to_byte_array."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.SAVE_STATE)
        ba += bmg.bmc.int8_to_byte_array(0)
        op = SaveStateOp()
        op.from_byte_array(ba)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = SaveStateOp()
        ba = op.to_byte_array()
        self.assertEqual(op.get_byte_array_len(), len(ba))

    def test_equal(self):
        """Тест оператора ==."""
        op_1 = SaveStateOp()
        self.assertTrue(op_1 == op_1)
        op_2 = SaveStateOp()
        self.assertTrue(op_1 == op_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op = SaveStateOp()
        self.assertFalse(op != op)


class TestRestoreStateOp(unittest.TestCase):
    """Тест класса RestoreStateOp."""

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        op = RestoreStateOp()
        bl = op.to_byte_array()
        self.assertTrue(op.check_byte_array(bl))

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = RestoreStateOp()
        bl = op.to_byte_array()
        self.assertTrue(op.check_byte_array(bl))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.RESTORE_STATE)
        ba += bmg.bmc.int8_to_byte_array(0)
        op = RestoreStateOp()
        op.from_byte_array(ba)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = RestoreStateOp()
        ba = op.to_byte_array()
        self.assertEqual(op.get_byte_array_len(), len(ba))

    def test_equal(self):
        """Тест оператора ==."""
        op_1 = RestoreStateOp()
        self.assertTrue(op_1 == op_1)
        op_2 = RestoreStateOp()
        self.assertTrue(op_1 == op_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op = RestoreStateOp()
        self.assertFalse(op != op)


class TestTransformTranslateOp(unittest.TestCase):
    """Тест класса TransformTranslateOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = TransformTranslateOp()
        self.assertAlmostEqual(op.x, 0.0)
        self.assertAlmostEqual(op.y, 0.0)

    def test_init(self):
        """Тест функции init."""
        op = TransformTranslateOp()
        op.init(100.0, 100.0)
        self.assertAlmostEqual(op.x, 100.0)
        self.assertAlmostEqual(op.y, 100.0)

    def test_create(self):
        """Тест функции create."""
        op = TransformTranslateOp.create(100.0, 100.0)
        self.assertAlmostEqual(op.x, 100.0)
        self.assertAlmostEqual(op.y, 100.0)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        pass

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = TransformTranslateOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = TransformTranslateOp()
        op.x = op.y = 1.0
        ba = op.to_byte_array()
        op.from_byte_array(ba)
        self.assertAlmostEqual(op.x, 1.0)
        self.assertAlmostEqual(op.y, 1.0)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = TransformTranslateOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op_1 = TransformTranslateOp()
        self.assertTrue(op_1 == op_1)
        op_2 = TransformTranslateOp.create(100.0, 100.0)
        self.assertFalse(op_1 == op_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op_1 = TransformTranslateOp()
        self.assertFalse(op_1 != op_1)
        op_2 = TransformTranslateOp.create(100.0, 100.0)
        self.assertTrue(op_1 != op_2)


class TestTransformRotateOp(unittest.TestCase):
    """Тест класса TransformRotateOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = TransformRotateOp()
        self.assertAlmostEqual(op.angle, 0.0)

    def test_init(self):
        """Тест функции init."""
        op = TransformRotateOp()
        op.init(1.5)
        self.assertAlmostEqual(op.angle, 1.5)

    def test_create(self):
        """Тест функции create."""
        op = TransformRotateOp.create(1.5)
        self.assertAlmostEqual(op.angle, 1.5)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        op = TransformRotateOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = TransformRotateOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = TransformRotateOp()
        op.angle = 1.0
        ba = op.to_byte_array()
        op.from_byte_array(ba)
        self.assertAlmostEqual(op.angle, 1.0)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = TransformRotateOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op_1 = TransformRotateOp()
        self.assertTrue(op_1 == op_1)
        op_2 = TransformRotateOp.create(1.0)
        self.assertFalse(op_1 == op_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op_1 = TransformRotateOp()
        self.assertFalse(op_1 != op_1)
        op_2 = TransformRotateOp.create(1.0)
        self.assertTrue(op_1 != op_2)


class TestTransformScaleOp(unittest.TestCase):
    """Тест класса TransformScaleOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = TransformScaleOp()
        self.assertAlmostEqual(op.x, 1.0)
        self.assertAlmostEqual(op.y, 1.0)

    def test_init(self):
        """Тест функции init."""
        op = TransformScaleOp()
        op.init(2.0, 2.0)
        self.assertAlmostEqual(op.x, 2.0)
        self.assertAlmostEqual(op.y, 2.0)

    def test_create(self):
        """Тест функции create."""
        op = TransformScaleOp.create(2.0, 2.0)
        self.assertAlmostEqual(op.x, 2.0)
        self.assertAlmostEqual(op.y, 2.0)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        op = TransformScaleOp()
        bl = op.to_byte_array()
        self.assertTrue(op.check_byte_array(bl))

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = TransformScaleOp()
        bl = op.to_byte_array()
        self.assertTrue(op.check_byte_array(bl))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = TransformScaleOp()
        ba = op.to_byte_array()
        op.from_byte_array(ba)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = TransformScaleOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op_1 = TransformScaleOp()
        self.assertTrue(op_1 == op_1)
        op_2 = TransformScaleOp.create(2.0, 2.0)
        self.assertFalse(op_1 == op_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op_1 = TransformScaleOp()
        self.assertFalse(op_1 != op_1)
        op_2 = TransformScaleOp.create(2.0, 2.0)
        self.assertTrue(op_1 != op_2)


class TestSetAntialiasingOp(unittest.TestCase):
    """Тест класса SetAntialiasingOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = SetAntialiasingOp()
        self.assertFalse(op.antialiasing)

    def test_init(self):
        """Тест функции init."""
        op = SetAntialiasingOp()
        op.antialiasing = True
        self.assertTrue(op.antialiasing)

    def test_create(self):
        """Тест функции create."""
        op = SetAntialiasingOp.create(True)
        self.assertTrue(op.antialiasing)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        pass

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = SetAntialiasingOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = SetAntialiasingOp()
        ba = op.to_byte_array()
        op.from_byte_array(ba)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = SetAntialiasingOp()
        ba = op.to_byte_array()
        self.assertEqual(op.get_byte_array_len(), len(ba))

    def test_equal(self):
        """Тест оператора ==."""
        op_1 = SetAntialiasingOp()
        self.assertTrue(op_1 == op_1)
        op_2 = SetAntialiasingOp.create(True)
        self.assertFalse(op_1 == op_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op_1 = SetAntialiasingOp()
        self.assertFalse(op_1 != op_1)
        op_2 = SetAntialiasingOp.create(True)
        self.assertTrue(op_1 != op_2)


class TestSetFontOp(object):
    """Тест класса SetFontOp."""

    def test_constructor(self):
        """."""
        op = SetFontOp()
        font = bmg.Font()
        self.assertEqual(op.font, font)

    def test_init(self):
        """Тест функции init."""
        op = SetFontOp()

    def test_create(self):
        """Тест фунции create."""
        op = SetFontOp()

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        pass

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = SetFontOp()
        bl = op.to_byte_list()
        self.assertTrue(op.check_byte_list(bl))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = SetFontOp()
        ba = op.to_byte_array()
        op.from_byte_list(ba)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = SetFontOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.to_byte_array())

    def test_equal(self):
        """Тест оператора ==."""
        op = SetFontOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        """Тест оператора !=."""
        op = SetFontOp()
        self.assertFalse(op != op)


class TestDrawLineOp(unittest.TestCase):
    """Тест класса DrawLineOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = DrawLineOp()
        self.assertEqual(op.line, bmg.Line())

    def test_init(self):
        """Тест функции init."""
        op = DrawLineOp()

    def test_init_2(self):
        """Тест функции init_2."""
        op = DrawLineOp()

    def test_init_3(self):
        """Тест функции init_3."""
        op = DrawLineOp()

    def test_create(self):
        """Тест функции create."""
        pass

    def test_create_2(self):
        """Тест функции create_2."""
        pass

    def test_create_3(self):
        """Тест функции create_3."""
        pass

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        pass

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = DrawLineOp()
        bl = op.to_byte_array()
        self.assertTrue(op.check_byte_array(bl))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        pass

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = DrawLineOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op_1 = DrawLineOp()
        self.assertTrue(op_1 == op_1)
        op_2 = DrawLineOp.create_3(10, 10, 200, 200)
        self.assertFalse(op_1 == op_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op_1 = DrawLineOp()
        self.assertFalse(op_1 != op_1)
        op_2 = DrawLineOp.create_3(10, 10, 200, 200)
        self.assertTrue(op_1 != op_2)


class TestDrawLinefOp(unittest.TestCase):
    """Тест класса DrawLinefOp."""

    def test_constructor(self):
        """Тест конструктора."""
        op = DrawLinefOp()
        self.assertEqual(op.line, bmg.LineF())

    def test_init(self):
        """Тест функции init."""
        op = DrawLinefOp()
        line = bmg.LineF.create_2(10.0, 10.0, 20.0, 20.0)
        op.init(line)
        self.assertEqual(op.line, line)

    def test_init_2(self):
        """Тест функции init_2."""
        op = DrawLinefOp()
        pt_1 = bmg.PointF.create(10.0, 10.0)
        pt_2 = bmg.PointF.create(20.0, 20.0)
        op.init_2(pt_1, pt_2)
        self.assertEqual(op.line, bmg.LineF.create(pt_1, pt_2))

    def test_init_3(self):
        """Тест функции init_3."""
        op = DrawLinefOp()
        x_1 = 10.0
        y_1 = 10.0
        x_2 = 20.0
        y_2 = 20.0
        op.init_3(x_1, y_1, x_2, y_2)
        self.assertEqual(op.line, bmg.LineF.create_2(x_1, y_1, x_2, y_2))

    def test_create(self):
        """Тест функции create."""
        line = bmg.LineF.create_2(10.0, 10.0, 20.0, 20.0)
        op = DrawLinefOp.create(line)
        self.assertEqual(op.line, line)

    def test_create_2(self):
        """Тест функции create_2."""
        pass

    def test_create_3(self):
        """Тест функции create_3."""
        pass

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        pass

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = DrawLinefOp()
        bl = op.to_byte_array()
        self.assertTrue(op.check_byte_array(bl))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        pass

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = DrawLinefOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op_1 = DrawLinefOp()
        self.assertTrue(op_1 == op_1)
        op_2 = DrawLinefOp.create_3(10.0, 10.0, 200.0, 200.0)
        self.assertFalse(op_1 == op_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op_1 = DrawLinefOp()
        self.assertFalse(op_1 != op_1)
        op_2 = DrawLinefOp.create_3(10.0, 10.0, 200.0, 200.0)
        self.assertTrue(op_1 != op_2)


class TestDrawRectOp(unittest.TestCase):
    """Тестирование класса DrawRectOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = DrawRectOp()
        self.assertEqual(op.rect, bmg.Rect())

    def test_init(self):
        """Тест функции init."""
        op = DrawRectOp()

    def test_create(self):
        """Тест функции create."""
        rect = bmg.Rect.create_2(10, 10, 300, 300)
        op = DrawRectOp.create(rect)
        self.assertEqual(op.rect, rect)
        
    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        pass

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = DrawRectOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        pass

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = DrawRectOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op_1 = DrawRectOp()
        self.assertTrue(op_1 == op_1)
        rect = bmg.Rect.create_2(10, 10, 300, 300)
        op_2 = DrawRectOp.create(rect)
        self.assertFalse(op_1 == op_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op_1 = DrawRectOp()
        self.assertFalse(op_1 != op_1)
        rect = bmg.Rect.create_2(10, 10, 300, 300)
        op_2 = DrawRectOp.create(rect)
        self.assertTrue(op_1 != op_2)


class TestDrawRectsOp(unittest.TestCase):
    """Тестирование класса DrawRectsOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = DrawRectsOp()

    def test_init(self):
        """Тест функции init."""
        op = DrawRectsOp()

    def test_create(self):
        """Тест функции create."""
        rects = [bmg.Rect()] * 3
        op = DrawRectsOp.create(rects)
        self.assertEqual(op.rects, rects)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        pass

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = DrawRectsOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        pass

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = DrawRectsOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op = DrawRectsOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        """Тест оператора !=."""
        op = DrawRectsOp()
        self.assertFalse(op != op)


class TestDrawRectfOp(unittest.TestCase):
    """Тестирование класса DrawRectfOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = DrawRectfOp()
        self.assertEqual(op.rect, bmg.RectF())

    def test_init(self):
        """Тест функции init."""
        op = DrawRectfOp()
        rect = bmg.RectF.create_2(0.0, 0.0, 200.0, 200.0)
        op.init(rect)
        self.assertEqual(op.rect, rect)

    def test_create(self):
        """Тест функции create."""
        op = DrawRectfOp()

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        op = DrawRectfOp()

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = DrawRectfOp()

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = DrawRectfOp()

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = DrawRectfOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        rect_1 = bmg.RectF.create_2(0.0, 0.0, 200.0, 200.0)
        op_1 = DrawRectfOp.create(rect_1)
        self.assertTrue(op_1 == op_1)
        rect_2 = bmg.RectF.create_2(10.0, 10.0, 200.0, 200.0)
        op_2 = DrawRectfOp.create(rect_2)
        self.assertFalse(op_1 == op_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        rect_1 = bmg.RectF.create_2(0.0, 0.0, 200.0, 200.0)
        op_1 = DrawRectfOp.create(rect_1)
        self.assertFalse(op_1 != op_1)
        rect_2 = bmg.RectF.create_2(10.0, 10.0, 300.0, 300.0)
        op_2 = DrawRectfOp.create(rect_2)
        self.assertTrue(op_1 != op_2)


class TestDrawRectsfOp(unittest.TestCase):
    """Тестирование класса DrawRectsfOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = DrawRectsfOp()
        self.assertEqual(op.rects, [])
        self.assertTrue(op.is_empty())

    def test_init(self):
        """Тест функции init."""
        rects = [bmg.RectF()] * 10
        op = DrawRectsfOp()
        op.init(rects)
        self.assertFalse(op.is_empty())
        self.assertTrue(op.rects, rects)

    def test_create(self):
        """Тест функции create."""
        rects = [bmg.RectF()] * 10
        op = DrawRectsfOp.create(rects)
        self.assertFalse(op.is_empty())
        self.assertTrue(op.rects, rects)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        op = DrawRectsfOp()

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = DrawRectsfOp()

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = DrawRectsfOp()

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = DrawRectsfOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op = DrawRectsfOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        """Тест оператора !=."""
        op = DrawRectsfOp()
        self.assertFalse(op != op)


class TestDrawEllipseOp(unittest.TestCase):
    """Тест класса DrawEllipseOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = DrawEllipseOp()
        self.assertEqual(op.rect, bmg.Rect())

    def test_init(self):
        """Тест функции init."""
        op = DrawEllipseOp()
        rect = bmg.Rect.create_2(10, 10, 20, 20)
        op.init(rect)

    def test_create(self):
        """Тест функции create."""
        rect = bmg.Rect.create_2(10, 10, 20, 20)
        op = DrawEllipseOp.create(rect)
        self.assertEqual(op.rect, rect)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        op = DrawEllipseOp()

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = DrawEllipseOp()

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = DrawEllipseOp()

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = DrawEllipseOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op_1 = DrawEllipseOp()
        self.assertTrue(op_1 == op_1)
        rect = bmg.Rect.create_2(100, 100, 200, 200)
        op_2 = DrawEllipseOp.create(rect)
        self.assertFalse(op_1 == op_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op_1 = DrawEllipseOp()
        self.assertFalse(op_1 != op_1)
        rect = bmg.Rect.create_2(100, 100, 200, 200)
        op_2 = DrawEllipseOp.create(rect)
        self.assertTrue(op_1 != op_2)


class TestDrawEllipsesOp(unittest.TestCase):
    """Тестирование класса DrawEllipsesOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = DrawEllipsesOp()
        self.assertTrue(op.is_empty())
        self.assertEqual(op.get_rect_count(), 0)

    def test_init(self):
        """Тест функции init."""
        rects = [bmg.Rect()]
        op = DrawEllipsesOp()
        op.init(rects)
        self.assertFalse(op.is_empty())
        self.assertEqual(op.get_rect_count(), 1)

    def test_create(self):
        """Тест функции create."""
        rects = [bmg.Rect()]
        op = DrawEllipsesOp.create(rects)
        self.assertFalse(op.is_empty())
        self.assertEqual(op.rects, rects)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        op = DrawEllipsesOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = DrawEllipsesOp()

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = DrawEllipsesOp()

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = DrawEllipsesOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест функции ==."""
        op = DrawEllipsesOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        """Тест функции !=."""
        op = DrawEllipsesOp()
        self.assertFalse(op != op)


class TestDrawEllipsefOp(unittest.TestCase):
    """Тестирование класса DrawEllipsefOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = DrawEllipsefOp()
        self.assertEqual(op.rect, bmg.RectF())

    def test_init(self):
        """Тест функции init."""
        op = DrawEllipsefOp()
        rect = bmg.RectF.create_2(100.0, 100.0, 200.0, 200.0)
        op.init(rect)
        self.assertEqual(op.rect, rect)

    def test_create(self):
        """Тест функции create."""
        rect = bmg.RectF.create_2(100.0, 100.0, 200.0, 200.0)
        op = DrawEllipsefOp.create(rect)
        self.assertEqual(op.rect, rect)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        op = DrawEllipsefOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = DrawEllipsefOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = DrawEllipsefOp()
        ba = op.to_byte_array()
        op.from_byte_array(ba)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = DrawEllipsefOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op_1 = DrawEllipsefOp()
        self.assertTrue(op_1 == op_1)
        rect = bmg.RectF.create_2(100.0, 100.0, 200.0, 200.0)
        op_2 = DrawEllipsefOp.create(rect)
        self.assertFalse(op_1 == op_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op_1 = DrawEllipsefOp()
        self.assertFalse(op_1 != op_1)
        rect = bmg.RectF.create_2(100.0, 100.0, 200.0, 200.0)
        op_2 = DrawEllipsefOp.create(rect)
        self.assertTrue(op_1 != op_2)


class TestDrawEllipsesfOp(unittest.TestCase):
    """Тестирование класса DrawEllipsesfOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = DrawEllipsesfOp()
        self.assertTrue(op.is_empty())

    def test_init(self):
        """Тест функции init."""
        op = DrawEllipsesfOp()
        rects = [bmg.RectF()] * 3
        op.init(rects)
        self.assertEqual(op.get_rect_count(), len(rects))

    def test_create(self):
        """Тест функции create."""
        rects = [bmg.RectF()] * 3
        op = DrawEllipsesfOp.create(rects)
        self.assertEqual(op.get_rect_count(), len(rects))

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        rects = [bmg.RectF()] * 10
        op = DrawEllipsesfOp.create(rects)
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = DrawEllipsesfOp()
        rects = [bmg.RectF()] * 3
        op.init(rects)
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = DrawEllipsesfOp()

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        rects = [bmg.RectF()] * 10
        op = DrawEllipsesfOp.create(rects)
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op_1 = DrawEllipsesfOp()
        self.assertTrue(op_1 == op_1)
        rects = [bmg.RectF()] * 10
        op_2 = DrawEllipsesfOp.create(rects)
        self.assertFalse(op_1 == op_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op_1 = DrawEllipsesfOp()
        self.assertFalse(op_1 != op_1)
        rects = [bmg.RectF()] * 10
        op_2 = DrawEllipsesfOp.create(rects)
        self.assertTrue(op_1 != op_2)


class TestDrawPolylineOp(unittest.TestCase):
    """Тестирование класса DrawPolylineOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = DrawPolylineOp()
        self.assertEqual(op.polyline, bmg.Polyline())

    def init(self):
        """Тест функции init."""
        p = bmg.Polyline.create([bmg.Point()] * 3)
        op = DrawPolylineOp()
        op.init(p)
        self.assertFalse(op.is_empty())
        self.assertEqual(op.get_point_count(), 3)

    def test_create(self):
        """Тест функции create."""
        p = bmg.Polyline.create([bmg.Point()] * 3)
        op = DrawPolylineOp.create(p)
        self.assertFalse(op.is_empty())
        self.assertEqual(op.get_point_count(), 3)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        pass

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = DrawPolylineOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = DrawPolylineOp()

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = DrawPolylineOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op = DrawPolylineOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        """Тест оператора !=."""
        op = DrawPolylineOp()
        self.assertFalse(op != op)


class TestDrawPolylinefOp(unittest.TestCase):
    """Тестирование класса DrawPolylinefOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = DrawPolylinefOp()
        self.assertEqual(op.polyline, bmg.PolylineF())

    def init(self):
        """Тест функции init."""
        p = bmg.PolylineF.create([bmg.PointF()])
        op = DrawPolylinefOp()
        op.init(p)
        self.assertFalse(op.is_empty())
        self.assertEqual(op.get_point_count(), 1)

    def test_create(self):
        """Тест функции create."""
        p = bmg.PolylineF.create([bmg.PointF()])
        op = DrawPolylinefOp.create(p)
        self.assertEqual(op.get_point_count(), 1)
        self.assertFalse(op.is_empty())

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        op = DrawPolylinefOp()

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = DrawPolylinefOp()

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = DrawPolylinefOp()

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = DrawPolylinefOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op = DrawPolylinefOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        """Тест оператора !=."""
        op = DrawPolylinefOp()
        self.assertFalse(op != op)


class TestDrawPolygonOp(unittest.TestCase):
    """Тестирование класса DrawPolygonOp."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        op = DrawPolygonOp()
        self.assertEqual(op.polygon, bmg.Polygon())

    def init(self):
        """Тест функции init."""
        p = bmg.Polygon.create([bmg.Point()] * 100)
        op = DrawPolygonOp()
        op.init(p)
        self.assertEqual(op.polygon, p)

    def test_create(self):
        """Тест функции create."""
        p = bmg.Polygon.create([bmg.Point()] * 100)
        op = DrawPolygonOp.create(p)
        self.assertEqual(op.polygon, p)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        op = DrawPolygonOp()

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = DrawPolygonOp()

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = DrawPolygonOp()

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = DrawPolygonOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op = DrawPolygonOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        """Тест оператора !=."""
        op = DrawPolygonOp()
        self.assertFalse(op != op)


class TestDrawPolygonfOp(unittest.TestCase):
    """Тест класса DrawPolygonfOp."""

    def test_constructor(self):
        """Тест конструктор по умолчанию."""
        op = DrawPolygonfOp()
        self.assertEqual(op.polygon, bmg.PolygonF())

    def test_init(self):
        """Тест функции init."""
        p = bmg.PolygonF.create([bmg.PointF()])
        op = DrawPolygonfOp()
        op.init(p)
        self.assertEqual(op.polygon, p)

    def test_create(self):
        """Тест функции create."""
        p = bmg.PolygonF.create([bmg.PointF()])
        op = DrawPolygonfOp.create(p)
        self.assertEqual(op.polygon, p)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        op = DrawPolygonfOp()

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        p = bmg.PolygonF.create([bmg.PointF()])
        op = DrawPolygonfOp.create(p)
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = DrawPolygonfOp()

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = DrawPolygonfOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op = DrawPolygonfOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        """Тест оператора !=."""
        op = DrawPolygonfOp()
        self.assertFalse(op != op)


class TestDrawImageOp(unittest.TestCase):
    """Тест класса DrawImageOp."""

    def test_constructor(self):
        """Тест конструктор по умолчанию."""
        op = DrawImageOp()
        self.assertEqual(op.path, bmg.String())
        self.assertEqual(op.point, bmg.PointF())
        self.assertEqual(op.align, AlignFlags())

    def test_init(self):
        """Тест функции init."""
        op = DrawImageOp()

    def test_create(self):
        """Тест функции create."""
        pass

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        op = DrawImageOp()

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = DrawImageOp()

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = DrawImageOp()

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = DrawImageOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op = DrawImageOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        """Тест оператора !=."""
        op = DrawImageOp()
        self.assertFalse(op != op)


class TestDrawTextOp(unittest.TestCase):
    """Тест класса DrawTextOp."""

    def test_constructor(self):
        """Тест конструктор по умолчанию."""
        op = DrawTextOp()
        self.assertEqual(op.text, bmg.String())
        self.assertEqual(op.point, bmg.PointF())
        self.assertEqual(op.align, AlignFlags())

    def test_init(self):
        """Тест функции init."""
        text = bmg.String.create("text")
        point = bmg.PointF.create(100.0, 100.0)
        align = AlignFlags.create(HorzAlignFlags.LEFT, VertAlignFlags.TOP)
        op = DrawTextOp()
        op.init(text, point, align)
        self.assertEqual(op.text, text)
        self.assertEqual(op.point, point)
        self.assertEqual(op.align, align)

    def test_create(self):
        """Тест функции create."""
        text = bmg.String.create("text")
        point = bmg.PointF.create(100.0, 100.0)
        align = AlignFlags.create(HorzAlignFlags.LEFT, VertAlignFlags.TOP)
        op = DrawTextOp.create(text, point, align)
        self.assertEqual(op.text, text)
        self.assertEqual(op.point, point)
        self.assertEqual(op.align, align)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        op = DrawTextOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        op = DrawTextOp()
        op.text = bmg.String.create("text")
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        op = DrawTextOp()
        op.text = bmg.String.create("text")
        ba = op.to_byte_array()
        op.from_byte_array(ba)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        op = DrawTextOp()
        op.text = bmg.String.create("text")
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        """Тест оператора ==."""
        op_1 = DrawTextOp()
        self.assertTrue(op_1 == op_1)
        op_2 = DrawTextOp()
        op_2.text = bmg.String.create("text")
        self.assertFalse(op_1 == op_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op_1 = DrawTextOp()
        self.assertFalse(op_1 != op_1)
        op_2 = DrawTextOp()
        op_2.text = bmg.String.create("text")
        self.assertTrue(op_1 != op_2)


class TestFuncs(unittest.TestCase):
    """Тест различных функций."""

    def test_ops_to_byte_array(self):
        """Тест функцци ops_to_byte_array."""
        pass

    def test_byte_array_to_ops(self):
        """Тест функции byte_array_to_ops."""
        pass

    def test_create_op(self):
        """Тест функции create_op."""
        op_code = DrawOpCodes.DRAW_ARC
        op = create_op(op_code)
        self.assertTrue(isinstance(op, DrawArcOp))

    def test_create_op_from_bytes(self):
        """Тест функции create_op_from_bytes."""
        pass

    def test_get_op_code(self):
        """Тест функции get_op_codes."""
        op = DrawArcOp()
        ba = op.to_byte_array()
        op_code = get_op_code(ba)
        self.assertEqual(op_code, DrawOpCodes.DRAW_ARC)


# Вызывается при загрузке модуля главным.
if __name__ == "__main__":
    unittest.main()
