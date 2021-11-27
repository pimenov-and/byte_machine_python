"""
ByteMachine.

Функции с функциональностью некоторых узлов-нодов.
"""
__author__ = "EnergyLabs"
__version__ = "0.9129"


import random
import unittest


# Функции повторяют функциональность некоторых узлов-нодов.

def generate(count: int, filled_byte: int = 0) -> bytearray:
    """Генерация списка размера count и заполненного определенным значением."""
    # assert isinstance(count, int)
    assert count >= 0
    assert isinstance(filled_byte, int)
    assert 0 <= filled_byte <= 255
    return bytearray([filled_byte] * count)


def rand_generate(count: int) -> bytearray:
    """Генерация байтового массива со случайными значениями."""
    # assert isinstance(count, int)
    assert count >= 0
    return bytearray([random.randint(0, 255) for i in range(count)])


def take(byte_array: bytearray, count: int,
         is_begin: bool = True) -> bytearray:
    """Получение определенного количества значений списка."""
    assert len(byte_array) >= count
    if is_begin:
        return byte_array[:count]
    else:
        return byte_array[-count:]


def take_while(byte_array: bytearray, value: int,
               is_begin: bool = True) -> bytearray:
    """Получение значений списка, совпадающих с value."""
    assert isinstance(value, int)
    assert 0 <= value <= 255
    ba = byte_array if is_begin else reverse(byte_array)
    r = bytearray()
    for b in ba:
        if b == value:
            r.append(b)
        else:
            break
    return r


def take_while_2(byte_array: bytearray, pred,
                 is_begin: bool = True) -> bytearray:
    """Получение значений списка с предикатом func для проверки значений."""
    ba = byte_array if is_begin else reverse(byte_array)
    take_count = 0
    for b in ba:
        if pred(b):
            take_count += 1
        else:
            break
    return take(byte_array, take_count, is_begin)


def skip(byte_array: bytearray, count: int,
         is_begin: bool = True) -> bytearray:
    """Пропуск определенного количества значений списка."""
    assert len(byte_array) >= count
    if is_begin:
        return byte_array[count:]
    else:
        return byte_array[:-count]


def skip_while(byte_array: bytearray, value: int,
               is_begin: bool = True) -> bytearray:
    """Пропуск значений, равных value."""
    assert isinstance(value, int)
    assert 0 <= value <= 255
    skip_count = 0
    ba = byte_array if is_begin else reverse(byte_array)
    for b in ba:
        if b == value:
            skip_count += 1
    return skip(byte_array, skip_count, is_begin)


def skip_while_2(byte_array: bytearray, pred,
                 is_begin: bool = True) -> bytearray:
    """Пропуск значений с предикатом func для проверки значений."""
    skip_count = 0
    ba = byte_array if is_begin else reverse(byte_array)
    for b in ba:
        if pred(b):
            skip_count += 1
    return skip(byte_array, skip_count, is_begin)


def change(byte_array: bytearray, func) -> bytearray:
    """Функция изменение массива байтов через функцию."""
    s = size(byte_array)
    ba = bytearray()
    for i in range(s):
        v = byte_array[i]
        ba.append(func(i, v, s))
    return ba


def filter_2(byte_array: bytearray, func) -> bytearray:
    """Функция фильтрации (filter - стандартная функция, поэтому здесь номер 2)."""
    s = size(byte_array)
    ba = bytearray()
    for i in range(s):
        v = byte_array[i]
        if func(i, v, s):
            ba.append(v)
    return ba


def reverse(byte_array: bytearray) -> bytearray:
    """Реверс списка."""
    return byte_array[::-1]


def size(byte_array: bytearray) -> int:
    """Получение размера списка."""
    return len(byte_array)


def count(byte_array: bytearray, value: int) -> int:
    """Получение количество значений, равных value."""
    return byte_array.count(value)


def count_2(byte_array: bytearray, pred) -> int:
    """Получение количества значений, проходящих через функцию pred."""
    count = 0
    for v in byte_array:
        if pred(v):
            count += 1
    return count


def merge(byte_array_1: bytearray, byte_array_2: bytearray) -> bytearray:
    """Объединение списков."""
    return byte_array_1 + byte_array_2


def print_dump(values: bytearray, byte_width: int = 16) -> None:
    """Вывод дампа значений."""
    assert isinstance(byte_width, int)
    assert byte_width in (8, 16)
    address = 0
    line_count = len(values) // byte_width
    tail_size = len(values) % byte_width
    is_tail = tail_size > 0
    for ln in range(line_count):
        index = ln * byte_width
        byte_line = values[index:index + byte_width]
        line = _bytes_to_hex_str(byte_line)
        address = _address32_to_hex_str(index)
        print(address + ' | ' + line)
    if is_tail:
        index = line_count * byte_width
        byte_line = values[index:index + tail_size]
        line = _bytes_to_hex_str(byte_line)
        address = _address32_to_hex_str(index)
        print(address + ' | ' + line)


def byte_to_hex_str(value: int) -> str:
    """Конвертация числа в строку с шестнадцатиричным представлением."""
    # assert isinstance(value, int)
    assert 0 <= value <= 255
    hex_str = hex(value)
    return hex_str[2:].upper().zfill(2)


def _address32_to_hex_str(address: int) -> str:
    """Конвертация 32-разрядного адреса в строку с шестнадцатиричным представлением."""
    # assert isinstance(address, int)
    assert 0 <= address <= 2147483647
    hex_str = hex(address)
    return hex_str[2:].upper().zfill(8)


def _bytes_to_hex_str(byte_array: bytearray) -> str:
    """Перевод байтов в строку с шестнадцатиричным представлением с разделителем ' '."""
    parts = [byte_to_hex_str(b) for b in byte_array]
    return ' '.join(parts)


class TestNodes(unittest.TestCase):
    """Класс для тестирования."""

    def test_generate(self):
        """Тест функции genarate."""
        ba = generate(3)
        self.assertEqual(ba, bytearray([0, 0, 0]))
        ba = generate(3, 1)
        self.assertEqual(ba, bytearray([1, 1, 1]))

    def test_rand_generate(self):
        """Тест функции rand_generate."""
        ba = rand_generate(100)
        self.assertEqual(len(ba), 100)

    def test_take(self):
        """Тест функции take."""
        ba = bytearray(range(10))
        r = take(ba, 3)
        self.assertEqual(r, bytearray([0, 1, 2]))
        r = take(ba, 3, False)
        self.assertEqual(r, bytearray([7, 8, 9]))

    def test_take_while(self):
        """Тест функции take_while."""
        ba = bytearray([0, 1, 2, 3, 4, 5])
        r = take_while(ba, 0)
        self.assertEqual(r, bytearray([0]))

    def test_take_while_2(self):
        """Тест функции take_while_2."""
        ba = bytearray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        r = take_while_2(ba, lambda v: v < 3)
        self.assertEqual(r, bytearray([0, 1, 2]))

    def test_skip(self):
        """Тест функции skip."""
        ba = bytearray(range(10))
        r = skip(ba, 7)
        self.assertEqual(r, bytearray([7, 8, 9]))
        r = skip(ba, 7, False)
        self.assertEqual(r, bytearray([0, 1, 2]))

    def test_skip_while(self):
        """Тест функции skip_while."""
        ba = bytearray([0, 1, 1, 1, 1, 1])
        r = skip_while(ba, 0)
        self.assertEqual(r, bytearray([1] * 5))
        r = skip_while(ba, 1, False)
        self.assertEqual(r, bytearray([0]))

    def test_skip_while_2(self):
        """Тест функции skip_while_2."""
        ba = bytearray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        r = skip_while_2(ba, lambda v: v < 5)
        self.assertEqual(r, bytearray([5, 6, 7, 8, 9]))

    def test_change(self):
        """Тест функции change."""
        ba = bytearray([0, 2, 4])
        r = change(ba, lambda i, v, s: v // 2)
        self.assertEqual(r, bytearray([0, 1, 2]))

    def test_filter_2(self):
        """Тест функции change_2."""
        ba = bytearray([0, 3, 4])
        r = filter_2(ba, lambda i, v, s: v % 2 == 0)
        self.assertEqual(r, bytearray([0, 4]))

    def test_reverse(self):
        """Тесть функции reverse."""
        ba = bytearray([1, 2, 3])
        r = bytearray([3, 2, 1])
        self.assertEqual(reverse(ba), r)

    def test_size(self):
        """Тест функции size."""
        ba = bytearray([0, 0, 0])
        self.assertEqual(size(ba), 3)
        ba = bytearray()
        self.assertEqual(size(ba), 0)

    def test_count(self):
        """Тест функции count."""
        ba = bytearray([0, 1, 2, 3, 4, 0])
        c = count(ba, 0)
        self.assertEqual(c, 2)

    def test_count_2(self):
        """Тест функции count_2."""
        ba = bytearray([0, 1, 2, 3, 4, 0])
        c = count_2(ba, lambda v: v == 0)
        self.assertEqual(c, 2)

    def test_merge(self):
        """Тест функции merge."""
        ba_1 = bytearray([0, 1])
        ba_2 = bytearray([2, 3])
        r = ba_1 + ba_2
        self.assertEqual(merge(ba_1, ba_2), r)

    def test_byte_to_hex_str(self):
        """Тест функции byte_to_hex_str."""
        hs = byte_to_hex_str(1)
        self.assertEqual(hs, '01')
        hs = byte_to_hex_str(255)
        self.assertEqual(hs, 'FF')


# Вызывается при загрузке модуля главным.
if __name__ == "__main__":
    unittest.main()
