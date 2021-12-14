"""
ByteMachine.

Генерация файла с графическими операциями.
"""
__author__ = "EnergyLabs"
__version__ = "0.9133"


import byte_machine_paint_helper as bmph


with open("F:/paint_ops.bin", "wb") as f:
    ba = bytearray()

    path = "C:/Users/pimen/Pictures/pribor.png"
    align = bmph.bmp.AlignFlags.create(bmph.bmp.HorzAlignFlags.CENTER,
                                       bmph.bmp.VertAlignFlags.CENTER)
    for i in range(20):
        for j in range(20):
            # Координаты
            x = 70 + 150.0 * i
            y = 70 + 150.0 * j

            # Вывод изображения
            point_image = bmph.bmp.bmg.PointF.create(x, y)
            ba += bmph.draw_image_op_to_byte_array_2(path, point_image, align)

            # Задание шрифта
            font = bmph.bmp.bmg.Font.create_2("Courier New", 18, True)
            ba += bmph.set_font_op_to_byte_array(font)

            # Вывод текста
            text = str(i) + ":" + str(j)
            point_text = bmph.bmp.bmg.PointF.create(x, y + 75)
            ba += bmph.draw_text_op_to_byte_array_2(text, point_text, align)

    f.write(ba)
