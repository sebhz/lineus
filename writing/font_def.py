#!/usr/bin/env python3
"""Base classes for glyphs and fonts"""


class Glyph:
    """A glyph = a set of strokes describing a character.
    Strokes are describing the glyph as written horizontally
    and left to right. Strokes coordinates must be positive with
    glyph bottom left at coordinate 0,0"""

    def __init__(self, name, strokes):
        """Initialization code: set name, values,strokes, width and height.
        We compute width and height from strokes"""
        self.name = name
        self.strokes = strokes
        self.init_size()

    def get_width(self):
        """Width getter"""
        return self.width

    def get_height(self):
        """Height getter"""
        return self.height

    def get_strokes(self):
        """Strokes getter"""
        return self.strokes

    def init_size(self):
        """Initialize glyph height and width from its stroke list"""
        x_s, y_s = [], []
        for stroke in self.strokes:
            x_s.append(stroke[0])
            y_s.append(stroke[1])
            if len(stroke) == 4:
                x_s.append(stroke[2])
                y_s.append(stroke[3])
        self.width, self.height = abs(max(x_s) - min(x_s)), abs(max(y_s) - min(y_s))


class Font:
    """A Font: set of glyphs"""

    def __init__(self, name, g_space, glyphs):
        """Initialize font"""
        self.name = name
        self.g_space = g_space
        self.glyph_index = {} # From glyph name to glyph
        self.glyph_value = {} # From glyph value to glyph
        self.create_font_indexes(glyphs)

    def create_font_indexes(self, glyphs):
        """Create the glyph index"""
        for glyph in glyphs:
            self.glyph_index[glyph.name] = glyph

    def set_glyph_value_map(self, map_desc):
        """Create a dict value -> Glyph object"""
        self.glyph_value = {}
        for values, name in map_desc.items():
            for value in values:
                self.glyph_value[value] = self.get_glyph_by_name(name)

    def get_glyph_by_name(self, name):
        """Get a glyph by its name"""
        return self.glyph_index.get(name)

    def get_glyph_by_value(self, value):
        """Get a glyph by its value"""
        return self.glyph_value.get(value)

    def is_value_mapped(self, value):
        """Check if a value is mapped"""
        return value in self.glyph_value

    def get_glyph_spacing(self):
        """Get the space between glyphs"""
        return self.g_space
