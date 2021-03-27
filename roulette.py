#!/usr/bin/python3
''' Simple roulette computation and visualization '''
import argparse
from math import pi, cos, sin, copysign
from PIL import Image, ImageDraw

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

    def compute(self, nstep):
        ''' Returns nstep points corresponding to nstep evenly
            spaced angular steps '''
        raise NotImplementedError

class Hypotrochoid(Cycloidal):
    ''' Hypotrochoid '''
    def compute(self, nstep):
        points = list()
        for i in range(nstep):
            theta = 2*pi*self.r*i/nstep
            points.append((self.r*(self.k-1)*cos(theta) + self.d*cos((self.k-1)*theta), \
                           self.r*(self.k-1)*sin(theta) - self.d*sin((self.k-1)*theta),))
        return points

class Epitrochoid(Cycloidal):
    ''' Epitrochoids '''
    def compute(self, nstep):
        points = list()
        for i in range(nstep):
            theta = 2*pi*self.r*i/nstep
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
    def draw_line(p0, p1):
        raise NotImplementedError

    def show():
        raise NotImplementedError

class PilDrawEngine(DrawEngine):
    def __init__(self, canvas_box):
        self.canvas_box = canvas_box
        self.im = Image.new('RGB', (abs(canvas_box[1]-canvas_box[0]),\
                                    abs(canvas_box[3]-canvas_box[2])),
                            (255, 255, 255))
        self.draw = ImageDraw.Draw(self.im)

    def draw_line(self, p0, p1):
        self.draw.line(p0 + p1, fill=(0, 0, 0))

    def show(self):
        self.im.show()

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

def draw_cycloidal(points, pixel_size):
    ''' Draw our nice cycloid '''
    draw_engine = PilDrawEngine((0, pixel_size, 0, pixel_size))

    (maxx, maxy) = map(max, zip(*points))
    (minx, miny) = map(min, zip(*points))

    fit_func = fit_func_factory((minx, miny, maxx, maxy), (0, pixel_size, pixel_size, 0))

    p0 = fit_func(points[0])
    porig = p0
    for p1 in points[1:]:
        draw_engine.draw_line(p0, fit_func(p1))
        p0 = fit_func(p1)
    draw_engine.draw_line(p0, porig)
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
    _args = parser.parse_args()
    return _args


ARGS = parse_args()
if ARGS.type == "ht":
    draw_cycloidal(Hypotrochoid(ARGS.R, ARGS.r, ARGS.d).compute(ARGS.np), ARGS.size)
elif ARGS.type == "et":
    draw_cycloidal(Epitrochoid(ARGS.R, ARGS.r, ARGS.d).compute(ARGS.np), ARGS.size)
