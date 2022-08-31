#!/usr/bin/env python3
"""Writing in Ogham"""
import math
import sys
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
    "beith": {"values": ("B"), "strokes": (("M", 0, 0), ("T", 1, 0))},
    "luis": {
        "values": ("L"),
        "strokes": (("M", 0, 0), ("T", 1, 0), ("M", 0, ILN), ("T", 1, ILN)),
    },
    "fearn": {
        "values": ("F"),
        "strokes": (
            ("M", 0, 0),
            ("T", 1, 0),
            ("M", 0, ILN),
            ("T", 1, ILN),
            ("M", 0, 2 * ILN),
            ("T", 1, 2 * ILN),
        ),
    },
    "saille": {
        "values": ("S"),
        "strokes": (
            ("M", 0, 0),
            ("T", 1, 0),
            ("M", 0, ILN),
            ("T", 1, ILN),
            ("M", 0, 2 * ILN),
            ("T", 1, 2 * ILN),
            ("M", 0, 3 * ILN),
            ("T", 1, 3 * ILN),
        ),
    },
    "nuin": {
        "values": ("N"),
        "strokes": (
            ("M", 0, 0),
            ("T", 1, 0),
            ("M", 0, ILN),
            ("T", 1, ILN),
            ("M", 0, 2 * ILN),
            ("T", 1, 2 * ILN),
            ("M", 0, 3 * ILN),
            ("T", 1, 3 * ILN),
            ("M", 0, 4 * ILN),
            ("T", 1, 4 * ILN),
        ),
    },
    "uath": {"values": ("H"), "strokes": (("M", 0, 0), ("T", -1, 0))},
    "duir": {
        "values": ("D"),
        "strokes": (("M", 0, 0), ("T", -1, 0), ("M", 0, ILN), ("T", -1, ILN)),
    },
    "tinne": {
        "values": ("T"),
        "strokes": (
            ("M", 0, 0),
            ("T", -1, 0),
            ("M", 0, ILN),
            ("T", -1, ILN),
            ("M", 0, 2 * ILN),
            ("T", -1, 2 * ILN),
        ),
    },
    "coll": {
        "values": ("C", "K"),
        "strokes": (
            ("M", 0, 0),
            ("T", -1, 0),
            ("M", 0, ILN),
            ("T", -1, ILN),
            ("M", 0, 2 * ILN),
            ("T", -1, 2 * ILN),
            ("M", 0, 3 * ILN),
            ("T", -1, 3 * ILN),
        ),
    },
    "ceirt": {
        "values": ("Q"),
        "strokes": (
            ("M", 0, 0),
            ("T", -1, 0),
            ("M", 0, ILN),
            ("T", -1, ILN),
            ("M", 0, 2 * ILN),
            ("T", -1, 2 * ILN),
            ("M", 0, 3 * ILN),
            ("T", -1, 3 * ILN),
            ("M", 0, 4 * ILN),
            ("T", -1, 4 * ILN),
        ),
    },
    "muin": {"values": ("M"), "strokes": (("M", -1, 2 * M_Y), ("T", 1, 0))},
    "gort": {
        "values": ("G"),
        "strokes": (
            ("M", -1, 2 * M_Y),
            ("T", 1, 0),
            ("M", -1, 2 * M_Y + ILN),
            ("T", 1, ILN),
        ),
    },
    "ngeadal": {
        "values": ("NG"),
        "strokes": (
            ("M", -1, 2 * M_Y),
            ("T", 1, 0),
            ("M", -1, 2 * M_Y + ILN),
            ("T", 1, ILN),
            ("M", -1, 2 * M_Y + 2 * ILN),
            ("T", 1, 2 * ILN),
        ),
    },
    "straif": {
        "values": ("Z"),
        "strokes": (
            ("M", -1, 2 * M_Y),
            ("T", 1, 0),
            ("M", -1, 2 * M_Y + ILN),
            ("T", 1, ILN),
            ("M", -1, 2 * M_Y + 2 * ILN),
            ("T", 1, 2 * ILN),
            ("M", -1, 2 * M_Y + 3 * ILN),
            ("T", 1, 3 * ILN),
        ),
    },
    "ruis": {
        "values": ("R"),
        "strokes": (
            ("M", -1, 2 * M_Y),
            ("T", 1, 0),
            ("M", -1, 2 * M_Y + ILN),
            ("T", 1, ILN),
            ("M", -1, 2 * M_Y + 2 * ILN),
            ("T", 1, 2 * ILN),
            ("M", -1, 2 * M_Y + 3 * ILN),
            ("T", 1, 3 * ILN),
            ("M", -1, 2 * M_Y + 4 * ILN),
            ("T", 1, 4 * ILN),
        ),
    },
    "ailm": {"values": ("A"), "strokes": (("M", -1, 0), ("T", 1, 0))},
    "onn": {
        "values": ("O"),
        "strokes": (("M", -1, 0), ("T", 1, 0), ("M", -1, ILN), ("T", 1, ILN)),
    },
    "ur": {
        "values": ("U"),
        "strokes": (
            ("M", -1, 0),
            ("T", 1, 0),
            ("M", -1, ILN),
            ("T", 1, ILN),
            ("M", -1, 2 * ILN),
            ("T", 1, 2 * ILN),
        ),
    },
    "edad": {
        "values": ("E"),
        "strokes": (
            ("M", -1, 0),
            ("T", 1, 0),
            ("M", -1, ILN),
            ("T", 1, ILN),
            ("M", -1, 2 * ILN),
            ("T", 1, 2 * ILN),
            ("M", -1, 3 * ILN),
            ("T", 1, 3 * ILN),
        ),
    },
    "idad": {
        "values": ("I"),
        "strokes": (
            ("M", -1, 0),
            ("T", 1, 0),
            ("M", -1, ILN),
            ("T", 1, ILN),
            ("M", -1, 2 * ILN),
            ("T", 1, 2 * ILN),
            ("M", -1, 3 * ILN),
            ("T", 1, 3 * ILN),
            ("M", -1, 4 * ILN),
            ("T", 1, 4 * ILN),
        ),
    },
    "ebad": {
        "values": ("EA", "K", "EO"),
        "strokes": (
            ("M", -1, 0),
            ("T", 1, 3 * ILN),
            ("M", -1, 3 * ILN),
            ("T", 1, 0),
        ),
    },
    "or": {
        "values": ("O", "OI", "OE"),
        "strokes": (
            ("M", -1, 1.5 * ILN),
            ("T", 0, 3 * ILN),
            ("T", 1, 1.5 * ILN),
            ("T", 0, 0),
            ("T", -1, 1.5 * ILN),
        ),
    },
    "uillean": {
        "value": ("UI", "UA"),
        "strokes": (
            ("M", 0, 0),
            ("T", 0.5, 0),
            ("T", 0.5, 4 * ILN),
            ("T", 0.25, 4 * ILN),
            ("T", 0.25, ILN),
        ),
    },
    "pin": {
        "values": ("P", "IO", "IA"),
        "strokes": (
            ("M", 0, 0),
            ("T", 1, 2 * ILN),
            ("M", 0, ILN),
            ("T", 1, 3 * ILN),
            ("M", 0, 3 * ILN),
            ("T", 1, 0),
            ("M", 0, 4 * ILN),
            ("T", 1, ILN),
        ),
    },
    "emancholl": {
        "values": ("X", "CH", "AE"),
        "strokes": (
            ("M", 0, ILN),
            ("T", -4 * ILN, ILN),
            ("M", 0, 2 * ILN),
            ("T", -4 * ILN, 2 * ILN),
            ("M", 0, 3 * ILN),
            ("T", -4 * ILN, 3 * ILN),
            ("M", -ILN, 0),
            ("T", -ILN, 4 * ILN),
            ("M", -2 * ILN, 0),
            ("T", -2 * ILN, 4 * ILN),
            ("M", -3 * ILN, 0),
            ("T", -3 * ILN, 4 * ILN),
        ),
    },
    "peith": {
        "values": ("P"),
        "strokes": (("M", 0.5, 0), ("T", 0.5, 2 * ILN)),
    },
}

# TODO - finish the table

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


def trace_strokes(strokes, offset, fit_func, draw_engine):
    """Trace a stroke"""
    for stroke in strokes:
        point = fit_func(
            (
                stroke[1] + offset[0],
                stroke[2] + offset[1],
            )
        )
        if stroke[0] == "M":
            draw_engine.set_pos(point)
        else:
            draw_engine.draw_line(point)


def trace_sentence(sentence, canvas, draw_engine, margin=0.05):
    """Trace a sentence"""
    b_box = get_sentence_binding_box(sentence, margin)
    fit_func = drawing_engine.fit_func_factory(b_box, canvas)
    x = b_box[2] / 2.0  # Our letter strokes are centered
    y = b_box[3] * margin / 2.0

    end_line_y = b_box[3] * (1 - margin / 2.0) - IOG
    # Draw center line and markers
    strokes = (
        ("M", x, y + IOG),
        ("T", x, end_line_y),
        ("M", x, y + IOG),
        ("T", x - IOG / 2, y),
        ("M", x, y + IOG),
        ("T", x + IOG / 2, y),
        ("M", x, end_line_y),
        ("T", x - IOG / 2, end_line_y + IOG),
        ("M", x, end_line_y),
        ("T", x + IOG / 2, end_line_y + IOG),
    )
    trace_strokes(strokes, (0, 0), fit_func, draw_engine)
    y += 2 * IOG

    # Now draw the characters
    for word in sentence.split():
        for letter in word.upper():
            glyph = VALUES.get(letter)
            if not glyph in OGHAM_REF:
                continue
            trace_strokes(OGHAM_REF[glyph]["strokes"], (x, y), fit_func, draw_engine)
            y += IOG + get_letter_height(letter)

    draw_engine.show()


def get_letter_height(letter):
    """Get the height of a letter
    This is just the max Y of each stroke in the letter"""
    glyph = VALUES.get(letter.upper())
    if not glyph in OGHAM_REF:
        return 0
    return max([_[2] for _ in OGHAM_REF[glyph]["strokes"]])


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
    w, h = 0, 0
    for word in sentence.split():
        w = max(w, get_word_width(word))
        h += get_word_height(word)
        h += IOG  # Add a space between words
    h -= IOG
    # Now add two spaces on top and bottom for the start and end markers
    h += 4 * IOG
    # And add the margin
    w *= 1 + margin
    h *= 1 + margin
    return (0, 0, w, h)

def sanitize_sentence(sentence):
    txt = ""
    for letter in sentence:
        if letter != " " and letter.upper() not in VALUES:
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
    CANVAS = (0, ARGS.w, ARGS.H, 0)
    draw_engine = drawing_engine.PilDrawEngine(CANVAS)
else:
    CANVAS = draw_engine.LineUsDrawEngine.LINEUS_CANVAS
    draw_engine = drawing_engine.LineUsDrawEngine(CANVAS)

TXT = sanitize_sentence(ARGS.text)
trace_sentence(TXT, CANVAS, draw_engine)
