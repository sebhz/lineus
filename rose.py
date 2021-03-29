#!/usr/bin/env python3
''' Rhodonea curves (roses) '''
import argparse
from math import pi, sin
import drawing_engine

class Rose():
    ''' Describe a rose '''
    def __init__(self, n, d):
        if not isinstance(n, int):
            raise TypeError("n must be an integer")
        if not isinstance(d, int):
            raise TypeError("d must be an integer")
        while (n % 2 == 0) and (d % 2 == 0):
            n = n/2
            d = d/2

        self.n = n
        self.d = d

    def get_n_rotations(self):
        ''' Get number of rotations needed to complete the rose '''
        if self.n % self.d == 0:
            return self.n/self.d
        if (self.n % 2 == 1) and (self.d % 2 == 1):
            return self.d/2
        return self.d

    def compute(self, nstep):
        ''' Compute rose points '''
        points = list()
        n_rot = self.get_n_rotations()
        k = self.n/self.d
        for i in range(nstep):
            theta = 2*pi*n_rot*i/nstep
            points.append((cos(k*theta)*cos(theta), cos(k*theta)*sin(theta),))
        return points

def parse_args():
    ''' Basic argument parser '''
    parser = argparse.ArgumentParser(description='Playing with rhodoneas (roses)')
    parser.add_argument('-n',
                        help='n parameter (k=n/d)',
                        default=5,
                        type=int)
    parser.add_argument('-d',
                        help='d parameter (k=n/d)',
                        default=3,
                        type=int)
    parser.add_argument('-p',
                        help='number of points',
                        default=256,
                        type=int)
    parser.add_argument('-s',
                        help='size of PIL square canvas side, in pixels',
                        default=256,
                        type=int)
    parser.add_argument('-e',
                        help='Drawing engine',
                        default="pil",
                        type=str,
                        choices=("pil", "lineus"))
    _args = parser.parse_args()
    return _args

ARGS = parse_args()
CANVAS = (0, ARGS.s, ARGS.s, 0)
drawing_engine.draw_continuous(Rose(ARGS.n, ARGS.d).compute(ARGS.p), \
                               CANVAS, \
                               ARGS.e)
