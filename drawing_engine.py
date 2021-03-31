#!/usr/bin/env python3
''' Lineus and PIL drawing engine '''
from math import copysign

class DrawEngine():
    ''' Drawing engine base class '''
    def draw_line(self, p0, p1=None):
        ''' Draw a line between p0 and p1 or between the current position and p0 '''
        raise NotImplementedError

    def set_pos(self, p):
        ''' Set current pen position '''
        raise NotImplementedError

    def show(self):
        ''' Display the drawing '''

class PilDrawEngine(DrawEngine):
    ''' Drawing engine based on Python Image Library '''
    def __init__(self, canvas_box):
        from PIL import Image, ImageDraw
        self.canvas_box = canvas_box
        self.im = Image.new('RGB', (abs(canvas_box[1]-canvas_box[0]),\
                                    abs(canvas_box[3]-canvas_box[2])),
                            (255, 255, 255))
        self.draw = ImageDraw.Draw(self.im)
        self.pos = (canvas_box[0], canvas_box[2])

    def set_pos(self, p):
        ''' Set current position '''
        self.pos = p

    def draw_line(self, p0, p1=None):
        ''' Draw a line between p0 and p1 or between the current position and p0 '''
        if p1 is None:
            self.draw.line(self.pos + p0, fill=(0, 0, 0))
            self.pos = p0
        else:
            self.draw.line(p0 + p1, fill=(0, 0, 0))
            self.pos = p1

    def show(self):
        ''' Show our canvas '''
        self.im.show()

class LineUsDrawEngine(DrawEngine):
    ''' Drawing engine based on Lineus python library '''
    LINEUS_HIGH_Z = 1000
    LINEUS_LOW_Z = 200
    LINEUS_CANVAS = (650, -1000, 1775, 1000)

    def __init__(self, bounds=LINEUS_CANVAS):
        from lineus import LineUs
        self.lineus = LineUs()
        if not self.lineus.connect():
            raise Exception("Can't connect to Line-us")

    def raise_stylus(self):
        ''' Raise lineus head '''
        self.lineus.g01(z=self.LINEUS_HIGH_Z)

    def lower_stylus(self):
        ''' lower lineus head '''
        self.lineus.g01(z=self.LINEUS_LOW_Z)

    def move(self, p):
        ''' Move lineus head in x, y plane. This might trace
            something or not, if the stylus is up or down '''
        # Round coordinates - seems the API has issues with
        # at least coordinates between -1 and 1
        s_p = [round(x, 0) for x in p]
        self.lineus.g01(*s_p)

    def set_pos(self, p):
        ''' Raise style, move head, lower stylus '''
        self.raise_stylus()
        self.move(p)
        self.lower_stylus()

    def reset_position(self):
        ''' Moves lineus back to its reset position '''
        self.lineus.send_gcode('G28')

    def draw_line(self, p0, p1=None):
        ''' Draw a line between p0 and p1 or between the current position and p0 '''
        if p1 is None:
            self.move(p0)
        else:
            self.raise_stylus()
            self.move(p0)
            self.lower_stylus()
            self.move(p1)

    def start_recording(self, slot):
        ''' Start move recording in the requested memory slot '''
        if not isinstance(slot, int) or slot < 1 or slot > 32:
            raise Exception("Incorrect slot number (must be int between 1 and 32)")
        self.lineus.send_gcode('M28', 'S'+str(slot))

    def stop_recording(self):
        ''' Stop recording - save file '''
        self.lineus.send_gcode('M29')

def fit_func_factory(from_box, to_box):
    ''' Return a function transforming coordinates to center
        a figure contained in from_box, when projecting it
        inside to_box, so that it takes as much space as possible
        while keeping its aspect ratio.
        Also, invert the x and y axis if needed '''
    (x0_from, y0_from, x1_from, y1_from) = from_box
    (x0_to, y0_to, x1_to, y1_to) = to_box
    (w_from, h_from) = (x1_from-x0_from, y1_from-y0_from)
    (w_to, h_to) = (x1_to-x0_to, y1_to-y0_to)
    (a_from, a_to) = (abs(w_from/h_from), abs(w_to/h_to))

    if a_from > a_to: # Landscape to portrait
        xscale = w_to/w_from
        yscale = copysign(xscale, h_to*h_from)
        trans = (x0_to, y0_to + (h_to - h_from*yscale)/2)
    else: # Portrait to landscape
        yscale = h_to/h_from
        xscale = copysign(yscale, w_to*w_from)
        trans = (x0_to + (w_to - w_from*xscale)/2, y0_to)

    return lambda p: (trans[0] + xscale*(p[0]-x0_from), trans[1] + yscale*(p[1]-y0_from))

def draw_continuous(points, canvas, engine):
    ''' Continuous drawing: lower pen on the first point then
        draw line between each point in sequence. '''
    engine_params = {"pil" : { \
                              'bounds' : canvas, \
                              'eng' : PilDrawEngine},
                     "lineus" : {'bounds' : LineUsDrawEngine.LINEUS_CANVAS, \
                              'eng' : LineUsDrawEngine}
                    }

    engine_param = engine_params[engine]
    draw_engine = engine_param['eng'](engine_param['bounds'])

    (maxx, maxy) = map(max, zip(*points))
    (minx, miny) = map(min, zip(*points))

    fit_func = fit_func_factory((minx, miny, maxx, maxy), engine_param['bounds'])

    p0 = fit_func(points[0])
    draw_engine.set_pos(p0)
    for p in points[1:]:
        draw_engine.draw_line(fit_func(p))
    draw_engine.draw_line(p0)
    draw_engine.show()
