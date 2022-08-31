#!/usr/bin/env python3
""" Lissajous curves """
import argparse
from math import pi, sin
import drawing_engine


class Lissajous:
    """Describe a Lissajous curve"""

    def __init__(self, a, b, phi):
        if not isinstance(a, int):
            raise TypeError("n must be an integer")
        if not isinstance(b, int):
            raise TypeError("d must be an integer")
        if phi < -0.5 or phi > 0.5:
            raise ValueError("phi must be in [-0.5;0.5]")

        while (a % 2 == 0) and (b % 2 == 0):
            a = a / 2
            b = b / 2

        self.a = a
        self.b = b
        self.phi = phi

    def compute(self, nstep):
        """Compute Lissajous points"""
        points = list()
        phase = pi * self.phi
        for i in range(nstep):
            theta = 2 * pi * i / nstep
            points.append((sin(self.a * theta + phase), sin(self.b * theta)))
        return points


def parse_args():
    """Basic argument parser"""
    parser = argparse.ArgumentParser(description="Playing Lissajous figure")
    parser.add_argument("-a", help="a parameter", default=5, type=int)
    parser.add_argument("-b", help="b parameter", default=3, type=int)
    parser.add_argument("-P", help="phase parameter", default=0.5, type=float)
    parser.add_argument("-p", help="number of points", default=256, type=int)
    parser.add_argument(
        "-s", help="size of PIL square canvas side, in pixels", default=256, type=int
    )
    parser.add_argument(
        "-e", help="Drawing engine", default="pil", type=str, choices=("pil", "lineus")
    )
    _args = parser.parse_args()
    return _args


ARGS = parse_args()
CANVAS = (0, ARGS.s, ARGS.s, 0)
drawing_engine.draw_continuous(
    Lissajous(ARGS.a, ARGS.b, ARGS.P).compute(ARGS.p), CANVAS, ARGS.e
)
