#!/usr/bin/python3
''' Simple roulette computation and visualization '''
from math import pi, cos, sin
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

def fit(from_box, to_box):
    (x0_from, y0_from, x1_from, y1_from) = from_box
    (x0_to, y0_to, x1_to, y1_to) = to_box
    (w_from, h_from) = (x1_from-x0_from, y1_from-y0_from)
    (w_to, h_to) = (x1_to-x0_to, y1_to-y0_to)
    (a_from, a_to) = (w_from/h_from, w_to/h_to)

    if a_from > a_to:
        scale = w_to/w_from
        trans = (x0_to, y0_to + (h_to - scale*h_from)/2)
    else:
        scale = h_to/h_from
        trans = (x0_to + (w_to - scale*w_from)/2)

    #return scale, trans
    return lambda p: (trans[0] + scale*(p[0]-x0_from), trans[1] + scale*(p[1]-y0_from))


def draw_cycloidal(points, pixel_size):
    ''' Draw our nice cycloid '''
    im = Image.new('RGB', (pixel_size, pixel_size), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    (maxx, maxy) = map(min, zip(*points))
    (minx, miny) = map(max, zip(*points))

    fit_func = fit((minx, miny, maxx, maxy), (0, 255, 0, 255))
    #scale = pixel_size/(maxx-minx)
    #offset = (maxx-minx)/2*scale

    #scale_point = lambda p: [x*scale + offset for x in p]
    p0 = scale_point(points[0])
    porig = p0
    for p1 in points[1:]:
        draw.line(p0 + scale_point(p1), fill=(0, 0, 0), width=2)
        p0 = scale_point(p1)
    draw.line(p0 + porig, fill=(0, 0, 0), width=2)
    im.show()

e = Hypotrochoid(5, 3, 5)
v = e.compute(256)
draw_cycloidal(v, 768)
