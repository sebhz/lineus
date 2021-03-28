#!/usr/bin/env python3
''' Simple roulette computation '''
import argparse
from math import pi, cos, sin
import drawing_engine

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
        if self.d != self.r:
            return 0
        if self.r % self.R == 0:
            return 1
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
                        help='size of PIL square canvas side, in pixels',
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
CANVAS = (0, ARGS.size, ARGS.size, 0)
if ARGS.type == "ht":
    drawing_engine.draw_continuous(Hypotrochoid(ARGS.R, ARGS.r, ARGS.d).compute(ARGS.np), \
                                   CANVAS, \
                                   ARGS.engine)
elif ARGS.type == "et":
    drawing_engine.draw_continuous(Epitrochoid(ARGS.R, ARGS.r, ARGS.d).compute(ARGS.np), \
                                   CANVAS, \
                                   ARGS.engine)
