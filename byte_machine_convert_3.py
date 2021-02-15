# coding: utf8
"""
ByteMachine
Функции преобразования значений в массивы байтов и обратно.
"""
import struct
import unittest


# Функции конвертации одиночных значений
def str_to_byte_array(value: str) -> bytearray:
    """Функция переводит строку в bytearray."""
    b = value.encode()
    return bytearray(b)


def byte_array_to_str(byte_array: bytearray) -> str:
    """Функция переводит bytearray в строку."""
    return byte_array.decode()


def bool_to_byte_array(value: bool) -> bytearray:
    """Функция переводит bool в bytearray."""
    return bytearray([1]) if value else bytearray([0])


def byte_array_to_bool(byte_array: bytearray) -> bool:
    """Функция переводит bytearray в bool."""
    return byte_array[0] != 0


def int8_to_byte_array(value: int) -> bytearray:
    """Функция переводит int8 в bytearray."""
    # assert -128 <= value <= 127
    return struct.pack('b', value)


def byte_array_to_int8(byte_array: bytearray) -> int:
    """Функция переводит bytearray в int8."""
    # assert len(byte_array) == 1
    r = struct.unpack('b', byte_array)
    return r[0]


def uint8_to_byte_array(value: int) -> bytearray:
    """Функция переводит uint8 в bytearray."""
    # assert 0 <= value <= 255
    return bytearray([value])


def byte_array_to_uint8(byte_array: bytearray) -> int:
    """Функция переводит bytearray в uint8."""
    # assert len(byte_array) == 1
    return byte_array[0]


def int16_to_byte_array(value: int,
                        is_little_endian: bool = True) -> bytearray:
    """
    Функция переводит int16 в bytearray.

    is_little_endian определяет порядок байтов.
    """
    # assert -32768 <= value <= 32767
    if is_little_endian:
        return struct.pack('<h', value)
    else:
        return struct.pack('>h', value)


def byte_array_to_int16(byte_array: bytearray,
                        is_little_endian: bool = True) -> int:
    """
    Функция переводит bytearray в int16.

    is_little_endian определяет порядок байтов.
    """
    # assert len(byte_array) == 2
    if is_little_endian:
        r = struct.unpack('<h', byte_array)
    else:
        r = struct.unpack('>h', byte_array)
    return r[0]


def uint16_to_byte_array(value: int,
                         is_little_endian: bool = True) -> bytearray:
    """
    Функция переводит uint16 в bytearray.

    is_little_endian определяет порядок байтов.
    """
    # assert 0 <= value <= 65535
    if is_little_endian:
        return struct.pack('<H', value)
    else:
        return struct.pack('>H', value)


def byte_array_to_uint16(byte_array: bytearray,
                         is_little_endian: bool = True) -> int:
    """
    Функция переводит bytearray в int16.

    is_little_endian определяет порядок байтов.
    """
    # assert len(byte_array) == 2
    if is_little_endian:
        r = struct.unpack('<H', byte_array)
    else:
        r = struct.unpack('>H', byte_array)
    return r[0]


def int32_to_byte_array(value: int,
                        is_little_endian: bool = True) -> bytearray:
    """
    Функция переводит int32 в bytearray.

    is_little_endian определяет порядок байтов.
    """
    # assert -2147483648 <= value <= 2147483647
    if is_little_endian:
        return struct.pack('<i', value)
    else:
        return struct.pack('>i', value)


def byte_array_to_int32(byte_array: bytearray,
                        is_little_endian: bool = True) -> int:
    """
    Функция переводит bytearray в int32.

    is_little_endian определяет порядок байтов.
    """
    # assert len(byte_array) == 4
    if is_little_endian:
        r = struct.unpack('<i', byte_array)
    else:
        r = struct.unpack('>i', byte_array)
    return r[0]


def uint32_to_byte_array(value: int,
                         is_little_endian: bool = True) -> bytearray:
    """
    Функция переводит bytearray в uint32.

    is_little_endian определяет порядок байтов.
    """
    # assert 0 <= value <= 4294967295
    if is_little_endian:
        return struct.pack('<I', value)
    else:
        return struct.pack('>I', value)


def byte_array_to_uint32(byte_array: bytearray,
                         is_little_endian: bool = True) -> int:
    """
    Функция переводит список байтов в uint32.

    is_little_endian определяет порядок байтов.
    """
    # assert len(byte_array) == 4
    if is_little_endian:
        r = struct.unpack('<I', byte_array)
    else:
        r = struct.unpack('>I', byte_array)
    return r[0]


def int64_to_byte_array(value: int,
                        is_little_endian: bool = True) -> bytearray:
    """
    Функция конвертации значения int64 в набор байтов.

    is_little_endian определяет порядок байтов.
    """
    # assert -9223372036854775808 <= value <= 9223372036854775807
    if is_little_endian:
        return struct.pack('<q', value)
    else:
        return struct.pack('>q', value)


def byte_array_to_int64(byte_array: bytearray,
                        is_little_endian: bool = True) -> int:
    """
    Функция переводит список байтов в int64.

    is_little_endian определяет порядок байтов.
    """
    # assert len(byte_array) == 8
    if is_little_endian:
        r = struct.unpack('<q', byte_array)
    else:
        r = struct.unpack('>q', byte_array)
    return r[0]


def uint64_to_byte_array(value: int,
                         is_little_endian: bool = True) -> bytearray:
    """
    Конвертация uint64 в bytearray.

    is_little_endian определяет порядок байтов.
    """
    # assert 0 <= value <= 18446744073709551615
    if is_little_endian:
        return struct.pack('<Q', value)
    else:
        return struct.pack('>Q', value)


def byte_array_to_uint64(byte_array: bytearray,
                         is_little_endian: bool = True) -> int:
    """
    Конвертация bytearray в int64.

    is_little_endian определяет порядок байтов.
    """
    # assert len(byte_array) == 8
    if is_little_endian:
        r = struct.unpack('<Q', byte_array)
    else:
        r = struct.unpack('>Q', byte_array)
    return r[0]


def float_to_byte_array(value: float,
                        is_little_endian: bool = True) -> bytearray:
    """
    Конвертация значения float в bytearray.

    is_little_endian определяет порядок байтов.
    """
    if is_little_endian:
        return struct.pack('<f', value)
    else:
        return struct.pack('>f', value)


def byte_array_to_float(byte_array: bytearray,
                        is_little_endian: bool = True) -> float:
    """
    Конвертация bytearray во float.

    is_little_endian определяет порядок байтов.
    """
    # assert len(byte_array) == 4
    if is_little_endian:
        r = struct.unpack('<f', byte_array)
    else:
        r = struct.unpack('>f', byte_array)
    return r[0]


def double_to_byte_array(value: float,
                         is_little_endian: bool = True) -> bytearray:
    """
    Функция преобразует double в bytearray.

    is_little_endian определяет порядок байтов.
    """
    if is_little_endian:
        return struct.pack('<d', value)
    else:
        return struct.pack('>d', value)


def byte_array_to_double(byte_array: bytearray,
                         is_little_endian: bool = True) -> float:
    """
    Функция преобразует bytearray в double.

    is_little_endian определяет порядок байтов.
    """
    # assert len(byte_array) == 8
    if is_little_endian:
        r = struct.unpack('<d', byte_array)
    else:
        r = struct.unpack('>d', byte_array)
    return r[0]


# Функции конвертации последовательности значений
def bool_list_to_byte_array(bool_list: list) -> bytearray:
    """Функция преобразует список bool в bytearray."""
    ba = bytearray()
    for v in bool_list:
        ba += bool_to_byte_array(v)
    return ba


def byte_array_to_bool_list(byte_array: bytearray) -> list:
    """Функция преобразует bytearray в список bool."""
    bl = []
    for v in byte_array:
        ba = bytearray([v])
        bl.append(byte_array_to_bool(ba))
    return bl


def int8_list_to_byte_array(int8_list: list) -> bytearray:
    """Функция преобразует список int8 в bytearray."""
    ba = bytearray()
    for v in int8_list:
        ba += int8_to_byte_array(v)
    return ba


def byte_array_to_int8_list(byte_array: bytearray) -> list:
    """Функция преобразует bytearray в список int8."""
    il = []
    for v in byte_array:
        ba = bytearray([v])
        il.append(byte_array_to_int8(ba))
    return il


def uint8_list_to_byte_array(uint8_list: list) -> bytearray:
    """Функция преобразует список uint8 в bytearray."""
    return bytearray(uint8_list)


def byte_array_to_uint8_list(byte_array: bytearray) -> list:
    """Функция преобразует bytearray в список uint8."""
    return [v for v in byte_array]


def int16_list_to_byte_array(int16_list: list,
                             is_little_endian: bool = True) -> bytearray:
    """
    Функция преобразует список int16 в byte_array.

    is_little_endian определяет порядок байтов.
    """
    ba = bytearray()
    for v in int16_list:
        ba += int16_to_byte_array(v, is_little_endian)
    return ba


def byte_array_to_int16_list(byte_array: bytearray,
                             is_little_endian: bool = True) -> list:
    """
    Функция преобразует bytearray в список int16.

    is_little_endian определяет порядок байтов.
    """
    type_size = 2
    r = []
    for i in range(0, len(byte_array) - 1, type_size):
        ba = byte_array[i:i + type_size]
        v = byte_array_to_int16(ba, is_little_endian)
        r.append(v)
    return r


def uint16_list_to_byte_array(uint16_list: list,
                              is_little_endian: bool = True) -> bytearray:
    """
    Функция преобразует список uint16 в bytearray.

    is_little_endian определяет порядок байтов.
    """
    ba = bytearray()
    for v in uint16_list:
        ba += uint16_to_byte_array(v, is_little_endian)
    return ba


def byte_array_to_uint16_list(byte_array: bytearray,
                              is_little_endian: bool = True) -> list:
    """
    Функция преобразует bytearray в список uint16.

    is_little_endian определяет порядок байтов.
    """
    type_size = 2
    r = []
    for i in range(0, len(byte_array) - 1, type_size):
        ba = byte_array[i:i + type_size]
        v = byte_array_to_uint16(ba, is_little_endian)
        r.append(v)
    return r


def int32_list_to_byte_array(int32_list: list,
                             is_little_endian: bool = True) -> bytearray:
    """
    Функция преобразует список uint32 в bytearray.

    is_little_endian определяет порядок байтов.
    """
    ba = bytearray()
    for v in int32_list:
        ba += int32_to_byte_array(v, is_little_endian)
    return ba


def byte_array_to_int32_list(byte_array: bytearray,
                             is_little_endian: bool = True) -> list:
    """
    Функция преобразует bytearray в список int32.

    is_little_endian определяет порядок байтов.
    """
    type_size = 4
    r = []
    for i in range(0, len(byte_array) - 1, type_size):
        ba = byte_array[i:i + type_size]
        v = byte_array_to_int32(ba, is_little_endian)
        r.append(v)
    return r


def uint32_list_to_byte_array(int32_list: list,
                              is_little_endian: bool = True) -> bytearray:
    """
    Функция преобразует список uint16 в bytearray.

    is_little_endian определяет порядок байтов.
    """
    ba = bytearray()
    for v in int32_list:
        ba += uint32_to_byte_array(v, is_little_endian)
    return ba


def byte_array_to_uint32_list(byte_array: bytearray,
                              is_little_endian: bool = True) -> list:
    """
    Функция преобразует bytearray в список uint32.

    is_little_endian определяет порядок байтов.
    """
    type_size = 4
    r = []
    for i in range(0, len(byte_array) - 1, type_size):
        ba = byte_array[i:i + type_size]
        v = byte_array_to_uint32(ba, is_little_endian)
        r.append(v)
    return r


def int64_list_to_byte_array(uint64_array: list,
                             is_little_endian: bool = True) -> bytearray:
    """
    Функция преобразует список uint64 в список байтов.

    is_little_endian определяет порядок байтов.
    """
    ba = bytearray()
    for v in uint64_array:
        ba += int64_to_byte_array(v, is_little_endian)
    return ba


def byte_array_to_int64_list(byte_array: bytearray,
                             is_little_endian: bool = True) -> list:
    """
    Функция преобразует список байтов в список uint64.

    Все значения представляются типом int
    """
    type_size = 8
    r = []
    for i in range(0, len(byte_array) - 1, type_size):
        ba = byte_array[i:i + type_size]
        v = byte_array_to_int64(ba, is_little_endian)
        r.append(v)
    return r


def uint64_list_to_byte_array(uint64_array: list,
                              is_little_endian: bool = True) -> bytearray:
    """
    Функция преобразует список uint64 в список байтов.

    is_little_endian определяет порядок байтов.
    """
    ba = bytearray()
    for v in uint64_array:
        ba += uint64_to_byte_array(v, is_little_endian)
    return ba


def byte_array_to_uint64_list(byte_array: bytearray,
                              is_little_endian: bool = True) -> list:
    """
    Функция преобразует список байтов в список uint64.

    Все значения представляются типом int
    """
    type_size = 8
    r = []
    for i in range(0, len(byte_array) - 1, type_size):
        ba = byte_array[i:i + type_size]
        v = byte_array_to_uint64(ba, is_little_endian)
        r.append(v)
    return r


def float_list_to_byte_array(float_list: list,
                             is_little_endian: bool = True) -> bytearray:
    """
    Функция преобразует список uint16 в bytearray.

    is_little_endian определяет порядок байтов.
    """
    ba = bytearray()
    for v in float_list:
        ba += float_to_byte_array(v, is_little_endian)
    return ba


def byte_array_to_float_list(byte_array: [],
                             is_little_endian: bool = True) -> list:
    """
    Функция преобразует список байтов в список float.

    is_little_endian определяет порядок байтов.
    """
    type_size = 4
    r = []
    for i in range(0, len(byte_array) - 1, type_size):
        ba = byte_array[i:i + type_size]
        v = byte_array_to_float(ba, is_little_endian)
        r.append(v)
    return r


def double_list_to_byte_array(double_list: list,
                              is_little_endian: bool = True) -> bytearray:
    """
    Функция преобразует список uint16 в bytearray.

    is_little_endian определяет порядок байтов.
    """
    ba = bytearray()
    for v in double_list:
        ba += double_to_byte_array(v, is_little_endian)
    return ba


def byte_array_to_double_list(byte_array: bytearray,
                              is_little_endian: bool = True) -> list:
    """
    Функция преобразует bytearray в список double.

    is_little_endian определяет порядок байтов.
    """
    type_size = 8
    r = []
    for i in range(0, len(byte_array) - 1, type_size):
        ba = byte_array[i:i + type_size]
        v = byte_array_to_double(ba, is_little_endian)
        r.append(v)
    return r


class TestConvert(unittest.TestCase):
    """Класс для тестирования одиночных пребразований."""

    def test_str_to_byte_array(self):
        """Тест функции str_to_byte_array."""
        s = '123'
        ba = str_to_byte_array(s)
        self.assertEqual(len(ba), 3)

    def test_byte_array_to_str(self):
        """Тест функции byte_array_to_str."""
        ba = bytearray([49, 50, 51])
        s = byte_array_to_str(ba)
        self.assertEqual(s, '123')

    def test_bool_to_byte_array(self):
        """Тест функции bool_to_byte_array."""
        r = bool_to_byte_array(True)
        self.assertEqual(r, bytearray([1]))
        r = bool_to_byte_array(False)
        self.assertEqual(r, bytearray([0]))

    def test_byte_array_to_bool(self):
        """Тест функции byte_array_to_bool."""
        v = bytearray([0])
        r = byte_array_to_bool(v)
        self.assertEqual(r, False)

    def test_int8_to_byte_array(self):
        """Тест функции int8_to_byte_array."""
        r = int8_to_byte_array(2)
        self.assertEqual(r, bytearray([2]))

    def test_byte_array_to_int8(self):
        """Тест функции byte_array_to_int8."""
        ba = bytearray([2])
        r = byte_array_to_int8(ba)
        self.assertEqual(r, 2)

    def test_uint8_to_byte_array(self):
        """Тест функции uint8_to_byte_array."""
        r = uint8_to_byte_array(3)
        self.assertEqual(r, bytearray([3]))

    def test_byte_array_to_uint8(self):
        """Тест функции byte_array_to_uint8."""
        ba = bytearray([2])
        r = byte_array_to_uint8(ba)
        self.assertEqual(r, 2)

    def test_int16_to_byte_array(self):
        """Тест функции int16_to_byte_array."""
        r = int16_to_byte_array(4)
        self.assertEqual(r, bytearray([4, 0]))
        r = int16_to_byte_array(5, False)
        self.assertEqual(r, bytearray([0, 5]))

    def test_byte_array_to_int16(self):
        """Тест функции byte_array_to_int16."""
        ba = bytearray([1, 0])
        r = byte_array_to_int16(ba)
        self.assertEqual(r, 1)
        ba = bytearray([0, 1])
        r = byte_array_to_int16(ba, False)
        self.assertEqual(r, 1)

    def test_uint16_to_byte_array(self):
        """Тест функции uint16_to_byte_array."""
        r = uint16_to_byte_array(1)
        self.assertEqual(r, bytearray([1, 0]))
        r = uint16_to_byte_array(3, False)
        self.assertEqual(r, bytearray([0, 3]))

    def test_byte_array_to_uint16(self):
        """Тест функции byte_array_to_uint16."""
        ba = bytearray([1, 0])
        r = byte_array_to_uint16(ba)
        self.assertEqual(r, 1)
        ba = bytearray([0, 1])
        r = byte_array_to_uint16(ba, False)
        self.assertEqual(r, 1)

    def test_int32_to_byte_array(self):
        """Тест функции int32_to_byte_array."""
        r = int32_to_byte_array(3)
        self.assertEqual(r, bytearray([3, 0, 0, 0]))
        r = int32_to_byte_array(5, False)
        self.assertEqual(r, bytearray([0, 0, 0, 5]))

    def test_byte_array_to_int32(self):
        """Тест функции byte_array_to_int32."""
        ba = bytearray([2, 0, 0, 0])
        r = byte_array_to_int32(ba)
        self.assertEqual(r, 2)
        ba = bytearray([0, 0, 0, 2])
        r = byte_array_to_int32(ba, False)
        self.assertEqual(r, 2)

    def test_int64_to_byte_array(self):
        """Тест функции int64_to_byte_array."""
        r = int64_to_byte_array(200)
        self.assertEqual(r, bytearray([200, 0, 0, 0, 0, 0, 0, 0]))
        r = int64_to_byte_array(99, False)
        self.assertEqual(r, bytearray([0, 0, 0, 0, 0, 0, 0, 99]))

    def test_byte_arrray_to_int64(self):
        """Тест функции byte_arrray_to_int64."""
        ba = bytearray([3, 0, 0, 0, 0, 0, 0, 0])
        r = byte_array_to_int64(ba)
        self.assertEqual(r, 3)

    def test_float_to_byte_array(self):
        """Тест функции float_to_byte_array."""
        r = float_to_byte_array(0.0)
        self.assertEqual(r, bytearray([0, 0, 0, 0]))
        r = float_to_byte_array(0.0, False)
        self.assertEqual(r, bytearray([0, 0, 0, 0]))

    def test_byte_array_to_float(self):
        """Тест функции byte_array_to_float."""
        ba = bytearray([0] * 4)
        r = byte_array_to_float(ba)
        self.assertAlmostEqual(r, 0.0)
        values = bytearray([0] * 4)
        r = byte_array_to_float(values, False)
        self.assertAlmostEqual(r, 0.0)

    def test_double_to_byte_array(self):
        """Тест функции double_to_byte_array."""
        r = double_to_byte_array(0.0)
        self.assertEqual(r, bytearray([0] * 8))
        r = double_to_byte_array(0.0, False)
        self.assertEqual(r, bytearray([0] * 8))

    def test_byte_list_to_double(self):
        """Тест функции byte_list_to_double."""
        ba = bytearray([0] * 8)
        r = byte_array_to_double(ba)
        self.assertAlmostEqual(r, 0.0)
        r = byte_array_to_double(ba, False)
        self.assertAlmostEqual(r, 0.0)


class TestListConvert(unittest.TestCase):
    """Класс для тестирования пребразований списков."""

    def test_bool_list_to_byte_array(self):
        """Тест функции bool_list_to_byte_array."""
        bl = [True, False, True, False, True]
        r = bool_list_to_byte_array(bl)
        self.assertEqual(r, bytearray([1, 0, 1, 0, 1]))

    def test_byte_array_to_bool_list(self):
        """Тест функции byte_array_to_bool_list."""
        b = bytearray([1, 0, 1, 0, 1])
        r = byte_array_to_bool_list(b)
        self.assertEqual(r, [True, False, True, False, True])

    def test_int8_list_to_byte_array(self):
        """Тест функции int8_list_to_byte_array."""
        v = [1, 2, 3, 4]
        r = int8_list_to_byte_array(v)
        self.assertEqual(r, bytearray(v))

    def test_byte_array_to_int8_list(self):
        """Тест функции byte_array_to_int8_list."""
        ba = bytearray([1, 2, 3, 4])
        r = byte_array_to_int8_list(ba)
        self.assertEqual(r, [1, 2, 3, 4])

    def test_uint8_list_to_byte_array(self):
        """Тест функции uint8_list_to_byte_array."""
        v = [1, 2, 3, 4]
        r = uint8_list_to_byte_array(v)
        self.assertEqual(r, bytearray([1, 2, 3, 4]))

    def test_byte_array_to_uint8_list(self):
        """Тест функции byte_array_to_uint8_list."""
        v = bytearray([1, 2, 3, 4])
        r = byte_array_to_uint8_list(v)
        self.assertEqual(r, [1, 2, 3, 4])

    def test_int16_list_to_byte_array(self):
        """Тест функции int16_list_to_byte_array."""
        v = [2, 3]
        r = int16_list_to_byte_array(v)
        self.assertEqual(r, bytearray([2, 0, 3, 0]))
        v = [2, 3]
        r = int16_list_to_byte_array(v, False)
        self.assertEqual(r, bytearray([0, 2, 0, 3]))

    def test_byte_array_to_int16_list(self):
        """Тест функции byte_array_to_int16_list."""
        ba = bytearray([2, 0, 3, 0])
        r = byte_array_to_int16_list(ba)
        self.assertEqual(r, [2, 3])
        ba = bytearray([0, 2, 0, 3])
        r = byte_array_to_int16_list(ba, False)
        self.assertEqual(r, [2, 3])

    def test_uint16_list_to_byte_array(self):
        """Тест функции uint16_list_to_byte_array."""
        v = [2, 3]
        r = uint16_list_to_byte_array(v)
        self.assertEqual(r, bytearray([2, 0, 3, 0]))
        r = uint16_list_to_byte_array(v, False)
        self.assertEqual(r, bytearray([0, 2, 0, 3]))

    def test_byte_array_to_uint16_list(self):
        """Тест функции byte_array_to_uint16_list."""
        v = bytearray([2, 0, 3, 0])
        r = byte_array_to_uint16_list(v)
        self.assertEqual(r, [2, 3])
        v = bytearray([0, 2, 0, 3])
        r = byte_array_to_uint16_list(v, False)
        self.assertEqual(r, [2, 3])

    def test_int32_list_to_byte_array(self):
        """Тест функции int32_list_to_byte_array."""
        v = [2, 3]
        r = int32_list_to_byte_array(v)
        self.assertEqual(r, bytearray([2, 0, 0, 0] + [3, 0, 0, 0]))
        r = int32_list_to_byte_array(v, False)
        self.assertEqual(r, bytearray([0, 0, 0, 2] + [0, 0, 0, 3]))

    def test_byte_array_to_int32_list(self):
        """Тест функции byte_array_to_int32_list."""
        ba = bytearray([2, 0, 0, 0] + [3, 0, 0, 0])
        r = byte_array_to_int32_list(ba)
        self.assertEqual(r, [2, 3])
        ba = bytearray([0, 0, 0, 2] + [0, 0, 0, 3])
        r = byte_array_to_int32_list(ba, False)
        self.assertEqual(r, [2, 3])

    def test_uint32_list_to_byte_array(self):
        """Тест функции uint32_list_to_byte_array."""
        vl = [2, 3]
        ba = uint32_list_to_byte_array(vl)
        self.assertEqual(ba, bytearray([2, 0, 0, 0] + [3, 0, 0, 0]))
        ba = uint32_list_to_byte_array(vl, False)
        self.assertEqual(ba, bytearray([0, 0, 0, 2] + [0, 0, 0, 3]))

    def test_byte_array_uint32_list(self):
        """Тест функции byte_array_uint32_list."""
        ba = bytearray([2, 0, 0, 0] + [3, 0, 0, 0])
        bl = byte_array_to_uint32_list(ba)
        self.assertEqual(bl, [2, 3])
        ba = bytearray([0, 0, 0, 2] + [0, 0, 0, 3])
        bl = byte_array_to_uint32_list(ba, False)
        self.assertEqual(bl, [2, 3])

    def test_int64_list_to_byte_array(self):
        """Тест функции int64_list_to_byte_array."""
        vl = [0]
        ba = int64_list_to_byte_array(vl)
        self.assertEqual(ba, bytearray([0] * 8))

    def test_byte_array_to_int64_list(self):
        """Тест функции byte_array_to_int64_list."""
        ba = bytearray([0] * 16)
        vl = byte_array_to_int64_list(ba)
        self.assertEqual(vl, [0, 0])

    def test_uint64_list_to_byte_array(self):
        """Тест функции uint64_list_to_byte_array."""
        vl = [0, 0]
        ba = uint64_list_to_byte_array(vl)
        self.assertEqual(ba, bytearray([0] * 16))

    def test_byte_array_to_uint64_list(self):
        """Тест функции byte_array_to_uint64_list."""
        ba = bytearray([0] * 8)
        vl = byte_array_to_uint64_list(ba)
        self.assertEqual(vl, [0])

    def test_float_list_to_byte_array(self):
        """Тест функции float_list_to_byte_array."""
        vl = [0.0, 0.0]
        ba = float_list_to_byte_array(vl)
        self.assertEqual(ba, bytearray([0] * 8))

    def test_byte_array_to_float_list(self):
        """Тест функции byte_array_to_float_list."""
        ba = bytearray([0] * 4)
        vl = byte_array_to_float_list(ba)
        self.assertEqual(vl, [0.0])

    def test_double_list_to_byte_array(self):
        """Тест функции double_list_to_byte_array."""
        vl = [0.0, 0.0]
        ba = double_list_to_byte_array(vl)
        self.assertEqual(ba, bytearray([0] * 16))

    def test_byte_array_to_double_list(self):
        """Тест функции byte_array_to_double_list."""
        ba = bytearray([0] * 16)
        vl = byte_array_to_double_list(ba)
        self.assertAlmostEqual(vl[0], 0.0)
        self.assertAlmostEqual(vl[1], 0.0)


# Вызывается при загрузке модуля главным
if __name__ == '__main__':
    unittest.main()
