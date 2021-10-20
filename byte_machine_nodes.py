"""
ByteMachine.

Функции с функциональностью некоторых узлов-нодов.
"""
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


def skip(byte_array: bytearray, count: int,
         is_begin: bool = True) -> bytearray:
    """Пропуск определенного количества значений списка."""
    assert len(byte_array) >= count
    if is_begin:
        return byte_array[count:]
    else:
        return byte_array[:-count]


def reverse(byte_array: bytearray) -> bytearray:
    """Реверс списка."""
    return byte_array[::-1]


def size(byte_array: bytearray) -> int:
    """Получение размера списка."""
    return len(byte_array)


def merge(byte_array1: bytearray, byte_array2: bytearray) -> bytearray:
    """Объединение списков."""
    return byte_array1 + byte_array2


def dump(values: bytearray, byte_width: int = 16) -> None:
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
        ba = bytearray(range(10))
        r = take(ba, 3)
        self.assertEqual(r, bytearray([0, 1, 2]))
        r = take(ba, 3, False)
        self.assertEqual(r, bytearray([7, 8, 9]))

    def test_skip(self):
        """Тест функции skip."""
        ba = bytearray(range(10))
        r = skip(ba, 7)
        self.assertEqual(r, bytearray([7, 8, 9]))
        r = skip(ba, 7, False)
        self.assertEqual(r, bytearray([0, 1, 2]))

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

    def test_merge(self):
        """Тест функции merge."""
        ba1 = bytearray([0, 1])
        ba2 = bytearray([2, 3])
        r = ba1 + ba2
        self.assertEqual(merge(ba1, ba2), r)

    def test_dump(self):
        """Тест функции dump."""
        pass  # не тестируется ввиду вывода на консоль.

    def test_byte_to_hex_str(self):
        """Тест функции byte_to_hex_str."""
        hs = byte_to_hex_str(1)
        self.assertEqual(hs, '01')
        hs = byte_to_hex_str(255)
        self.assertEqual(hs, 'FF')


# Вызывается при загрузке модуля главным.
if __name__ == "__main__":
    unittest.main()
