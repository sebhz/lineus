#!/usr/bin/env python3
"""Writing in Ogham"""
import math
import argparse
import drawing_engine

# The length of a bar is arbitrarily set to 1
# e.g. beith has a width of 1 and a height of 0.
# e.g. ailm has a width of 2 and a height of 0.

ILN = 0.2  # Space between 2 strokes in a given Ogham
IOG = 0.6  # Space between 2 Oghams
ANG = 15  # Obliquity of the "Aicme Muine" series, in degree

M_Y = math.tan(ANG * math.pi / 180.0)

# strokes instructions:
# (M, x, y): move to x,y
# (T, x, y): draw a line between current position and x,y
# Coordinates assume origin at the bottom middle of the letter bounding box, with
# x ascending right and y ascending up.
# strokes instructions are for ogham in vertical position
OGHAM_REF = {
    "beith": {"values": ("B"), "strokes": ((0, 0, 1, 0),)},
    "luis": {
        "values": ("L"),
        "strokes": ((0, 0, 1, 0), (0, ILN, 1, ILN)),
    },
    "fearn": {
        "values": ("F"),
        "strokes": (
            (0, 0, 1, 0),
            (0, ILN, 1, ILN),
            (0, 2 * ILN, 1, 2 * ILN),
        ),
    },
    "saille": {
        "values": ("S"),
        "strokes": (
            (0, 0, 1, 0),
            (0, ILN, 1, ILN),
            (0, 2 * ILN, 1, 2 * ILN),
            (0, 3 * ILN, 1, 3 * ILN),
        ),
    },
    "nuin": {
        "values": ("N"),
        "strokes": (
            (0, 0, 1, 0),
            (0, ILN, 1, ILN),
            (0, 2 * ILN, 1, 2 * ILN),
            (0, 3 * ILN, 1, 3 * ILN),
            (0, 4 * ILN, 1, 4 * ILN),
        ),
    },
    "uath": {"values": ("H"), "strokes": ((0, 0, -1, 0),)},
    "duir": {
        "values": ("D"),
        "strokes": ((0, 0, -1, 0), (0, ILN, -1, ILN)),
    },
    "tinne": {
        "values": ("T"),
        "strokes": (
            (0, 0, -1, 0),
            (0, ILN, -1, ILN),
            (0, 2 * ILN, -1, 2 * ILN),
        ),
    },
    "coll": {
        "values": ("C", "K"),
        "strokes": (
            (0, 0, -1, 0),
            (0, ILN, -1, ILN),
            (0, 2 * ILN, -1, 2 * ILN),
            (0, 3 * ILN, -1, 3 * ILN),
        ),
    },
    "ceirt": {
        "values": ("Q"),
        "strokes": (
            (0, 0, -1, 0),
            (0, ILN, -1, ILN),
            (0, 2 * ILN, -1, 2 * ILN),
            (0, 3 * ILN, -1, 3 * ILN),
            (0, 4 * ILN, -1, 4 * ILN),
        ),
    },
    "muin": {"values": ("M"), "strokes": ((-1, 2 * M_Y, 1, 0))},
    "gort": {
        "values": ("G"),
        "strokes": (
            (-1, 2 * M_Y, 1, 0),
            (-1, 2 * M_Y + ILN, 1, ILN),
        ),
    },
    "ngeadal": {
        "values": ("NG"),
        "strokes": (
            (-1, 2 * M_Y, 1, 0),
            (-1, 2 * M_Y + ILN, 1, ILN),
            (-1, 2 * M_Y + 2 * ILN, 1, 2 * ILN),
        ),
    },
    "straif": {
        "values": ("Z"),
        "strokes": (
            (-1, 2 * M_Y, 1, 0),
            (-1, 2 * M_Y + ILN, 1, ILN),
            (-1, 2 * M_Y + 2 * ILN, 1, 2 * ILN),
            (-1, 2 * M_Y + 3 * ILN, 1, 3 * ILN),
        ),
    },
    "ruis": {
        "values": ("R"),
        "strokes": (
            (-1, 2 * M_Y, 1, 0),
            (-1, 2 * M_Y + ILN, 1, ILN),
            (-1, 2 * M_Y + 2 * ILN, 1, 2 * ILN),
            (-1, 2 * M_Y + 3 * ILN, 1, 3 * ILN),
            (-1, 2 * M_Y + 4 * ILN, 1, 4 * ILN),
        ),
    },
    "ailm": {"values": ("A"), "strokes": ((-1, 0, 1, 0),)},
    "onn": {
        "values": ("O"),
        "strokes": ((-1, 0, 1, 0), (-1, ILN, 1, ILN)),
    },
    "ur": {
        "values": ("U"),
        "strokes": (
            (-1, 0, 1, 0),
            (-1, ILN, 1, ILN),
            (-1, 2 * ILN, 1, 2 * ILN),
        ),
    },
    "edad": {
        "values": ("E"),
        "strokes": (
            (-1, 0, 1, 0),
            (-1, ILN, 1, ILN),
            (-1, 2 * ILN, 1, 2 * ILN),
            (-1, 3 * ILN, 1, 3 * ILN),
        ),
    },
    "idad": {
        "values": ("I"),
        "strokes": (
            (-1, 0, 1, 0),
            (-1, ILN, 1, ILN),
            (-1, 2 * ILN, 1, 2 * ILN),
            (-1, 3 * ILN, 1, 3 * ILN),
            (-1, 4 * ILN, 1, 4 * ILN),
        ),
    },
    "ebad": {
        "values": ("EA", "K", "EO"),
        "strokes": (
            (-1, 0, 1, 3 * ILN),
            (-1, 3 * ILN, 1, 0),
        ),
    },
    "or": {
        "values": ("O", "OI", "OE"),
        "strokes": (
            (-1, 1.5 * ILN, 0, 3 * ILN),
            (1, 1.5 * ILN),
            (0, 0),
            (-1, 1.5 * ILN),
        ),
    },
    "uillean": {
        "value": ("UI", "UA"),
        "strokes": (
            (0, 0, 0.5, 0),
            (0.5, 4 * ILN),
            (0.25, 4 * ILN),
            (0.25, ILN),
        ),
    },
    "pin": {
        "values": ("P", "IO", "IA"),
        "strokes": (
            (0, 0, 1, 2 * ILN),
            (0, ILN, 1, 3 * ILN),
            (0, 3 * ILN, 1, 0),
            (0, 4 * ILN, 1, ILN),
        ),
    },
    "emancholl": {
        "values": ("X", "CH", "AE"),
        "strokes": (
            (0, ILN, -4 * ILN, ILN),
            (0, 2 * ILN, -4 * ILN, 2 * ILN),
            (0, 3 * ILN, -4 * ILN, 3 * ILN),
            (-ILN, 0, -ILN, 4 * ILN),
            (-2 * ILN, 0, -2 * ILN, 4 * ILN),
            (-3 * ILN, 0, -3 * ILN, 4 * ILN),
        ),
    },
    "peith": {
        "values": ("P"),
        "strokes": ((0.5, 0, 0.5, 2 * ILN),),
    },
}


VALUES = {
    "A": "ailm",
    "B": "beith",
    "C": "coll",
    "D": "duir",
    "E": "edad",
    "F": "fearn",
    "G": "gort",
    "H": "uath",
    "I": "idad",
    "J": "idad",
    "K": "ebad",
    "L": "luis",
    "M": "muin",
    "N": "nuin",
    "O": "onn",
    "P": "peith",
    "Q": "ceirt",
    "R": "ruis",
    "S": "saille",
    "T": "tinne",
    "U": "ur",
    "V": "ur",
    "W": "pin",
    "X": "emancholl",
    "Y": "idad",
    "Z": "straif",
}


def trace_strokes(strokes, offset, fit_func, d_e):
    """Trace a stroke"""
    f_f = lambda x, y: fit_func(
        (
            x + offset[0],
            y + offset[1],
        )
    )
    for stroke in strokes:
        point0 = f_f(stroke[0], stroke[1])
        if len(stroke) == 2:
            d_e.draw_line(point0)
        else:
            point1 = f_f(stroke[2], stroke[3])
            d_e.draw_line(point0, point1)


def trace_sentence(sentence, canvas, d_e, margin=0.05):
    """Trace a sentence"""
    b_box = get_sentence_binding_box(sentence, margin)
    fit_func = drawing_engine.fit_func_factory(b_box, canvas)
    x_c = b_box[2] / 2.0  # Our letter strokes are centered
    y_c = b_box[3] * margin / 2.0

    end_line_y = b_box[3] * (1 - margin / 2.0) - IOG
    # Draw center line and markers
    strokes = (
        (x_c, y_c + IOG, x_c, end_line_y),
        (x_c, y_c + IOG, x_c - IOG / 2, y_c),
        (x_c, y_c + IOG, x_c + IOG / 2, y_c),
        (x_c, end_line_y, x_c - IOG / 2, end_line_y + IOG),
        (x_c, end_line_y, x_c + IOG / 2, end_line_y + IOG),
    )
    trace_strokes(strokes, (0, 0), fit_func, d_e)
    y_c += 2 * IOG

    # Now draw the characters
    for word in sentence.split():
        for letter in word.upper():
            glyph = VALUES.get(letter)
            if not glyph in OGHAM_REF:
                continue
            trace_strokes(OGHAM_REF[glyph]["strokes"], (x_c, y_c), fit_func, d_e)
            y_c += IOG + get_letter_height(letter)

    d_e.show()


def get_letter_height(letter):
    """Get the height of a letter
    This is just the max Y of each stroke in the letter"""
    glyph = VALUES.get(letter.upper())
    if not glyph in OGHAM_REF:
        return 0
    y_s = []
    for stroke in OGHAM_REF[glyph]["strokes"]:
        y_s.append(stroke[1])
        if len(stroke) == 4:
            y_s.append(stroke[3])
    return max(y_s)


def get_word_height(word):
    """Get the height of a word"""
    height = 0
    for letter in word:
        height += get_letter_height(letter)
        height += IOG
    return height - IOG


def get_word_width(word):
    """Get the width of a word"""
    return 2


def get_sentence_binding_box(sentence, margin=0.05):
    """Get the binding box of a full sentence
    margin is the percentage to be added on all sides
    Ogham are written vertically, so add all height but
    take the max of all width"""
    width, height = 0, 0
    for word in sentence.split():
        width = max(width, get_word_width(word))
        height += get_word_height(word)
        height += IOG  # Add a space between words
    height -= IOG
    # Now add two spaces on top and bottom for the start and end markers
    height += 4 * IOG
    # And add the margin
    width *= 1 + margin
    height *= 1 + margin
    return (0, 0, width, height)


def sanitize_sentence(sentence):
    """Remove all unknown characters from input"""
    txt = ""
    for letter in sentence:
        if letter.upper() not in VALUES:
            continue
        txt += letter
    return txt


def parse_args():
    """Basic argument parser"""
    parser = argparse.ArgumentParser(description="Ogham transliteration")
    parser.add_argument(
        "-w", help="width of PIL canvas side, in pixels", default=256, type=int
    )
    parser.add_argument(
        "-H", help="height of PIL canvas side, in pixels", default=256, type=int
    )
    parser.add_argument(
        "-e", help="Drawing engine", default="pil", type=str, choices=("pil", "lineus")
    )
    parser.add_argument("text", help="Text to translate", type=str)
    _args = parser.parse_args()
    return _args


ARGS = parse_args()
if ARGS.e == "pil":
    # Reverse Y axis as Pil has it increasing downward
    CANVAS = (0, ARGS.H, ARGS.w, 0)
    draw_engine = drawing_engine.PilDrawEngine(CANVAS)
else:
    CANVAS = drawing_engine.LineUsDrawEngine.LINEUS_CANVAS
    draw_engine = drawing_engine.LineUsDrawEngine(CANVAS)

TXT = sanitize_sentence(ARGS.text)
trace_sentence(TXT, CANVAS, draw_engine)
