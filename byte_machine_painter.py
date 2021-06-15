# coding: utf8
'''
ByteMachine
Класс для вывода графики.
'''
import unittest
import byte_machine_paint_3 as bmp


class TestPainter(unittest.TestCase):
    '''
    Тестирование класса Painter.
    '''

    def test_save_state(self):
        painter = Painter()
        painter.save_state()
        self.assertFalse(painter.is_op_empty())
        self.assertEqual(painter.get_op_count(), 1)

    def test_restore_state(self):
        painter = Painter()
        painter.restore_state()

    def test_set_clip_rect(self):
        painter = Painter()
        rect = bmp.bmg.Rect.create2(0, 0, 100, 100)
        painter.set_clip_rect(rect)

    def test_transform_translate(self):
        painter = Painter()
        painter.transform_translate(0.0, 0.0)

    def test_transform_rotate(self):
        painter = Painter()
        painter.transform_rotate(45.0)

    def test_transform_scale(self):
        painter = Painter()
        painter.transform_scale(2.0, 2.0)

    def test_set_pen(self):
        painter = Painter()
        pen = bmp.bmg.Pen()
        painter.set_pen(pen)

    def test_set_brush(self):
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
        painter = Painter()

    def test_draw_polygonf(self):
        painter = Painter()

    def test_draw_image(self):
        painter = Painter()
        path = ''

    def test_draw_text(self):
        painter = Painter()
        text = '123'


# Вызывается при загрузке модуля главным
if __name__ == '__main__':
    unittest.main()
