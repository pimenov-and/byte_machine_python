# coding: utf8
import sys
import struct
import random
import unittest


#----------------------------------------------------------------
# Функции конвертации одиночных значений
#----------------------------------------------------------------

def str_to_byte_list(value):
    '''
    Функция переводит string в список байтов.
    Список байтов имеет тип int.
    '''
    assert isinstance(value, str)
    return [ord(c) for c in value]


def byte_list_to_str(byte_list):
    '''
    Функция переводит список байтов в string.
    Список байтов имеет тип int.
    '''
    s = ''
    for b in byte_list:
        s += chr(b)
    return s


def unicode_to_byte_list(value):
    '''
    Функция переводит unicode в список байтов.
    Список байтов имеет тип int.
    '''
    assert isinstance(value, unicode)
    us = value.encode('utf-8')
    return str_to_byte_list(us)


def byte_list_to_unicode(value):
    '''
    Функция переводит список байтов в unicode.
    Список байтов имеет тип int.
    '''
    s = byte_list_to_str(value)
    return s.decode('utf-8')


def bool_to_byte_list(value):
    '''
    Функция переводит bool в список байтов.
    Список байтов имеет тип int.
    '''
    assert isinstance(value, bool)
    r = struct.pack('?', value)
    return [ord(b) for b in r]


def byte_list_to_bool(byte_list):
    '''
    Функция переводит список байтов в bool.
    Список байтов имеет тип int.
    '''
    assert len(byte_list) == 1
    ba = bytearray(byte_list)
    r = struct.unpack('?', ba)
    return r[0]


def int8_to_byte_list(value):
    '''
    Функция переводит int8 в список байтов.
    Все значения имеют тип int.
    '''
    assert -128 <= value <= 127
    r = struct.pack('b', value)
    return [ord(b) for b in r]


def byte_list_to_int8(byte_list):
    '''
    Функция переводит последовательность байтов в int8.
    Все значения имеют тип int.
    '''
    assert len(byte_list) == 1
    ba = bytearray(byte_list)
    r = struct.unpack('b', ba)
    return r[0]


def uint8_to_byte_list(value):
    '''
    Функция переводит uint8 в список байтов.
    Все значения представлены типом int.
    '''
    assert 0 <= value <= 255
    r = struct.pack('B', value)
    return [ord(b) for b in r]


def byte_list_to_uint8(byte_list):
    '''
    Функция переводит список байтов в uint8.
    Все значения имеют тип int.
    '''
    assert len(byte_list) == 1
    ba = bytearray(byte_list)
    r = struct.unpack('B', ba)
    return r[0]


def int16_to_byte_list(value, is_little_endian=True):
    '''
    Функция переводит int16 в список байтов.
    Все значения имеют тип int.
    is_little_endian определяет порядок байтов.
    '''
    assert -32768 <= value <= 32767
    if is_little_endian:
        r = struct.pack('<h', value)
    else:
        r = struct.pack('>h', value)
    return [ord(b) for b in r]


def byte_list_to_int16(byte_list, is_little_endian=True):
    '''
    Функция переводит список байтов в int16.
    Все значения имеют тип int.
    is_little_endian определяет порядок байтов.
    '''
    assert len(byte_list) == 2
    ba = bytearray(byte_list)
    if is_little_endian:
        r = struct.unpack('<h', ba)
    else:
        r = struct.unpack('>h', ba)
    return r[0]


def uint16_to_byte_list(value, is_little_endian=True):
    '''
    Функция переводит uint16 в список байтов.
    Все значения имеют тип int.
    is_little_endian определяет порядок байтов.
    '''
    assert 0 <= value <= 65535
    if is_little_endian:
        r = struct.pack('<H', value)
    else:
        r = struct.pack('>H', value)
    return [ord(b) for b in r]


def byte_list_to_uint16(byte_list, is_little_endian=True):
    '''
    Функция переводит список байтов в int16.
    Все значения представлены типом int.
    is_little_endian определяет порядок байтов.
    '''
    assert len(byte_list) == 2
    ba = bytearray(byte_list)
    if is_little_endian:
        r = struct.unpack('<H', ba)
    else:
        r = struct.unpack('>H', ba)
    return r[0]


def int32_to_byte_list(value, is_little_endian=True):
    '''
    Функция переводит int32 в список байтов.
    Все значения преставлены типом int.
    is_little_endian определяет порядок байтов.
    '''
    assert -2147483648 <= value <= 2147483647
    if is_little_endian:
        r = struct.pack('<i', value)
    else:
        r = struct.pack('>i', value)
    return [ord(b) for b in r]


def byte_list_to_int32(byte_list, is_little_endian=True):
    '''
    Функция переводит список байтов в int32.
    Все значения представлены типом int.
    is_little_endian определяет порядок байтов.
    '''
    assert len(byte_list) == 4
    ba = bytearray(byte_list)
    if is_little_endian:
        r = struct.unpack('<i', ba)
    else:
        r = struct.unpack('>i', ba)
    return r[0]


def uint32_to_byte_list(value, is_little_endian=True):
    '''
    Функция переводит список байтов в uint32.
    Все значения имеют тип int.
    is_little_endian определяет порядок байтов.
    '''
    assert 0 <= value <= 4294967295
    if is_little_endian:
        r = struct.pack('<I', value)
    else:
        r = struct.pack('>I', value)
    return [ord(b) for b in r]


def byte_list_to_uint32(byte_list, is_little_endian=True):
    '''
    Функция переводит список байтов в uint32.
    Все значения представлены типом int.
    is_little_endian определяет порядок байтов.
    '''
    assert len(byte_list) == 4
    ba = bytearray(byte_list)
    if is_little_endian:
        r = struct.unpack('<I', ba)
    else:
        r = struct.unpack('>I', ba)
    return r[0]


def int64_to_byte_list(value, is_little_endian=True):
    '''
    Функция конвертации значения int64 в набор байтов.
    Все значения представлены типом int.
    is_little_endian определяет порядок байтов.
    '''
    assert -9223372036854775808 <= value <= 9223372036854775807
    if is_little_endian:
        r = struct.pack('<q', value)
    else:
        r = struct.pack('>q', value)
    return [ord(b) for b in r]


def byte_list_to_int64(byte_list, is_little_endian=True):
    '''
    Функция переводит список байтов в int64.
    Все значения представлены типом int.
    is_little_endian определяет порядок байтов.
    '''
    assert len(byte_list) == 8
    ba = bytearray(byte_list)
    if is_little_endian:
        r = struct.unpack('<q', ba)
    else:
        r = struct.unpack('>q', ba)
    return r[0]


def uint64_to_byte_list(value, is_little_endian=True):
    '''
    Конвертация int64 в список байтов.
    Все значения представлены типом int.
    is_little_endian определяет порядок байтов.
    '''
    assert 0 <= value <= 18446744073709551615
    if is_little_endian:
        r = struct.pack('<Q', value)
    else:
        r = struct.pack('>Q', value)
    return [ord(b) for b in r]


def byte_list_to_uint64(byte_list, is_little_endian=True):
    '''
    Конвертация списка байтов в int64.
    Все значения представлены типом int.
    is_little_endian определяет порядок байтов.
    '''
    assert len(byte_list) == 8
    ba = bytearray(byte_list)
    if is_little_endian:
        r = struct.unpack('<Q', ba)
    else:
        r = struct.unpack('>Q', ba)
    return r[0]


def float_to_byte_list(value, is_little_endian=True):
    '''
    Конвертация значения float в список байтов.
    Выходящий список байтов представлен типом int.
    is_little_endian определяет порядок байтов.
    '''
    if is_little_endian:
        byte_str = struct.pack('<f', value)
    else:
        byte_str = struct.pack('>f', value)
    return [ord(b) for b in byte_str]


def byte_list_to_float(byte_list, is_little_endian=True):
    '''
    Конвертация списка байтов во float.
    Входящий список байтов представлен типом int.
    is_little_endian определяет порядок байтов.
    '''
    assert len(byte_list) == 4
    ba = bytearray(byte_list)
    if is_little_endian:
        r = struct.unpack('<f', ba)
    else:
        r = struct.unpack('>f', ba)
    return r[0]    


def double_to_byte_list(value, is_little_endian=True):
    '''
    Функция преобразует double в список байтов.
    Список байтов имеет тип int.
    is_little_endian определяет порядок байтов.
    '''
    if is_little_endian:
        r = struct.pack('<d', value)
    else:
        r = struct.pack('>d', value)
    return [ord(b) for b in r]


def byte_list_to_double(byte_list, is_little_endian=True):
    '''
    Функция преобразует список байтов в double.
    Список байтов имеет тип int.
    is_little_endian определяет порядок байтов.
    '''
    assert len(byte_list) == 8
    ba = bytearray(byte_list)
    if is_little_endian:
        r = struct.unpack('<d', ba)
    else:
        r = struct.unpack('>d', ba)
    return r[0]


#----------------------------------------------------------------
# Функции конвертации последовательности значений
#----------------------------------------------------------------

def bool_list_to_byte_list(bool_list):
    '''
    Функция преобразует список bool в список байтов.
    Входящий список bool, выходящий список int.
    '''
    r = [bool_to_byte_list(v) for v in bool_list]
    return sum(r, [])


def byte_list_to_bool_list(byte_list):
    '''
    Функция преобразует список байтов в список bool.
    Байты представляеются списком int.
    '''
    return [byte_list_to_bool([b]) for b in byte_list]


def int8_list_to_byte_list(int8_list):
    '''
    Функция преобразует список int8 в список байтов.
    Все значения представляются типом int.
    '''
    r = [int8_to_byte_list(v) for v in int8_list]
    return sum(r, [])


def byte_list_to_int8_list(byte_list):
    '''
    Функция преобразует список байтов в список int8.
    Все значения представляются типом int.
    '''
    return [byte_list_to_int8([v]) for v in byte_list]


def uint8_list_to_byte_list(int8_list):
    '''
    Функция преобразует список uint8 в список байтов.
    Все значения представляются типом int.
    '''
    r = [uint8_to_byte_list(v) for v in int8_list]
    return sum(r, [])


def byte_list_to_uint8_list(byte_list):
    '''
    Функция преобразует список байтов в список uint8.
    Все значения представляются типом int.
    '''
    return [byte_list_to_uint8([b]) for b in byte_list]


def int16_list_to_byte_list(int16_list, is_little_endian=True):
    '''
    Функция преобразует список int16 в список байтов.
    Все значения представляются типом int.
    '''
    r = [int16_to_byte_list(v, is_little_endian) for v in int16_list]
    return sum(r, [])


def byte_list_to_int16_list(byte_list, is_little_endian=True):
    '''
    Функция преобразует список байтов в список int16.
    Все значения представляются типом int.
    '''
    type_size = 2
    r = []
    for i in range(0, len(byte_list) - 1, type_size):
        b = byte_list[i:i + type_size]
        v = byte_list_to_int16(b, is_little_endian)
        r.append(v)
    return r


def uint16_list_to_byte_list(uint16_list, is_little_endian=True):
    '''
    Функция преобразует список uint16 в список байтов.
    Все значения представляются типом int.
    '''
    r = [uint16_to_byte_list(v, is_little_endian) for v in uint16_list]
    return sum(r, [])


def byte_list_to_uint16_list(byte_list, is_little_endian=True):
    '''
    Функция преобразует список байтов в список uint16.
    Все значения представляются типом int.
    '''
    type_size = 2
    r = []
    for i in range(0, len(byte_list) - 1, type_size):
        b = byte_list[i:i + type_size]
        v = byte_list_to_uint16(b, is_little_endian)
        r.append(v)
    return r


def int32_list_to_byte_list(int32_list, is_little_endian=True):
    '''
    Функция преобразует список uint16 в список байтов.
    Все значения представляются типом int.
    '''
    r = [int32_to_byte_list(v, is_little_endian) for v in int32_list]
    return sum(r, [])


def byte_list_to_int32_list(byte_list, is_little_endian=True):
    '''
    Функция преобразует список байтво в список int32.
    Все значения представляются типом int
    '''
    type_size = 4
    r = []
    for i in range(0, len(byte_list) - 1, type_size):
        b = byte_list[i:i + type_size]
        v = byte_list_to_int32(b, is_little_endian)
        r.append(v)
    return r


def uint32_list_to_byte_list(int32_list, is_little_endian=True):
    '''
    Функция преобразует список uint16 в список байтов.
    Все значения представляются типом int
    '''
    r = [uint32_to_byte_list(v, is_little_endian) for v in int32_list]
    return sum(r, [])


def byte_list_to_uint32_list(byte_list, is_little_endian=True):
    '''
    Функция преобразует список байтов в список uint32.
    Все значения представляются типом int
    '''
    type_size = 4
    r = []
    for i in range(0, len(byte_list) - 1, type_size):
        b = byte_list[i:i + type_size]
        v = byte_list_to_uint32(b, is_little_endian)
        r.append(v)
    return r


def int64_list_to_byte_list(int64_list, is_little_endian=True):
    '''
    Функция преобразует список uint16 в список байтов.
    Все значения представляются типом int
    '''
    r = [int64_to_byte_list(v, is_little_endian) for v in int64_list]
    return sum(r, [])


def byte_list_to_int64_list(byte_list, is_little_endian=True):
    '''
    Функция преобразует список байтов в список int64.
    Все значения представляются типом int
    '''
    type_size = 8
    r = []
    for i in range(0, len(byte_list) - 1, type_size):
        b = byte_list[i:i + type_size]
        v = byte_list_to_int64(b, is_little_endian)
        r.append(v)
    return r


def uint64_list_to_byte_list(uint64_list, is_little_endian=True):
    '''
    Функция преобразует список uint16 в список байтов.
    Все значения представляются типом int
    '''
    r = [uint64_to_byte_list(v, is_little_endian) for v in uint64_list]
    return sum(r, [])


def byte_list_to_uint64_list(byte_list, is_little_endian=True):
    '''
    Функция преобразует список байтов в список uint64.
    Все значения представляются типом int
    '''
    type_size = 8
    r = []
    for i in range(0, len(byte_list) - 1, type_size):
        b = byte_list[i:i + type_size]
        v = byte_list_to_uint64(b, is_little_endian)
        r.append(v)
    return r


def float_list_to_byte_list(float_list, is_little_endian=True):
    '''
    Функция преобразует список uint16 в список байтов.
    Все значения представляются типом int.
    '''
    r = [float_to_byte_list(v, is_little_endian) for v in float_list]
    return sum(r, [])


def byte_list_to_float_list(byte_list, is_little_endian=True):
    '''
    Функция преобразует список байтов в список float.
    Список байтов представляется типом int, возвращаемый список типом float (8 байт).
    '''
    type_size = 4
    r = []
    for i in range(0, len(byte_list) - 1, type_size):
        b = byte_list[i:i + type_size]
        v = byte_list_to_float(b, is_little_endian)
        r.append(v)
    return r


def double_list_to_byte_list(double_list, is_little_endian=True):
    '''
    Функция преобразует список uint16 в список байтов.
    Все значения представляются типом int.
    '''
    r = [double_to_byte_list(v, is_little_endian) for v in double_list]
    return sum(r, [])


def byte_list_to_double_list(byte_list, is_little_endian=True):
    '''
    Функция преобразует список байтов в список double.
    Список байтов представляется типом int, возвращаемый список типом float (8 байт).
    '''
    type_size = 8
    r = []
    for i in range(0, len(byte_list) - 1, type_size):
        b = byte_list[i:i + type_size]
        v = byte_list_to_double(b, is_little_endian)
        r.append(v)
    return r


#----------------------------------------------------------------
# Функции для работы с битами
#----------------------------------------------------------------

def get_lo_bits(value):
    '''Получение старшей тетрады байта.'''
    assert 0 <= value <= 255
    return value & 0x0F


def get_hi_bits(value):
    '''Получение старшей тетрады байта.'''
    assert 0 <= value <= 255
    return value >> 4


def byte_to_bits(value):
    '''Конвертация байта в биты. Все значения представлены типом int.'''
    assert 0 <= value <= 255
    bit_list = []
    for i in range(8):
        v = value & (1 << i)
        bit_list.append(value_to_bit(v))
    return bit_list


def bits_to_byte(b0, b1, b2, b3, b4, b5, b6, b7):
    '''Конвертация битов в байт.'''
    bits = [b0, b1, b2, b3, b4, b5, b6, b7]
    return bit_list_to_byte(bits)


def bit_list_to_byte(values):
    '''Конвертация списка битов в байт.'''
    assert len(values) == 8
    byte = 0
    for i in range(8):
        bit = values[i]
        assert is_correct_bit(bit)
        byte |= (bit << i)
    return byte


def bytes_to_bit_list(values):
    '''
    Конвертация списка байтов в список битов.
    Списки представлены типом int.
    '''
    r = [byte_to_bits(i) for i in values]
    return sum(r, [])


def bit_list_to_bytes(values):
    '''
    Конвертация списка битов в список байтов.
    Списки представлены типом int.
    '''
    bits_in_byte = 8
    r = []
    for i in range(0, len(values) - 1, bits_in_byte):
        b = values[i:i + bits_in_byte]
        v = bit_list_to_byte(b)
        r.append(v)
    return r


def value_to_bit(value):
    '''Функция приводит значение к биту, 0 или 1.'''
    return 1 if value != 0 else 0


def is_correct_bit(value):
    '''Функция проверяет корректность значения бита.'''
    return value == 0 or value == 1


def test_bit(value, bit_index):
    '''Проверка выставленного бита.'''
    assert 0 <= value <= 255
    assert 0 <= bit_index <=7
    is_bit = value & (1 << bit_index) != 0
    return value_to_bit(is_bit)


def set_bit(value, bit_index):
    '''Бит устанавливается в 1.'''
    assert 0 <= value <= 255
    assert 0 <= bit_index <=7
    return value | (1 << bit_index)


def reset_bit(value, bit_index):
    '''Бит сбрасывается в 0.'''
    assert 0 <= value <= 255
    assert 0 <= bit_index <=7
    m = ~(1 << bit_index)
    return value & m


def flip_bit(value, bit_index):
    '''Если бит выставлен, то он сбрасывается, иначе выставляется.'''
    assert 0 <= value <= 255
    assert 0 <= bit_index <=7
    if test_bit(value, bit_index):
        return reset_bit(value, bit_index)
    else:
        return set_bit(value, bit_index)
    

def all_bits(value):
    '''Получение признака, что все биты в байте выставлены.'''
    assert 0 <= value <= 255
    return value == 255


def any_bits(value):
    '''Получение признака, что хоть один бит в байте выставлен.'''
    assert 0 <= value <= 255
    for i in range(8):
        if test_bit(value, i):
            return True
    return False


def none_bits(value):
    '''Получение признака, что все биты сброшены.'''
    assert 0 <= value <= 255
    return value == 0


def count_bits(value):
    '''Получение количества битов в байте.'''
    assert 0 <= value <= 255
    count = 0
    for i in range(8):
        if test_bit(value, i):
            count += 1
    return count


#----------------------------------------------------------------
# Функции повторяют функциональность нодов
#----------------------------------------------------------------

def generate(count, filledByte=0):
    '''Генерация списка размера count и заполненного значением filledByte.'''
    assert count >= 0
    assert 0 <= filledByte <= 255
    return [filledByte] * count


def rand_generate(count):
    '''Генерация списка размера count и заполненного случайными значениями в диапазоне 0-255.'''
    assert count >= 0
    return [random.randint(0, 255) for i in range(count)]


def take(values, count, is_begin=True):
    '''
    Получение определенного количества значений списка.
    Если is_begin равен True, то значения берутся из начала списка, иначе с конца.
    '''
    assert len(values) >= count
    if is_begin:
        return values[:count]
    else:
        size = len(values)
        return values[size - count:]


def skip(values, count, is_begin=True):
    '''
    Пропуск определенного количества значений списка.
    Если is_begin равен True, то значения пропускаются из начала списка, иначе с конца.
    '''
    assert len(values) >= count
    if is_begin:
        return values[count:]
    else:
        size = len(values)
        return values[:size - count]


def reverse(values):
    '''Реверс списка.'''
    return values[::-1]


def size(values):
    '''Получение размера списка.'''
    return len(values)


def merge(values1, values2):
    '''Объединение списков.'''
    return values1 + values2


def dump(values, byte_width=16):
    '''
    Вывод дампа значений.
    byte_width определяет ширину вывода и может быть равным 8 или 16.
    '''
    assert byte_width == 8 or byte_width == 16
    address = 0
    line_count = len(values) // byte_width
    tail_size = len(values) % byte_width
    is_tail = tail_size > 0
    for l in range(line_count):
        index = l * byte_width
        byte_line = values[index:index + byte_width]
        line = _bytes_to_hex_line(byte_line)
        address = _address32_to_hex(index)
        print(address + ' | ' + line)
    if is_tail:
        index = line_count * byte_width
        byte_line = values[index:index + tail_size]
        line = _bytes_to_hex_line(byte_line)
        address = _address32_to_hex(index)
        print(address + ' | ' + line)


def byte_to_hex(value):
    '''
    Конвертация числа в строку с шестнадцатиричным представлением без префикса 0x и
    шириной 2 символа.
    '''
    assert 0 <= value <= 255
    hex_str = hex(value)
    return hex_str[2:].upper().zfill(2)


def _address32_to_hex(value):
    '''
    Конвертация 32-разрядного адреса в строку с шестнадцатиричным представлением
    без префикса 0x и шириной 8 символа.
    '''
    assert 0 <= value <= 2147483647
    hex_str = hex(value)
    return hex_str[2:].upper().zfill(8)


def _bytes_to_hex_line(values):
    '''
    Перевод байтов в строку с разделителем ' '.
    '''
    parts = [byte_to_hex(v) for v in values]
    return ' '.join(parts)


#----------------------------------------------------------------
# Функции сравнения для float
#----------------------------------------------------------------

def float_equal(value1, value2):
    '''Функция проверки на равенство для float.'''
    eps = sys.float_info.epsilon
    return abs(value1 - value2) < eps


def float_not_equal(value1, value2):
    '''Функция проверки на неравенство для float.'''
    return not float_equal(value1, value2)


def is_float_null(value):
    '''Функция проверки float на равенство 0.'''
    return float_equal(value, 0.0)
    

#----------------------------------------------------------------
# Класс для тестирования
#----------------------------------------------------------------

class TestFileDumpMethods(unittest.TestCase):

    def test_str_to_byte_list(self):
        s = '1'
        bl = str_to_byte_list(s)
        self.assertEqual(bl, [49])

    def test_byte_list_to_str(self):
        bl = [49]
        s = byte_list_to_str(bl)
        self.assertEqual(s, '1')

    def test_unicode_to_byte_list(self):
        us = u'Андрей'
        bl = unicode_to_byte_list(us)
        us = byte_list_to_unicode(bl)

    def test_byte_list_to_unicode(self):
        pass
    
    def test_bool_to_byte_list(self):
        r = bool_to_byte_list(True)
        self.assertEqual(r, [1])

        r = bool_to_byte_list(False)
        self.assertEqual(r, [0])

    def test_byte_list_to_bool(self):
        v = [0]
        r = byte_list_to_bool(v)
        self.assertEqual(r, False)
            
    def test_int8_to_byte_list(self):
        r = int8_to_byte_list(2)
        self.assertEqual(r, [2])

    def test_byte_list_to_int8(self):
        v = [2]
        r = byte_list_to_int8(v)
        self.assertEqual(r, 2)

    def test_uint8_to_byte_list(self):
        r = uint8_to_byte_list(3)
        self.assertEqual(r, [3])

    def test_byte_list_to_uint8(self):
        v = [2]
        r = byte_list_to_uint8(v)
        self.assertEqual(r, 2)

    def test_int16_to_byte_list(self):
        r = int16_to_byte_list(4)
        self.assertEqual(r, [4, 0])

        r = int16_to_byte_list(5, False)
        self.assertEqual(r, [0, 5])
    
    def test_byte_list_to_int16(self):
        values = [1, 0]
        r = byte_list_to_int16(values)
        self.assertEqual(r, 1)

        values = [0, 1]
        r = byte_list_to_int16(values, False)
        self.assertEqual(r, 1)

    def test_uint16_to_byte_list(self):
        r = uint16_to_byte_list(1)
        self.assertEqual(r, [1, 0])

        r = uint16_to_byte_list(3, False)
        self.assertEqual(r, [0, 3])

    def test_byte_list_to_uint16(self):
        values = [1, 0]
        r = byte_list_to_uint16(values)
        self.assertEqual(r, 1)

        values = [0, 1]
        r = byte_list_to_uint16(values, False)
        self.assertEqual(r, 1)

    def test_int32_to_byte_list(self):
        r = int32_to_byte_list(3)
        self.assertEqual(r, [3, 0, 0, 0])

        r = int32_to_byte_list(5, False)
        self.assertEqual(r, [0, 0, 0, 5])

    def test_byte_list_to_int32(self):
        values = [2, 0, 0, 0]
        r = byte_list_to_int32(values)
        self.assertEqual(r, 2)

        values = [0, 0, 0, 2]
        r = byte_list_to_int32(values, False)
        self.assertEqual(r, 2)

    def test_uint32_to_byte_list(self):
        r = uint32_to_byte_list(5)
        self.assertEqual(r, [5, 0, 0, 0])

        r = uint32_to_byte_list(10, False)
        self.assertEqual(r, [0, 0, 0, 10])

    def test_byte_list_to_uint32(self):
        values = [2, 0, 0, 0]
        r = byte_list_to_uint32(values)
        self.assertEqual(r, 2)

        values = [0, 0, 0, 2]
        r = byte_list_to_uint32(values, False)
        self.assertEqual(r, 2)

    def test_int64_to_byte_list(self):
        r = int64_to_byte_list(200)
        self.assertEqual(r, [200, 0, 0, 0, 0, 0, 0, 0])

        r = int64_to_byte_list(99, False)
        self.assertEqual(r, [0, 0, 0, 0, 0, 0, 0, 99])

    def test_byte_list_to_int64(self):
        v = [3, 0, 0, 0, 0, 0, 0, 0]
        r = byte_list_to_int64(v)
        self.assertEqual(r, 3)

        v = [0, 0, 0, 0, 0, 0, 0, 3]
        r = byte_list_to_int64(v, False)
        self.assertEqual(r, 3)

    def test_uint64_to_byte_list(self):
        r = uint64_to_byte_list(200)
        self.assertEqual(r, [200, 0, 0, 0, 0, 0, 0, 0])

        r = uint64_to_byte_list(99, False)
        self.assertEqual(r, [0, 0, 0, 0, 0, 0, 0, 99])

    def test_byte_list_to_uint64(self):
        b = [2, 0, 0, 0, 0, 0, 0, 0]
        r = byte_list_to_uint64(b)
        self.assertEqual(r, 2)

        b = [0, 0, 0, 0, 0, 0, 0, 2]
        r = byte_list_to_uint64(b, False)
        self.assertEqual(r, 2)

    def test_float_to_byte_list(self):
        r = float_to_byte_list(0.0)
        self.assertEqual(r, [0, 0, 0, 0])

        r = float_to_byte_list(0.0, False)
        self.assertEqual(r, [0, 0, 0, 0])
        
    def test_byte_list_to_float(self):
        values = [0, 0, 0, 0]
        r = byte_list_to_float(values)
        self.assertEqual(r, 0)

        values = [0, 0, 0, 0]
        r = byte_list_to_float(values, False)
        self.assertEqual(r, 0)

    def test_double_to_byte_list(self):
        r = double_to_byte_list(0.0)
        self.assertEqual(r, [0, 0, 0, 0, 0, 0, 0, 0])

        r = double_to_byte_list(0.0, False)
        self.assertEqual(r, [0, 0, 0, 0, 0, 0, 0, 0])

    def test_byte_list_to_double(self):
        values = [0, 0, 0, 0, 0, 0, 0, 0]
        r = byte_list_to_double(values)
        self.assertEqual(r, 0)

        r = byte_list_to_double(values, False)
        self.assertEqual(r, 0)

    def test_bool_list_to_bytes(self):
        bl = [True, False, True, False, True]
        r = bool_list_to_byte_list(bl)
        self.assertEqual(r, [1, 0, 1, 0, 1])

    def test_byte_list_to_bool_list(self):
        b = [1, 0, 1, 0, 1]
        r = byte_list_to_bool_list(b)
        self.assertEqual(r, [True, False, True, False, True])

    def test_int8_list_to_byte_list(self):
        v = [1, 2, 3, 4]
        r = int8_list_to_byte_list(v)
        self.assertEqual(r, v)

    def test_byte_list_to_int8_list(self):
        v = [1, 2, 3, 4]
        r = byte_list_to_int8_list(v)
        self.assertEqual(r, v)

    def test_uint8_list_to_byte_list(self):
        v = [1, 2, 3, 4]
        r = uint8_list_to_byte_list(v)
        self.assertEqual(r, v)

    def test_byte_list_to_uint8_list(self):
        v = [1, 2, 3, 4]
        r = byte_list_to_uint8_list(v)
        self.assertEqual(r, v)

    def test_int16_list_to_byte_list(self):
        v = [2, 3]
        r = int16_list_to_byte_list(v)
        self.assertEqual(r, [2, 0, 3, 0])

        v = [2, 3]
        r = int16_list_to_byte_list(v, False)
        self.assertEqual(r, [0, 2, 0, 3])

    def test_byte_list_to_int16_list(self):
        v = [2, 0, 3, 0]
        r = byte_list_to_int16_list(v)
        self.assertEqual(r, [2, 3])

        v = [0, 2, 0, 3]
        r = byte_list_to_int16_list(v, False)
        self.assertEqual(r, [2, 3])

    def test_uint16_list_to_byte_list(self):
        v = [2, 3]
        r = uint16_list_to_byte_list(v)
        self.assertEqual(r, [2, 0, 3, 0])

        v = [2, 3]
        r = uint16_list_to_byte_list(v, False)
        self.assertEqual(r, [0, 2, 0, 3])

    def test_byte_list_to_uint16_list(self):
        v = [2, 0, 3, 0]
        r = byte_list_to_uint16_list(v)
        self.assertEqual(r, [2, 3])

        v = [0, 2, 0, 3]
        r = byte_list_to_uint16_list(v, False)
        self.assertEqual(r, [2, 3])

    def test_int32_list_to_byte_list(self):
        v = [2, 3]
        r = int32_list_to_byte_list(v)
        self.assertEqual(r, [2, 0, 0, 0, 3, 0, 0, 0])

        r = int32_list_to_byte_list(v, False)
        self.assertEqual(r, [0, 0, 0, 2, 0, 0, 0, 3])

    def test_byte_list_to_int32_list(self):
        v = [2, 0, 0, 0, 3, 0, 0, 0]
        r = byte_list_to_int32_list(v)
        self.assertEqual(r, [2, 3])

        v = [0, 0, 0, 2, 0, 0, 0, 3]
        r = byte_list_to_int32_list(v, False)
        self.assertEqual(r, [2, 3])

    def test_uint32_list_to_byte_list(self):
        v = [2, 3]
        r = uint32_list_to_byte_list(v)
        self.assertEqual(r, [2, 0, 0, 0, 3, 0, 0, 0])

        r = uint32_list_to_byte_list(v, False)
        self.assertEqual(r, [0, 0, 0, 2, 0, 0, 0, 3])

    def test_byte_list_to_uint32_list(self):
        v = [2, 0, 0, 0, 3, 0, 0, 0]
        r = byte_list_to_uint32_list(v)
        self.assertEqual(r, [2, 3])

        v = [0, 0, 0, 2, 0, 0, 0, 3]
        r = byte_list_to_uint32_list(v, False)
        self.assertEqual(r, [2, 3])
        
    def test_int64_list_to_byte_list(self):
        v = [2, 3]
        r = int64_list_to_byte_list(v)
        self.assertEqual(r, [2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0])

        r = int64_list_to_byte_list(v, False)
        self.assertEqual(r, [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3])

    def test_byte_list_to_int64_list(self):
        v = [2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0]
        r = byte_list_to_int64_list(v)
        self.assertEqual(r, [2, 3])

        v = [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3]
        r = byte_list_to_int64_list(v, False)
        self.assertEqual(r, [2, 3])

    def test_uint64_list_to_byte_list(self):
        v = [2, 3]
        r = uint64_list_to_byte_list(v)
        self.assertEqual(r, [2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0])

        r = uint64_list_to_byte_list(v, False)
        self.assertEqual(r, [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3])

    def test_byte_list_to_uint64_list(self):
        v = [2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0]
        r = byte_list_to_uint64_list(v)
        self.assertEqual(r, [2, 3])

        v = [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3]
        r = byte_list_to_uint64_list(v, False)
        self.assertEqual(r, [2, 3])

    def test_float_list_to_byte_list(self):
        v = [0.0]
        r = float_list_to_byte_list(v)
        self.assertEqual(r, [0, 0, 0, 0])

        v = [0.0]
        r = float_list_to_byte_list(v, False)
        self.assertEqual(r, [0, 0, 0, 0])

    def test_byte_list_to_float_list(self):
        b = generate(16)
        r = byte_list_to_float_list(b)
        self.assertEqual(len(r), 4)

    def test_double_list_to_bytes(self):
        values = [0.0, 0.0, 0.0]
        r = double_list_to_byte_list(values)
        self.assertEqual(len(r), 24)

    def test_byte_list_to_double_list(self):
        b = generate(16)
        r = byte_list_to_double_list(b)
        self.assertEqual(len(r), 2)

        b = generate(17)
        r = byte_list_to_double_list(b)
        self.assertEqual(len(r), 2)

    def test_generate(self):
        r = generate(5)
        self.assertEqual(r, [0, 0, 0, 0, 0])

        r = generate(3, 1)
        self.assertEqual(r, [1, 1, 1])

    def test_rand_generate(self):
        r = rand_generate(5)
        self.assertEqual(len(r), 5)

    def test_reverse(self):
        values = [1, 2, 3]
        r = reverse(values)
        self.assertEqual(r, [3, 2, 1])

    def test_size(self):
        values = [1, 2, 3]
        r = size(values)
        self.assertEqual(r, 3)

    def test_merge(self):
        values = [1, 2, 3]
        r = merge(values, values)
        self.assertEqual(r, [1, 2, 3, 1, 2, 3])

    def test_take(self):
        values = [1, 2, 3]
        r = take(values, 1)
        self.assertEqual(r, [1])

        r = take(values, 1, False)
        self.assertEqual(r, [3])

    def test_skip(self):
        values = [1, 2, 3]
        r = skip(values, 2)
        self.assertEqual(r, [3])

        r = skip(values, 2, False)
        self.assertEqual(r, [1])

    def test_test_bit(self):
        self.assertEqual(test_bit(1, 0), 1)
        self.assertEqual(test_bit(0, 0), 0)

    def test_is_correct_bit(self):
        self.assertTrue(is_correct_bit(0))
        self.assertTrue(is_correct_bit(1))
        self.assertFalse(is_correct_bit(2))

    def test_byte_to_hex(self):
        self.assertEqual(byte_to_hex(1), '01')
        self.assertEqual(byte_to_hex(255), 'FF')

    def test_get_lo_bits(self):
        self.assertEqual(get_lo_bits(1), 1)
        self.assertEqual(get_lo_bits(1 << 4 | 1), 1)

    def test_get_hi_bits(self):
        self.assertEqual(get_hi_bits(1), 0)
        self.assertEqual(get_hi_bits(1 << 4 | 1), 1)

    def test_value_to_bit(self):
        self.assertEqual(value_to_bit(2), 1)
        self.assertEqual(value_to_bit(0), 0)

    def test_byte_to_bits(self):
        r = byte_to_bits(1)
        self.assertEqual(r, [1, 0, 0, 0, 0, 0, 0, 0])

    def test_bits_to_byte(self):
        r = bits_to_byte(1, 1, 0, 0, 0, 0, 0, 0)
        self.assertEqual(r, 3)

        r = bits_to_byte(1, 1, 1, 1, 1, 1, 1, 1)
        self.assertEqual(r, 255)

    def test_bit_list_to_byte(self):
        b = [0, 1, 0, 0, 0, 0, 0, 0]
        r = bit_list_to_byte(b)
        self.assertEqual(r, 2)

    def test_set_bit(self):
        self.assertEqual(set_bit(1, 0), 1)
        self.assertEqual(set_bit(2, 0), 3)

    def test_reset_bit(self):
        self.assertEqual(reset_bit(1, 0), 0)
        self.assertEqual(reset_bit(2, 1), 0)
        self.assertEqual(reset_bit(3, 0), 2)

    def test_flip_bit(self):
        self.assertEqual(flip_bit(1, 0), 0)
        self.assertEqual(flip_bit(0, 0), 1)

    def test_count_bits(self):
        self.assertEqual(count_bits(1), 1)
        self.assertEqual(count_bits(3), 2)

    def test_any_bits(self):
        self.assertTrue(any_bits(1))
        self.assertTrue(any_bits(255))
        self.assertFalse(any_bits(0))

    def test_none_bits(self):
        self.assertFalse(none_bits(1))
        self.assertFalse(none_bits(255))
        self.assertTrue(none_bits(0))

    def test_all_bits(self):
        self.assertFalse(all_bits(0))
        self.assertTrue(all_bits(255))

    def test_float_equal(self):
        self.assertTrue(float_equal(1.0, 1.0))

    def test_float_not_equal(self):
        self.assertTrue(float_not_equal(0.0, 1.0))


#----------------------------------------------------------------
# Вызывается при загрузке модуля главным
#----------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
