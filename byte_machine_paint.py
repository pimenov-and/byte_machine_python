"""
ByteMachine.

Операции рисования.
"""
from __future__ import annotations
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
    COUNT = 38


class AlignmentFlags:
    """Флаги выравнивания (объединяются через ИЛИ)."""

    ALIGN_UNKNOWN = 0x00
    ALIGN_LEFT = 0x01
    ALIGN_RIGHT = 0x02
    ALIGN_HCENTER = 0x04
    ALIGN_TOP = 0x20
    ALIGN_BOTTOM = 0x40
    ALIGN_VCENTER = 0x80


class SaveStateOp:
    """Операция "Сохранения состояния"."""

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.SAVE_STATE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.SAVE_STATE)
        ba += bmg.bmc.uint8_to_byte_array(0) # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        reserve = byte_array[2:3]

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
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.RESTORE_STATE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.RESTORE_STATE)
        ba += bmg.bmc.uint8_to_byte_array(0) # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        reserve = byte_array[2:3]

    def get_byte_array_len(self):
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
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.SET_CLIP_RECT:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.int16_to_byte_list(DrawOpCodes.SET_CLIP_RECT)
        ba += self.rect.to_byte_array()
        ba += bmg.uint8_to_byte_array(0) # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        bar = byte_array[2:18]
        self.rect.from_byte_array(bar)
        reverse = byte_array[18:19]

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
        return not (self == other)

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
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.TRANSFORM_TRANSLATE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.TRANSFORM_TRANSLATE)
        ba += bmg.bmc.double_to_byte_array(self.x)
        ba += bmg.bmc.double_to_byte_array(self.y)
        ba += bmg.bmc.uint8_to_byte_array(0) # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        ba = byte_array[2:18]
        data = bmg.bmc.byte_array_to_double_list(ba)
        self.x = data[0]
        self.y = data[1]
        reverse = byte_array[18:19]

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
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.TRANSFORM_ROTATE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.TRANSFORM_ROTATE)
        ba += bmg.bmc.double_to_byte_array(self.angle)
        ba += bmg.bmc.uint8_to_byte_array(0) # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        ba = byte_array[2:10]
        self.angle = bmg.bmc.byte_array_to_double(ba)
        reserve = byte_array[10:11]

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
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.TRANSFORM_SCALE:
            return False
        return True

    def to_byte_array(self):
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.TRANSFORM_SCALE)
        ba += bmg.bmc.double_to_byte_array(self.x)
        ba += bmg.bmc.double_to_byte_array(self.y)
        ba += bmg.bmc.uint8_to_byte_array(0) # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализации через список байтов."""
        assert self.check_byte_array(byte_array)
        ba = byte_array[2:18]
        bc = bmg.bmc.double_list_to_byte_array(ba)
        self.x = bc[0]
        self.y = bc[1]
        reserve = byte_array[18:19]

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
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.SET_ANTIALIASING:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.SET_ANTIALIASING)
        ba += bmg.bmc.bool_to_byte_array(self.antialiasing)
        ba += bmg.bmc.uint8_to_byte_array(0) # резерв
        return ba

    def from_byte_list(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        ba = byte_array[2:3]
        self.antialiasing = bmg.bmc.byte_array_to_bool(ba)
        reverse = byte_array[3:4]

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
        if len(byte_array) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.SET_PEN:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.SET_PEN)
        ba += self.pen.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0) # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через массив байтов."""
        assert self.check_byte_array(byte_array)
        bap = byte_array[2:13]
        self.pen.from_byte_list(bap)
        reverse = byte_array[13:14]

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
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.SET_BRUSH:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.SET_BRUSH)
        ba += self.brush.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0) # резерв
        return ba

    def from_byte_array(self, byte_list):
        """Инициализация через список байтов."""
        assert self.check_byte_list(byte_list)
        bb = byte_list[2:7]
        self.brush.from_byte_list(bb)
        reverse = byte_array[7:8]

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
        if len(byte_array) < 2:
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.SET_FONT:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.SET_FONT)
        ba += self.font.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0) # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert check_byte_array(byte_array)
        baf = byte_array[2:]
        self.font.from_byte_array(baf)

    def get_byte_list_array(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_list())

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
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_POINT:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_POINT)
        ba += self.point.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_array(0) # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        bap = byte_array[2:10]
        self.point.from_byte_array(bap)
        reserve = byte_array[10:11]

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
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_POINTS:
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
            p.from_byte_list(pbl)
            self.add_point(p)
            offset += point_len

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_list())

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

    def init(self, point: bmg.Point) -> None:
        """Функция инициализации."""
        assert isinstance(point, bmg.Point)
        self.point = point

    @staticmethod
    def create(point: bmg.Point) -> DrawPointfOp:
        """Функция создания."""
        assert isinstance(point, bmg.Point)
        op = DrawPointfOp()
        op.init(point)
        return op

    def check_byte_array(self, byte_list):
        """Проверка корректности списка байтов для инициализации."""
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_POINTF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_POINTF)
        ba += self.point.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_list(0)  # резерв
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

    def check_byte_list(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_POINTSF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_POINTSF)
        ba += bmg.bmc.int32_to_byte_list(self.get_point_count())
        for p in self.points:
            ba += p.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0) # резерв
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
            p.from_byte_list(pbl)
            self.add_point(p)
            offset += point_len

    def get_byte_list_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_list())

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

    def init2(self, pt1: bmg.Line, pt2: bmg.Line) -> None:
        """Функция инициализации."""
        assert isinstance(pt1, bmg.Point)
        assert isinstance(pt2, bmg.Point)
        self.line = bmg.Line.create(pt1, pt2)

    def init3(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """Функция инициализации."""
        assert isinstance(x1, int)
        assert isinstance(y1, int)
        assert isinstance(x2, int)
        assert isinstance(y2, int)
        self.line = bmg.Line.create_2(x1, y1, x2, y2)

    @staticmethod
    def create(line: bmg.Line) -> DrawLineOp:
        """Функция создания."""
        assert isinstance(line, bmg.Line)
        op = DrawLineOp()
        op.init(line)
        return op

    @staticmethod
    def create2(pt1: bmg.Point, pt2: bmg.Point) -> DrawLineOp:
        """Функция создания."""
        assert isinstance(pt1, bmg.Point)
        assert isinstance(pt2, bmg.Point)
        op = DrawLineOp()
        op.init2(pt1, pt2)
        return op

    @staticmethod
    def create3(x1: int, y1: int, x2: int, y2: int) -> DrawLineOp:
        """Функция создания."""
        assert isinstance(x1, int)
        assert isinstance(y1, int)
        assert isinstance(x2, int)
        assert isinstance(y2, int)
        op = DrawLineOp()
        op.init3(x1, y1, x2, y2)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_LINE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_LINE)
        ba += self.line.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_array(0) # резерв
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
        assert DrawLinesOp.check_lines(lines)
        self.lines = lines

    def create(lines: list) -> DrawLinesOp:
        """Функция создания."""
        assert DrawLinesOp.check_lines(lines)
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
        if len(byte_array) < 6:
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_LINES:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_array(DrawOpCodes.DRAW_LINES)
        ba += bmg.bmc.int32_to_byte_array(self.get_line_count())
        for line in self.lines:
            ba += line.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0) # резерв
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
            line.from_byte_list(lbl)
            self.add_point(line)
            offset += line_len

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_list())

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
    def check_lines(lines):
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

    def init2(self, pt1: bmg.PointF, pt2: bmg.PointF) -> None:
        """Функция инициализации 2."""
        assert isinstance(pt1, bmg.PointF)
        assert isinstance(pt2, bmg.PointF)
        self.line = bmg.LineF.create(pt1, pt2)

    def init3(self, x1: float, y1: float, x2: float, y2: float) -> None:
        """Функция инициализации 3."""
        assert isinstance(x1, float)
        assert isinstance(y1, float)
        assert isinstance(x2, float)
        assert isinstance(y2, float)
        self.line = bmg.LineF.create_2(x1, y1, x2, y2)

    @staticmethod
    def create(line: bmg.LineF) -> DrawLinefOp:
        """Функция создания."""
        assert isinstance(line, bmg.LineF)
        op = DrawLinefOp()
        op.init(line)
        return op

    @staticmethod
    def create2(pt1, pt2) -> DrawLinefOp:
        """Функция создания 2."""
        assert isinstance(pt1, bmg.PointF)
        assert isinstance(pt2, bmg.PointF)
        op = DrawLinefOp()
        op.init2(pt1, pt2)
        return op

    @staticmethod
    def create3(x1, y1, x2, y2):
        """Функция создания 3."""
        assert isinstance(x1, float)
        assert isinstance(y1, float)
        assert isinstance(x2, float)
        assert isinstance(y2, float)
        op = DrawLinefOp()
        op.init3(x1, y1, x2, y2)
        return op

    def check_byte_array(self, byte_list):
        """Проверка корректности списка байтов для инициализации."""
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_LINEF:
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
        self.line.from_byte_list(ba)

    def get_byte_list_len(self) -> int:
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
        assert DrawLinesfOp.check_lines(lines)
        self.lines = lines

    @staticmethod
    def create(lines: list) -> DrawLinesfOp:
        """Функция создания."""
        assert DrawLinesfOp.check_lines(lines)
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
        if len(byte_array) < 6:
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_LINEF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_LINESF)
        ba += bmg.bmc.int32_to_byte_list(self.get_line_count())
        for line in self.lines:
            ba += line.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_list(0)  # резерв
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
            line.from_byte_list(lbl)
            self.add_line(line)
            offset += line_len

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_list())

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
    def check_lines(lines: list) -> bool:
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

    def check_byte_list(self, byte_array):
        """Проверка корректности списка байтов для инициализации."""
        if len(byte_array) < 6:
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_POLYLINE:
            return False
        return True

    def to_byte_list(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_POLYLINE)
        ba += self.polyline.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0) # резерв
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

    def to_byte_list(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_POLYLINEF)
        ba += self.polyline.to_byte_array()
        ba += bmg.bmc.uint8_to_byte_list(0) # резерв
        return ba

    def from_byte_list(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        bapl = byte_array[:2]
        self.polyline.from_byte_array(bapl)

    def get_byte_list_len(self):
        """Получение длины списка байтов."""
        return len(self.to_byte_list())

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
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_RECT:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_RECT)
        ba += self.rect.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0) # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        # bar = 

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 18

    def __eq__(self, other: DrawRectOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawRectOp)
        return self.rect == other.rect

    def __ne__(self, other: DrawRectOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawRectOp)
        return not (self == other)

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
        assert isinstance(rects, list)
        self.rects = rects

    @staticmethod
    def create(rects: list) -> DrawRectsOp:
        """Функция создания."""
        assert isinstance(rects, list)
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

    def check_byte_array(self, byte_list):
        """Проверка корректности списка байтов для инициализации."""
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_RECTS:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_RECTS)
        ba += bmg.bmc.int32_to_byte_list(self.get_rect_count())
        for rect in self.rects:
            ba += rect.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0) # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_list())

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
    def check_lines(rects):
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
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_RECTF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_RECTF)
        ba += self.rect.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 34

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
        assert isinstance(rects, list)
        self.rects = rects

    @staticmethod
    def create(rects):
        """Функция создания."""
        assert isinstance(rects, list)
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
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_RECTSF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_RECTSF)
        ba += bmg.bmc.int32_to_byte_list(self.get_rect_count())
        for rect in self.rects:
            ba += rect.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0) # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через массив байтов."""
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_list())

    def __eq__(self, other: DrawRectsfOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawRectsfOp)
        return self.rects == other.rects

    def __ne__(self, other: DrawRectsfOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawRectsfOp)
        return not (self == other)

    def __str__(self) -> str:
        """Получение строкового представления."""
        return '{}'.format(self.rects)

    @staticmethod
    def check_lines(rects):
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
        if len(byte_array) < self.get_byte_list_array():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_ELLIPSE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_ELLIPSE)
        ba += self.rect.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через массив байтов."""
        assert self.check_byte_array(byte_array)
        ba = byte_array[2:]
        self.rect.from_byte_array(ba)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 18

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
        assert isinstance(rects, list)
        self.rects = rects

    @staticmethod
    def create(rects) -> DrawEllipsesOp:
        """Функция создания."""
        assert isinstance(rects, list)
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

    def check_byte_list(self, byte_list) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_ELLIPSES:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение массива байтов."""
        ba = []
        ba += bmg.bmc.int32_to_byte_list(self.get_rect_count())
        for r in self.rects:
            ba += r.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0) # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        '''
        Инициализация через список байтов.
        '''
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_list())

    def __eq__(self, other: DrawEllipsesOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawEllipsesOp)
        return self.rects == other.rects

    def __ne__(self, other: DrawEllipsesOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawEllipsesOp)
        return not (self == other)

    def __str__(self) -> str:
        """Получение строкового представления."""
        return '{}'.format(self.rects)

    @staticmethod
    def check_lines(rects):
        """Проверка списка прямоугольников."""
        if not isinstance(rects, list):
            return False
        if not all([isinstance(rect, bmg.Rect) for rect in rects]):
            return False
        return True


class DrawEllipsefOp:
    """Операция "Нарисовать эллипс с дробными координатами"."""

    def __init__(self):
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
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_ELLIPSEF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        '''
        Получение в виде списка байтов.
        '''
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_ELLIPSEF)
        ba += self.rect.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        '''
        Инициализация через список байтов.
        '''
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        '''
        Получение длины списка байтов.
        '''
        return 34

    def __eq__(self, other: DrawEllipsefOp) -> bool:
        '''
        Оператор ==.
        '''
        assert isinstance(other, DrawEllipsefOp)
        return self.rect == other.rect

    def __ne__(self, other: DrawEllipsefOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawEllipsefOp)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return '{}'.format(self.rect)


class DrawEllipsesfOp:
    """Операция "Нарисовать эллипсы с дробными координатами"."""

    def __init__(self):
        """Конструктор без параметров."""
        self.rects = []

    def init(self, rects):
        """Функция инициализации."""
        assert check_rects(rects)
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
        return self.get_rect_count() == 0

    def check_byte_list(self, byte_list):
        """Проверка корректности массива байтов для инициализации."""
        if len(byte_list) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_ELLIPSESF:
            return False
        return True

    def to_byte_list(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_ELLIPSESF)
        ba += bmg.bmc.int32_to_byte_list(self.get_rect_count())
        for rect in self.rects:
            ba += rect.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0)  # резерв
        return ba

    def from_byte_array(self, byte_array):
        """Инициализация через массив байтов."""
        assert self.check_byte_array(byte_array)
        basz = byte_array[2:6]
        sz = bmg.bmc.byte_list_to_int32(basz)

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
    def check_rects(rects: list) -> bool:
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
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_ROUND_RECT:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_ROUND_RECT)
        ba += self.rect.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0)  # резерв
        return ba

    def from_byte_list(self, byte_array: bytearray) -> None:
        """Инициализация через массив байтов."""
        assert self.check_byte_array(byte_array)
        bar = byte_array[2:26]
        self.rect.from_byte_array(bar)

    def get_byte_list_len(self):
        """Получение длины списка байтов."""
        return 27

    def __eq__(self, other: DrawRoundRectOp) -> bool:
        '''
        Оператор ==.
        '''
        assert isinstance(other, DrawRoundRectOp)
        return self.rect == other.rect

    def __ne__(self, other: DrawRoundRectOp) -> bool:
        '''
        Оператор !=.
        '''
        assert isinstance(other, DrawRoundRectOp)
        return not (self == other)

    def __str__(self) -> str:
        '''
        Получение строкового представления.
        '''
        return '{}'.format(self.rect)


class DrawRoundRectsOp:
    """Операция "Вывод прямоугольников с целочисленными координатами со сглаженными углами"."""

    def __init__(self):
        """Конструктор по умолчанию."""
        self.rects = []

    def init(self, rects: list) -> None:
        """Функция инициализации."""
        assert DrawRoundRectsOp.check_lines(rects)
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
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_ROUND_RECTS:
            return False
        return True

    def to_byte_list(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_ROUND_RECTS)
        ba += bmg.bmc.int32_to_byte_list(self.get_rect_count())
        for rect in self.rects:
            ba += rect.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0)  # резерв
        return ba

    def from_byte_list(self, byte_array: bytearray) -> None:
        """Инициализация через массив байтов."""
        assert self.check_byte_array(byte_array)
        basz = byte_array[2:6]
        sz = bmg.bmc.byte_array_to_int32(basz)
        for i in range(sz):
            rect = bmg.RoundRect()
            rs = rect.get_byte_list_len()
            bbegin = 6 + i * rs
            bend = bbegin + rs
            rbl = byte_array[bbegin:bend]
            rect.from_byte_list(rbl)
            self.add_rect(rect)

    def get_byte_array_len(self) -> int:
        """Получение длины массива байтов."""
        return len(self.to_byte_list())

    def __eq__(self, other: DrawRoundRectsOp) -> bool:
        """Оператор ==."""
        assert isinstance(other, DrawRoundRectsOp)
        return self.rects == other.rects

    def __ne__(self, other: DrawRoundRectsOp) -> bool:
        """Оператор !=."""
        assert isinstance(other, DrawRoundRectsOp)
        return not (self == other)

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.rects}"

    @staticmethod
    def check_lines(rects):
        """Проверка списка прямоугольников."""
        if not isinstance(rects, list):
            return False
        if not all([isinstance(rect, bmg.RoundRect) for rect in rects]):
            return False
        return True


class DrawRoundRectfOp:
    """ Операция "Вывод прямоугольника с дробными координатами со сглаженными углами"."""

    def __init__(self):
        """Конструктор без параметров."""
        self.rect = bmg.RoundRectF()

    def init(self, rect):
        """Функция инициализации."""
        assert isinstance(rect, bmg.RoundRectF)
        self.rect = rect

    @staticmethod
    def create(rect):
        """Функция создания."""
        assert isinstance(rect, bmg.RoundRectF)
        op = DrawRoundRectfOp()
        op.init(rect)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if len(byte_array) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_ROUND_RECTF:
            return False
        return True

    def to_byte_list(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_ROUND_RECTF)
        ba += self.rect.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0)  # резерв
        return ba

    def from_byte_list(self, byte_list):
        """Инициализация через список байтов."""
        assert self.check_byte_list(byte_list)
        rbl = byte_list[2:50]
        self.rect.from_byte_list(rbl)

    def get_byte_list_len(self):
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
        assert DrawRoundRectsfOp.check_rects(rects)
        self.rects = rects

    @staticmethod
    def create(rects: list) -> DrawRoundRectsfOp:
        """Функция создания."""
        assert DrawRoundRectsfOp.check_rects(rects)
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
        if len(byte_array) < self.get_byte_list_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_ROUND_RECTSF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_ROUND_RECTSF)
        ba += bmg.bmc.int32_to_byte_list(self.get_rect_count())
        for rect in self.rects:
            ba += rect.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0) # резерв
        return ba

    def from_byte_array(self, byte_list):
        """Инициализация через список байтов."""
        assert self.check_byte_list(byte_list)
        pass

    def get_byte_list_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_list())

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
    def check_rects(rects) -> bool:
        """Проверка списка прямоугольников."""
        if not isinstance(rects, list):
            return False
        if not all([isinstance(rect, bmg.RoundRectF) for rect in rects]):
            return False
        return True


class DrawTextOp:
    """Операция "Вывод текста"."""

    def __init__(self):
        """Конструктор без параметров."""
        self.text = bmg.String()
        self.point = bmg.PointF()

    def init(self, text: bmg.String, point: bmg.PointF):
        """Функция инициализации."""
        assert isinstance(text, bmg.String)
        assert isinstance(point, bmg.PointF)
        self.text = text
        self.point = point

    @staticmethod
    def create(text: bmg.String, point: bmg.PointF) -> DrawTextOp:
        """Функция создания."""
        assert isinstance(text, bmg.String)
        assert isinstance(point, bmg.PointF)
        op = DrawTextOp()
        op.init(text, point)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_TEXT:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_TEXT)
        ba += self.text.to_byte_list()
        ba += self.point.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0) # резерв
        return ba

    def from_byte_array(self, byte_array) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other) -> bool:
        """Оператор ==."""
        is_eq_text = (self.text == other.text)
        is_eq_point = (self.point == other.point)
        return is_eq_text and is_eq_point

    def __ne__(self, other) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return self.text


class DrawImageOp:
    """Операция "Вывод изображения"."""

    def __init__(self):
        """Конструктор по умолчанию."""
        self.path = bmg.String()
        self.point = bmg.PointF()
        self.align = AlignmentFlags.ALIGN_LEFT | AlignmentFlags.ALIGN_TOP

    def init(self, path, point: bmg.PointF, align: int):
        """Функция инициализации."""
        assert isinstance(path, bmg.String)
        assert isinstance(point, bmg.PointF)
        assert isinstance(align, bmg.int)
        self.path = path
        self.point = point
        self.align = align

    @staticmethod
    def create(path, point, align):
        """Функция создания."""
        assert isinstance(path, bmg.String)
        assert isinstance(point, bmg.PointF)
        assert isinstance(align, int)
        op = DrawImageOp()
        op.init(path, point, align)
        return op

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if len(byte_array) < self.get_byte_array_len():
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_IMAGE:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_IMAGE)
        ba += self.path.to_byte_list()
        ba += self.point.to_byte_list()
        ba += bmg.bmc.int32_to_byte_list(self.align)
        ba += bmg.bmc.uint8_to_byte_list(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        # Получение пути
        size_path_ba = byte_array[2:6]
        path_size = bmg.bmc.byte_list_to_int32(size_path_ba)
        path_begin = 2
        path_end = 6 + path_size
        path_ba = byte_array[path_begin:path_end]
        self.path.from_byte_array(path_ba)
        # Получение точки
        point_begin = path_end
        point_end = point_begin + 16
        point_ba = byte_array[point_begin:point_end]
        self.point.from_byte_array(point_ba)
        # Получение выравнивания
        align_begin = point_end
        align_end = align_begin + 4
        align_ba = byte_array[align_begin:align_end]
        self.align = bmg.bmc.byte_list_to_int32(align_ba)

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
        return f"{self.path}, {self.point}"


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
        if len(byte_array) < 24:
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_ARC:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        '''
        Получение в виде списка байтов.
        '''
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_ARC)
        ba += self.rect.to_byte_array()
        ba += bmg.bmc.int32_to_byte_list(self.startAngle)
        ba += bmg.bmc.int32_to_byte_list(self.spanAngle)
        ba += bmg.bmc.uint8_to_byte_list(0)  # резерв
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        '''
        Инициализация через список байтов.
        '''
        assert self.check_byte_array(byte_array)
        pass

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 24

    def __eq__(self, other: DrawArcOp) -> bool:
        """Оператор ==."""
        is_eq_rect = (self.rect == other.rect)
        is_eq_start_angle = (self.startAngle == other.startAngle)
        is_eq_span_angle = (self.spanAngle == other.spanAngle)
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
        self.startAngle = 0
        self.spanAngle = 0

    def init(self, rect: bmg.RectF, startAngle: int, spanAngle: int) -> None:
        """Функция инициализации."""
        assert isinstance(rect, bmg.RectF)
        assert isinstance(startAngle, int)
        assert isinstance(spanAngle, int)
        self.rect = rect
        self.startAngle = startAngle
        self.spanAngle = spanAngle

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
        if len(byte_array) < 40:
            return False
        if get_draw_op_code(byte_array) != DrawOpCodes.DRAW_ARCF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = []
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_ARCF)
        ba += self.rect.to_byte_array()
        ba += bmg.bmc.int32_to_byte_list(self.startAngle)
        ba += bmg.bmc.int32_to_byte_list(self.spanAngle)
        ba += bmg.bmc.uint8_to_byte_list(0)  # резерв
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
        is_eq_start_angle = (self.startAngle == other.startAngle)
        is_eq_span_angle = (self.spanAngle == other.spanAngle)
        return is_eq_rect and is_eq_start_angle and is_eq_span_angle

    def __ne__(self, other: DrawArcfOp) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.rect}, {self.startAngle}, {self.spanAngle}"


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

    def check_byte_array(self, byte_list: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if len(byte_list) < 6:
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_POLYGON:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_POLYGON)
        ba += self.polygon.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0)  # резерв
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

    def check_byte_list(self, byte_list):
        """Проверка корректности списка байтов для инициализации."""
        if len(byte_list) < 6:
            return False
        if get_draw_op_code(byte_list) != DrawOpCodes.DRAW_POLYGONF:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmg.bmc.int16_to_byte_list(DrawOpCodes.DRAW_POLYGONF)
        ba += self.polygon.to_byte_list()
        ba += bmg.bmc.uint8_to_byte_list(0)  # резерв
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
        return not (self == other)

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.polygon}"


def draw_ops_to_byte_array(ops: list) -> bytearray:
    """Преобразование последовательности операций в список байтов."""
    ba = bytearray()
    for op in ops:
        ba += op.to_byte_array()
    return ba


def byte_array_to_draw_ops(byte_array: bytearray) -> list:
    """Преобразование списка байтов в последовательность операций."""
    ops = []
    while len(byte_array) > 0:
        code = get_draw_op_code(byte_array)
        op = create_draw_op(code)
        op.from_byte_array(byte_array)
        ops.append(op)
        sz = op.get_byte_list_len()
        assert sz > 0
        byte_array = byte_array[sz:]
    return ops


def create_draw_op(code):
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
        raise Exception('Bad operation code')


def get_draw_op_code(byte_array: bytearray) -> int:
    """Получение кода операции из списка байтов."""
    assert len(byte_array) >= 2
    bac = byte_array[:2]
    code = bmg.bmc.byte_array_to_int16(bac)
    if 0 <= code < DrawOpCodes.COUNT:
        return code
    else:
        return DrawOpCodes.UNKNOWN


class TestSaveStateOp(unittest.TestCase):
    """Тест для класса SaveStateOp."""

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

    def test_get_byte_list_len(self):
        """Тест функции get_byte_list_len."""
        op = SaveStateOp()
        ba = op.to_byte_array()
        self.assertEqual(op.get_byte_array_len(), len(ba))

    def test_equal(self):
        """Тест оператора ==."""
        op1 = SaveStateOp()
        self.assertTrue(op1 == op1)
        op2 = SaveStateOp()
        self.assertTrue(op1 == op2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op1 = SaveStateOp()
        self.assertFalse(op1 != op1)


class TestRestoreStateOp(unittest.TestCase):
    """Тестирование класса RestoreStateOp."""

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
        op1 = RestoreStateOp()
        self.assertTrue(op1 == op1)
        op2 = RestoreStateOp()
        self.assertTrue(op1 == op2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op1 = RestoreStateOp()
        self.assertFalse(op1 != op1)


# Тестирование класса TransformTranslateOp
class TestTransformTranslateOp(unittest.TestCase):

    def test_constructor(self):
        op = TransformTranslateOp()
        self.assertAlmostEqual(op.x, 0.0)
        self.assertAlmostEqual(op.y, 0.0)

    def test_init(self):
        op = TransformTranslateOp()
        op.init(100.0, 100.0)
        self.assertAlmostEqual(op.x, 100.0)
        self.assertAlmostEqual(op.y, 100.0)

    def test_create(self):
        op = TransformTranslateOp.create(100.0, 100.0)
        self.assertAlmostEqual(op.x, 100.0)
        self.assertAlmostEqual(op.y, 100.0)

    def test_to_byte_list(self):
        op = TransformTranslateOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_from_byte_list(self):
        op = TransformTranslateOp()
        op.x = op.y = 1.0
        ba = op.to_byte_array()
        op.from_byte_array(ba)
        self.assertAlmostEqual(op.x, 1.0)
        self.assertAlmostEqual(op.y, 1.0)

    def test_get_byte_list_len(self):
        op = TransformTranslateOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

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


# Тестирование класса TransformRotateOp
class TestTransformRotateOp(unittest.TestCase):

    def test_constructor(self):
        op = TransformRotateOp()
        self.assertAlmostEqual(op.angle, 0.0)

    def test_init(self):
        op = TransformRotateOp()
        op.init(1.5)
        self.assertAlmostEqual(op.angle, 1.5)

    def test_create(self):
        op = TransformRotateOp.create(1.5)
        self.assertAlmostEqual(op.angle, 1.5)

    def test_to_byte_array(self):
        op = TransformRotateOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_from_byte_array(self):
        op = TransformRotateOp()
        op.angle = 1.0
        ba = op.to_byte_array()
        op.from_byte_array(ba)
        self.assertAlmostEqual(op.angle, 1.0)

    def test_get_byte_array_len(self):
        op = TransformRotateOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        op1 = TransformRotateOp()
        self.assertTrue(op1 == op1)
        op2 = TransformRotateOp.create(1.0)
        self.assertFalse(op1 == op2)

    def test_not_equal(self):
        op1 = TransformRotateOp()
        op2 = TransformRotateOp.create(1.0)
        self.assertTrue(op1 != op2)


# Тестирование класса TransformScaleOp
class TestTransformScaleOp(unittest.TestCase):

    def test_constructor(self):
        op = TransformScaleOp()
        self.assertAlmostEqual(op.x, 1.0)
        self.assertAlmostEqual(op.y, 1.0)

    def test_init(self):
        op = TransformScaleOp()
        op.init(2.0, 2.0)
        self.assertAlmostEqual(op.x, 2.0)
        self.assertAlmostEqual(op.y, 2.0)

    def test_create(self):
        op = TransformScaleOp.create(2.0, 2.0)
        self.assertAlmostEqual(op.x, 2.0)
        self.assertAlmostEqual(op.y, 2.0)

    def test_to_byte_array(self):
        op = TransformScaleOp()
        bl = op.to_byte_array()
        self.assertTrue(op.check_byte_array(bl))

    def test_from_byte_array(self):
        op = TransformScaleOp()
        ba = op.to_byte_array()
        op.from_byte_array(ba)

    def test_get_byte_array_len(self):
        op = TransformScaleOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.get_byte_array_len())

    def test_equal(self):
        op1 = TransformScaleOp()
        self.assertTrue(op1 == op1)
        op2 = TransformScaleOp.create(2.0, 2.0)
        self.assertFalse(op1 == op2)

    def test_not_equal(self):
        op1 = TransformScaleOp()
        op2 = TransformScaleOp.create(2.0, 2.0)
        self.assertTrue(op1 != op2)


# Тестирование класса SetAntialiasingOp
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

    def test_to_byte_array(self):
        op = SetAntialiasingOp()
        ba = op.to_byte_array()
        self.assertTrue(op.check_byte_array(ba))

    def test_from_byte_array(self):
        op = SetAntialiasingOp()
        bl = op.to_byte_array()
        op.from_byte_list(bl)

    def test_get_byte_array_len(self):
        op = SetAntialiasingOp()
        bl = op.to_byte_array()
        self.assertEqual(op.get_byte_array_len(), len(bl))

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


# Тестирование класса SetFontOp
class TestSetFontOp(object):

    def test_constructor(self):
        op = SetFontOp()
        font = bmg.Font()
        self.assertEqual(op.font, font)

    def test_init(self):
        op = SetFontOp()

    def test_create(self):
        op = SetFontOp()

    def test_to_byte_array(self):
        op = SetFontOp()
        bl = op.to_byte_list()
        self.assertTrue(op.check_byte_list(bl))

    def test_from_byte_array(self):
        op = SetFontOp()
        ba = op.to_byte_array()
        op.from_byte_list(ba)

    def test_get_byte_array_len(self):
        op = SetFontOp()
        ba = op.to_byte_array()
        self.assertEqual(len(ba), op.to_byte_array())

    def test_equal(self):
        op = SetFontOp()
        self.assertTrue(op == op)

    def test_not_equal(self):
        op = SetFontOp()
        self.assertFalse(op != op)


# Тестирование класса DrawLineOp
class TestDrawLineOp(unittest.TestCase):

    def test_constructor(self):
        op = DrawLineOp()
        self.assertEqual(op.line, bmg.Line())

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

    def test_to_byte_array(self):
        op = DrawLineOp()
        bl = op.to_byte_array()
        self.assertTrue(op.check_byte_array(bl))

    def test_from_byte_array(self):
        pass

    def test_get_byte_array_len(self):
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


class TestDrawLinefOp(unittest.TestCase):
    """Тест класса DrawLinefOp."""

    def test_constructor(self):
        """Тест конструктора."""
        op = DrawLinefOp()
        line = op.line

    def test_init(self):
        """Тест функции init."""
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

    def test_to_byte_array(self):
        op = DrawLinefOp()
        bl = op.to_byte_array()
        self.assertTrue(op.check_byte_array(bl))

    def test_from_byte_array(self):
        pass

    def test_get_byte_array_len(self):
        pass

    def test_equal(self):
        """Тест оператора ==."""
        op1 = DrawLinefOp()
        self.assertTrue(op1 == op1)
        op2 = DrawLinefOp.create3(10.0, 10.0, 200.0, 200.0)
        self.assertFalse(op1 == op2)

    def test_not_equal(self):
        """Тест оператора !=."""
        op1 = DrawLinefOp()
        self.assertFalse(op1 != op1)
        op2 = DrawLinefOp.create3(10.0, 10.0, 200.0, 200.0)
        self.assertTrue(op1 != op2)


# Тестирование класса DrawRectOp
# class TestDrawRectOp(unittest.TestCase):

#     def test_constructor(self):
#         op = DrawRectOp()

#     def test_init(self):
#         op = DrawRectOp()

#     def test_create(self):
#         rect = Rect.create2(10, 10, 300, 300)
#         op = DrawRectOp.create(rect)
#         self.assertEqual(op.rect, rect)

#     def test_to_byte_list(self):
#         op = DrawRectOp()
#         bl = op.to_byte_list()
#         self.assertTrue(op.check_byte_list(bl))

#     def test_from_byte_list(self):
#         pass

#     def test_get_byte_list_len(self):
#         pass

#     def test_equal(self):
#         op1 = DrawRectOp()
#         self.assertTrue(op1 == op1)
#         rect = Rect.create2(10, 10, 300, 300)
#         op2 = DrawRectOp.create(rect)
#         self.assertFalse(op1 == op2)

#     def test_not_equal(self):
#         op1 = DrawRectOp()
#         self.assertFalse(op1 != op1)
#         rect = Rect.create2(10, 10, 300, 300)
#         op2 = DrawRectOp.create(rect)
#         self.assertTrue(op1 != op2)


# Тестирование класса DrawRectsOp
# class TestDrawRectsOp(unittest.TestCase):

#     def test_constructor(self):
#         op = DrawRectsOp()

#     def test_init(self):
#         op = DrawRectsOp()

#     def test_create(self):
#         rects = [Rect(), Rect(), Rect()]
#         op = DrawRectsOp.create(rects)
#         self.assertEqual(op.rects, rects)

#     def test_to_byte_list(self):
#         op = DrawRectsOp()
#         bl = op.to_byte_list()
#         self.assertTrue(op.check_byte_list(bl))

#     def test_from_byte_list(self):
#         pass

#     def test_get_byte_list_len(self):
#         pass

#     def test_equal(self):
#         pass

#     def test_not_equal(self):
#         pass


# Тестирование класса DrawRectfOp
# class TestDrawRectfOp(unittest.TestCase):

#     def test_constructor(self):
#         op = DrawRectfOp()
#         self.assertEqual(op.rect, RectF())

#     def test_init(self):
#         op = DrawRectfOp()
#         rect = RectF.create2(0.0, 0.0, 200.0, 200.0)
#         op.init(rect)
#         self.assertEqual(op.rect, rect)

#     def test_create(self):
#         op = DrawRectfOp()

#     def test_to_byte_list(self):
#         op = DrawRectfOp()

#     def test_from_byte_list(self):
#         op = DrawRectfOp()

#     def test_get_byte_list_len(self):
#         pass

#     def test_equal(self):
#         rect1 = RectF.create2(0.0, 0.0, 200.0, 200.0)
#         op1 = DrawRectfOp.create(rect1)
#         self.assertTrue(op1 == op1)
#         rect2 = RectF.create2(10.0, 10.0, 200.0, 200.0)
#         op2 = DrawRectfOp.create(rect2)
#         self.assertFalse(op1 == op2)

#     def test_not_equal(self):
#         rect1 = RectF.create2(0.0, 0.0, 200.0, 200.0)
#         op1 = DrawRectfOp.create(rect1)
#         self.assertFalse(op1 != op1)
#         rect2 = RectF.create2(10.0, 10.0, 300.0, 300.0)
#         op2 = DrawRectfOp.create(rect2)
#         self.assertTrue(op1 != op2)


# Тестирование класса DrawRectsfOp
# class TestDrawRectsfOp(unittest.TestCase):

#     def test_constructor(self):
#         op = DrawRectsfOp()
#         self.assertEqual(op.rects, [])
#         self.assertTrue(op.is_empty())

#     def test_init(self):
#         op = DrawRectsfOp()

#     def test_create(self):
#         pass

#     def test_to_byte_list(self):
#         pass

#     def test_from_byte_list(self):
#         pass

#     def test_get_byte_list_len(self):
#         pass

#     def test_equal(self):
#         DrawRectsfOp()

#     def test_not_equal(self):
#         pass


# Тестирование класса DrawEllipseOp
# class TestDrawEllipseOp(unittest.TestCase):

#     def test_constructor(self):
#         op = DrawEllipseOp()
#         self.assertEqual(op.rect, Rect())

#     def test_init(self):
#         op = DrawEllipseOp()

#     def test_create(self):
#         op = DrawEllipseOp()

#     def test_to_byte_list(self):
#         op = DrawEllipseOp()

#     def test_from_byte_list(self):
#         op = DrawEllipseOp()

#     def test_get_byte_list_len(self):
#         pass

#     def test_equal(self):
#         op1 = DrawEllipseOp()
#         self.assertTrue(op1 == op1)
#         rect = Rect.create2(100, 100, 200, 200)
#         op2 = DrawEllipseOp.create(rect)
#         self.assertFalse(op1 == op2)

#     def test_not_equal(self):
#         op1 = DrawEllipseOp()
#         self.assertFalse(op1 != op1)
#         rect = Rect.create2(100, 100, 200, 200)
#         op2 = DrawEllipseOp.create(rect)
#         self.assertTrue(op1 != op2)


# Тестирование класса DrawEllipsesOp
# class TestDrawEllipsesOp(unittest.TestCase):

#     def test_constructor(self):
#         op = DrawEllipsesOp()
#         self.assertTrue(op.is_empty())
#         self.assertEqual(op.get_rect_count(), 0)

#     def test_init(self):
#         rects = [Rect(), Rect(), Rect()]
#         op = DrawEllipsesOp()

#     def test_create(self):
#         op = DrawEllipsesOp()

#     def test_to_byte_list(self):
#         op = DrawEllipsesOp()

#     def test_from_byte_list(self):
#         op = DrawEllipsesOp()

#     def test_get_byte_list_len(self):
#         pass

#     def test_equal(self):
#         op = DrawEllipsesOp()
#         self.assertTrue(op == op)

#     def test_not_equal(self):
#         op = DrawEllipsesOp()
#         self.assertFalse(op != op)


# Тестирование класса DrawEllipsefOp
# class TestDrawEllipsefOp(unittest.TestCase):

#     def test_constructor(self):
#         op = DrawEllipsefOp()
#         self.assertEqual(op.rect, RectF())

#     def test_init(self):
#         op = DrawEllipsefOp()
#         rect = RectF.create2(100.0, 100.0, 200.0, 200.0)
#         op.init(rect)
#         self.assertEqual(op.rect, rect)

#     def test_create(self):
#         rect = RectF.create2(100.0, 100.0, 200.0, 200.0)
#         op = DrawEllipsefOp.create(rect)
#         self.assertEqual(op.rect, rect)

#     def test_to_byte_list(self):
#         op = DrawEllipsefOp()
#         bl = op.to_byte_list()
#         self.assertTrue(op.check_byte_list(bl))

#     def test_from_byte_list(self):
#         op = DrawEllipsefOp()

#     def test_get_byte_list_len(self):
#         pass

#     def test_equal(self):
#         op1 = DrawEllipsefOp()
#         self.assertTrue(op1 == op1)
#         rect = RectF.create2(100.0, 100.0, 200.0, 200.0)
#         op2 = DrawEllipsefOp.create(rect)
#         self.assertFalse(op1 == op2)

#     def test_not_equal(self):
#         op1 = DrawEllipsefOp()
#         self.assertFalse(op1 != op1)
#         rect = RectF.create2(100.0, 100.0, 200.0, 200.0)
#         op2 = DrawEllipsefOp.create(rect)
#         self.assertTrue(op1 != op2)


# Тестирование класса DrawEllipsesfOp
# class TestDrawEllipsesfOp(unittest.TestCase):

#     def test_constructor(self):
#         op = DrawEllipsesfOp()
#         self.assertTrue(op.is_empty())

#     def test_init(self):
#         op = DrawEllipsesfOp()
#         rects = [RectF(), RectF(), RectF()]
#         op.init(rects)
#         self.assertEqual(op.get_rect_count(), len(rects))

#     def test_create(self):
#         rects = [RectF(), RectF(), RectF()]
#         op = DrawEllipsesfOp.create(rects)
#         self.assertEqual(op.get_rect_count(), len(rects))

#     def test_to_byte_list(self):
#         op = DrawEllipsesfOp()
#         rects = [RectF(), RectF(), RectF()]
#         op.init(rects)
#         bl = op.to_byte_list()
#         self.assertTrue(op.check_byte_list(bl))

#     def test_from_byte_list(self):
#         op = DrawEllipsesfOp()

#     def test_get_byte_list_len(self):
#         pass

#     def test_equal(self):
#         op = DrawEllipsesfOp()
#         self.assertTrue(op == op)

#     def test_not_equal(self):
#         op = DrawEllipsesfOp()
#         self.assertFalse(op != op)


# Тестирование класса DrawPolylineOp
# class TestDrawPolylineOp(unittest.TestCase):

#     def test_constructor(self):
#         op = DrawPolylineOp()
#         self.assertEqual(op.polyline, Polyline())

#     def init(self):
#         polyline = Polyline.create([Point()])
#         op = DrawPolylineOp()
#         op.init(polyline)
#         self.assertFalse(op.is_empty())
#         self.assertEqual(op.get_point_count(), 1)

#     def test_create(self):
#         polyline = Polyline.create([Point()])
#         op = DrawPolylineOp.create(polyline)
#         self.assertFalse(op.is_empty())
#         self.assertEqual(op.get_point_count(), 1)

#     def test_to_byte_list(self):
#         op = DrawPolylineOp()
#         bl = op.to_byte_list()
#         self.assertTrue(op.check_byte_list(bl))

#     def test_from_byte_list(self):
#         pass

#     def test_get_byte_list_len(self):
#         pass

#     def test_equal(self):
#         op = DrawPolylineOp()
#         self.assertTrue(op == op)

#     def test_not_equal(self):
#         op = DrawPolylineOp()
#         self.assertFalse(op != op)


# Тестирование класса DrawPolylinefOp
# class TestDrawPolylinefOp(unittest.TestCase):

#     def test_constructor(self):
#         op = DrawPolylinefOp()
#         self.assertEqual(op.polyline, PolylineF())

#     def init(self):
#         polyline = PolylineF.create([PointF()])
#         op = DrawPolylinefOp()
#         op.init(polyline)
#         self.assertFalse(op.is_empty())
#         self.assertEqual(op.get_point_count(), 1)

#     def test_create(self):
#         polyline = PolylineF.create([PointF()])
#         op = DrawPolylinefOp.create(polyline)

#     def test_to_byte_list(self):
#         pass

#     def test_from_byte_list(self):
#         pass

#     def test_get_byte_list_len(self):
#         pass

#     def test_equal(self):
#         op = DrawPolylinefOp()
#         self.assertTrue(op == op)

#     def test_not_equal(self):
#         op = DrawPolylinefOp()
#         self.assertFalse(op != op)


# Тестирование класса DrawPolygonOp
# class TestDrawPolygonOp(unittest.TestCase):

#     def test_constructor(self):
#         op = DrawPolygonOp()
#         self.assertEqual(op.polygon, Polygon())

#     def init(self):
#         polygon = Polygon.create([Point()])
#         op = DrawPolygonOp()
#         op.init(polygon)
#         self.assertEqual(op.polygon, polygon)

#     def test_create(self):
#         pass

#     def test_to_byte_list(self):
#         pass

#     def test_from_byte_list(self):
#         pass

#     def test_get_byte_list_len(self):
#         pass

#     def test_equal(self):
#         op = DrawPolygonOp()
#         self.assertTrue(op == op)

#     def test_not_equal(self):
#         op = DrawPolygonOp()
#         self.assertFalse(op != op)


# Тестирование класса DrawPolygonfOp
# class TestDrawPolygonfOp(unittest.TestCase):

#     def test_constructor(self):
#         op = DrawPolygonfOp()
#         self.assertEqual(op.polygon, PolygonF())

#     def test_init(self):
#         polygon = PolygonF.create([PointF()])
#         op = DrawPolygonfOp()
#         op.init(polygon)
#         self.assertEqual(op.polygon, polygon)

#     def test_create(self):
#         polygon = PolygonF.create([PointF()])
#         op = DrawPolygonfOp.create(polygon)
#         self.assertEqual(op.polygon, polygon)

#     def test_to_byte_list(self):
#         polygon = PolygonF.create([PointF()])
#         op = DrawPolygonfOp.create(polygon)
#         bl = op.to_byte_list()
#         self.assertTrue(op.check_byte_list(bl))

#     def test_from_byte_list(self):
#         pass

#     def test_get_byte_list_len(self):
#         op = DrawPolygonfOp()

#     def test_equal(self):
#         op = DrawPolygonfOp()
#         self.assertTrue(op == op)
#         points = [Point()]

#     def test_not_equal(self):
#         op = DrawPolygonfOp()
#         self.assertFalse(op != op)


# class TestPainter(unittest.TestCase):
#     '''
#     Тестирование класса Painter.
#     '''

#     def test_save_state(self):
#         painter = Painter()
#         painter.save_state()
#         self.assertFalse(painter.is_op_empty())
#         self.assertEqual(painter.get_op_count(), 1)

#     def test_restore_state(self):
#         painter = Painter()
#         painter.restore_state()

#     def test_set_clip_rect(self):
#         painter = Painter()
#         rect = bmp.bmg.Rect.create2(0, 0, 100, 100)
#         painter.set_clip_rect(rect)

#     def test_transform_translate(self):
#         painter = Painter()
#         painter.transform_translate(0.0, 0.0)

#     def test_transform_rotate(self):
#         painter = Painter()
#         painter.transform_rotate(45.0)

#     def test_transform_scale(self):
#         painter = Painter()
#         painter.transform_scale(2.0, 2.0)

#     def test_set_pen(self):
#         painter = Painter()
#         pen = bmp.bmg.Pen()
#         painter.set_pen(pen)

#     def test_set_brush(self):
#         painter = Painter()
#         brush = bmp.bmg.Brush()
#         painter.set_brush(brush)

#     def test_set_font(self):
#         painter = Painter()
#         font = bmp.bmg.Font()

#     def test_set_antialiasing(self):
#         painter = Painter()

#     def test_draw_point(self):
#         painter = Painter()
#         pt = bmp.bmg.Point.create(100, 100)

#     def test_draw_point_2(self):
#         painter = Painter()
#         x = y = 100

#     def test_draw_points(self):
#         painter = Painter()

#     def test_draw_pointf(self):
#         painter = Painter()

#     def test_draw_pointf_2(self):
#         painter = Painter()
#         x = y = 100.0

#     def test_draw_pointsf(self):
#         painter = Painter()

#     def test_draw_line(self):
#         painter = Painter()

#     def test_draw_line_2(self):
#         painter = Painter()

#     def test_draw_line_3(self):
#         painter = Painter()

#     def test_draw_lines(self):
#         painter = Painter()

#     def test_draw_linef(self):
#         painter = Painter()

#     def test_draw_linef_2(self):
#         painter = Painter()

#     def test_draw_linef_3(self):
#         painter = Painter()

#     def test_draw_linesf(self):
#         painter = Painter()

#     def test_draw_rect(self):
#         painter = Painter()

#     def test_draw_rects(self):
#         painter = Painter()

#     def test_draw_rectf(self):
#         painter = Painter()

#     def test_draw_rectsf(self):
#         painter = Painter()

#     def test_draw_round_rect(self):
#         painter = Painter()

#     def test_draw_round_rects(self):
#         painter = Painter()

#     def test_draw_round_rectf(self):
#         painter = Painter()

#     def test_draw_round_rectsf(self):
#         painter = Painter()

#     def test_draw_ellipse(self):
#         painter = Painter()

#     def test_draw_ellipses(self):
#         painter = Painter()

#     def test_draw_ellipsef(self):
#         painter = Painter()

#     def test_draw_ellipsesf(self):
#         painter = Painter()

#     def test_draw_polygon(self):
#         painter = Painter()

#     def test_draw_polygonf(self):
#         painter = Painter()

#     def test_draw_image(self):
#         painter = Painter()
#         path = ''

#     def test_draw_text(self):
#         painter = Painter()
#         text = '123'


# Вызывается при загрузке модуля главным.
if __name__ == "__main__":
    unittest.main()
