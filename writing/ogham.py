#!/usr/bin/env python3
"""Definition of ogham stroke font"""
import math
from font_def import Font, Glyph


# The length of a bar is arbitrarily set to 1
# The glyph are drawn in their horizontal form
# e.g. beith has a width of 0 and a height of 1.
# e.g. ailm has a width of 0 and a height of 2.

ILN = 0.2  # Space between 2 strokes in a given Ogham
IOG = 0.6  # Space between two oghams
ANG = 15  # Obliquity of the "Aicme Muine" series, in degrees

M_Y = math.tan(ANG * math.pi / 180.0)


class Ogham(Font):
    """Ogham font"""

    GLYPHS = [
        Glyph("beith", ((0, 1, 0, 0),)),
        Glyph("luis", ((0, 1, 0, 0), (ILN, 1, ILN, 0))),
        Glyph(
            "fearn",
            ((0, 1, 0, 0), (ILN, 1, ILN, 0), (2 * ILN, 1, 2 * ILN, 0)),
        ),
        Glyph(
            "saille",
            (
                (0, 1, 0, 0),
                (ILN, 1, ILN, 0),
                (2 * ILN, 1, 2 * ILN, 0),
                (3 * ILN, 1, 3 * ILN, 0),
            ),
        ),
        Glyph(
            "nuin",
            (
                (0, 1, 0, 0),
                (ILN, 1, ILN, 0),
                (2 * ILN, 1, 2 * ILN, 0),
                (3 * ILN, 1, 3 * ILN, 0),
                (4 * ILN, 1, 4 * ILN, 0),
            ),
        ),
        Glyph("uath", ((0, 1, 0, 2),)),
        Glyph("duir", ((0, 1, 0, 2), (ILN, 1, ILN, 2))),
        Glyph(
            "tinne",
            (
                (0, 1, 0, 2),
                (ILN, 1, ILN, 2),
                (2 * ILN, 1, 2 * ILN, 2),
            ),
        ),
        Glyph(
            "coll",
            (
                (0, 1, 0, 2),
                (ILN, 1, ILN, 2),
                (2 * ILN, 1, 2 * ILN, 2),
                (3 * ILN, 1, 3 * ILN, 2),
            ),
        ),
        Glyph(
            "ceirt",
            (
                (0, 1, 0, 2),
                (ILN, 1, ILN, 2),
                (2 * ILN, 1, 2 * ILN, 2),
                (3 * ILN, 1, 3 * ILN, 2),
                (4 * ILN, 1, 4 * ILN, 2),
            ),
        ),
        Glyph("muin", ((2 * M_Y, 2, 0, 0),)),
        Glyph(
            "gort",
            (
                (2 * M_Y, 2, 0, 0),
                (2 * M_Y + ILN, 2, ILN, 0),
            ),
        ),
        Glyph(
            "ngeadal",
            (
                (2 * M_Y, 2, 0, 0),
                (2 * M_Y + ILN, 2, ILN, 0),
                (2 * M_Y + 2 * ILN, 2, 2 * ILN, 0),
            ),
        ),
        Glyph(
            "straif",
            (
                (2 * M_Y, 2, 0, 0),
                (2 * M_Y + ILN, 2, ILN, 0),
                (2 * M_Y + 2 * ILN, 2, 2 * ILN, 0),
                (2 * M_Y + 3 * ILN, 2, 3 * ILN, 0),
            ),
        ),
        Glyph(
            "ruis",
            (
                (2 * M_Y, 2, 0, 0),
                (2 * M_Y + ILN, 2, ILN, 0),
                (2 * M_Y + 2 * ILN, 2, 2 * ILN, 0),
                (2 * M_Y + 3 * ILN, 2, 3 * ILN, 0),
                (2 * M_Y + 4 * ILN, 2, 4 * ILN, 0),
            ),
        ),
        Glyph("ailm", ((0, 2, 0, 0),)),
        Glyph(
            "onn",
            ((0, 2, 0, 0), (ILN, 2, ILN, 0)),
        ),
        Glyph(
            "ur",
            (
                (0, 2, 0, 0),
                (ILN, 2, ILN, 0),
                (2 * ILN, 2, 2 * ILN, 0),
            ),
        ),
        Glyph(
            "edad",
            (
                (0, 2, 0, 0),
                (ILN, 2, ILN, 0),
                (2 * ILN, 2, 2 * ILN, 0),
                (3 * ILN, 2, 3 * ILN, 0),
            ),
        ),
        Glyph(
            "idad",
            (
                (0, 2, 0, 0),
                (ILN, 2, ILN, 0),
                (2 * ILN, 2, 2 * ILN, 0),
                (3 * ILN, 2, 3 * ILN, 0),
                (4 * ILN, 2, 4 * ILN, 0),
            ),
        ),
        Glyph(
            "ebad",
            (
                (0, 2, 3 * ILN, 0),
                (3 * ILN, 0, 0, 0),
            ),
        ),
        Glyph(
            "or",
            (
                (1.5 * ILN, 2, 3 * ILN, 1),
                (1.5 * ILN, 0),
                (0, 1),
                (1.5 * ILN, 0),
            ),
        ),
        Glyph(
            "uillean",
            (
                (0, 1, 0, 0.5),
                (4 * ILN, 0.5),
                (4 * ILN, 0.75),
                (ILN, 0.75),
            ),
        ),
        Glyph(
            "pin",
            (
                (0, 1, 2 * ILN, 0),
                (ILN, 1, 3 * ILN, 0),
                (3 * ILN, 1, 0, 0),
                (4 * ILN, 1, ILN, 0),
            ),
        ),
        Glyph(
            "emancholl",
            (
                (ILN, 1, ILN, 1 + 4 * ILN),
                (2 * ILN, 1, 2 * ILN, 1 + 4 * ILN),
                (3 * ILN, 1, 3 * ILN, 1 + 4 * ILN),
                (0, 1 + ILN, 4 * ILN, 1 + ILN),
                (0, 1 + 2 * ILN, 4 * ILN, 1 + 2 * ILN),
                (0, 1 + 3 * ILN, 4 * ILN, 1 + 3 * ILN),
            ),
        ),
        Glyph(
            "peith",
            ((0, 0.5, 2 * ILN, 0.5),),
        ),
    ]
    DEFAULT_MAP_DESC = {
        ("a", "A"): "ailm",
        ("b", "B"): "beith",
        ("c", "C", "k", "K"): "coll",
        ("d", "D"): "duir",
        ("e", "E"): "edad",
        ("f", "F"): "fearn",
        ("g", "G"): "gort",
        ("h", "H"): "uath",
        ("i", "I"): "idad",
        ("l", "L"): "luis",
        ("m", "M"): "muin",
        ("o", "O"): "onn",
        ("p", "P"): "peith",
        ("q", "Q"): "ceirt",
        ("n", "N"): "nuin",
        ("r", "R"): "ruis",
        ("s", "S"): "saille",
        ("t", "T"): "tinne",
        ("u", "U"): "ur",
        ("z", "Z"): "straif",
        ("ng", "NG"): "ngeadal",
        ("EA", "EO", "ea", "eo"): "ebad",
        ("OI", "OE", "oi", "oe"): "or",
        ("UI", "UA", "ui", "ua"): "uillean",
        ("IO", "IA", "io", "ia"): "pin",
        ("X", "CH", "AE", "x", "ch", "ae"): "emancholl",
    }

    def __init__(self, map_desc=None):
        super().__init__("ogham", IOG, self.GLYPHS)
        if map_desc is None:
            self.create_glyph_value_map(self.DEFAULT_MAP_DESC)
        else:
            self.create_glyph_value_map(map_desc)


font = Ogham()
