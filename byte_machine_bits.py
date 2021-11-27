"""
ByteMachine.

Работа с битами.
"""
__author__ = "EnergyLabs"
__version__ = "0.9129"


import unittest


# Функции для работы с битами.

def value_to_bit(value: int) -> int:
    """Функция приводит значение к биту, 0 или 1."""
    assert isinstance(value, int)
    return 1 if value != 0 else 0


def is_correct_bit(value: int) -> bool:
    """Функция проверяет корректность значения бита."""
    assert isinstance(value, int)
    return value in (0, 1)


def get_lo_nibble(value: int) -> int:
    """Получение младщей тетрады байта."""
    assert isinstance(value, int)
    assert 0 <= value <= 255
    return value & 0x0F


def get_hi_nibble(value: int) -> int:
    """Получение старшей тетрады байта."""
    # assert isinstance(value, int)
    assert 0 <= value <= 255
    return value >> 4


def byte_to_bits(value: int) -> bytearray:
    """Конвертация байта в биты."""
    assert 0 <= value <= 255
    ba = bytearray()
    for i in range(8):
        v = value & (1 << i)
        ba.append(value_to_bit(v))
    return ba


def test_bit(value: int, bit_index: int) -> bool:
    """Проверка по индексу выставленного бита."""
    # assert isinstance(value, int)
    assert 0 <= value <= 255
    # assert isinstance(bit_index, int)
    assert 0 <= bit_index <= 7
    return value & (1 << bit_index) != 0


def set_bit(value: int, bit_index: int) -> int:
    """Установка бита по индексу."""
    # assert isinstance(value, int)
    assert 0 <= value <= 255
    # assert isinstance(bit_index, int)
    assert 0 <= bit_index <= 7
    return value | (1 << bit_index)


def reset_bit(value: int, bit_index: int) -> int:
    """Сброс бита по индексу."""
    # assert isinstance(value, int)
    assert 0 <= value <= 255
    # assert isinstance(bit_index, int)
    assert 0 <= bit_index <= 7
    m = ~(1 << bit_index)
    return value & m


def flip_bit(value: int, bit_index: int) -> int:
    """Инверсия бита."""
    # assert isinstance(value, int)
    assert 0 <= value <= 255
    # assert isinstance(bit_index, int)
    assert 0 <= bit_index <= 7
    if test_bit(value, bit_index):
        return reset_bit(value, bit_index)
    else:
        return set_bit(value, bit_index)


def is_all_bits(value: int) -> bool:
    """Получение признака, что все биты в байте выставлены."""
    assert isinstance(value, int)
    assert 0 <= value <= 255
    return value == 255


def is_any_bits(value: int) -> bool:
    """Получение признака, что хоть один бит в байте выставлен."""
    assert isinstance(value, int)
    assert 0 <= value <= 255
    return value != 0


def is_none_bits(value: int) -> bool:
    """Получение признака, что все биты сброшены."""
    assert isinstance(value, int)
    assert 0 <= value <= 255
    return value == 0


def get_bit_count(value: int) -> int:
    """Получение количества установленных битов в байте."""
    assert isinstance(value, int)
    assert 0 <= value <= 255
    count = 0
    for i in range(8):
        if test_bit(value, i):
            count += 1
    return count


def byte_array_to_bit_array(byte_array: bytearray) -> bytearray:
    """Конвертация списка байтов в список битов."""
    assert isinstance(byte_array, bytearray)
    ba = bytearray()
    for b in byte_array:
        ba += byte_to_bits(b)
    return ba


class TestBits(unittest.TestCase):
    """Тест для функций работы с битами."""

    def test_value_to_bit(self):
        """Тест функции value_to_bit."""
        self.assertEqual(value_to_bit(0), 0)
        self.assertEqual(value_to_bit(1), 1)
        self.assertEqual(value_to_bit(2), 1)

    def test_is_correct_bit(self):
        """Тест функции is_correct_bit."""
        self.assertTrue(is_correct_bit(0))
        self.assertTrue(is_correct_bit(1))
        self.assertFalse(is_correct_bit(2))

    def test_get_lo_nibble(self):
        """Тест функции get_lo_nibble."""
        self.assertEqual(get_lo_nibble(1), 1)
        self.assertEqual(get_lo_nibble(0x0F), 0x0F)

    def test_get_hi_nibble(self):
        """Тест функции get_hi_nibble."""
        self.assertEqual(get_hi_nibble(1), 0)
        self.assertEqual(get_hi_nibble(1 << 4), 1)

    def test_test_bit(self):
        """Тест функции test_bit."""
        self.assertTrue(test_bit(1, 0))
        self.assertFalse(test_bit(1, 1))

    def test_byte_to_bits(self):
        """Тест функции byte_to_bits."""
        r = byte_to_bits(1)
        self.assertEqual(r, bytearray([1] + [0] * 7))

    def test_set_bit(self):
        """Тест функции set_bit."""
        self.assertEqual(set_bit(0, 0), 1)

    def test_reset_bit(self):
        """Тест функции reset_bit."""
        self.assertEqual(reset_bit(1, 0), 0)

    def test_flip_bit(self):
        """Тест функции flip_bit."""
        self.assertEqual(flip_bit(1, 0), 0)
        self.assertEqual(flip_bit(0, 0), 1)

    def test_is_all_bits(self):
        """Тест функции is_all_bits."""
        self.assertTrue(is_all_bits(255))
        self.assertFalse(is_all_bits(254))

    def test_is_any_bits(self):
        """Тест функции is_any_bits."""
        self.assertTrue(is_any_bits(1))
        self.assertFalse(is_any_bits(0))

    def test_is_none_bits(self):
        """Тест функции is_none_bits."""
        self.assertTrue(is_none_bits(0))
        self.assertFalse(is_none_bits(1))

    def test_count_bits(self):
        """Тест функции count_bits."""
        count = get_bit_count(1)
        self.assertEqual(count, 1)

        count = get_bit_count(2)
        self.assertEqual(count, 1)

        count = get_bit_count(3)
        self.assertEqual(count, 2)

    def test_byte_array_to_bit_array(self):
        """Тест функции byte_array_to_bit_array."""
        ba = bytearray([0] * 2)
        r = byte_array_to_bit_array(ba)
        self.assertEqual(r, bytearray([0] * 16))


# Вызывается при загрузке модуля главным.
if __name__ == "__main__":
    unittest.main()
