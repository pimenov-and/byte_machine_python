# coding: utf8
'''
ByteMachine
Состояние дизайнера.
'''
from __future__ import annotations
import unittest
import byte_machine_graphics_3 as bmg


class Designer(object):
    '''
    Состояние дизайнера.
    '''

    def __init__(self):
        '''
        Конструктор без параметров.
        '''
        self.size = bmg.Size()
        self.viewportSize = bmg.Size()
        self.horzScrollPos = 0
        self.vertScrollPos = 0

    def init(self, size: bmg.Size, viewportSize: bmg.Size,
             horzScrollPos: int = 0, vertScrollPos: int = 0) -> None:
        '''
        Функция инициализации
        '''
        assert isinstance(size, bmg.Size)
        assert isinstance(viewportSize, bmg.Size)
        assert isinstance(horzScrollPos, int)
        assert isinstance(vertScrollPos, int)
        self.size = size
        self.viewportSize = viewportSize
        self.horzScrollPos = horzScrollPos
        self.vertScrollPos = vertScrollPos

    def check_byte_array(self, byte_array: bytearray) -> bool:
        '''
        Проверка корректности списка байтов для инициализации.
        '''
        # assert isinstance(byte_array, bytearray)
        return len(byte_array) == self.get_byte_array_len()

    def from_byte_array(self, byte_array: bytearray) -> None:
        '''
        Инициализация из массива байтов.
        '''
        assert self.check_byte_array(byte_array)
        ba_size = byte_array[:16]
        self.size.from_byte_array(ba_size)
        ba_viewport_size = byte_array[16:32]
        self.viewportSize.from_byte_array(ba_viewport_size)
        # self.isLeftBtnDown = bmg.bmc.byte_array_to_bool([byte_array[8]])
        # self.isMiddleBtnDown = bmg.bmc.byte_array_to_bool([byte_array[9]])
        # self.isRightBtnDown = bmg.bmc.byte_array_to_bool([byte_array[10]])

    def to_byte_array(self) -> bytearray:
        '''
        Получение в виде массива байтов.
        '''
        ba = bytearray()
        ba += self.size.to_byte_array()
        ba += self.viewportSize.to_byte_array()
        ba += bmg.bmc.int32_to_byte_array(self.horzScrollPos)
        ba += bmg.bmc.int32_to_byte_array(self.vertScrollPos)
        ba += bmg.bmc.uint8_to_byte_array(0)  # резерв
        return ba

    def get_byte_array_len(self) -> int:
        '''
        Получение длины массива байтов.
        '''
        return 25

    def __eq__(self, other: Designer) -> bool:
        '''
        Оператор ==.
        '''
        isSizeEq = (self.size == other.size)
        isViewportSizeEq = (self.viewportSize == other.viewportSize)
        isHorzScrollPosEq = (self.horzScrollPos == other.horzScrollPos)
        isVertScrollPosEq = (self.vertScrollPos == other.vertScrollPos)
        return isSizeEq and isViewportSizeEq and isHorzScrollPosEq \
            and isVertScrollPosEq

    def __ne__(self, other: Designer) -> bool:
        '''
        Оператор !=.
        '''
        return not (self == other)

    def __str__(self) -> str:
        '''
        Получение строкового представления.
        '''
        return '{}, {}, {}, {}'.format(self.size, self.viewportSize,
                                       self.horzScrollPos,
                                       self.vertScrollPos)


class TestDesigner(unittest.TestCase):
    '''
    Тестирование класса Designer.
    '''

    pass
