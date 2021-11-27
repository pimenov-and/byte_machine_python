"""
ByteMachine.

Генерация файла с графическими операциями.
"""
__author__ = "EnergyLabs"
__version__ = "0.9129"


import byte_machine_paint as bmp


def get_pen() -> bytearray:
    op = bmp.SetPenOp()
    op.pen.width = 8
    op.pen.color = bmp.bmg.Color.get_green()
    return op.to_byte_array()


def get_brush() -> bytearray:
    op = bmp.SetBrushOp()
    op.brush.color = bmp.bmg.Color.get_dark_red()
    return op.to_byte_array()


def get_line(x_1: int, y_1: int, x_2: int, y_2: int) -> bytearray:
    op = bmp.DrawLineOp.create_3(x_1, y_1, x_2, y_2)
    return op.to_byte_array()


def get_lines() -> bytearray:
    ba = bytearray()
    for i in range(-100, 100):
        ba += get_line(i * 40, -2000, i * 40 + 50, 2000)
    return ba


def get_rect(left: int, top: int, width: int, height: int) -> bytearray:
    ba = bytearray()
    op = bmp.DrawRectOp.create(bmp.bmg.Rect.create_2(left, top, width, height))
    ba += op.to_byte_array()
    return ba


def get_rects() -> bytearray:
    ba = bytearray()
    for i in range(100):
        for j in range(100):
            ba += get_rect(i * 30 + 10, j * 30 + 10, 20, 20)
    return ba


with open("F:/paint_ops.bin", "wb") as f:
    ba = bytearray()
    # print(get_pen())
    ba += get_pen()
    ba += get_brush()
    ba += get_rects()
    f.write(ba)
