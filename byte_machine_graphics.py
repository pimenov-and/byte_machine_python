"""
ByteMachine.

Классы для графического вывода.
"""
from __future__ import annotations


__author__ = "EnergyLabs"
__version__ = "0.9129"


import math
import unittest
import byte_machine_helper as bmh
import byte_machine_convert as bmc


class Color:
    """Цвет."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.__r = 0
        self.__g = 0
        self.__b = 0
        self.__a = 255

    def init(self, r: int, g: int, b: int, a: int = 255) -> None:
        """Функция инициализации."""
        assert isinstance(r, int)
        assert 0 <= r <= 255
        assert isinstance(g, int)
        assert 0 <= g <= 255
        assert isinstance(b, int)
        assert 0 <= b <= 255
        assert isinstance(a, int)
        assert 0 <= a <= 255
        self.__r = r
        self.__g = g
        self.__b = b
        self.__a = a

    @staticmethod
    def create(r: int, g: int, b: int, a: int = 255) -> Color:
        """Функция создания с параметрами."""
        assert isinstance(r, int)
        assert 0 <= r <= 255
        assert isinstance(g, int)
        assert 0 <= g <= 255
        assert isinstance(b, int)
        assert 0 <= b <= 255
        assert isinstance(a, int)
        assert 0 <= a <= 255
        c = Color()
        c.init(r, g, b, a)
        return c

    def get_r(self) -> int:
        """Получение составляющей цвета red."""
        return self.__r

    def set_r(self, r: int) -> None:
        """Задание составляющей цвета red."""
        assert isinstance(r, int)
        assert 0 <= r <= 255
        self.__r = r

    def get_g(self) -> int:
        """Получение составляющей цвета green."""
        return self.__g

    def set_g(self, g: int) -> None:
        """Задание составляющей цвета green."""
        assert isinstance(g, int)
        assert 0 <= g <= 255
        self.__g = g

    def get_b(self) -> int:
        """Получение составляющей цвета blue."""
        return self.__b

    def set_b(self, b: int) -> None:
        """Задание составляющей цвета blue."""
        assert isinstance(b, int)
        assert 0 <= b <= 255
        self.__b = b

    def get_a(self) -> int:
        """Получение прозрачности цвета."""
        return self.__a

    def set_a(self, a: int) -> None:
        """Задание прозрачности цвета."""
        assert isinstance(a, int)
        assert 0 <= a <= 255
        self.__a = a

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 4:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        return bytearray([self.__r, self.__g, self.__b, self.__a])

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
        is_eq_r = self.get_r() == other.get_r()
        is_eq_g = self.get_g() == other.get_g()
        is_eq_b = self.get_b() == other.get_b()
        is_eq_a = self.get_a() == other.get_a()
        return is_eq_r and is_eq_g and is_eq_b and is_eq_a

    def __ne__(self, other: Color) -> bool:
        """Функция проверки на неравенство."""
        assert isinstance(other, Color)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.__r}, {self.__g}, {self.__b}, {self.__a}"

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
        """Получение цвета IndianRed."""
        return Color.create(205, 92, 92)

    @staticmethod
    def get_light_coral() -> Color:
        """Получение цвета LightCoral."""
        return Color.create(240, 128, 128)

    @staticmethod
    def get_dark_salmon() -> Color:
        """Получение цвета DarkSalmon."""
        return Color.create(233, 150, 122)

    @staticmethod
    def get_light_salmon() -> Color:
        """Получение цвета LightSalmon."""
        return Color.create(255, 160, 122)

    @staticmethod
    def get_crimson() -> Color:
        """Получение цвета Crimson."""
        return Color.create(220, 20, 60)

    @staticmethod
    def get_fire_brick() -> Color:
        """Получение цвета FireBrick."""
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
        """Получение цвета ТёмныйХаки."""
        return Color.create(189, 183, 107)

    # Фиолетовые тона
    @staticmethod
    def get_lavender() -> Color:
        """Получение цвета Lavender."""
        return Color.create(230, 230, 250)

    @staticmethod
    def get_thistle() -> Color:
        """Получение цвета Thistle."""
        return Color.create(216, 191, 216)

    @staticmethod
    def get_plum() -> Color:
        """Получение цвета Plum."""
        return Color.create(221, 160, 221)

    @staticmethod
    def get_violet() -> Color:
        """Получение цвета Violet."""
        return Color.create(238, 130, 238)

    @staticmethod
    def get_orchid() -> Color:
        """Получение цвета Orchid."""
        return Color.create(218, 112, 214)

    @staticmethod
    def get_fuchsia() -> Color:
        """Получение цвета Fuchsia."""
        return Color.create(255, 0, 255)

    @staticmethod
    def get_magenta() -> Color:
        """Получение цвета Magenta."""
        return Color.create(255, 0, 255)

    @staticmethod
    def get_medium_orchid() -> Color:
        """Получение цвета MediumOrchid."""
        return Color.create(186, 85, 211)

    @staticmethod
    def get_medium_purple() -> Color:
        """Получение цвета MediumPurple."""
        return Color.create(147, 112, 219)

    @staticmethod
    def get_blue_violet() -> Color:
        """Получение цвета BlueViolet."""
        return Color.create(138, 43, 226)

    @staticmethod
    def get_dark_violet() -> Color:
        """Получение цвета DarkViolet."""
        return Color.create(148, 0, 211)

    @staticmethod
    def get_dark_orchid() -> Color:
        """Получение цвета DarkOrchid."""
        return Color.create(153, 50, 204)

    @staticmethod
    def get_dark_magenta() -> Color:
        """Получение цвета DarkMagenta."""
        return Color.create(139, 0, 139)

    @staticmethod
    def get_purple() -> Color:
        """Получение пурпурного цвета."""
        return Color.create(128, 0, 128)

    @staticmethod
    def get_indigo() -> Color:
        """Получение цвета индиго."""
        return Color.create(75, 0, 130)

    @staticmethod
    def get_slate_blue() -> Color:
        """Получение цвета SlateBlue."""
        return Color.create(106, 90, 205)

    @staticmethod
    def get_dark_slate_blue() -> Color:
        """Получение цвета DarkSlateBlue."""
        return Color.create(72, 61, 139)

    # Коричневые тона.
    @staticmethod
    def get_cornsilk() -> Color:
        """Получение цвета DarkSlateBlue."""
        return Color.create(255, 248, 220)

    @staticmethod
    def get_blanched_almond() -> Color:
        """Получение цвета BlanchedAlmond."""
        return Color.create(255, 235, 205)

    @staticmethod
    def get_bisque() -> Color:
        """Получение цвета Bisque."""
        return Color.create(255, 228, 196)

    @staticmethod
    def get_navajo_white() -> Color:
        """Получение цвета NavajoWhite."""
        return Color.create(255, 222, 173)

    @staticmethod
    def get_wheat() -> Color:
        """Получение цвета Wheat."""
        return Color.create(245, 222, 179)

    @staticmethod
    def get_burly_wood() -> Color:
        """Получение цвета BurlyWood."""
        return Color.create(222, 184, 135)

    @staticmethod
    def get_tan() -> Color:
        """Получение цвета Tan."""
        return Color.create(210, 180, 140)

    @staticmethod
    def get_rosy_brown() -> Color:
        """Получение цвета RosyBrown."""
        return Color.create(188, 143, 143)

    @staticmethod
    def get_sandy_brown() -> Color:
        """Получение цвета SandyBrown."""
        return Color.create(244, 164, 96)

    @staticmethod
    def get_goldenrod() -> Color:
        """Получение цвета Goldenrod."""
        return Color.create(218, 165, 32)

    @staticmethod
    def get_dark_golden_rod() -> Color:
        """Получение цвета DarkGoldenRod."""
        return Color.create(184, 134, 11)

    @staticmethod
    def get_peru() -> Color:
        """Получение цвета Peru."""
        return Color.create(205, 133, 63)

    @staticmethod
    def get_chocolate() -> Color:
        """Получение шоколадного цвета."""
        return Color.create(210, 105, 30)

    @staticmethod
    def get_saddle_brown() -> Color:
        """Получение цвета SaddleBrown."""
        return Color.create(139, 69, 19)

    @staticmethod
    def get_sienna() -> Color:
        """Получение цвета Sienna."""
        return Color.create(160, 82, 45)

    @staticmethod
    def get_brown() -> Color:
        """Получение коричневого цвета."""
        return Color.create(165, 42, 42)

    @staticmethod
    def get_maroon() -> Color:
        """Получение цвета Maroon."""
        return Color.create(128, 0, 0)

    # Зелёные тона
    @staticmethod
    def get_green_yellow() -> Color:
        """Получение цвета GreenYellow."""
        return Color.create(173, 255, 47)

    @staticmethod
    def get_chartreuse() -> Color:
        """Получение цвета Chartreuse."""
        return Color.create(127, 255, 0)

    @staticmethod
    def get_lawn_green() -> Color:
        """Получение цвета LawnGreen."""
        return Color.create(124, 252, 0)

    @staticmethod
    def get_lime() -> Color:
        """Получение цвета Lime."""
        return Color.create(0, 255, 0)

    @staticmethod
    def get_lime_green() -> Color:
        """Получение цвета LimeGreen."""
        return Color.create(50, 205, 50)

    @staticmethod
    def get_pale_green() -> Color:
        """Получение цвета PaleGreen."""
        return Color.create(152, 251, 152)

    @staticmethod
    def get_light_green() -> Color:
        """Получение цвета LightGreen."""
        return Color.create(144, 238, 144)

    @staticmethod
    def get_medium_spring_green() -> Color:
        """Получение цвета MediumSpringGreen."""
        return Color.create(0, 250, 154)

    @staticmethod
    def get_spring_green() -> Color:
        """Получение цвета SpringGreen."""
        return Color.create(0, 255, 127)

    @staticmethod
    def get_medium_sea_green() -> Color:
        """Получение цвета MediumSeaGreen."""
        return Color.create(60, 179, 113)

    @staticmethod
    def get_sea_green() -> Color:
        """Получение цвета SeaGreen."""
        return Color.create(46, 139, 87)

    @staticmethod
    def get_forest_green() -> Color:
        """Получение цвета ForestGreen."""
        return Color.create(34, 139, 34)

    @staticmethod
    def get_dark_green() -> Color:
        """Получение цвета DarkGreen."""
        return Color.create(0, 100, 0)

    @staticmethod
    def get_yellow_green() -> Color:
        """Получение цвета YellowGreen."""
        return Color.create(154, 205, 50)

    @staticmethod
    def get_olive_drab() -> Color:
        """Получение цвета OliveDrab."""
        return Color.create(107, 142, 35)

    @staticmethod
    def get_olive() -> Color:
        """Получение цвета Olive."""
        return Color.create(128, 128, 0)

    @staticmethod
    def get_dark_olive_green() -> Color:
        """Получение цвета DarkOliveGreen."""
        return Color.create(85, 107, 47)

    @staticmethod
    def get_medium_aquamarine() -> Color:
        """Получение цвета MediumAquamarine."""
        return Color.create(102, 205, 170)

    @staticmethod
    def get_dark_sea_green() -> Color:
        """Получение цвета DarkSeaGreen."""
        return Color.create(143, 188, 143)

    @staticmethod
    def get_light_sea_green() -> Color:
        """Получение цвета LightSeaGreen."""
        return Color.create(32, 178, 170)

    @staticmethod
    def get_dark_cyan() -> Color:
        """Получение цвета DarkCyan."""
        return Color.create(0, 139, 139)

    @staticmethod
    def get_teal() -> Color:
        """Получение цвета Teal."""
        return Color.create(0, 128, 128)

    # Синие тона
    @staticmethod
    def get_aqua() -> Color:
        """Получение цвета Aqua."""
        return Color.create(0, 255, 255)

    @staticmethod
    def get_color() -> Color:
        """Получение цвета Cyan."""
        return Color.create(0, 255, 255)

    @staticmethod
    def get_light_cyan() -> Color:
        """Получение цвета LightCyan."""
        return Color.create(224, 255, 255)

    @staticmethod
    def get_pale_turquoise() -> Color:
        """Получение цвета."""
        return Color.create(175, 238, 238)

    @staticmethod
    def get_aquamarine() -> Color:
        """Получение цвета Aquamarine."""
        return Color.create(127, 255, 212)

    @staticmethod
    def get_turquoise() -> Color:
        """Получение цвета Turquoise."""
        return Color.create(64, 224, 208)

    @staticmethod
    def get_medium_turquoise() -> Color:
        """Получение цвета MediumTurquoise."""
        return Color.create(72, 209, 204)

    @staticmethod
    def get_dark_turquoise() -> Color:
        """Получение цвета DarkTurquoise."""
        return Color.create(0, 206, 209)

    @staticmethod
    def get_cadet_blue() -> Color:
        """Получение цвета."""
        return Color.create(95, 158, 160)

    @staticmethod
    def get_steel_blue() -> Color:
        """Получение цвета CadetBlue."""
        return Color.create(70, 130, 180)

    @staticmethod
    def get_light_steel_blue() -> Color:
        """Получение цвета LightSteelBlue."""
        return Color.create(176, 196, 222)

    @staticmethod
    def get_powder_blue() -> Color:
        """Получение цвета PowderBlue."""
        return Color.create(176, 224, 230)

    @staticmethod
    def get_light_blue() -> Color:
        """Получение цвета LightBlue."""
        return Color.create(173, 216, 230)

    @staticmethod
    def get_sky_blue() -> Color:
        """Получение цвета SkyBlue."""
        return Color.create(135, 206, 235)

    @staticmethod
    def get_light_sky_blue() -> Color:
        """Получение цвета LightSkyBlue."""
        return Color.create(135, 206, 250)

    @staticmethod
    def get_deep_sky_blue() -> Color:
        """Получение цвета DeepSkyBlue."""
        return Color.create(0, 191, 255)

    @staticmethod
    def get_dodger_blue() -> Color:
        """Получение цвета DodgerBlue."""
        return Color.create(30, 144, 255)

    @staticmethod
    def get_cornflower_blue() -> Color:
        """Получение цвета."""
        return Color.create(100, 149, 237)

    @staticmethod
    def get_medium_slate_blue() -> Color:
        """Получение цвета MediumSlateBlue."""
        return Color.create(123, 104, 238)

    @staticmethod
    def get_royal_blue() -> Color:
        """Получение цвета RoyalBlue."""
        return Color.create(65, 105, 225)

    @staticmethod
    def get_medium_blue() -> Color:
        """Получение цвета MediumBlue."""
        return Color.create(0, 0, 205)

    @staticmethod
    def get_dark_blue() -> Color:
        """Получение цвета DarkBlue."""
        return Color.create(0, 0, 139)

    @staticmethod
    def get_navy() -> Color:
        """Получение цвета Navy."""
        return Color.create(0, 0, 128)

    @staticmethod
    def get_midnight_blue() -> Color:
        """Получение цвета MidnightBlue."""
        return Color.create(25, 25, 112)

    # Белые тона
    @staticmethod
    def get_snow() -> Color:
        """Получение цвета Snow."""
        return Color.create(255, 250, 250)

    @staticmethod
    def get_honeydew() -> Color:
        """Получение цвета Honeydew."""
        return Color.create(240, 255, 240)

    @staticmethod
    def get_mint_cream() -> Color:
        """Получение цвета MintCream."""
        return Color.create(245, 255, 250)

    @staticmethod
    def get_alice_blue() -> Color:
        """Получение цвета AliceBlue."""
        return Color.create(240, 248, 255)

    @staticmethod
    def get_ghost_white() -> Color:
        """Получение цвета GhostWhite."""
        return Color.create(248, 248, 255)

    @staticmethod
    def get_white_smoke() -> Color:
        """Получение цвета WhiteSmoke."""
        return Color.create(245, 245, 245)

    @staticmethod
    def get_seashell() -> Color:
        """Получение цвета Seashell."""
        return Color.create(255, 245, 238)

    @staticmethod
    def get_beige() -> Color:
        """Получение цвета Beige."""
        return Color.create(245, 245, 220)

    @staticmethod
    def get_old_lace() -> Color:
        """Получение цвета OldLace."""
        return Color.create(253, 245, 230)

    @staticmethod
    def get_floral_white() -> Color:
        """Получение цвета FloralWhite."""
        return Color.create(255, 250, 240)

    @staticmethod
    def get_ivory() -> Color:
        """Получение цвета Ivory."""
        return Color.create(255, 255, 240)

    @staticmethod
    def get_antique_white() -> Color:
        """Получение цвета AntiqueWhite."""
        return Color.create(250, 235, 215)

    @staticmethod
    def get_linen() -> Color:
        """Получение цвета Linen."""
        return Color.create(250, 240, 230)

    @staticmethod
    def get_lavender_blush() -> Color:
        """Получение цвета LavenderBlush."""
        return Color.create(255, 240, 245)

    @staticmethod
    def get_misty_rose() -> Color:
        """Получение цвета MistyRose."""
        return Color.create(255, 228, 225)

    # Серые тона
    @staticmethod
    def get_gainsboro() -> Color:
        """Получение цвета Gainsboro."""
        return Color.create(220, 220, 220)

    @staticmethod
    def get_light_grey() -> Color:
        """Получение цвета LightGrey."""
        return Color.create(211, 211, 211)

    @staticmethod
    def get_light_gray() -> Color:
        """Получение цвета LightGray."""
        return Color.create(211, 211, 211)

    @staticmethod
    def get_silver() -> Color:
        """Получение цвета Silver."""
        return Color.create(192, 192, 192)

    @staticmethod
    def get_dim_gray() -> Color:
        """Получение цвета DimGray."""
        return Color.create(105, 105, 105)

    @staticmethod
    def get_dim_grey() -> Color:
        """Получение цвета DimGrey."""
        return Color.create(105, 105, 105)

    @staticmethod
    def get_light_slate_gray() -> Color:
        """Получение цвета LightSlateGray."""
        return Color.create(119, 136, 153)

    @staticmethod
    def get_light_slate_grey() -> Color:
        """Получение цвета LightSlateGrey."""
        return Color.create(119, 136, 153)

    @staticmethod
    def get_slate_gray() -> Color:
        """Получение цвета SlateGray."""
        return Color.create(112, 128, 144)

    @staticmethod
    def get_slate_grey() -> Color:
        """Получение цвета SlateGrey."""
        return Color.create(112, 128, 144)

    @staticmethod
    def get_dark_slate_gray() -> Color:
        """Получение цвета DarkSlateGray."""
        return Color.create(47, 79, 79)

    @staticmethod
    def get_dark_slate_grey() -> Color:
        """Получение цвета DarkSlateGrey."""
        return Color.create(47, 79, 79)


class String:
    """Строка."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.s = ""

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
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 4:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba_str = bmc.str_to_byte_array(self.s)
        ba_size = bmc.int32_to_byte_array(len(ba_str))
        return ba_size + ba_str

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        ba_size = byte_array[:4]
        size = bmc.byte_array_to_int32(ba_size)
        assert size <= len(byte_array) - 4
        ba_str = byte_array[4:4 + size]
        self.s = bmc.byte_array_to_str(ba_str)

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


class Point:
    """Точка с целочисленными координатами."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
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
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 8:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba_x = bmc.int32_to_byte_array(self.x)
        ba_y = bmc.int32_to_byte_array(self.y)
        return ba_x + ba_y

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        ba_values = byte_array[:8]
        vl = bmc.byte_array_to_int32_list(ba_values)
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

    def __pos__(self) -> Point:
        """Унарный оператор +."""
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
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления цвета."""
        return f"{self.x}, {self.y}"


class PointF:
    """Точка с дробными координатами."""

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
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 16:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba_x = bmc.double_to_byte_array(self.x)
        ba_y = bmc.double_to_byte_array(self.y)
        return ba_x + ba_y

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        ba_values = byte_array[:16]
        vl = bmc.byte_array_to_double_list(ba_values)
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

    def __pos__(self) -> PointF:
        """Унарный оператор +."""
        return self

    def __neg__(self) -> PointF:
        """Унарный оператор -."""
        return Point.create(-self.x, -self.y)

    def __eq__(self, other: PointF) -> bool:
        """Оператор ==."""
        assert isinstance(other, PointF)
        is_eq_x = bmh.float_equal(self.x, other.x)
        is_eq_y = bmh.float_equal(self.y, other.y)
        return is_eq_x and is_eq_y

    def __ne__(self, other) -> bool:
        """Оператор !=."""
        assert isinstance(other, PointF)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.x}, {self.y}"


class Size:
    """Размер с целочисленными координатами."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.__width = 0
        self.__height = 0

    def init(self, width: int, height: int) -> None:
        """Функция инициализации."""
        assert isinstance(width, int)
        assert isinstance(height, int)
        self.__width = width
        self.__height = height

    @staticmethod
    def create(width: int, height: int) -> Size:
        """Функция создания."""
        assert isinstance(width, int)
        assert isinstance(height, int)
        size = Size()
        size.init(width, height)
        return size

    def get_width(self) -> int:
        """Получение ширины."""
        return self.__width

    def set_width(self, width: int) -> None:
        """Задание ширины."""
        self.__width = width

    def get_height(self) -> int:
        """Получение высоты."""
        return self.__height

    def set_height(self, height: int) -> None:
        """Задание высоты."""
        self.__height = height

    def is_null(self):
        """Проверка ширины и высоты на 0."""
        return self.__width == 0 and self.__height == 0

    def is_valid(self):
        """Является ли размер валидным."""
        return self.__width >= 0 and self.__height >= 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 8:
            return False
        return True

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        ba_values = byte_array[:8]
        vl = bmc.byte_array_to_int32_list(ba_values)
        self.init(vl[0], vl[1])

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmc.int32_to_byte_array(self.__width)
        ba += bmc.int32_to_byte_array(self.__height)
        return ba

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 8

    def __eq__(self, other: Size) -> bool:
        """Оператор ==."""
        assert isinstance(other, Size)
        is_eq_width = self.__width == other.__width
        is_eq_height = self.__height == other.__height
        return is_eq_width and is_eq_height

    def __ne__(self, other: Size) -> bool:
        """Оператор !=."""
        assert isinstance(other, Size)
        return not self == other

    def __mul__(self, other: int) -> Size:
        """Оператор *."""
        assert isinstance(other, int)
        width = self.__width * other
        height = self.__height * other
        Size.init(width, height)
        return self

    def __imul__(self, other: int) -> Size:
        """Оператор *=."""
        assert isinstance(other, int)
        self.__width *= other
        self.__height *= other
        return self

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.__width}, {self.__height}"


class SizeF:
    """Размер с дробными координатами."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.__width = 0.0
        self.__height = 0.0

    def init(self, width: float, height: float) -> None:
        """Функция инициализации."""
        assert isinstance(width, float)
        assert isinstance(height, float)
        self.__width = width
        self.__height = height

    @staticmethod
    def create(width: float, height: float) -> SizeF:
        """Функция создания."""
        assert isinstance(width, float)
        assert isinstance(height, float)
        size = SizeF()
        size.init(width, height)
        return size

    def get_width(self) -> float:
        """Получение ширины."""
        return self.__width

    def set_width(self, width: float) -> None:
        """Задание ширины."""
        self.__width = width

    def get_height(self) -> float:
        """Получение высоты."""
        return self.__height

    def set_height(self, height: float) -> None:
        """Задание высоты."""
        self.__height = height

    def is_null(self) -> bool:
        """Проверка ширины и высоты на 0."""
        return bmh.is_float_null(self.__width) and bmh.is_float_null(self.__height)

    def is_valid(self) -> bool:
        """Является ли размер валидным."""
        return self.__width >= 0 and self.__height >= 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 16:
            return False
        return True

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        ba_width = byte_array[:8]
        self.__width = bmc.byte_array_to_double(ba_width)
        ba_height = byte_array[8:16]
        self.__height = bmc.byte_array_to_double(ba_height)

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba_width = bmc.double_to_byte_array(self.__width)
        ba_height = bmc.double_to_byte_array(self.__height)
        return ba_width + ba_height

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 16

    def __eq__(self, other) -> bool:
        """Оператор ==."""
        assert isinstance(other, SizeF)
        is_eq_width = bmh.float_equal(self.__width, other.__width)
        is_eq_height = bmh.float_equal(self.__height, other.__height)
        return is_eq_width and is_eq_height

    def __ne__(self, other) -> bool:
        """Оператор !=."""
        assert isinstance(other, SizeF)
        return not self == other

    def __mul__(self, other: float) -> SizeF:
        """Оператор *."""
        assert isinstance(other, float)
        width = self.__width * other
        height = self.__height * other
        return SizeF.create(width, height)

    def __imul__(self, other: float) -> SizeF:
        """Оператор *=."""
        assert isinstance(other, float)
        self.__width *= other
        self.__height *= other
        return self

    def __str__(self):
        """Получение строкового представления."""
        return f"{self.width}, {self.height}"


class Diap:
    """Диапазон с целочисленными границами."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.begin = 0
        self.end = 100

    def init(self, begin: int, end: int) -> None:
        """Функция инициализации."""
        assert isinstance(begin, int)
        assert isinstance(end, int)
        self.begin = begin
        self.end = end

    @staticmethod
    def create(begin: int, end: int) -> SizeF:
        """Функция создания."""
        assert isinstance(begin, int)
        assert isinstance(end, int)
        diap = Diap()
        diap.init(begin, end)
        return diap

    def is_valid(self):
        """Проверка корректности диапазона."""
        return self.begin <= self.end

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 8:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmc.int32_to_byte_array(self.begin)
        ba += bmc.int32_to_byte_array(self.end)
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        ba_begin = byte_array[:4]
        self.begin = bmc.byte_array_to_int32(ba_begin)
        ba_end = byte_array[4:8]
        self.end = bmc.byte_array_to_int32(ba_end)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 8

    def __eq__(self, other: Diap) -> bool:
        """Оператор ==."""
        assert isinstance(other, Diap)
        is_eq_begin = self.begin == other.begin
        is_eq_end = self.end == other.end
        return is_eq_begin and is_eq_end

    def __ne__(self, other: Diap) -> bool:
        """Оператор !=."""
        assert isinstance(other, Diap)
        return not self == other

    def __str__(self):
        """Получение строкового представления."""
        return f"{self.begin}, {self.end}"


class DiapF:
    """Диапазон с дробными границами."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.begin = 0.0
        self.end = 100.0

    def init(self, begin: float, end: float) -> None:
        """Функция инициализации."""
        assert isinstance(begin, float)
        assert isinstance(end, float)
        self.begin = begin
        self.end = end

    @staticmethod
    def create(begin: float, end: float) -> SizeF:
        """Функция создания."""
        assert isinstance(begin, float)
        assert isinstance(end, float)
        diap = DiapF()
        diap.init(begin, end)
        return diap

    def is_valid(self):
        """Проверка корректности диапазона."""
        return self.begin <= self.end

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности массива байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 16:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        ba = bytearray()
        ba += bmc.double_to_byte_array(self.begin)
        ba += bmc.double_to_byte_array(self.end)
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        assert self.check_byte_array(byte_array)
        ba_begin = byte_array[:8]
        self.begin = bmc.byte_array_to_double(ba_begin)
        ba_end = byte_array[8:16]
        self.end = bmc.byte_array_to_double(ba_end)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 16

    def __eq__(self, other: DiapF) -> bool:
        """Оператор ==."""
        assert isinstance(other, DiapF)
        is_eq_begin = bmh.float_equal(self.begin, other.begin)
        is_eq_end = bmh.float_equal(self.end, other.end)
        return is_eq_begin and is_eq_end

    def __ne__(self, other: DiapF) -> bool:
        """Оператор !=."""
        assert isinstance(other, DiapF)
        return not self == other

    def __str__(self):
        """Получение строкового представления."""
        return f"{self.begin}, {self.end}"


class Line:
    """Линия с целочисленными координатами."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.pt_1 = Point()
        self.pt_2 = Point()

    def init(self, pt_1, pt_2) -> None:
        """Функция инициализации."""
        assert isinstance(pt_1, Point)
        assert isinstance(pt_2, Point)
        self.pt_1 = pt_1
        self.pt_2 = pt_2

    def init_2(self, x_1: int, y_1: int, x_2: int, y_2: int) -> None:
        """Функция инициализации."""
        assert isinstance(x_1, int)
        assert isinstance(y_1, int)
        assert isinstance(x_2, int)
        assert isinstance(y_2, int)
        self.pt_1.init(x_1, y_1)
        self.pt_2.init(x_2, y_2)

    @staticmethod
    def create(pt_1: Point, pt_2: Point) -> Line:
        """Функция инициализации (вариант 2)."""
        assert isinstance(pt_1, Point)
        assert isinstance(pt_2, Point)
        line = Line()
        line.pt_1 = pt_1
        line.pt_2 = pt_2
        return line

    @staticmethod
    def create_2(x_1: int, y_1: int, x_2: int, y_2: int) -> Line:
        """Функция инициализации (вариант 2)."""
        assert isinstance(x_1, int)
        assert isinstance(y_1, int)
        assert isinstance(x_2, int)
        assert isinstance(y_2, int)
        line = Line()
        line.pt_1.init(x_1, y_1)
        line.pt_2.init(x_2, y_2)
        return line

    def is_empty(self) -> bool:
        """Проверка на линию нулевой длины."""
        return self.pt_1 == self.pt_2

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 16:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba_pt_1 = self.pt_1.to_byte_array()
        ba_pt_2 = self.pt_2.to_byte_array()
        return ba_pt_1 + ba_pt_2

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        ba_pt_1 = byte_array[:8]
        self.pt_1.from_byte_array(ba_pt_1)
        ba_pt_2 = byte_array[8:16]
        self.pt_2.from_byte_array(ba_pt_2)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 16

    def __eq__(self, other: Line) -> bool:
        """Оператор ==."""
        assert isinstance(other, Line)
        is_eq_pt_1 = self.pt_1 == other.pt_1
        is_eq_pt_2 = self.pt_2 == other.pt_2
        return is_eq_pt_1 and is_eq_pt_2

    def __ne__(self, other: Line) -> bool:
        """Оператор !=."""
        assert isinstance(other, Line)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления объекта."""
        return f"{self.pt_1}, {self.pt_2}"


class LineF:
    """Линия с дробными координатами."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.pt_1 = PointF()
        self.pt_2 = PointF()

    def init(self, pt_1: PointF, pt_2: PointF) -> None:
        """Функция инициализации."""
        assert isinstance(pt_1, PointF)
        assert isinstance(pt_2, PointF)
        self.pt_1 = pt_1
        self.pt_2 = pt_2

    def init_2(self, x_1: float, y_1: float, x_2: float, y_2: float) -> None:
        """Функция инициализации."""
        assert isinstance(x_1, float)
        assert isinstance(y_1, float)
        assert isinstance(x_2, float)
        assert isinstance(y_2, float)
        self.pt_1.init(x_1, y_1)
        self.pt_2.init(x_2, y_2)

    @staticmethod
    def create(pt_1: PointF, pt_2: PointF) -> LineF:
        """Функция инициализации 2."""
        assert isinstance(pt_1, PointF)
        assert isinstance(pt_2, PointF)
        line = LineF()
        line.pt_1 = pt_1
        line.pt_2 = pt_2
        return line

    @staticmethod
    def create_2(x_1: float, y_1: float, x_2: float, y_2: float) -> LineF:
        """Функция инициализации 2."""
        assert isinstance(x_1, float)
        assert isinstance(y_1, float)
        assert isinstance(x_2, float)
        assert isinstance(y_2, float)
        line = LineF()
        line.pt_1.init(x_1, y_1)
        line.pt_2.init(x_2, y_2)
        return line

    def is_empty(self) -> bool:
        """Проверка на линию нулевой длины."""
        return self.pt_1 == self.pt_2

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 32:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba_pt_1 = self.pt_1.to_byte_array()
        ba_pt_2 = self.pt_2.to_byte_array()
        return ba_pt_1 + ba_pt_2

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        ba_pt_1 = byte_array[:16]
        self.pt_1.from_byte_array(ba_pt_1)
        ba_pt_2 = byte_array[16:32]
        self.pt_2.from_byte_array(ba_pt_2)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 32

    def __eq__(self, other: PointF) -> bool:
        """Оператор ==."""
        assert isinstance(other, LineF)
        is_eq_pt1 = (self.pt_1 == other.pt_1)
        is_eq_pt2 = (self.pt_2 == other.pt_2)
        return is_eq_pt1 and is_eq_pt2

    def __ne__(self, other: PointF) -> bool:
        """Оператор !=."""
        assert isinstance(other, LineF)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления объекта."""
        return f"{self.pt_1}, {self.pt_2}"


class Polyline:
    """Ломаная линия с целыми координатами."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
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
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 4:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmc.int32_to_byte_array(self.get_point_count())
        for point in self.points:
            ba += point.to_byte_array()
        return ba

    def from_byte_array(self, byte_array):
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        ba_count = byte_array[:4]
        count = bmc.byte_array_to_int32(ba_count)
        points = []
        for i in range(count):
            pt = Point()
            bi = 4 + i * 8
            ei = bi + 8
            ba_pt = byte_array[bi:ei]
            pt.from_byte_array(ba_pt)
            points.append(pt)
        self.points = points

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
        return f"{self.points}"

    @staticmethod
    def _check_points(points: list) -> bool:
        """Проверка списка точек."""
        if not isinstance(points, list):
            return False
        if not all(isinstance(pt, Point) for pt in points):
            return False
        return True


class PolylineF:
    """Ломаная линия с дробными координатами."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
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
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 4:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        count = self.get_point_count()
        ba += bmc.int32_to_byte_array(count)
        for point in self.points:
            ba += point.to_byte_array()
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        ba_count = byte_array[:4]
        count = bmc.byte_array_to_int32(ba_count)
        points = []
        for i in range(count):
            pt = PointF()
            bi = 4 + i * 16
            ei = bi + 16
            ba_pt = byte_array[bi:ei]
            pt.from_byte_array(ba_pt)
            points.append(pt)
        self.points = points

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
        return f"{self.points}"

    @staticmethod
    def _check_points(points: list) -> bool:
        """Проверка списка точек."""
        if not isinstance(points, list):
            return False
        if not all(isinstance(pt, PointF) for pt in points):
            return False
        return True


class Rect:
    """Прямоугольник с целочисленными координатами."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.left_top = Point()
        self.size = Size()

    def init(self, left_top: Point, size: Size) -> None:
        """Функция инициализации."""
        assert isinstance(left_top, Point)
        assert isinstance(size, Size)
        self.left_top = left_top
        self.size = size

    def init_2(self, left: int, top: int, width: int, height: int) -> None:
        """Функция инициализации (вариант 2)."""
        assert isinstance(left, int)
        assert isinstance(top, int)
        assert isinstance(width, int)
        assert isinstance(height, int)
        self.left_top = Point.create(left, top)
        self.size.init(width, height)

    @staticmethod
    def create(left_top: Point, size: Size) -> Rect:
        """Функция создания."""
        assert isinstance(left_top, Point)
        assert isinstance(size, Size)
        rect = Rect()
        rect.init(left_top, size)
        return rect

    @staticmethod
    def create_2(left: int, top: int, width: int, height: int) -> Rect:
        """Функция создания (вариант 2)."""
        assert isinstance(left, int)
        assert isinstance(top, int)
        assert isinstance(width, int)
        assert isinstance(height, int)
        rect = Rect()
        rect.init_2(left, top, width, height)
        return rect

    def get_left(self) -> int:
        """Получение смещения слева."""
        return self.left_top.x

    def set_left(self, left: int) -> None:
        """Задание смещения слева."""
        assert isinstance(left, int)
        self.left_top.init(left, self.get_top())

    def get_top(self) -> int:
        """Получение смещения слева."""
        return self.left_top.y

    def set_top(self, top: int) -> None:
        """Задание смещения сверху."""
        assert isinstance(top, int)
        self.left_top.y = top

    def get_width(self) -> int:
        """Получение ширины."""
        return self.size.get_width()

    def set_width(self, width: int) -> None:
        """Задание ширины."""
        assert isinstance(width, int)
        self.size.width = width

    def get_height(self) -> int:
        """Получение высоты."""
        return self.size.get_height()

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
        return self.size.width() >= 0 and self.size.height() >= 0

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов для инициализации."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 16:
            return False
        return True

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
        self.init_2(vl[0], vl[1], vl[2], vl[3])

    def get_byte_array_len(self):
        """Получение длины списка байтов."""
        return 16

    def __eq__(self, other: Rect) -> bool:
        """Оператор ==."""
        is_eq_left_top = self.left_top == other.left_top
        is_eq_size = self.size == other.size
        return is_eq_left_top and is_eq_size

    def __ne__(self, other: Rect) -> bool:
        """Оператор !=."""
        assert isinstance(other, Rect)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.left_top}, {self.size}"


class RectF:
    """Прямоугольник с дробными координатами."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.left_top = PointF()
        self.size = SizeF()

    def init(self, left_top: PointF, size: SizeF) -> None:
        """Функция инициализации."""
        assert isinstance(left_top, PointF)
        assert isinstance(size, SizeF)
        self.left_top = left_top
        self.size = size

    def init_2(self, left: float, top: float, width: float,
               height: float) -> None:
        """Функция инициализации (вариант 2)."""
        assert isinstance(left, float)
        assert isinstance(top, float)
        assert isinstance(width, float)
        assert isinstance(height, float)
        self.left_top.init(left, top)
        self.size.init(width, height)

    @staticmethod
    def create(left_top: PointF, size: SizeF) -> RectF:
        """Функция создания."""
        assert isinstance(left_top, PointF)
        assert isinstance(size, SizeF)
        rect = RectF()
        rect.init(left_top, size)
        return rect

    @staticmethod
    def create_2(left: float, top: float, width: float,
                 height: float) -> RectF:
        """Функция создания (вариант 2)."""
        assert isinstance(left, float)
        assert isinstance(top, float)
        assert isinstance(width, float)
        assert isinstance(height, float)
        rect = RectF()
        rect.init_2(left, top, width, height)
        return rect

    def get_left(self) -> float:
        """Получение смещения слева."""
        return self.left_top.x

    def set_left(self, left: float) -> None:
        """Задание смещения слева."""
        assert isinstance(left, float)
        self.top_left.init(left, self.get_top())

    def get_top(self) -> float:
        """Получение смещения сверху."""
        return self.left_top.y

    def set_top(self, top: float) -> None:
        """Задание смещения сверху."""
        assert isinstance(top, float)
        self.top_left.init(self.get_left(), top)

    def get_width(self) -> float:
        """Получение ширины."""
        return self.size.get_width()

    def get_height(self) -> float:
        """Получение высоты."""
        return self.size.get_height()

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
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 32:
            return False
        return True

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
        self.init_2(vl[0], vl[1], vl[2], vl[3])

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 32

    def __eq__(self, other: RectF) -> bool:
        """Оператор ==."""
        is_eq_left_top = (self.left_top == other.left_top)
        is_eq_size = (self.size == other.size)
        return is_eq_left_top and is_eq_size

    def __ne__(self, other: RectF) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления объекта."""
        return f"{self.left_top}, {self.size}"


class RoundRect:
    """Прямоугольник со сглажененными углами с целыми координатами."""

    def __init__(self):
        """Конструктор без параметров."""
        self.rect = Rect()
        self.radius_x = 0
        self.radius_y = 0

    def init(self, rect: Rect, radius_x: int, radius_y: int) -> None:
        """Функция инициализации."""
        assert isinstance(rect, Rect)
        assert isinstance(radius_x, int)
        assert isinstance(radius_y, int)
        self.rect = rect
        self.radius_x = RoundRect._correctRadius(radius_x)
        self.radius_y = RoundRect._correctRadius(radius_y)

    @staticmethod
    def create(rect: Rect, radius_x: int, radius_y: int) -> RoundRect:
        """Функция создания."""
        assert isinstance(rect, Rect)
        assert isinstance(radius_x, int)
        assert isinstance(radius_y, int)
        r = RoundRect()
        r.init(rect, radius_x, radius_y)
        return r

    def get_center(self) -> Point:
        """Получение центра."""
        return self.rect.get_center()

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 24:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba_rect = self.rect.to_byte_array()
        ba_radius_x = bmc.int32_to_byte_array(self.radius_x)
        ba_radius_y = bmc.int32_to_byte_array(self.radius_y)
        return ba_rect + ba_radius_x + ba_radius_y

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        ba_rect = byte_array[:16]
        self.rect.from_byte_array(ba_rect)
        ba_radius_x = byte_array[16:20]
        self.radius_x = bmc.byte_array_to_int32(ba_radius_x)
        ba_radius_y = byte_array[20:24]
        self.radius_y = bmc.byte_array_to_int32(ba_radius_y)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 24

    def __eq__(self, other: RoundRect) -> bool:
        """Оператор ==."""
        is_eq_rect = self.rect == other.rect
        is_eq_radius_x = self.radius_x == other.radius_x
        is_eq_radius_y = self.radius_y == other.radius_y
        return is_eq_rect and is_eq_radius_x and is_eq_radius_y

    def __ne__(self, other: RoundRect) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления объекта."""
        return f"{self.rect}, {self.radius_x}, {self.radius_y}"

    @staticmethod
    def _correctRadius(radius: int) -> int:
        """Корректировка радиуса."""
        if radius < 0:
            return 0
        elif radius > 100:
            return 100
        else:
            return radius


class RoundRectF:
    """Прямоугольник со сглажененными углами с дробными координатами."""

    def __init__(self) -> None:
        """Конструктор без параметров."""
        self.rect = RectF()
        self.radius_x = 0.0
        self.radius_y = 0.0

    def init(self, rect: RectF, radius_x: float, radius_y: float) -> None:
        """Функция инициализации."""
        assert isinstance(rect, RectF)
        assert isinstance(radius_x, float)
        assert isinstance(radius_y, float)
        self.rect = rect
        self.radius_x = RoundRectF._correctRadius(radius_x)
        self.radius_y = RoundRectF._correctRadius(radius_y)

    @staticmethod
    def create(rect: RectF, radius_x: float, radius_y: float) -> RoundRectF:
        """Функция создания."""
        assert isinstance(rect, RectF)
        assert isinstance(radius_x, float)
        assert isinstance(radius_y, float)
        r = RoundRectF()
        r.init(rect, radius_x, radius_y)
        return r

    def get_center(self) -> PointF:
        """Получение центра."""
        return self.rect.get_center()

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 48:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba_rect = self.rect.to_byte_array()
        ba_radius_x = bmc.double_to_byte_array(self.radius_x)
        ba_radius_y = bmc.double_to_byte_array(self.radius_y)
        return ba_rect + ba_radius_x + ba_radius_y

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        ba_rect = byte_array[:32]
        self.rect.from_byte_array(ba_rect)
        ba_radius_x = byte_array[32:40]
        self.radius_x = bmc.byte_array_to_double(ba_radius_x)
        ba_radius_y = byte_array[40:48]
        self.radius_y = bmc.byte_array_to_double(ba_radius_y)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 48

    def __eq__(self, other: RoundRectF) -> bool:
        """Оператор ==."""
        is_eq_rect = self.rect == other.rect
        is_eq_radius_x = self.radius_x == other.radius_x
        is_eq_radius_y = self.radius_y == other.radius_y
        return is_eq_rect and is_eq_radius_x and is_eq_radius_y

    def __ne__(self, other: RoundRectF) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления объекта."""
        return f"{self.rect}, {self.radius_x}, {self.radius_y}"

    @staticmethod
    def _correctRadius(radius: float) -> float:
        """Корректировка радиуса."""
        if radius < 0.0:
            return 0.0
        elif radius > 100.0:
            return 100.0
        else:
            return radius


class Polygon:
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
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 4:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += bmc.int32_to_byte_array(self.get_point_count())
        for pt in self.points:
            ba += pt.to_byte_array()
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из списка байтов."""
        assert self.check_byte_array(byte_array)
        ba_count = byte_array[:4]
        count = bmc.byte_array_to_int32(ba_count)
        points = []
        for i in range(count):
            pt = Point()
            pt_size = pt.get_byte_array_len()
            bi = 4 + i * pt_size
            ei = bi + pt_size
            ba_pt = byte_array[bi:ei]
            pt.from_byte_array(ba_pt)
            points.append(pt)
        self.points = points

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: Polygon) -> bool:
        """Оператор ==."""
        return self.points == other.points

    def __ne__(self, other: Polygon) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.points}"

    @staticmethod
    def _check_points(points):
        """Проверка списка точек."""
        if not isinstance(points, list):
            return False
        if not all(isinstance(pt, Point) for pt in points):
            return False
        return True


class PolygonF:
    """Полигон с точками с дробными координатами."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.points = []

    def init(self, points: list) -> None:
        """Функция инициализации."""
        assert PolygonF._check_points(points)
        self.points = points

    @staticmethod
    def create(points) -> PolygonF:
        """Функция создания."""
        assert PolygonF._check_points(points)
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

    def check_byte_array(self, byte_array: bytearray) -> bool:
        """Проверка корректности списка байтов."""
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 4:
            return False
        return True

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
        assert self.check_byte_array(byte_array)
        ba_count = byte_array[:4]
        count = bmc.byte_array_to_int32(ba_count)
        points = []
        for i in range(count):
            pt = PointF()
            pt_size = pt.get_byte_array_len()
            bi = 4 + i * pt_size
            ei = bi + pt_size
            ba_pt = byte_array[bi:ei]
            pt.from_byte_array(ba_pt)
            points.append(pt)
        self.points = points

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: PolygonF) -> bool:
        """Оператор ==."""
        return self.points == other.points

    def __ne__(self, other: list) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.points}"

    @staticmethod
    def _check_points(points: list) -> bool:
        """Проверка списка точек."""
        if not isinstance(points, list):
            return False
        if not all(isinstance(pt, PointF) for pt in points):
            return False
        return True


class PenStyle:
    """Стиль пера."""

    @staticmethod
    def style_to_str(style: int) -> str:
        """Конвертация стиля в строку."""
        assert isinstance(style, int)
        if style == PenStyle.NO_PEN:
            return "NO_PEN"
        elif style == PenStyle.DASH_LINE:
            return "DASH_LINE"
        elif style == PenStyle.DOT_LINE:
            return "DOT_LINE"
        elif style == PenStyle.DASH_DOT_LINE:
            return "DASH_DOT_LINE"
        elif style == PenStyle.DASH_DOT_DOT_LINE:
            return "DASH_DOT_DOT_LINE"
        else:
            return "SOLID_LINE"

    @staticmethod
    def str_to_style(s: str) -> int:
        """Конвертация строки в стиль."""
        assert isinstance(s, str)
        if s == "NO_PEN":
            return PenStyle.NO_PEN
        elif s == "DASH_LINE":
            return PenStyle.DASH_LINE
        elif s == "DOT_LINE":
            return PenStyle.DOT_LINE
        elif s == "DASH_DOT_LINE":
            return PenStyle.DASH_DOT_LINE
        elif s == "DASH_DOT_DOT_LINE":
            return PenStyle.DASH_DOT_DOT_LINE
        else:
            return PenStyle.SOLID_LINE

    @staticmethod
    def get_values():
        """Получение значений стилей."""
        return (PenStyle.NO_PEN,
                PenStyle.SOLID_LINE,
                PenStyle.DASH_LINE,
                PenStyle.DOT_LINE,
                PenStyle.DASH_DOT_LINE,
                PenStyle.DASH_DOT_DOT_LINE)

    @staticmethod
    def is_correct_value(value: int) -> bool:
        """Проверка корректности значения."""
        return value in PenStyle.get_values()

    @staticmethod
    def get_count():
        """Получение количества стилей."""
        return 6

    NO_PEN = 0
    SOLID_LINE = 1
    DASH_LINE = 2
    DOT_LINE = 3
    DASH_DOT_LINE = 4
    DASH_DOT_DOT_LINE = 5


class PenJoinStyle:
    """Стиль соединения линий для пера."""

    @staticmethod
    def style_to_str(style: int) -> str:
        """Конвертация стиля в строку."""
        assert isinstance(style, int)
        if style == PenJoinStyle.BEVEL_JOIN:
            return "BEVEL_JOIN"
        elif style == PenJoinStyle.ROUND_JOIN:
            return "ROUND_JOIN"
        else:
            return "MITER_JOIN"

    @staticmethod
    def str_to_style(s: str) -> int:
        """Конвертация строки в стиль."""
        assert isinstance(s, str)
        if s == "BEVEL_JOIN":
            return PenJoinStyle.BEVEL_JOIN
        elif s == "ROUND_JOIN":
            return PenJoinStyle.ROUND_JOIN
        else:
            return PenJoinStyle.MITER_JOIN

    @staticmethod
    def get_values():
        """Получение значений стилей."""
        return (PenJoinStyle.MITER_JOIN,
                PenJoinStyle.BEVEL_JOIN,
                PenJoinStyle.ROUND_JOIN)

    @staticmethod
    def is_correct_value(value: int) -> bool:
        """Проверка корректности значения."""
        return value in PenJoinStyle.get_values()

    @staticmethod
    def get_count():
        """Получение количества стилей."""
        return 3

    MITER_JOIN = 0x00
    BEVEL_JOIN = 0x40
    ROUND_JOIN = 0x80


class PenCapStyle:
    """Стиль окончания пера."""

    @staticmethod
    def style_to_str(style: int) -> str:
        """Конвертация стиля в строку."""
        assert isinstance(style, int)
        if style == PenCapStyle.SQUARE_CAP:
            return "SQUARE_CAP"
        elif style == PenCapStyle.ROUND_CAP:
            return "ROUND_CAP"
        else:
            return "FLAT_CAP"

    @staticmethod
    def str_to_style(s: str) -> int:
        """Конвертация строки в стиль."""
        assert isinstance(s, str)
        if s == "SQUARE_CAP":
            return PenCapStyle.FLAT_CAP
        elif s == "ROUND_CAP":
            return PenCapStyle.SQUARE_CAP
        else:
            return PenCapStyle.FLAT_CAP

    @staticmethod
    def get_values():
        """Получение значений стилей."""
        return (PenCapStyle.FLAT_CAP,
                PenCapStyle.SQUARE_CAP,
                PenCapStyle.ROUND_CAP)

    @staticmethod
    def is_correct_value(value: int) -> bool:
        """Проверка корректности значения."""
        return value in PenCapStyle.get_values()

    @staticmethod
    def get_count():
        """Получение количества стилей."""
        return 3

    FLAT_CAP = 0x00
    SQUARE_CAP = 0x10
    ROUND_CAP = 0x20


class Pen:
    """Перо."""

    def __init__(self):
        """Конструктор по умолчанию."""
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
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < self.get_byte_array_len():
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba = bytearray()
        ba += self.color.to_byte_array()
        ba += bmc.int32_to_byte_array(self.width)
        ba += bmc.uint8_to_byte_array(self.style)
        ba += bmc.uint8_to_byte_array(self.join_style)
        ba += bmc.uint8_to_byte_array(self.cap_style)
        return ba

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        ba_color = byte_array[:4]
        self.color.from_byte_array(ba_color)
        ba_width = byte_array[4:8]
        self.width = bmc.byte_array_to_int32(ba_width)
        ba_style = byte_array[8:9]
        self.style = bmc.byte_array_to_uint8(ba_style)
        ba_join_style = byte_array[9:10]
        self.join_style = bmc.byte_array_to_uint8(ba_join_style)
        ba_cap_style = byte_array[10:11]
        self.cap_style = bmc.byte_array_to_uint8(ba_cap_style)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 11

    def __eq__(self, other: Pen) -> bool:
        """Оператор ==."""
        is_eq_color = self.color == other.color
        is_eq_weidth = self.width == other.width
        is_eq_style = self.style == other.style
        is_eq_join_style = self.join_style == other.join_style
        is_eq_cap_style = (self.cap_style == other.cap_style)
        return is_eq_color and is_eq_weidth and is_eq_style \
            and is_eq_join_style and is_eq_cap_style

    def __ne__(self, other: Pen) -> bool:
        """Оператор !=."""
        assert isinstance(other, Pen)
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.color}, {self.width}, {self.style}, \
            {self.join_style}, {self.cap_style}"


class BrushStyle:
    """Стиль кисти."""

    @staticmethod
    def style_to_str(style: int) -> str:
        """Конвертация стиля в строку."""
        assert isinstance(style, int)
        if style == BrushStyle.NO_BRUSH:
            return "NO_BRUSH"
        elif style == BrushStyle.DENSE1_PATTERN:
            return "DENSE1_PATTERN"
        elif style == BrushStyle.DENSE2_PATTERN:
            return "DENSE2_PATTERN"
        elif style == BrushStyle.DENSE3_PATTERN:
            return "DENSE3_PATTERN"
        elif style == BrushStyle.DENSE4_PATTERN:
            return "DENSE4_PATTERN"
        elif style == BrushStyle.DENSE5_PATTERN:
            return "DENSE5_PATTERN"
        elif style == BrushStyle.DENSE6_PATTERN:
            return "DENSE6_PATTERN"
        elif style == BrushStyle.DENSE7_PATTERN:
            return "DENSE7_PATTERN"
        elif style == BrushStyle.HOR_PATTERN:
            return "HOR_PATTERN"
        elif style == BrushStyle.VER_PATTERN:
            return "VER_PATTERN"
        elif style == BrushStyle.CROSS_PATTERN:
            return "CROSS_PATTERN"
        elif style == BrushStyle.BDIAG_PATTERN:
            return "BDIAG_PATTERN"
        elif style == BrushStyle.FDIAG_PATTERN:
            return "FDIAG_PATTERN"
        else:
            return "SOLID_PATTERN"

    @staticmethod
    def str_to_style(s: str) -> int:
        """Конвертация строки в стиль."""
        assert isinstance(s, str)
        if s == "NO_BRUSH":
            return BrushStyle.NO_BRUSH
        elif s == "DENSE1_PATTERN":
            return BrushStyle.DENSE1_PATTERN
        elif s == "DENSE2_PATTERN":
            return BrushStyle.DENSE2_PATTERN
        elif s == "DENSE3_PATTERN":
            return BrushStyle.DENSE3_PATTERN
        elif s == "DENSE4_PATTERN":
            return BrushStyle.DENSE4_PATTERN
        elif s == "DENSE5_PATTERN":
            return BrushStyle.DENSE5_PATTERN
        elif s == "DENSE6_PATTERN":
            return BrushStyle.DENSE6_PATTERN
        elif s == "DENSE7_PATTERN":
            return BrushStyle.DENSE7_PATTERN
        elif s == "HOR_PATTERN":
            return BrushStyle.HOR_PATTERN
        elif s == "VER_PATTERN":
            return BrushStyle.VER_PATTERN
        elif s == "CROSS_PATTERN":
            return BrushStyle.CROSS_PATTERN
        elif s == "BDIAG_PATTERN":
            return BrushStyle.BDIAG_PATTERN
        elif s == "FDIAG_PATTERN":
            return BrushStyle.FDIAG_PATTERN
        else:
            return BrushStyle.SOLID_PATTERN

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


class Brush:
    """Кисть."""

    def __init__(self):
        """Конструктор по умолчанию."""
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
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 5:
            return False
        return True

    def to_byte_array(self) -> bytearray:
        """Получение в виде списка байтов."""
        ba_color = self.color.to_byte_array()
        ba_style = bmc.int8_to_byte_array(self.style)
        return ba_color + ba_style

    def from_byte_array(self, byte_array) -> None:
        """Инициализация через список байтов."""
        assert self.check_byte_array(byte_array)
        ba_color = byte_array[:4]
        self.color.from_byte_array(ba_color)
        ba_style = byte_array[4:]
        self.style = bmc.byte_array_to_int8(ba_style)

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return 5

    def __eq__(self, other: Brush) -> bool:
        """Оператор ==."""
        return self.color == other.color and self.style == other.style

    def __ne__(self, other: Brush) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.color}"


class Font:
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
        if not isinstance(byte_array, bytearray):
            return False
        if len(byte_array) < 10:
            return False
        return True

    def from_byte_array(self, byte_array: bytearray) -> None:
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
        ba_family = self.family.to_byte_array()
        ba_size = bmc.int32_to_byte_array(self.size)
        ba_bold = bmc.bool_to_byte_array(self.is_bold)
        return ba_family + ba_size + ba_bold

    def get_byte_array_len(self) -> int:
        """Получение длины списка байтов."""
        return len(self.to_byte_array())

    def __eq__(self, other: Font) -> bool:
        """Оператор ==."""
        is_eq_family = self.family == other.family
        is_eq_size = self.size == other.size
        is_eq_bold = self.is_bold == other.is_bold
        return is_eq_family and is_eq_size and is_eq_bold

    def __ne__(self, other: Font) -> bool:
        """Оператор !=."""
        return not self == other

    def __str__(self) -> str:
        """Получение строкового представления."""
        return f"{self.family}, {self.size}, {self.is_bold}"


class TestColor(unittest.TestCase):
    """Тестирование класса Color."""

    def test_contructor(self):
        """Тест конструктора."""
        c = Color()
        self.assertEqual(c.get_r(), 0)
        self.assertEqual(c.get_g(), 0)
        self.assertEqual(c.get_b(), 0)
        self.assertEqual(c.get_a(), 255)

    def test_init(self):
        """Тест функции init."""
        c = Color()
        c.init(200, 200, 200)
        self.assertEqual(c.get_r(), 200)
        self.assertEqual(c.get_g(), 200)
        self.assertEqual(c.get_b(), 200)
        self.assertEqual(c.get_a(), 255)

        c.init(100, 100, 100, 100)
        self.assertEqual(c.get_r(), 100)
        self.assertEqual(c.get_g(), 100)
        self.assertEqual(c.get_b(), 100)
        self.assertEqual(c.get_a(), 100)

    def test_create(self):
        """Тест функции create."""
        c = Color.create(50, 50, 50)
        self.assertTrue(isinstance(c, Color))
        self.assertEqual(c.get_r(), 50)
        self.assertEqual(c.get_g(), 50)
        self.assertEqual(c.get_b(), 50)
        self.assertEqual(c.get_a(), 255)

        c = Color.create(40, 40, 40, 40)
        self.assertEqual(c.get_r(), 40)
        self.assertEqual(c.get_g(), 40)
        self.assertEqual(c.get_b(), 40)
        self.assertEqual(c.get_a(), 40)

    def test_get_r(self):
        """Тест функции get_r."""
        c = Color.create(100, 100, 100)
        self.assertEqual(c.get_r(), 100)

    def test_set_r(self):
        """Тест функции set_r."""
        c = Color()
        c.set_r(100)
        self.assertEqual(c.get_r(), 100)

    def test_get_g(self):
        """Тест функции get_g."""
        c = Color.create(100, 100, 100)
        self.assertEqual(c.get_g(), 100)

    def test_set_g(self):
        """Тест функции set_g."""
        c = Color()
        c.set_g(100)
        self.assertEqual(c.get_g(), 100)

    def test_get_b(self):
        """Тест функции get_b."""
        c = Color.create(100, 100, 100)
        self.assertEqual(c.get_b(), 100)

    def test_set_b(self):
        """Тест функции set_b."""
        c = Color()
        c.set_b(100)
        self.assertEqual(c.get_b(), 100)

    def test_get_a(self):
        """Тест функции get_a."""
        c = Color.create(100, 100, 100, 100)
        self.assertEqual(c.get_a(), 100)

    def test_set_a(self):
        """Тесть функции set_a."""
        c = Color()
        c.set_a(100)
        self.assertEqual(c.get_a(), 100)

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
        self.assertEqual(c.get_r(), 0)
        self.assertEqual(c.get_g(), 0)
        self.assertEqual(c.get_b(), 0)
        self.assertEqual(c.get_a(), 0)

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
        c_1 = Color()
        self.assertTrue(c_1 == c_1)
        c_2 = Color.create(200, 200, 200)
        self.assertFalse(c_1 == c_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        c_1 = Color()
        self.assertFalse(c_1 != c_1)
        c_2 = Color.get_green()
        self.assertTrue(c_1 != c_2)


class TestString(unittest.TestCase):
    """Тестирование класса String."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        s = String()
        s.s = "123"

    def test_init(self):
        """Тест функции init."""
        s = String()
        s.init("123")
        self.assertEqual(s.s, "123")

    def test_create(self):
        """Тест функции create."""
        s = String.create("123")
        self.assertEqual(s.s, "123")

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        s = String.create("123")
        ba = s.to_byte_array()
        self.assertTrue(s.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        s = String.create("123")
        ba = s.to_byte_array()
        s.from_byte_array(ba)
        self.assertEqual(s.s, "123")

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        s = String()
        ba = s.to_byte_array()
        self.assertEqual(s.get_byte_array_len(), len(ba))

    def test_equal(self):
        """Тест оператора ==."""
        s_1 = String()
        self.assertTrue(s_1 == s_1)
        s_2 = String.create("123'")
        self.assertFalse(s_1 == s_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        s_1 = String()
        self.assertFalse(s_1 != s_1)
        s_2 = String.create('123')
        self.assertTrue(s_1 != s_2)


class TestPoint(unittest.TestCase):
    """Тестирование класса Point."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
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
        """Тест бинарного оператора +."""
        pt_1 = Point.create(200, 200)
        pt_2 = Point.create(100, 100)
        self.assertEqual(pt_1 + pt_2, Point.create(300, 300))

    def test_iadd(self):
        """Тест оператора +=."""
        pt_1 = Point.create(200, 200)
        pt_2 = Point.create(100, 100)
        pt_1 += pt_2
        self.assertEqual(pt_1, Point.create(300, 300))

    def test_sub(self):
        """Тест бинарного оператора -."""
        pt_1 = Point.create(200, 200)
        pt_2 = Point.create(100, 100)
        self.assertEqual(pt_1 - pt_2, Point.create(100, 100))

    def test_isub(self):
        """Тест оператора -=."""
        pt_1 = Point.create(200, 200)
        pt_2 = Point.create(100, 100)
        pt_1 -= pt_2
        self.assertEqual(pt_1, Point.create(100, 100))

    def test_equal(self):
        """Тест оператора ==."""
        pt_1 = Point()
        self.assertTrue(pt_1 == pt_1)
        pt_2 = Point.create(100, 100)
        self.assertFalse(pt_1 == pt_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        pt_1 = Point()
        self.assertFalse(pt_1 != pt_1)
        pt_2 = Point.create(100, 100)
        self.assertTrue(pt_1 != pt_2)


class TestPointF(unittest.TestCase):
    """Тестирование класса PointF."""

    def test_constructor(self):
        """Тест конструктора по умолчанию."""
        pt = PointF()
        self.assertAlmostEqual(pt.x, 0.0)
        self.assertAlmostEqual(pt.y, 0.0)

    def test_init(self):
        """Тест функции init."""
        pt = PointF()
        pt.init(100.0, 100.0)
        self.assertAlmostEqual(pt.x, 100.0)
        self.assertAlmostEqual(pt.y, 100.0)

    def test_create(self):
        """Тест функции create."""
        pt = PointF.create(100.0, 100.0)
        self.assertAlmostEqual(pt.x, 100.0)
        self.assertAlmostEqual(pt.y, 100.0)

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        pt = PointF()
        ba = pt.to_byte_array()
        self.assertTrue(pt.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        pt = PointF()
        ba = bmc.double_list_to_byte_array([0.0, 0.0])
        pt.from_byte_array(ba)
        self.assertEqual(pt, PointF())

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        pt = PointF()
        bl = pt.to_byte_array()
        self.assertEqual(pt.get_byte_array_len(), len(bl))

    def test_add(self):
        """Тест бинарного оператора +."""
        pt_1 = PointF.create(200.0, 200.0)
        pt_2 = PointF.create(100.0, 100.0)
        self.assertEqual(pt_1 + pt_2, PointF.create(300.0, 300.0))

    def test_iadd(self):
        """Тест оператора +=."""
        pt_1 = PointF.create(200.0, 200.0)
        pt_2 = PointF.create(100.0, 100.0)
        pt_1 += pt_2
        self.assertEqual(pt_1, PointF.create(300.0, 300.0))

    def test_sub(self):
        """Тест бинарного оператора -."""
        pt_1 = PointF.create(200.0, 200.0)
        pt_2 = PointF.create(100.0, 100.0)
        self.assertEqual(pt_1 - pt_2, PointF.create(100.0, 100.0))

    def test_isub(self):
        """Тест оператора -=."""
        pt_1 = PointF.create(200.0, 200.0)
        pt_2 = PointF.create(100.0, 100.0)
        pt_1 -= pt_2
        self.assertEqual(pt_1, PointF.create(100.0, 100.0))

    def test_equal(self):
        """Тест оператора ==."""
        pt_1 = PointF()
        self.assertTrue(pt_1 == pt_1)
        pt_2 = PointF.create(100.0, 100.0)
        self.assertFalse(pt_1 == pt_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        pt_1 = PointF()
        self.assertFalse(pt_1 != pt_1)
        pt_2 = PointF.create(100.0, 100.0)
        self.assertTrue(pt_1 != pt_2)


class TestSize(unittest.TestCase):
    """Тестирование класса Size."""

    def test_contructor(self):
        """Тест конструктора по умолчанию."""
        sz = Size()
        self.assertEqual(sz.get_width(), 0)
        self.assertEqual(sz.get_height(), 0)

    def test_init(self):
        """Тест функции init."""
        sz = Size()
        sz.init(100, 100)
        self.assertEqual(sz.get_width(), 100)
        self.assertEqual(sz.get_height(), 100)

    def test_create(self):
        """Тест функции create."""
        sz = Size.create(100, 100)
        self.assertEqual(sz.get_width(), 100)
        self.assertEqual(sz.get_height(), 100)

    def test_get_width(self):
        """Тест функции get_width."""
        sz = Size.create(100, 100)
        self.assertEqual(sz.get_width(), 100)

    def test_set_width(self):
        """Тест функции set_width."""
        sz = Size()
        sz.set_width(100)
        self.assertEqual(sz.get_width(), 100)

    def test_get_height(self):
        """Тест функции get_height."""
        sz = Size.create(100, 100)
        self.assertEqual(sz.get_height(), 100)

    def test_set_height(self):
        """Тест функции set_height."""
        sz = Size()
        sz.set_height(100)
        self.assertEqual(sz.get_height(), 100)

    def test_is_null(self):
        """Тест функции is_null."""
        sz = Size()
        self.assertTrue(sz.is_null())

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        sz = Size.create(100, 100)
        ba = sz.to_byte_array()
        self.assertTrue(sz.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        sz = Size.create(100, 100)
        ba = bmc.int32_list_to_byte_array([100, 100])
        sz.from_byte_array(ba)
        self.assertEqual(sz.get_width(), 100)
        self.assertEqual(sz.get_height(), 100)

    def test_equal(self):
        """Тест оператора ==."""
        sz_1 = Size()
        self.assertTrue(sz_1 == sz_1)
        sz_2 = Size.create(100, 100)
        self.assertFalse(sz_1 == sz_2)

    def test_not_equal(self):
        """Тест оператора =."""
        sz_1 = Size()
        self.assertFalse(sz_1 != sz_1)
        sz_2 = Size.create(100, 100)
        self.assertTrue(sz_1 != sz_2)


class TestSizeF(unittest.TestCase):
    """Тестирование класса SizeF."""

    def test_contructor(self):
        """Тест конструктора по умолчанию."""
        sz = SizeF()
        self.assertAlmostEqual(sz.get_width(), 0.0)
        self.assertAlmostEqual(sz.get_height(), 0.0)

    def test_init(self):
        """Тест функции init."""
        sz = SizeF()
        sz.init(100.0, 100.0)
        self.assertAlmostEqual(sz.get_width(), 100.0)
        self.assertAlmostEqual(sz.get_height(), 100.0)

    def test_create(self):
        """Тест функции create."""
        sz = SizeF.create(100.0, 100.0)
        self.assertAlmostEqual(sz.get_width(), 100.0)
        self.assertAlmostEqual(sz.get_height(), 100.0)

    def test_get_width(self):
        """Тест функции get_width."""
        sz = SizeF.create(100.0, 100.0)
        self.assertAlmostEqual(sz.get_width(), 100.0)

    def test_set_width(self):
        """Тест функции set_width."""
        sz = SizeF()
        sz.set_width(100.0)
        self.assertAlmostEqual(sz.get_width(), 100.0)

    def test_get_height(self):
        """Тест функции get_height."""
        sz = SizeF.create(100.0, 100.0)
        self.assertAlmostEqual(sz.get_height(), 100.0)

    def test_set_height(self):
        """Тест функции set_height."""
        sz = SizeF()
        sz.set_height(100.0)
        self.assertAlmostEqual(sz.get_height(), 100.0)

    def test_is_null(self):
        """Тест функции is_null."""
        sz = Size()
        self.assertTrue(sz.is_null())

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        sz = SizeF.create(100.0, 100.0)
        ba = sz.to_byte_array()
        self.assertTrue(sz.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        sz = SizeF.create(100.0, 100.0)
        ba = bmc.double_list_to_byte_array([100.0, 100.0])
        sz.from_byte_array(ba)
        self.assertAlmostEqual(sz.get_width(), 100.0)
        self.assertAlmostEqual(sz.get_height(), 100.0)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        sz = SizeF()
        self.assertEqual(sz.get_byte_array_len(), len(sz.to_byte_array()))

    def test_equal(self):
        """Тест оператора ==."""
        sz1 = SizeF()
        self.assertTrue(sz1 == sz1)
        sz2 = SizeF.create(100.0, 100.0)
        self.assertFalse(sz1 == sz2)

    def test_not_equal(self):
        """Тест оператора !=."""
        sz_1 = SizeF()
        self.assertFalse(sz_1 != sz_1)
        sz_2 = SizeF.create(100.0, 100.0)
        self.assertTrue(sz_1 != sz_2)


class TestDiap(unittest.TestCase):
    """Тестирование класса Diap."""

    def test_contructor(self):
        """Тест конструктора по умолчанию."""
        d = Diap()
        self.assertEqual(d.begin, 0)
        self.assertEqual(d.end, 100)

    def test_init(self):
        """Тест функции init."""
        d = Diap()
        begin = 0
        end = 100
        d.init(0, 100)
        self.assertAlmostEqual(d.begin, begin)
        self.assertAlmostEqual(d.end, end)

    def test_create(self):
        """Тест функции create."""
        d = Diap.create(0, 100)
        self.assertAlmostEqual(d.begin, 0)
        self.assertAlmostEqual(d.end, 100)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        pass

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        pass

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        pass

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        pass

    def test_equal(self):
        """Тест операратор ==."""
        d_1 = Diap()
        self.assertTrue(d_1 == d_1)
        d_2 = Diap.create(-100, 200)
        self.assertFalse(d_1 == d_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        d_1 = Diap()
        self.assertFalse(d_1 != d_1)
        d_2 = Diap.create(-100, 200)
        self.assertTrue(d_1 != d_2)


class TestDiapF(unittest.TestCase):
    """Тестирование класса DiapF."""

    def test_contructor(self):
        """Тест конструктора по умолчанию."""
        d = DiapF()
        self.assertAlmostEqual(d.begin, 0.0)
        self.assertAlmostEqual(d.end, 100.0)

    def test_init(self):
        """Тест функции init."""
        d = DiapF()
        begin = 0.0
        end = 100.0
        d.init(0.0, 100.0)
        self.assertAlmostEqual(d.begin, begin)
        self.assertAlmostEqual(d.end, end)

    def test_create(self):
        """Тест функции create."""
        begin = 0.0
        end = 100.0
        d = DiapF.create(begin, end)
        self.assertAlmostEqual(d.begin, begin)
        self.assertAlmostEqual(d.end, end)

    def test_check_byte_array(self):
        """Тест функции check_byte_array."""
        pass

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        pass

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        pass

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        pass

    def test_equal(self):
        """Тест операратор ==."""
        d_1 = DiapF()
        self.assertTrue(d_1 == d_1)
        d_2 = DiapF.create(-100.0, 200.0)
        self.assertFalse(d_1 == d_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        d_1 = DiapF()
        self.assertFalse(d_1 != d_1)
        d_2 = DiapF.create(-100.0, 200.0)
        self.assertTrue(d_1 != d_2)


class TestLine(unittest.TestCase):
    """Тестирование класса Line."""

    def test_contructor(self):
        """Тест конструктора по умолчанию."""
        line = Line()
        self.assertEqual(line.pt_1, Point())
        self.assertEqual(line.pt_2, Point())

    def test_init(self):
        """Тест функции init."""
        line = Line()
        pt_1 = Point()
        pt_2 = Point.create(100, 100)
        line.init(pt_1, pt_2)
        self.assertEqual(line.pt_1, pt_1)
        self.assertEqual(line.pt_2, pt_2)

    def test_init_2(self):
        """Тест функции init_2."""
        line = Line()
        line.init_2(10, 10, 100, 100)
        self.assertEqual(line.pt_1.x, 10)
        self.assertEqual(line.pt_1.y, 10)
        self.assertEqual(line.pt_2.x, 100)
        self.assertEqual(line.pt_2.y, 100)

    def test_create(self):
        """Тест функции create."""
        pt_1 = Point()
        pt_2 = Point.create(100, 100)
        line = Line.create(pt_1, pt_2)
        self.assertEqual(line.pt_1, pt_1)
        self.assertEqual(line.pt_2, pt_2)

    def test_create_2(self):
        """Тест функции create_2."""
        line = Line.create_2(10, 10, 100, 100)
        self.assertEqual(line.pt_1.x, 10)
        self.assertEqual(line.pt_1.y, 10)
        self.assertEqual(line.pt_2.x, 100)
        self.assertEqual(line.pt_2.y, 100)

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        line = Line.create_2(10, 10, 100, 100)
        ba = line.to_byte_array()
        self.assertTrue(line.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        byte_array = bmc.int32_list_to_byte_array([0, 0, 0, 0])
        line = Line()
        line.from_byte_array(byte_array)
        self.assertEqual(line.pt_1, Point())
        self.assertEqual(line.pt_2, Point())

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        line = Line()
        self.assertEqual(line.get_byte_array_len(), len(line.to_byte_array()))

    def test_equal(self):
        """Тест операратор ==."""
        line_1 = Line()
        self.assertTrue(line_1 == line_1)
        line_2 = Line.create_2(0, 0, 100, 100)
        self.assertFalse(line_1 == line_2)

    def test_not_equal(self):
        """Тест оператор !=."""
        line_1 = Line()
        self.assertFalse(line_1 != line_1)
        line_2 = Line.create_2(0, 0, 100, 100)
        self.assertTrue(line_1 != line_2)


class TestLineF(unittest.TestCase):
    """Тест класса LineF."""

    def test_contructor(self):
        """Тест конструктора."""
        line = LineF()
        self.assertEqual(line.pt_1, PointF())
        self.assertEqual(line.pt_2, PointF())

    def test_init(self):
        """Тест функции init."""
        line = LineF()
        pt_1 = PointF()
        pt_2 = PointF.create(100.0, 100.0)
        line.init(pt_1, pt_2)
        self.assertEqual(line.pt_1, pt_1)
        self.assertEqual(line.pt_2, pt_2)

    def test_init_2(self):
        """Тест функции init_2."""
        line = LineF()
        x_1 = 100.0
        y_1 = 100.0
        x_2 = 200.0
        y_2 = 200.0
        line.init_2(x_1, y_1, x_2, y_2)
        self.assertAlmostEqual(line.pt_1.x, x_1)
        self.assertAlmostEqual(line.pt_1.y, y_1)
        self.assertAlmostEqual(line.pt_2.x, x_2)
        self.assertAlmostEqual(line.pt_2.y, y_2)

    def test_create(self):
        """Тест функции create."""
        pt_1 = PointF()
        pt_2 = PointF.create(100.0, 100.0)
        line = LineF.create(pt_1, pt_2)
        self.assertEqual(line.pt_1, pt_1)
        self.assertEqual(line.pt_2, pt_2)

    def test_create_2(self):
        """Тест функции create_2."""
        x_1 = 100.0
        y_1 = 100.0
        x_2 = 200.0
        y_2 = 200.0
        line = LineF.create_2(x_1, y_1, x_2, y_2)
        self.assertAlmostEqual(line.pt_1.x, 100.0)
        self.assertAlmostEqual(line.pt_1.y, 100.0)
        self.assertAlmostEqual(line.pt_2.x, 200.0)
        self.assertAlmostEqual(line.pt_2.y, 200.0)

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        line = LineF.create_2(100.0, 100.0, 200.0, 200.0)
        byte_array = line.to_byte_array()
        line.from_byte_array(byte_array)
        self.assertAlmostEqual(line.pt_1.x, 100.0)
        self.assertAlmostEqual(line.pt_1.y, 100.0)
        self.assertAlmostEqual(line.pt_2.x, 200.0)
        self.assertAlmostEqual(line.pt_2.y, 200.0)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        line = Line()
        self.assertEqual(line.get_byte_array_len(), len(line.to_byte_array()))

    def test_equal(self):
        """Тест оператора ==."""
        line_1 = LineF()
        self.assertTrue(line_1 == line_1)
        line_2 = LineF.create_2(0.0, 0.0, 100.0, 100.0)
        self.assertFalse(line_1 == line_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        line_1 = LineF()
        self.assertFalse(line_1 != line_1)
        line_2 = LineF.create_2(0.0, 0.0, 100.0, 100.0)
        self.assertTrue(line_1 != line_2)


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
        p_1 = Polyline()
        self.assertTrue(p_1 == p_1)
        points = [Point().create(100, 100)]
        p_2 = Polyline.create(points)
        self.assertFalse(p_1 == p_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        p_1 = Polyline()
        self.assertFalse(p_1 != p_1)
        points = [Point().create(100, 100)]
        p_2 = Polyline.create(points)
        self.assertTrue(p_1 != p_2)


class TestPolylineF(unittest.TestCase):
    """Тест класса PolylineF."""

    def test_contructor(self):
        """Тест конструктора."""
        p = PolylineF()
        self.assertTrue(p.is_empty())
        self.assertEqual(p.get_point_count(), 0)

    def test_init(self):
        """Тест функции init."""
        p = PolylineF()
        points = [PointF().create(200.0, 200.0)]
        p.init(points)
        self.assertFalse(p.is_empty())
        self.assertEqual(p.get_point_count(), 1)

    def test_create(self):
        """Тест функции create."""
        points = [PointF(), PointF().create(200.0, 200.0)]
        p = PolylineF().create(points)
        self.assertFalse(p.is_empty())

    def test_add_point(self):
        """Тест функции add_point."""
        pt = PointF().create(100.0, 100.0)
        p = PolylineF()
        p.add_point(pt)
        self.assertFalse(p.is_empty())
        self.assertEqual(p.get_point_count(), 1)

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        p = PolylineF()
        ba = p.to_byte_array()
        self.assertTrue(p.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        p_1 = PolylineF()
        p_1.add_point(PointF().create(100.0, 100.0))
        ba = p_1.to_byte_array()
        p_2 = PolylineF()
        p_2.from_byte_array(ba)
        self.assertEqual(p_1, p_2)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        p = PolylineF()
        self.assertEqual(p.get_byte_array_len(), len(p.to_byte_array()))

    def test_equal(self):
        """Тест оператора ==."""
        p_1 = PolylineF()
        self.assertTrue(p_1 == p_1)
        points = [PointF().create(100.0, 100.0)]
        p_2 = PolylineF.create(points)
        self.assertFalse(p_1 == p_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        p_1 = PolylineF()
        self.assertFalse(p_1 != p_1)
        points = [PointF().create(100.0, 100.0)]
        p_2 = PolylineF.create(points)
        self.assertTrue(p_1 != p_2)


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

    def test_init_2(self):
        """Тест функции init_2."""
        rect = Rect()
        rect.init_2(100, 100, 200, 200)
        self.assertEqual(rect.get_left(), 100)
        self.assertEqual(rect.get_top(), 100)
        self.assertEqual(rect.get_width(), 200)
        self.assertEqual(rect.get_height(), 200)

    def test_create(self):
        """Тест функции create."""
        left_top = Point.create(10, 10)
        size = Size.create(100, 100)
        rect = Rect.create(left_top, size)
        self.assertEqual(rect.left_top, left_top)
        self.assertEqual(rect.size, size)

    def test_create_2(self):
        """Тест функции create_2."""
        rect = Rect.create_2(50, 50, 300, 300)
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
        rect = Rect()
        self.assertEqual(rect.get_byte_array_len(), len(rect.to_byte_array()))

    def test_equal(self):
        """Тест оператора ==."""
        rect_1 = Rect()
        self.assertTrue(rect_1 == rect_1)
        rect_2 = Rect.create_2(0, 0, 200, 200)
        self.assertFalse(rect_1 == rect_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        rect_1 = Rect()
        self.assertFalse(rect_1 != rect_1)
        rect_2 = Rect.create_2(100, 100, 200, 200)
        self.assertTrue(rect_1 != rect_2)


class TestRectF(unittest.TestCase):
    """Тест класса RectF."""

    def test_constructor(self):
        """Тест конструктора."""
        rect = RectF()
        self.assertEqual(rect.left_top, PointF())
        self.assertEqual(rect.size, SizeF())

    def test_init(self):
        """Тест функции init."""
        left_top = PointF.create(100.0, 100.0)
        size = SizeF.create(200.0, 200.0)
        rect = RectF()
        rect.init(left_top, size)
        self.assertEqual(rect.left_top, left_top)
        self.assertEqual(rect.size, size)

    def test_init_2(self):
        """Тест функции init_2."""
        rect = RectF()
        rect.init_2(100.0, 100.0, 200.0, 200.0)
        self.assertAlmostEqual(rect.get_left(), 100.0)
        self.assertAlmostEqual(rect.get_top(), 100.0)
        self.assertAlmostEqual(rect.get_width(), 200.0)
        self.assertAlmostEqual(rect.get_height(), 200.0)

    def test_create(self):
        """Тест функции create класса RectF."""
        left_top = PointF.create(100.0, 100.0)
        size = SizeF.create(200.0, 200.0)
        rect = RectF.create(left_top, size)
        self.assertEqual(rect.left_top, left_top)
        self.assertEqual(rect.size, size)

    def test_create_2(self):
        """Тест функции create_2 класса RectF."""
        rect = RectF.create_2(100.0, 100.0, 200.0, 200.0)
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
        rect = Rect()
        self.assertEqual(rect.get_byte_array_len(), len(rect.to_byte_array()))

    def test_equal(self):
        """Тест operator == класса RectF."""
        rect_1 = RectF()
        self.assertTrue(rect_1 == rect_1)
        rect_2 = RectF.create_2(100.0, 100.0, 200.0, 200.0)
        self.assertFalse(rect_1 == rect_2)

    def test_not_equal(self):
        """Тест operator !=."""
        rect_1 = RectF()
        self.assertTrue(rect_1 == rect_1)
        rect_2 = RectF.create_2(10.0, 10.0, 100.0, 100.0)
        self.assertFalse(rect_1 == rect_2)


class TestRoundRect(unittest.TestCase):
    """Тест класса RoundRect."""

    def test_constructor(self):
        """Тест конструтора по умолчанию."""
        rrect = RoundRect()
        self.assertEqual(rrect.rect, Rect())
        self.assertEqual(rrect.radius_x, 0)
        self.assertEqual(rrect.radius_y, 0)

    def test_init(self):
        """Тест функции init."""
        rrect = RoundRect()
        rect = Rect.create_2(0, 0, 100, 100)
        radius_x = 1
        radius_y = 1
        rrect.init(rect, radius_x, radius_y)
        self.assertEqual(rrect.rect, rect)
        self.assertEqual(rrect.radius_x, radius_x)
        self.assertEqual(rrect.radius_y, radius_y)

    def test_create(self):
        """Тест функции create."""
        rect = Rect.create_2(0, 0, 100, 100)
        radius_x = 1
        radius_y = 1
        rrect = RoundRect.create(rect, radius_x, radius_y)
        self.assertEqual(rrect.rect, rect)
        self.assertEqual(rrect.radius_x, radius_x)
        self.assertEqual(rrect.radius_y, radius_y)

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        rrect = RoundRect()
        ba = rrect.to_byte_array()
        self.assertTrue(rrect.check_byte_array(ba))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        rrect_1 = RoundRect()
        rrect_1.rect = Rect.create_2(10, 10, 101, 101)
        rrect_1.radius_x = 1
        rrect_1.radius_y = 1
        ba = rrect_1.to_byte_array()
        rrect_2 = RoundRect()
        rrect_2.from_byte_array(ba)
        self.assertEqual(rrect_1, rrect_2)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        rrect = RoundRect()
        self.assertEqual(rrect.get_byte_array_len(), len(rrect.to_byte_array()))

    def test_equal(self):
        """Тест оператора ==."""
        rrect_1 = RoundRect()
        self.assertTrue(rrect_1 == rrect_1)
        rrect_2 = RoundRect.create(Rect.create_2(0, 0, 100, 100), 10, 10)
        self.assertFalse(rrect_1 == rrect_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        rrect_1 = RoundRect()
        self.assertFalse(rrect_1 != rrect_1)
        rrect_2 = RoundRect.create(Rect.create_2(0, 0, 100, 100), 10, 10)
        self.assertTrue(rrect_1 != rrect_2)


class TestRoundRectF(unittest.TestCase):
    """Тест класса RoundRectF."""

    def test_constructor(self):
        """Тест конструктора."""
        rrect = RoundRectF()
        self.assertEqual(rrect.rect, RectF())
        self.assertAlmostEqual(rrect.radius_x, 0.0)
        self.assertAlmostEqual(rrect.radius_y, 0.0)

    def test_init(self):
        """Тест функции init."""
        rrect = RoundRectF()
        rect = RectF()
        radius_x = 0.0
        radius_y = 0.0
        rrect.init(rect, radius_x, radius_y)
        self.assertEqual(rrect.rect, rect)
        self.assertEqual(rrect.radius_x, radius_x)
        self.assertEqual(rrect.radius_y, radius_y)

    def test_create(self):
        """Тест функции create."""
        rect = RectF.create_2(0.0, 0.0, 100.0, 100.0)
        radius_x = 1.0
        radius_y = 1.0
        rrect = RoundRectF.create(rect, radius_x, radius_y)
        self.assertEqual(rrect.rect, rect)
        self.assertEqual(rrect.radius_x, radius_x)
        self.assertEqual(rrect.radius_y, radius_y)

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        rrect = RoundRectF()
        byte_array = rrect.to_byte_array()
        self.assertTrue(rrect.check_byte_array(byte_array))

#     def test_from_byte_array(self):
#         rect = RectF.create_2(100.0, 100.0, 200.0, 200.0)
#         radiusX = 1.0
#         radiusY = 1.0
#         bl = rect.to_byte_array() + double_to_byte_array(radiusX) +
#             double_to_byte_array(radiusY)
#         rrect = RoundRectF()
#         rrect.from_byte_array(bl)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        rrect = RoundRectF()
        self.assertEqual(rrect.get_byte_array_len(),
                         len(rrect.to_byte_array()))

    def test_equal(self):
        """Тест оператора ==."""
        rrect_1 = RoundRectF()
        self.assertTrue(rrect_1 == rrect_1)
        rect = RectF.create_2(0.0, 0.0, 100.0, 100.0)
        rrect_2 = RoundRectF.create(rect, 10.0, 10.0)
        self.assertFalse(rrect_1 == rrect_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        rrect_1 = RoundRectF()
        self.assertFalse(rrect_1 != rrect_1)

        rect = RectF.create_2(0.0, 0.0, 100.0, 100.0)
        rrect_2 = RoundRectF.create(rect, 10.0, 10.0)
        self.assertTrue(rrect_1 != rrect_2)


class TestPenStyle(unittest.TestCase):
    """Тест класса PenStyle."""

    def test_style_to_str(self):
        """Тест функции style_to_str."""
        style = PenStyle.DASH_DOT_DOT_LINE
        s = PenStyle.style_to_str(style)
        self.assertEqual(s, "DASH_DOT_DOT_LINE")

    def test_str_to_style(self):
        """Тест функции str_to_style."""
        s = "DASH_DOT_DOT_LINE"
        style = PenStyle.str_to_style(s)
        self.assertEqual(style, PenStyle.DASH_DOT_DOT_LINE)

    def test_get_count(self):
        """Тест функции get_count."""
        count = PenStyle.get_count()
        self.assertEqual(count, len(PenStyle.get_values()))


class TestPenJoinStyle(unittest.TestCase):
    """Тест класса PenJoinStyle."""

    def test_style_to_str(self):
        """Тест функции style_to_str."""
        style = PenJoinStyle.BEVEL_JOIN
        s = PenJoinStyle.style_to_str(style)
        self.assertEqual(s, "BEVEL_JOIN")

    def test_str_to_style(self):
        """Тест функции str_to_style."""
        s = "BEVEL_JOIN"
        style = PenJoinStyle.str_to_style(s)
        self.assertEqual(style, PenJoinStyle.BEVEL_JOIN)

    def test_get_count(self):
        """Тест функции get_count."""
        count = PenJoinStyle.get_count()
        self.assertEqual(count, len(PenJoinStyle.get_values()))


class TestPenCapStyle(unittest.TestCase):
    """Тест класса PenCapStyle."""

    def test_style_to_str(self):
        """Тест функции style_to_str."""
        style = PenCapStyle.FLAT_CAP
        s = PenCapStyle.style_to_str(style)
        self.assertEqual(s, "FLAT_CAP")

    def test_str_to_style(self):
        """Тест функции str_to_style."""
        s = "FLAT_CAP"
        style = PenCapStyle.str_to_style(s)
        self.assertEqual(style, PenCapStyle.FLAT_CAP)

    def test_get_count(self):
        """Тест функции get_count."""
        count = PenCapStyle.get_count()
        self.assertEqual(count, len(PenCapStyle.get_values()))


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

    def test_to_byte_array(self):
        """Тест функции to_byte_array."""
        pen = Pen()
        byte_array = pen.to_byte_array()
        self.assertTrue(pen.check_byte_array(byte_array))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        pen_1 = Pen()
        pen_1.color = Color.get_blue()
        pen_1.width = 3
        ba = pen_1.to_byte_array()
        pen_2 = Pen()
        pen_2.from_byte_array(ba)
        self.assertEqual(pen_2.color, Color.get_blue())
        self.assertEqual(pen_2.width, 3)

    def test_get_byte_list_len(self):
        """Тест функции get_byte_list_len."""
        pen = Pen()
        self.assertEqual(pen.get_byte_array_len(), len(pen.to_byte_array()))

    def test_equal(self):
        """Тест оператора ==."""
        pen_1 = Pen()
        self.assertTrue(pen_1 == pen_1)
        pen_2 = Pen.create(Color.get_red(), 2)
        self.assertFalse(pen_1 == pen_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        pen_1 = Pen()
        self.assertFalse(pen_1 != pen_1)
        pen_2 = Pen.create(Color.get_red(), 2)
        self.assertTrue(pen_1 != pen_2)


class TestBrushStyle(unittest.TestCase):
    """Тест класса BrushStyle."""

    def test_style_to_str(self):
        """Тест функции style_to_str."""
        style = BrushStyle.DENSE6_PATTERN
        s = BrushStyle.style_to_str(style)
        self.assertEqual(s, "DENSE6_PATTERN")

    def test_str_to_style(self):
        """Тест функции str_to_style."""
        s = "DENSE6_PATTERN"
        style = BrushStyle.str_to_style(s)
        self.assertEqual(style, BrushStyle.DENSE6_PATTERN)


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
        byte_array = brush.to_byte_array()
        self.assertTrue(brush.check_byte_array(byte_array))

    def test_from_byte_array(self):
        """Тест функции from_byte_array."""
        color = Color.get_gold()
        style = BrushStyle.FDIAG_PATTERN
        byte_array = bytearray()
        byte_array += color.to_byte_array()
        byte_array += bmc.int8_to_byte_array(style)
        brush = Brush()
        brush.from_byte_array(byte_array)
        self.assertEqual(brush.color, color)
        self.assertEqual(brush.style, style)

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
        brush_1 = Brush()
        self.assertFalse(brush_1 != brush_1)
        brush_2 = Brush.create(Color.get_blue(), BrushStyle.SOLID_PATTERN)
        self.assertTrue(brush_1 != brush_2)


class TestFont(unittest.TestCase):
    """Тест класса Font."""

    def test_constructor(self):
        """Тест конструктора."""
        font = Font()
        self.assertEqual(font.family, String.create("Arial"))
        self.assertEqual(font.size, 12)
        self.assertEqual(font.is_bold, False)

    def test_init(self):
        """Тест функции init."""
        family = String.create("Courier New")
        size = 14
        is_bold = True
        font = Font()
        font.init(family, size, is_bold)
        self.assertEqual(font.family, family)
        self.assertEqual(font.size, size)
        self.assertEqual(font.is_bold, is_bold)

    def test_create(self):
        """Тест функции create."""
        family = String.create("Courier New")
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
        family = String.create("Courier New")
        size = 16
        is_bold = True
        byte_array = bytearray()
        byte_array += family.to_byte_array()
        byte_array += bmc.int32_to_byte_array(size)
        byte_array += bmc.bool_to_byte_array(is_bold)
        font.from_byte_array(byte_array)
        self.assertEqual(font.family, family)
        self.assertEqual(font.size, size)
        self.assertEqual(font.is_bold, is_bold)

    def test_get_byte_array_len(self):
        """Тест функции get_byte_array_len."""
        font = Font()
        self.assertEqual(font.get_byte_array_len(), len(font.to_byte_array()))

    def test_equal(self):
        """Тест оператора ==."""
        font_1 = Font()
        self.assertTrue(font_1 == font_1)
        family = String.create('Courier New')
        size = 14
        is_bold = True
        font_2 = Font.create(family, size, is_bold)
        self.assertFalse(font_1 == font_2)

    def test_not_equal(self):
        """Тест оператора !=."""
        font_1 = Font()
        self.assertFalse(font_1 != font_1)
        family = String.create('Courier New')
        size = 14
        is_bold = True
        font_2 = Font.create(family, size, is_bold)
        self.assertTrue(font_1 != font_2)


# Вызывается при загрузке модуля главным.
if __name__ == "__main__":
    unittest.main()
