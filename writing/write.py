#!/usr/bin/env python3
"""Writing in strokes"""
import argparse
import drawing_engine
import ogham


def draw_ogham_base(b_box, fit_func, d_e, margin=0.05):
    """Draw ogham base line"""
    x_c, y_c = (b_box[2] - b_box[0]) * margin / 2, (b_box[3] - b_box[1]) * margin / 2
    end_line_x = (b_box[2] - b_box[0]) * (1 - margin / 2.0)
    trace_strokes(((x_c, y_c, end_line_x, y_c),), (0, 1), fit_func, d_e)


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
    x_c, y_c = (b_box[2] - b_box[0]) * margin / 2, (b_box[3] - b_box[1]) * margin / 2
    space = FONT.get_glyph_spacing()
    if FONT.name == "ogham":  # Ogham is special - draw a line
        draw_ogham_base(b_box, fit_func, d_e, margin)

    # Now draw the characters
    for word in sentence.split():
        for letter in word:
            glyph = FONT.get_glyph_by_value(letter)
            if glyph is None:
                continue
            trace_strokes(glyph.get_strokes(), (x_c, y_c), fit_func, d_e)
            x_c += space + glyph.get_width()

    d_e.show()


def get_word_dimensions(word):
    """Get the width and height of a word"""
    width, height = 0, 0
    space = FONT.get_glyph_spacing()
    for letter in word:
        glyph = FONT.get_glyph_by_value(letter)
        if glyph is not None:
            width += glyph.get_width()
            height = max(height, glyph.get_height())
            width += space
    return width - space, height


def get_sentence_binding_box(sentence, margin=0.05):
    """Get the binding box of a full sentence
    margin is the percentage to be added on all sides.
    For now, assuming horizontal text"""
    width, height = 0, 0
    space = FONT.get_glyph_spacing()
    for word in sentence.split():
        _w, _h = get_word_dimensions(word)
        height = max(height, _h)
        width += _w + space  # Add a space between words
    width -= space

    # And add the margin
    width *= 1 + margin
    height *= 1 + margin
    return (0, 0, width, height)


def sanitize_sentence(sentence):
    """Remove all unknown characters from input"""
    txt = ""
    for letter in sentence:
        if not FONT.is_value_mapped(letter):
            continue
        txt += letter
    return txt


def get_font(font_name):
    """Return the font object referenced by name"""
    if font_name == "ogham":
        return ogham.font
    return None


def parse_args():
    """Basic argument parser"""
    parser = argparse.ArgumentParser(description="Lineus text drawing transliteration")
    parser.add_argument(
        "-w",
        "--width",
        help="width of PIL canvas side, in pixels",
        default=256,
        type=int,
    )
    parser.add_argument(
        "-H",
        "--height",
        help="height of PIL canvas side, in pixels",
        default=256,
        type=int,
    )
    parser.add_argument(
        "-e",
        "--engine",
        help="Drawing engine",
        default="pil",
        type=str,
        choices=("pil", "lineus"),
    )
    parser.add_argument(
        "-f",
        "--font",
        help="Font to use",
        default="ogham",
        type=str,
        choices=("ogham",),
    )
    parser.add_argument("text", help="Text to translate", type=str)
    _args = parser.parse_args()
    return _args


ARGS = parse_args()
if ARGS.engine == "pil":
    # Reverse Y axis as Pil has it increasing downward
    CANVAS = (0, ARGS.height, ARGS.width, 0)
    draw_engine = drawing_engine.PilDrawEngine(CANVAS)
else:
    CANVAS = drawing_engine.LineUsDrawEngine.LINEUS_CANVAS
    draw_engine = drawing_engine.LineUsDrawEngine(CANVAS)

FONT = get_font(ARGS.font)
TXT = sanitize_sentence(ARGS.text)
trace_sentence(TXT, CANVAS, draw_engine)
