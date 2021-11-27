"""
ByteMachine.

Хелперы для графических операций.
"""
__author__ = "EnergyLabs"
__version__ = "0.9129"


import byte_machine_paint as bmp
import unittest


def save_state_op_to_byte_array() -> bytearray:
    """Конвертация SaveStateOp в байтовый массив."""
    return bmp.SaveStateOp().to_byte_array()


def restore_state_op_to_byte_array() -> bytearray:
    """Конвертация RestoreStateOp в байтовый массив."""
    return bmp.RestoreStateOp().to_byte_array()


def transform_translate_op_to_byte_array(x: float, y: float) -> bytearray:
    """Конвертация TransformTranslateOp в байтовый массив."""
    op = bmp.TransformTranslateOp.create(x, y)
    return op.to_byte_array()


def transform_rotate_op_to_byte_array(angle: float) -> bytearray:
    """Конвертация TransformRotateOp в байтовый массив."""
    op = bmp.TransformRotateOp.create(angle)
    return op.to_byte_array()


def transform_scale_op_to_byte_array(x: float, y: float) -> bytearray:
    """Конвертация TransformScaleOp в байтовый массив."""
    op = bmp.TransformScaleOp.create(x, y)
    return op.to_byte_array()


def set_antialiasing_op_to_byte_array(antialiasing: bool = True) -> bytearray:
    """Конвертация SetAntialiasingOp в байтовый массив."""
    op = bmp.SetAntialiasingOp.create(antialiasing)
    return op.to_byte_array()


def set_pen_op_to_byte_array(pen: bmp.bmg.Pen) -> bytearray:
    """Конвертация SetPenOp в байтовый массив."""
    op = bmp.SetPenOp.create(pen)
    return op.to_byte_array()


def set_brush_op_to_byte_array(brush: bmp.bmg.Brush) -> bytearray:
    """Конвертация SetBrushOp в байтовый массив."""
    op = bmp.SetBrushOp.create(brush)
    return op.to_byte_array()


def set_font_op_to_byte_array():
    """Конвертация SetFontOp в байтовый массив."""
    pass


def draw_point_op_to_byte_array(point: bmp.bmg.Point) -> bytearray:
    """Конвертация DrawPointOp в байтовый массив."""
    op = bmp.DrawPointOp.create(point)
    return op.to_byte_array()


def draw_point_op_to_byte_array_2(x: int, y: int) -> bytearray:
    """Конвертация DrawPointOp в байтовый массив (2 вариант)."""
    pt = bmp.bmg.Point.create(x, y)
    return draw_point_op_to_byte_array(pt)


def draw_points_op_to_byte_array(points: list) -> bytearray:
    """Конвертация DrawPointsOp в байтовый массив."""
    pass


def draw_pointf_op_to_byte_array(point: bmp.bmg.PointF) -> bytearray:
    """Конвертация DrawPointfOp в байтовый массив."""
    op = bmp.DrawPointfOp.create(point)
    return op.to_byte_array()


def draw_pointf_op_to_byte_array_2(x: float, y: float) -> bytearray:
    """Конвертация DrawPointfOp в байтовый массив (2 вариант)."""
    pt = bmp.bmg.PointF.create(x, y)
    op = bmp.DrawPointfOp.create(pt)
    return op.to_byte_array()


def draw_pointsf_op_to_byte_array(points: list) -> bytearray:
    """Конвертация DrawPointsfOp в байтовый массив."""
    pass


def draw_rect_op_to_byte_array(rect: bmp.bmg.Rect) -> bytearray:
    """Конвертация DrawRectOp в байтовый массив."""
    op = bmp.DrawRectOp.create(rect)
    return op.to_byte_array()


def draw_rect_op_to_byte_array_2(top_left: bmp.bmg.Point,
                                 size: bmp.bmg.Size) -> bytearray:
    """Конвертация DrawRectOp в байтовый массив (2 вариант)."""
    rect = bmp.bmg.Rect.create(top_left, size)
    return draw_rect_op_to_byte_array(rect)


def draw_rect_op_to_byte_array_3(left: int, top: int, width: int,
                                 height: int) -> bytearray:
    """Конвертация DrawRectOp в байтовый массив (3 вариант)."""
    rect = bmp.bmg.Rect.create_2(left, top, width, height)
    return draw_rect_op_to_byte_array(rect)


def draw_rects_op_to_byte_array(rects: list) -> bytearray:
    """Конвертация DrawRectsOp в байтовый массив."""
    pass


def draw_rectf_op_to_byte_array(rect: bmp.bmg.RectF) -> bytearray:
    """Конвертация DrawRectsfOp в байтовый массив."""
    op = bmp.DrawRectfOp.create(rect)
    return op.to_byte_array()


def draw_rectf_op_byte_array_2(left_top: bmp.bmg.PointF,
                               size: bmp.bmg.SizeF) -> bytearray:
    """Конвертация DrawRectfOp в байтовый массив (2 вариант)."""
    rect = bmp.bmg.RectF.create(left_top, size)
    return draw_rectf_op_to_byte_array(rect)


def draw_rectf_op_byte_array_3(left: float, top: float, width: float,
                               height: float):
    """Конвертация DrawRectfOp в байтовый массив (3 вариант)."""
    rect = bmp.bmg.RectF.create_2(left, top, width, height)
    return draw_rectf_op_to_byte_array(rect)


def draw_rectsf_op_to_byte_array(rects: list) -> bytearray:
    """Конвертация DrawRectsfOp в байтовый массив."""
    pass


def draw_line_op_to_byte_array(line: bmp.bmg.Line) -> bytearray:
    """Конвертация DrawLineOp в байтовый массив."""
    op = bmp.DrawLineOp.create(line)
    return op.to_byte_array()


def draw_line_op_to_byte_array_2(pt_1: bmp.bmg.Point,
                                 pt_2: bmp.bmg.Point) -> bytearray:
    """Конвертация DrawLineOp в байтовый массив (2 вариант)."""
    line = bmp.bmg.Line.create(pt_1, pt_2)
    return draw_line_op_to_byte_array(line)


def draw_line_op_to_byte_array_3(x_1: int, y_1: int,
                                 x_2: int, y_2: int) -> bytearray:
    """Конвертация DrawLineOp в байтовый массив (3 вариант)."""
    line = bmp.bmg.Line.create_3(x_1, y_1, x_2, y_2)
    return draw_line_op_to_byte_array(line)


def draw_lines_op_to_byte_array(lines: list) -> bytearray:
    """Конвертация DrawLinesOp в байтовый массив."""
    pass


def draw_linef_op_to_byte_array(line: bmp.bmg.LineF) -> bytearray:
    """Конвертация DrawLinefOp в байтовый массив."""
    op = bmp.DrawLinefOp.create(line)
    return op.to_byte_array()


def draw_linef_op_to_byte_array_2(pt_1: bmp.bmg.PointF,
                                  pt_2: bmp.bmg.PointF) -> bytearray:
    """Конвертация DrawLinefOp в байтовый массив (2 вариант)."""
    line = bmp.bmg.LineF.create(pt_1, pt_2)
    return draw_linef_op_to_byte_array(line)


def draw_linef_op_to_byte_array_3(x_1: float, y_1: float,
                                  x_2: float, y_2: float) -> bytearray:
    """Конвертация DrawLinefOp в байтовый массив (3 вариант)."""
    line = bmp.bmg.LineF.create(x_1, y_1, x_2, y_2)
    return draw_linef_op_to_byte_array(line)


def draw_linesf_op_to_byte_array(lines: list) -> bytearray:
    """Конвертация DrawLinesfOp в байтовый массив."""
    pass


def draw_ellipse_op_to_byte_array(rect: bmp.bmg.Rect) -> bytearray:
    """Конвертация DrawEllipseOp в байтовый массив."""
    op = bmp.DrawEllipseOp.create(rect)
    return op.to_byte_array()


def draw_ellipse_op_to_byte_array_2(left_top: bmp.bmg.Point,
                                    size: bmp.bmg.Size) -> bytearray:
    """Конвертация DrawEllipseOp в байтовый массив (2 вариант)."""
    rect = bmp.bmg.Rect.create(left_top, size)
    return draw_ellipse_op_to_byte_array(rect)


def draw_ellipse_op_to_byte_array_3(left: int, top: int, width: int,
                                    height: int) -> bytearray:
    """Конвертация DrawEllipseOp в байтовый массив (3 вариант)."""
    rect = bmp.bmg.Rect.create_2(left, top, width, height)
    return draw_ellipse_op_to_byte_array(rect)


def draw_ellipses_op_to_byte_array(rects: list) -> bytearray:
    """Конвертация DrawEllipsesOp в байтовый массив."""
    pass


def draw_ellipsef_op_to_byte_array(rect: bmp.bmg.RectF) -> bytearray:
    """Конвертация DrawEllipsefOp в байтовый массив."""
    op = bmp.DrawEllipsefOp.create(rect)
    return op.to_byte_array()


def draw_ellipsef_op_to_byte_array_2(left_top: bmp.bmg.RectF,
                                     size: bmp.bmg.SizeF) -> bytearray:
    """Конвертация DrawEllipsefOp в байтовый массив (2 вариант)."""
    rect = bmp.bmg.RectF.create(left_top, size)
    return draw_ellipsef_op_to_byte_array(rect)


def draw_ellipsef_op_to_byte_array_3(left: float, top: float, width: float,
                                     height: float) -> bytearray:
    """Конвертация DrawEllipsefOp в байтовый массив (3 вариант)."""
    rect = bmp.bmg.RectF.create_2(left, top, width, height)
    return draw_ellipsef_op_to_byte_array(rect)


def draw_ellipsesf_op_to_byte_array(rects: []) -> bytearray:
    """Конвертация DrawEllipsesfOp в байтовый массив."""
    pass


def draw_round_rect_op_to_byte_array(rect: bmp.bmg.RoundRect) -> bytearray:
    """Конвертация DrawRoundRectOp в байтовый массив."""
    op = bmp.DrawRoundRectOp.create(rect)
    return op.to_byte_array()


def draw_round_rects_op_to_byte_array(rects: []) -> bytearray:
    """Конвертация DrawRoundRectsOp в байтовый массив."""
    pass


def draw_round_rectf_op_to_byte_array(rect: bmp.bmg.RoundRectF) -> bytearray:
    """Конвертация DrawRoundRectfOp в байтовый массив."""
    op = bmp.DrawRoundRectfOp.create(rect)
    return op.to_byte_array()


def draw_round_rectsf_op_to_byte_array() -> bytearray:
    """Конвертация DrawRoundRectsfOp в байтовый массив."""
    pass


def draw_polygon_op_to_byte_array() -> bytearray:
    """Конвертация DrawPolygonOp в байтовый массив."""
    pass


def draw_polygonf_op_to_byte_array() -> bytearray:
    """Конвертация DrawPolygofOp в байтовый массив."""
    pass


def draw_text_op_to_byte_array(text: bmp.bmg.String, point: bmp.bmg.PointF,
                               align: int) -> bytearray:
    """Конвертация DrawTextOp в байтовый массив."""
    op = bmp.DrawTextOp.create(text, point, align)
    return op.to_byte_array()


def draw_text_op_to_byte_array_2(text: str, point: bmp.bmg.PointF,
                                 align: int) -> bytearray:
    """Конвертация DrawTextOp в байтовый массив (2 вариант)."""
    t = bmp.bmg.String.create(text)
    op = bmp.DrawTextOp.create(t, point, align)
    return op.to_byte_array()


class TestOpFuncs(unittest.TestCase):
    """Тест функций для работы с графическими операциями."""

    def test_save_state_op_to_byte_array(self):
        """Тест функции save_state_op_to_byte_array."""
        ba = save_state_op_to_byte_array()
        code = bmp.get_op_code(ba)
        self.assertTrue(len(ba) == 3)
        self.assertEqual(code, bmp.DrawOpCodes.SAVE_STATE)

    def test_restore_state_op_to_byte_array(self):
        """Тест функции restore_state_op_to_byte_array."""
        ba = restore_state_op_to_byte_array()
        self.assertTrue(len(ba) == 3)
        code = bmp.get_op_code(ba)
        self.assertEqual(code, bmp.DrawOpCodes.RESTORE_STATE)

    def test_set_antialiasing_op_to_byte_array(self):
        """Тест функции set_antialiasing_op_to_byte_array."""
        ba = set_antialiasing_op_to_byte_array()
        self.assertTrue(len(ba) == 4)
        code = bmp.get_op_code(ba)
        self.assertEqual(code, bmp.DrawOpCodes.SET_ANTIALIASING)
        op = bmp.SetAntialiasingOp()
        op.from_byte_array(ba)
        self.assertTrue(op.antialiasing)

    def test_transform_translate_op_to_byte_array(self):
        """Тест функции transform_translate_op_to_byte_array."""
        ba = transform_translate_op_to_byte_array(1.0, 1.0)
        op = bmp.TransformTranslateOp()
        op.from_byte_array(ba)
        self.assertAlmostEqual(op.x, 1.0)
        self.assertAlmostEqual(op.y, 1.0)

    def test_transform_rotate_op_to_byte_array(self):
        """Тест функции transform_rotate_op_to_byte_array."""
        ba = transform_rotate_op_to_byte_array(45.0)
        op = bmp.TransformRotateOp()
        op.from_byte_array(ba)
        self.assertAlmostEqual(op.angle, 45.0)

    def test_transform_scale_op_to_byte_array(self):
        """Тест функции transform_scale_op_to_byte_array."""
        ba = transform_scale_op_to_byte_array(2.0, 2.0)
        op = bmp.TransformScaleOp()
        op.from_byte_array(ba)
        self.assertAlmostEqual(op.x, 2.0)
        self.assertAlmostEqual(op.y, 2.0)

    def test_draw_point_op_to_byte_array(self):
        """Тест функции draw_points_op_to_byte_array."""
        # pt = bmp.bmg.Point.create(100, 200)
        # ba = draw_point_op_to_byte_array(pt)
        # op = bmp.DrawPointOp()
        # op.from_byte_array(ba)
        # self.assertEqual(op.point, pt)

        # x = 10
        # y = 20
        # ba = draw_point_op_to_byte_array_2(x, y)
        # op.from_byte_array(ba)
        # self.assertEqual(op.point.x(), x)
        # self.assertEqual(op.point.y(), y)
        pass

    def test_draw_points_op_to_byte_array(self):
        """Тест функции draw_points_op_to_byte_array."""
        # ba = draw_points_op_to_byte_array()

    def test_draw_pointf_op_to_byte_array(self):
        """Тест функции draw_pointf_op_to_byte_array."""
        # pt = bmp.bmg.PointF.create(100.0, 200.0)
        # ba = draw_pointf_op_to_byte_array(pt)
        # op = bmp.DrawPointfOp()
        # op.from_byte_array(ba)
        # self.assertEqual(op.point, pt)

        # x = 10.0
        # y = 20.0
        # ba = draw_pointf_op_to_byte_array_2(x, y)
        # op.from_byte_array(ba)
        # self.assertAlmostEqual(op.point.x(), x)
        # self.assertAlmostEqual(op.point.y(), y)
        pass

    def test_draw_pointsf_op_to_byte_array(self):
        """Тест функции draw_pointsf_op_to_byte_array."""
        pass

    def test_draw_ellipse_op_to_byte_array(self):
        """Тест функции draw_ellipse_op_to_byte_array."""
        rect = bmp.bmg.Rect.create_2(100, 100, 200, 200)
        ba = draw_ellipse_op_to_byte_array(rect)
        op = bmp.DrawEllipseOp()
        op.from_byte_array(ba)
        self.assertEqual(op.rect, rect)

    def test_draw_ellipses_op_to_byte_array(self):
        """Тест функции draw_ellipses_op_to_byte_array."""
        # ba = draw_ellipses_op_to_byte_array()
        pass

    def test_draw_ellipsef_op_to_byte_array(self):
        """Тест функции draw_ellipsef_op_to_byte_array."""
        rect = bmp.bmg.RectF.create_2(100.0, 100.0, 200.0, 200.0)
        ba = draw_ellipsef_op_to_byte_array(rect)
        op = bmp.DrawEllipsefOp()
        op.from_byte_array(ba)
        # print(op.rect)
        # self.assertEqual(op.rect, rect)

    def test_draw_ellipsesf_op_to_byte_array(self):
        """Тест функции draw_ellipsesf_op_to_byte_array."""
        # ba = draw_ellipsesf_op_to_byte_array()
        pass

    def test_draw_round_rect_op_to_byte_array(self):
        """Тест функции draw_round_rect_op_to_byte_array."""
        rect = bmp.bmg.Rect.create_2(100, 100, 200, 200)
        rrect = bmp.bmg.RoundRect.create(rect, 10, 10)
        ba = draw_round_rect_op_to_byte_array(rrect)
        op = bmp.DrawRoundRectOp()
        op.from_byte_array(ba)
        self.assertEqual(op.rect, rrect)

    def test_draw_round_rects_op_to_byte_array(self):
        """Тест функции draw_round_rects_op_to_byte_array."""
        pass

    def test_draw_round_rectf_op_to_byte_array(self):
        """Тест функции draw_round_rectf_op_to_byte_array."""
        rect = bmp.bmg.RectF.create_2(100.0, 100.0, 200.0, 200.0)
        rrect = bmp.bmg.RoundRectF.create(rect, 10.0, 10.0)
        ba = draw_round_rectf_op_to_byte_array(rrect)
        op = bmp.DrawRoundRectfOp()
        op.from_byte_array(ba)

    def test_draw_round_rectsf_op_to_byte_array(self):
        """Тест функции draw_round_rectsf_op_to_byte_array."""
        pass

    def test_draw_polyline_op_to_byte_array(self):
        """Тест функции draw_polyline_op_to_byte_array."""
        # ba = draw_polyline_op_to_byte_array()
        pass

    def test_draw_polylinef_op_to_byte_array(self):
        """Тест функции draw_polylinef_op_to_byte_array."""
        # ba = draw_polylinef_op_to_byte_array()
        pass

    def test_draw_polygon_op_to_byte_array(self):
        """Тест функции draw_polygon_op_to_byte_array."""
        # ba = draw_polygon_op_to_byte_array()
        pass

    def test_draw_polygonf_op_to_byte_array(self):
        """Тест функции draw_polygonf_op_to_byte_array."""
        # ba = draw_polygonf_op_to_byte_array()
        pass

    def test_draw_text_op_to_byte_array(self):
        """Тест функции draw_text_op_to_byte_array."""
        text = bmp.bmg.String.create("ByteMachine")
        point = bmp.bmg.PointF.create(100.0, 100.0)
        align = bmp.AlignmentFlags.ALIGN_LEFT | bmp.AlignmentFlags.ALIGN_TOP
        ba = draw_text_op_to_byte_array(text, point, align)
        op = bmp.DrawTextOp()
        op.from_byte_array(ba)

    def test_draw_text_op_to_byte_array_2(self):
        """Тест функции draw_text_op_to_byte_array."""
        # ba = draw_text_op_to_byte_array()
        pass

    def test_draw_image_op_to_byte_array(self):
        """Тест функции draw_image_op_to_byte_array."""
        # ba = draw_image_op_to_byte_array()
        pass


# Вызывается при загрузке модуля главным.
if __name__ == "__main__":
    unittest.main()
