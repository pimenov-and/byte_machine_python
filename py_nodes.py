# coding: utf8
import math
import random


#----------------------------------------------------------------
# Функции для узлов на Python
#----------------------------------------------------------------

def py_in():
    ba = bytearray([0, 1, 2, 3])
    py_change(ba)
    return ba


def py_change(ba):
    # global s
    # s += 1.0

    # ops = []
    # ops += [TransformRotateOp.create(s)]
    
    return ba # + draw_ops_to_byte_list(ops)

    # c = Color()
    # c.from_byte_list(bl)

    # ops = []
    # pen = Pen.create(c, 1)
    # ops += [SetAntialiasingOp.create(True)]
    # ops += [TransformTranslateOp.create(100.0, 100.0)]
    # ops += [SetPenOp.create(pen)]
    # ops += [DrawLinefOp.create(LineF.create2(0.0, 0.0, 100.0, 100.0))]
    # return draw_ops_to_byte_list(ops)
    # return bl
        
        
# def py_change(l):
    # '''Функция для узла PyChange.'''
    # global pts
    
    # m = Mouse()
    # m.from_byte_list(l)
    # mpos = m.pos
    
    # if m.isLeftBtnDown:
        # pts.append(mpos)
        # if len(pts) > 1000:
            # del pts[0]
            
    # ops = []
    # ops += [SetPenOp.create(Pen.create(Color.get_orange(), 3.0))]
    # for i in range(0, len(pts) - 1, 2):
        # p = pts[i]
        # np = pts[i + 1]
        # ops += [DrawLineOp.create(Line.create(p, np))]
    
    # return ops_to_byte_list(ops)

# def py_change(l):
    # '''Функция для узла PyChange.'''
    # # r = byte_list_to_double(l)
    # m = Mouse()
    # m.from_byte_list(l)
    # x = m.pos.x
    # sc = x / 5

    # ts = x / 600.0
    # if ts < 0.1:
        # ts = 0.1
    # elif ts > 2.0:
        # ts = 2.0

    # global r, rc, a
    # if not m.isLeftBtnDown:
        # r += a
    # if m.isMiddleBtnDown and rc:
        # a = -a
        # rc = False
    # rc = not m.isMiddleBtnDown

    # ops = []
    # ops += [TransformScaleOp.create(ts, ts)]
    
    # Фон
    # ops += [SetPenOp.create(Pen.create(Color.get_black(), 1.0))]
    # ops += [SetBrushOp.create(Brush.create(Color.get_black()))]
    # ops += [DrawRectOp.create(Rect.create2(0, 0, 1700, 1100))]
    
    # # Звезды
    # ops += [SetPenOp.create(Pen.create(Color.get_white(), 1.0))]
    # random.seed(0)
    # for i in range(sc):
        # x = random.randint(0, 1700)
        # y = random.randint(0, 1100)
        # ops += [DrawRectOp.create(Rect.create2(x, y, 1, 1))]
    
    # # Солнце
    # ops += [SetAntialiasingOp.create(True)]
    # ops += [SetPenOp.create(Pen.create(Color.get_yellow(), 1.0))]
    # ops += [SetBrushOp.create(Brush.create(Color.get_yellow()))]
    # ops += [TransformTranslateOp.create(600.0, 400.0)]
    # ops += [DrawEllipsefOp.create(RectF.create2(-20.0, -20.0, 40.0, 40.0))]
    
    # # Земля
    # ops += [TransformRotateOp.create(r)]
    # ops += [SetPenOp.create(Pen.create(Color.get_blue(), 1.0))]
    # ops += [SetBrushOp.create(Brush.create(Color.create(66, 145, 255)))]
    # ops += [DrawEllipsefOp.create(RectF.create2(190.0, 190.0, 16.0, 16.0))]
    
    # # Луна
    # ops += [TransformTranslateOp.create(198.0, 198.0)]
    # ops += [SetPenOp.create(Pen.create(Color.get_white(), 1.0))]
    # ops += [SetBrushOp.create(Brush.create(Color.get_white()))]
    # ops += [TransformRotateOp.create(r * 3)]
    # ops += [DrawEllipsefOp.create(RectF.create2(20.0, 20.0, 8.0, 8.0))]
    # ops += [SetPenOp.create(Pen.create(Color.white(), 1.0))]
    # ops += [SetBrushOp.create(Brush.create(Color.get_white())]
    
    
    ##    # ops += [SetBrushOp.create(Brush.create(Color.get_black()))]
    ##    # ops += [DrawRectOp.create(Rect.create2(0, 0, 600, 600))]
    ##    # ops += [TransformScaleOp.create(r)]
    ##    ops += [SetAntialiasingOp.create(True)]
    ##    ops += [SetBrushOp.create(Brush.create(c))]
    ##    ops += [SetPenOp.create(Pen.create(Color.get_red(), 3.0))]
    ##    for i in range(90):
    ##        for j in range(90):
    ##            ops += [SaveStateOp()]
    ##            ops += [TransformTranslateOp.create(35.0 * i + 22, 35.0 * j + 34)]
    ##            # ops += [TransformRotateOp.create(r)]
    ##            ops += [DrawRectOp.create(Rect.create2(-10, -10, 20, 20))]
    ##            # ops += [TransformRotateOp.create(-r)]
    ##            # ops += [TransformTranslateOp.create(-(35.0 * i + 22), -(35.0 * j + 34))]
    ##            ops += [RestoreStateOp()]
            
    # return [] # ops_to_byte_list(ops)


def py_merge(ba1, ba2):
    """"Функция для узла PyMerge."""
    return ba1 + ba2


def py_out(l):
    '''Функция для узла PyOut.'''
    pass

pts = []

s = 0.0
state = True
