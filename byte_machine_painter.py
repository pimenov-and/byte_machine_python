"""
ByteMachine.

Класс для вывода графики.
"""
__author__ = "EnergyLabs"
__version__ = "0.9122"


import unittest
import byte_machine_paint as bmp


class Painter:
    """Класс для вывода графики."""

    def __init__(self) -> None:
        """Конструктор по умолчанию."""
        self.ops = []

    def save_state(self) -> None:
        """Сохранение состояния."""
        op = bmp.SaveStateOp()
        self.ops.append(op)

    def restore_state(self) -> None:
        """Восстановление состояния."""
        op = bmp.RestoreStateOp()
        self.ops.append(op)

    def set_clip_rect(self, rect: bmp.bmg.Rect) -> None:
        """Задание региона отсечения."""
        assert isinstance(rect, bmp.bmg.Rect)
        op = bmp.SetClipRectOp.create(rect)
        self.ops.append(op)

    def transform_translate(self, x: float, y: float) -> None:
        """Трансформация смещения."""
        assert isinstance(x, float)
        assert isinstance(y, float)
        op = bmp.TransformTranslateOp.create(x, y)
        self.ops.append(op)

    def transform_rotate(self, angle: float) -> None:
        """Трансформация поворота."""
        assert isinstance(angle, float)
        op = bmp.TransformRotateOp.create(angle)
        self.ops.append(op)

    def transform_scale(self, x: float, y: float) -> None:
        """Трансформация масштабирования."""
        assert isinstance(x, float)
        assert isinstance(y, float)
        op = bmp.TransformScaleOp.create(x, y)
        self.ops.append(op)

    def set_pen(self, pen: bmp.bmg.Pen) -> None:
        """Задание пера."""
        assert isinstance(pen, bmp.bmg.Pen)
        op = bmp.SetPenOp.create(pen)
        self.ops.append(op)

    def set_brush(self, brush: bmp.bmg.Brush) -> None:
        """Задание кисти."""
        assert isinstance(brush, bmp.bmg.Brush)
        op = bmp.SetBrushOp.create(brush)
        self.ops.append(op)

    def set_font(self, font: bmp.bmg.Font) -> None:
        """Задание шрифта."""
        assert isinstance(font, bmp.bmg.Font)
        op = bmp.SetFontOp.create(font)
        self.ops.append(op)

    def set_antialising(self, is_antialiasing: bool = True) -> None:
        """Задание сглаживания."""
        assert isinstance(is_antialiasing, bool)
        op = bmp.SetAntialiasingOp.create(is_antialiasing)
        self.ops.append(op)

    def draw_point(self, pt: bmp.bmg.Point) -> None:
        """Вывод точки с целочисленными координатами."""
        assert isinstance(pt, bmp.bmg.Point)
        op = bmp.DrawPointOp.create(pt)
        self.ops.append(op)

    def draw_point_2(self, x: int, y: int) -> None:
        """Вывод точки с целочисленными координатами 2."""
        assert isinstance(x, int)
        assert isinstance(y, int)
        pt = bmg.Point.create(x, y)
        op = bmp.DrawPointOp.create(pt)
        self.ops.append(op)

    def draw_pointf(self, pt: bmp.bmg.PointF) -> None:
        """Вывод точки с дробными координатами."""
        assert isinstance(pt, bmg.PointF)
        op = bmp.DrawPointfOp.create(pt)
        self.ops.append(op)

    def draw_pointf_2(self, x: float, y: float) -> None:
        """Вывод точки с дробными координатами 2."""
        assert isinstance(x, float)
        assert isinstance(y, float)
        pt = bmg.PointF.create(x, y)
        op = bmp.DrawPointfOp(pt)
        self.ops.append(op)

    def draw_line(self, line: bmp.bmg.Line) -> None:
        """Вывод линии."""
        assert isinstance(line, bmp.bmg.Line)
        op = bmp.DrawLineOp.create(line)
        self.ops.append(op)

    def draw_line_2(self, pt_1: bmp.bmg.Point, pt_2: bmp.bmg.Point) -> None:
        """Вывод линии (2 вариант)."""
        assert isinstance(pt_1, bmg.Point)
        assert isinstance(pt_2, bmg.Point)
        op = bmp.DrawLineOp.create2(pt_1, pt_2)
        self.ops.append(op)

    def draw_line_3(self, x_1: int, y_1: int, x_2: int, y_2: int) -> None:
        """Вывод линии (3 вариант)."""
        assert isinstance(x_1, int)
        assert isinstance(y_1, int)
        assert isinstance(x_2, int)
        assert isinstance(y_2, int)
        op = bmp.DrawLineOp.create(x_1, y_1, x_2, y_2)
        self.ops.append(op)

    def draw_linef(self, line: bmp.bmg.LineF) -> None:
        """Рисование линии."""
        assert isinstance(line, bmp.bmg.LineF)
        pass

    def draw_linef_2(self, pt_1: bmp.bmg.PointF, pt_2: bmp.bmg.PointF) -> None:
        """Рисование линии 2."""
        assert isinstance(pt_1, bmp.bmg.PointF)
        assert isinstance(pt_2, bmp.bmg.PointF)
        pass

    def draw_linef_3(self, x_1: float, y_1: float, x_2: float, y_2: float) -> None:
        """Рисование линии 3."""
        assert isinstance(x_1, float)
        assert isinstance(y_1, float)
        assert isinstance(x_2, float)
        assert isinstance(y_2, float)
        pass

    def draw_polyline(self):
        """."""
        pass

    def draw_polylinef(self):
        """."""
        pass

    def draw_arc(self):
        """."""
        pass

    def draw_arcf(self):
        """."""
        pass

    def draw_rect(self, rect: bmp.bmg.Rect) -> None:
        """Вывод прямоугольника."""
        assert isinstance(rect, bmp.bmg.Rect)
        pass

    def draw_rect_2(self, left_top: bmp.bmg.Point, size: bmp.bmg.Size) -> None:
        """Вывод прямоугольника 2."""
        assert isinstance(left_top, bmp.bmg.Point)
        assert isinstance(size, bmp.bmg.Size)
        pass

    def draw_rect_3(self, left: int, top: int, width: int,
                    height: int) -> None:
        """Вывод прямоугольника 3."""
        assert isinstance(left, int)
        assert isinstance(top, int)
        assert isinstance(width, int)
        assert isinstance(height, int)
        pass

    def draw_rects(self, rects: list) -> None:
        """Вывод прямоугольников с целочисленными координатами."""
        assert isinstance(rects, list)
        op = bmp.DrawRectsOp(rects)
        self.ops.append(op)

    def draw_rectf(self, rect: bmp.bmg.RectF) -> None:
        """Вывод прямоугольника с дробными координатами."""
        assert isinstance(rect, bmp.bmg.RectF)
        op = bmp.DrawRectfOp.create(rect)
        self.ops.append(op)

    def draw_rectf_2(self, left_top: bmp.bmg.PointF, size: bmp.bmg.SizeF) -> None:
        """Вывод прямоугольника с дробными координатами 2."""
        assert isinstance(left_top, bmp.bmg.PointF)
        assert isinstance(size, bmp.bmg.SizeF)
        op = bmp.DrawRectfOp.create2(left_top, size)
        self.ops.append(op)

    def draw_rectf_3(self, left: float, top: float, width: float,
                     height: float) -> None:
        """Вывод прямоугольника с дробными координатами 3."""
        assert isinstance(left, float)
        assert isinstance(top, float)
        assert isinstance(width, float)
        assert isinstance(height, float)
        op = bmp.DrawRectfOp.create2(left, top, width, height)
        self.ops.append(op)

    def draw_rectsf(self, rects: list) -> None:
        """Вывод прямоугольников с дробными координатами."""
        assert isinstance(rects, list)
        op = DrawRectsfOp.create(rects)
        self.ops.append(op)

    def draw_round_rect(self, rect: bmp.bmg.RoundRect) -> None:
        """Вывод прямоугольника с целочисленными координатами со сглаженными углами."""
        assert isinstance(rect, bmg.RoundRect)
        pass

    def draw_round_rects(self, rects: list) -> None:
        """Вывод прямоугольников с целочисленными координатами со сглаженными углами."""
        assert isinstance(rects, list)
        pass

    def draw_round_rectf(self, rect: bmp.bmg.RoundRectF) -> None:
        """Вывод прямоугольника с дробными координатами со сглаженными углами."""
        assert isinstance(rect, bmg.RoundRectF)
        pass

    def draw_round_rectsf(self, rects) -> None:
        """Вывод прямоугольника с дробными координатами со сглаженными углами."""
        assert isinstance(rects, list)
        pass

    def draw_ellipse(self, rect: bmp.bmg.Rect) -> None:
        """Вывод эллипса с целочисленными координатами."""
        assert isinstance(rect, bmp.bmg.Rect)
        pass

    def draw_ellipses(self, rects) -> None:
        """Вывод эллипсов с целочисленными координатами."""
        pass

    def draw_ellipsef(self, rect) -> None:
        """Вывод эллипса с дробными координатами."""
        assert isinstance(rect, bmg.RectF)
        pass

    def draw_ellipsesf(self, rects) -> None:
        """Вывод эллипсов с дробными координатами."""
        pass

    def draw_image(self, path: str) -> None:
        """Вывод изображения."""
        assert isinstance(path, str)
        pass

    def draw_text(self, text: str) -> None:
        """Вывод текста."""
        assert isinstance(text, str)
        pass

    def check_byte_array(self) -> bool:
        """Проверка массива байтов для инициализации."""
        pass

    def to_byte_array(self) -> bytearray:
        """Получение в виде массива байтов."""
        return draw_ops_to_byte_array(self.ops)

    def from_byte_array(self, byte_array: bytearray) -> None:
        """Инициализация из массива байтов."""
        pass

    def is_op_empty(self) -> bool:
        """Получение признака отстуствия операций."""
        return len(self.ops) == 0

    def add_op(self, op) -> None:
        """Добавление графической операции."""
        self.ops.append(op)

    def get_op_count(self) -> None:
        """Получение количества операций."""
        return len(self.ops)

    def clear_ops(self) -> None:
        """Очистка операций."""
        self.ops.clear()


class TestPainter(unittest.TestCase):
    """Тестирование класса Painter."""

    def test_save_state(self):
        """Тест функции save_state."""
        painter = Painter()
        painter.save_state()
        self.assertFalse(painter.is_op_empty())
        self.assertEqual(painter.get_op_count(), 1)

    def test_restore_state(self):
        """Тест функции restore_state."""
        painter = Painter()
        painter.restore_state()

    def test_set_clip_rect(self):
        """Тест функции set_clip_rect."""
        painter = Painter()
        rect = bmp.bmg.Rect.create_2(0, 0, 100, 100)
        painter.set_clip_rect(rect)

    def test_transform_translate(self):
        """Тест функции transform_translate."""
        painter = Painter()
        painter.transform_translate(0.0, 0.0)

    def test_transform_rotate(self):
        """Тест функции transform_rotate."""
        painter = Painter()
        painter.transform_rotate(45.0)

    def test_transform_scale(self):
        """Тест функции transform_scale."""
        painter = Painter()
        painter.transform_scale(2.0, 2.0)

    def test_set_pen(self):
        """Тест функции set_pen."""
        painter = Painter()
        pen = bmp.bmg.Pen()
        painter.set_pen(pen)

    def test_set_brush(self):
        """Тест функции set_brush."""
        painter = Painter()
        brush = bmp.bmg.Brush()
        painter.set_brush(brush)

    def test_set_font(self):
        painter = Painter()
        font = bmp.bmg.Font()

    def test_set_antialiasing(self):
        painter = Painter()

    def test_draw_point(self):
        painter = Painter()
        pt = bmp.bmg.Point.create(100, 100)

    def test_draw_point_2(self):
        painter = Painter()
        x = y = 100

    def test_draw_points(self):
        painter = Painter()

    def test_draw_pointf(self):
        painter = Painter()

    def test_draw_pointf_2(self):
        painter = Painter()
        x = y = 100.0

    def test_draw_pointsf(self):
        painter = Painter()

    def test_draw_line(self):
        painter = Painter()

    def test_draw_line_2(self):
        painter = Painter()

    def test_draw_line_3(self):
        painter = Painter()

    def test_draw_lines(self):
        painter = Painter()

    def test_draw_linef(self):
        painter = Painter()

    def test_draw_linef_2(self):
        painter = Painter()

    def test_draw_linef_3(self):
        painter = Painter()

    def test_draw_linesf(self):
        painter = Painter()

    def test_draw_rect(self):
        painter = Painter()

    def test_draw_rects(self):
        painter = Painter()

    def test_draw_rectf(self):
        painter = Painter()

    def test_draw_rectsf(self):
        painter = Painter()

    def test_draw_round_rect(self):
        painter = Painter()

    def test_draw_round_rects(self):
        painter = Painter()

    def test_draw_round_rectf(self):
        painter = Painter()

    def test_draw_round_rectsf(self):
        painter = Painter()

    def test_draw_ellipse(self):
        painter = Painter()

    def test_draw_ellipses(self):
        painter = Painter()

    def test_draw_ellipsef(self):
        painter = Painter()

    def test_draw_ellipsesf(self):
        painter = Painter()

    def test_draw_polygon(self):
        """Тест функции draw_polygon."""
        painter = Painter()

    def test_draw_polygonf(self):
        """Тест функции draw_image."""
        painter = Painter()

    def test_draw_image(self):
        """Тест функции draw_image."""
        painter = Painter()
        path = ''

    def test_draw_text(self):
        """Тест функции draw_text."""
        painter = Painter()
        text = "123"


# Вызывается при загрузке модуля главным
if __name__ == "__main__":
    unittest.main()
