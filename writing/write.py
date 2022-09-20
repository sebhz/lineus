#!/usr/bin/env python3
"""Writing in strokes"""
import argparse
import sys
import drawing_engine
import ogham
import cirth


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


def trace_text(glyph_seq, canvas, d_e, margin=0.05):
    """Trace a text"""
    b_box = get_text_binding_box(glyph_seq, margin)
    fit_func = drawing_engine.fit_func_factory(b_box, canvas)
    x_c, y_c = (b_box[2] - b_box[0]) * margin / 2, (b_box[3] - b_box[1]) * margin / 2
    space = FONT.get_glyph_spacing()
    if FONT.name == "ogham":  # Ogham is special - draw a line
        draw_ogham_base(b_box, fit_func, d_e, margin)

    # Now draw the characters
    for glyph in glyph_seq:
        if glyph is None:
            continue
        trace_strokes(glyph.get_strokes(), (x_c, y_c), fit_func, d_e)
        x_c += space + glyph.get_width()

    d_e.show()


def get_text_binding_box(glyph_seq, margin=0.05):
    """Get the binding box of a sequence of glyphs
    margin is the percentage to be added on all sides.
    For now, assuming horizontal text"""
    width, height = 0, 0
    space = FONT.get_glyph_spacing()
    for glyph in glyph_seq:
        if glyph is not None:
            width += glyph.get_width()
            height = max(height, glyph.get_height())
            width += space
    width -= space

    # And add the margin
    width *= 1 + margin
    height *= 1 + margin
    return (0, 0, width, height)


def glyphize_text(text):
    """Get a text, and returns a corresponding list of glyph.
    Unknown glyphs are ignored.
    Try and map diphtongs and triphtongs in a crude way. Will
    mostly work for simple cases"""
    glyph_list = []
    unknown_letters = set()
    text_i = 0
    while text_i < len(text):
        for _i in range(3, 0, -1):  # Check all triph/diphtongue + single char
            phtong = text[text_i : text_i + _i]
            if FONT.is_value_mapped(phtong):
                glyph_list.append(FONT.get_glyph_by_value(phtong))
                text_i += _i
                break
            if _i == 1:  # Single letter not found
                unknown_letters.add(phtong)
                text_i += 1

    if unknown_letters != set():
        print(
            "Following letters are not in the chosen font. Ignoring them:",
            unknown_letters,
            file=sys.stderr,
        )
    return glyph_list


def get_font(font_name):
    """Return the font object referenced by name"""
    if font_name == "ogham":
        _f = ogham.FONT
        _f.set_glyph_value_map(ogham.OGHAM_MAP_DESC)
        return _f
    if "cirth" in font_name:
        _f = cirth.FONT
        if font_name == "cirth":
            _f.set_glyph_value_map(cirth.CERTHAS_DAERON_MAP_DESC)
        if font_name == "cirth-d":
            _f.set_glyph_value_map(cirth.ANGERTHAS_DAERON_MAP_DESC)
        if font_name == "cirth-m":
            _f.set_glyph_value_map(cirth.ANGERTHAS_MORIA_MAP_DESC)
        if font_name == "cirth-e":
            _f.set_glyph_value_map(cirth.ANGERTHAS_EREBOR_MAP_DESC)
        return _f
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
        choices=("ogham", "cirth", "cirth-d", "cirth-m", "cirth-e"),
    )
    parser.add_argument("text", help="Text to translate", type=str)
    _args = parser.parse_args()
    return _args


ARGS = parse_args()
if ARGS.engine == "pil":
    # Reverse Y axis as Pil has it increasing downward
    CANVAS = (0, ARGS.height, ARGS.width, 0)
    DRAW_ENGINE = drawing_engine.PilDrawEngine(CANVAS)
else:
    CANVAS = drawing_engine.LineUsDrawEngine.LINEUS_CANVAS
    DRAW_ENGINE = drawing_engine.LineUsDrawEngine(CANVAS)

FONT = get_font(ARGS.font)
GLYPH_SEQ = glyphize_text(ARGS.text)
trace_text(GLYPH_SEQ, CANVAS, DRAW_ENGINE)
