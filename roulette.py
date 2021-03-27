#!/usr/bin/env python3
''' Simple roulette computation and visualization '''
import argparse
from math import pi, cos, sin, copysign

class Cycloidal():
    ''' Main class for our cycloids '''
    def __init__(self, R, r, d):
        if not isinstance(R, int):
            raise TypeError("R must be an integer to get a close curve")
        if not isinstance(r, int):
            raise TypeError("r must be an integer to get a close curve")
        self.R = R
        self.r = r
        self.d = d
        self.k = R/r

    def get_n_cusps(self):
        ''' Get number of cusps (sharp corners) '''
        if self.R < self.r:
            return 0
        if self.R % self.r == 0:
            return self.R/self.r
        return self.R

    def get_n_rotations(self):
        ''' Get number of rotations of the outer circle '''
        if self.R % self.r == 0:
            return 1
        if self.r % self.R == 0:
            return self.r/self.R
        return self.r

    def compute(self, nstep):
        ''' Returns nstep points corresponding to nstep evenly
            spaced angular steps '''
        raise NotImplementedError

class Hypotrochoid(Cycloidal):
    ''' Hypotrochoid '''
    def compute(self, nstep):
        points = list()
        n_rot = self.get_n_rotations()
        for i in range(nstep):
            theta = 2*pi*n_rot*i/nstep
            points.append((self.r*(self.k-1)*cos(theta) + self.d*cos((self.k-1)*theta), \
                           self.r*(self.k-1)*sin(theta) - self.d*sin((self.k-1)*theta),))
        return points

class Epitrochoid(Cycloidal):
    ''' Epitrochoid '''
    def compute(self, nstep):
        points = list()
        n_rot = self.get_n_rotations()
        for i in range(nstep):
            theta = 2*pi*n_rot*i/nstep
            points.append((self.r*(self.k+1)*cos(theta) - self.d*cos((self.k+1)*theta), \
                           self.r*(self.k+1)*sin(theta) - self.d*sin((self.k+1)*theta),))
        return points

class Hypocycloid(Hypotrochoid):
    ''' Hypocycloid = hypotrochoid with d = r '''
    def __init__(self, R, r):
        super().__init__(R, r, r)

class Epicycloid(Epitrochoid):
    ''' Epicycloid = epitrochoid with d = r '''
    def __init__(self, R, r):
        super().__init__(R, r, r)

class DrawEngine():
    ''' Drawing engine base class '''
    def draw_line(self, p0, p1=None):
        ''' Draw a line between p0 and p1 or between the current position and p0 '''
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
    LINEUS_LOW_Z = 400
    LINEUS_DEFAULT_POS = (1000, 1000, 1000)
    LINEUS_CANVAS = (650, -1000, 1775, 1000)

    def __init__(self, bounds=None):
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
        self.move(self.LINEUS_DEFAULT_POS)

    def draw_line(self, p0, p1=None):
        ''' Draw a line between p0 and p1 or between the current position and p0 '''
        if p1 is None:
            self.move(p0)
        else:
            self.raise_stylus()
            self.move(p0)
            self.lower_stylus()
            self.move(p1)

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

def draw_cycloidal(points, pixel_size, engine):
    ''' Draw our nice cycloid '''
    engine_params = {"pil" : { \
                              'bounds' : (0, pixel_size, pixel_size, 0), \
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

def parse_args():
    ''' Basic argument parser '''
    parser = argparse.ArgumentParser(description='Playing with cycloids')
    parser.add_argument('-R', '--R',
                        help='Circle 1 radius',
                        default=5,
                        type=int)
    parser.add_argument('-r', '--r',
                        help='Circle 2 radius',
                        default=3,
                        type=int)
    parser.add_argument('-d', '--d',
                        help='Distance of point from circle 2 center',
                        default=5.0,
                        type=float)
    parser.add_argument('-n', '--np',
                        help='number of points',
                        default=256,
                        type=int)
    parser.add_argument('-s', '--size',
                        help='size of canvas in pixels',
                        default=256,
                        type=int)
    parser.add_argument('-t', '--type',
                        help='type of cycloid',
                        default="ht",
                        type=str,
                        choices=("ht", "et"))
    parser.add_argument('-e', '--engine',
                        help='Drawing engine',
                        default="pil",
                        type=str,
                        choices=("pil", "lineus"))
    _args = parser.parse_args()
    return _args

ARGS = parse_args()
if ARGS.type == "ht":
    draw_cycloidal(Hypotrochoid(ARGS.R, ARGS.r, ARGS.d).compute(ARGS.np), ARGS.size, ARGS.engine)
elif ARGS.type == "et":
    draw_cycloidal(Epitrochoid(ARGS.R, ARGS.r, ARGS.d).compute(ARGS.np), ARGS.size, ARGS.engine)
