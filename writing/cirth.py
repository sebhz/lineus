#!/usr/bin/env python3
"""Definition of cirth stroke font"""
from font_def import Font, Glyph


class Cirth(Font):
    """Cirth font"""

    GLYPH_SPACING = 0.1
    GLYPHS = [
        Glyph("1", ((0, 0, 0, 1), (0.5, 0.75), (0, 0.5))),
        Glyph("2", ((0, 0, 0, 1), (0.5, 0.75), (0, 0.5), (0.5, 0))),
        Glyph("3", ((0.5, 0, 0.5, 1), (0, 0.75), (0.5, 0.5))),
        Glyph("4", ((0.5, 0, 0.5, 1), (0, 0.75), (0.5, 0.5), (0, 0))),
        Glyph(
            "5",
            ((0.375, 0, 0.375, 1), (0.0, 0.75), (0.375, 0.5), (0.75, 0.75), (0.375, 1)),
        ),
        Glyph("6", ((0, 0, 0, 1), (0.5, 0.75), (0, 0.5), (0.5, 0.25), (0, 0))),
        Glyph("7", ((0.5, 0, 0.5, 1), (0, 0.75), (0.5, 0.5), (0, 0.25), (0.5, 0))),
        Glyph("8", ((0, 0, 0, 1), (0.5, 0.75))),
        Glyph("9", ((0, 0, 0, 1), (0.5, 0.75), (0, 0.75, 0.5, 0.5))),
        Glyph("10", ((0.5, 0, 0.5, 1), (0, 0.75))),
        Glyph("11", ((0.5, 0, 0.5, 1), (0, 0.75), (0.5, 0.75, 0, 0.5))),
        Glyph("12", ((0.375, 0, 0.375, 1), (0.0, 0.75), (0.375, 1, 0.75, 0.75))),
        Glyph("13", ((0, 0, 0, 1), (0, 0.5, 0.5, 0.5))),
        Glyph("14", ((0, 0, 0, 1), (0, 0.5, 0.5, 0.5), (0, 0.25, 0.5, 0))),
        Glyph("15", ((0.5, 0, 0.5, 1), (0.5, 0.5, 0, 0))),
        Glyph("16", ((0.5, 0, 0.5, 1), (0.5, 0.5, 0, 0), (0.5, 0.25, 0.25, 0))),
        Glyph("17", ((0.375, 0, 0.375, 1), (0.375, 0.5, 0, 0), (0.375, 0.5, 0.75, 0))),
        Glyph("18", ((0, 0, 0, 1), (0, 0.5, 0.5, 1))),
        Glyph("19", ((0, 0, 0, 1), (0, 0.5, 0.5, 1), (0, 0.75, 0.25, 1))),
        Glyph("20", ((0.5, 0, 0.5, 1), (0.5, 0.5, 0, 1))),
        Glyph("21", ((0.5, 0, 0.5, 1), (0.5, 0.5, 0, 1), (0.5, 0.75, 0.25, 1))),
        Glyph("22", ((0.375, 0, 0.375, 1), (0.375, 0.5, 0, 1), (0.375, 0.5, 0.75, 1))),
        Glyph("23", ((0, 0, 0, 1), (0.375, 0.75), (0.75, 1))),
        Glyph(
            "24",
            (
                (0, 0, 0, 1),
                (0.375, 0.75),
                (0.75, 1),
                (0, 0.75, 0.375, 0.5),
                (0.75, 0.75),
            ),
        ),
        Glyph("25", ((0.75, 0, 0.75, 1), (0.375, 0.75), (0, 1))),
        Glyph(
            "26",
            (
                (0.75, 0, 0.75, 1),
                (0.375, 0.75),
                (0, 1),
                (0.75, 0.75, 0.375, 0.5),
                (0, 0.75),
            ),
        ),
        Glyph(
            "27",
            (
                (0.375, 0, 0.375, 1),
                (0.375 / 2, 0.75),
                (0, 1),
                (0.375, 1, 0.375 * 1.5, 0.75),
                (0.75, 1),
            ),
        ),
        Glyph(
            "28",
            ((0, 0, 0, 1), (0.375, 0.75), (0.75, 1), (0, 0, 0.375, 0.25), (0.75, 0)),
        ),
        Glyph("29", ((0, 0, 0, 1), (0, 0.5, 0.5, 1), (0, 0.5, 0.5, 0))),
        Glyph("30", ((0.5, 0, 0.5, 1), (0.5, 0.5, 0, 1), (0.5, 0.5, 0, 0))),
        Glyph("31", ((0.375, 0, 0.375, 1), (0, 0.25, 0.75, 0.75))),
        Glyph("32", ((0.375, 0, 0.375, 1), (0, 0.75, 0.75, 0.25))),
        Glyph("33", ((0.375, 0, 0.375, 1), (0, 0, 0.75, 1), (0, 1, 0.75, 0))),
        Glyph("34", ((0, 0, 0.5, 0.5), (0, 1))),
        Glyph("35", ((0.5, 0, 0, 0.5), (0.5, 1))),
        Glyph("36", ((0, 0, 0.75, 1), (0, 1, 0.75, 0))),
        Glyph(
            "37",
            (
                (0, 0, 0.75, 1),
                (0, 1, 0.75, 0),
                (0, 0.5, 0.375, 0.75 + 0.125),
                (0.75, 0.5),
                (0.375, 0.125),
                (0, 0.5),
            ),
        ),
        Glyph("38", ((0, 0, 0, 1), (0.75, 0), (0.75, 1), (0, 1))),
        Glyph("38-2", ((0, 0, 0, 1), (0.75, 0.75), (0.75, 0, 0.75, 1), (0, 0.75))),
        Glyph("39", ((0, 0, 0, 1),)),
        Glyph("40", ((0, 1, 0, 0.25), (0.5, 0.75), (0.5, 0))),
        Glyph("41", ((0, 0, 0, 0.75), (0.5, 0.25), (0.5, 1))),
        Glyph("42", ((0, 0, 0.75, 0.75), (0.375, 1), (0, 0.75), (0.75, 0))),
        Glyph("43", ((0, 0, 0.5, 0.5), (0, 1), (0.5, 0, 0, 0.5), (0.5, 1))),
        Glyph(
            "44", ((0.25, 0, 0.25, 0.5), (0.5, 0.75), (0.25, 1), (0, 0.75), (0.25, 0.5))
        ),
        Glyph(
            "45",
            (
                (0.25, 0, 0.25, 0.5),
                (0.5, 0.75),
                (0.25, 1),
                (0, 0.75),
                (0.25, 0.5),
                (0, 0.5, 0.5, 0.5),
            ),
        ),
        Glyph("46", ((0, 0, 0, 1), (0.5, 0, 0.5, 1), (0, 0.75, 0.5, 0.5))),
        Glyph(
            "47",
            ((0, 0, 0, 1), (0.5, 0, 0.5, 1), (0, 0.75, 0.5, 0.5), (0, 0.5, 0.5, 0.25)),
        ),
        Glyph("48", ((0, 0, 0, 1), (0.5, 0.75), (0.5, 0), (0, 0.75, 0.5, 0.5))),
        Glyph("49", ((0, 0, 0, 1), (0.5, 0.75), (0.5, 0))),
        Glyph("50", ((0, 0, 0.375, 1), (0.75, 0))),
        Glyph(
            "51",
            (
                (0, 0, 0.375 / 2, 1),
                (0.375 * 1.5, 0),
                (0.375, 0, 0.375 * 1.5, 1),
                (0.75, 0),
            ),
        ),
        Glyph("52", ((0, 0, 0.375, 1), (0.75, 0), (0.375, 0, 0.375, 1))),
        Glyph("53", ((0.375, 0, 0.375, 0.5), (0, 1), (0.375, 0.5, 0.75, 1))),
        Glyph("54", ((0.375, 1, 0.375, 0.5), (0, 0), (0.375, 0.5, 0.75, 0))),
        Glyph("55", ((0, 0, 0, 1), (0, 0.5, 0.5, 0.25))),
        Glyph("56", ((0.5, 0, 0.5, 1), (0.5, 0.5, 0, 0.25))),
        Glyph("57", ((0, 0, 0, 1), (0, 0.75, 0.5, 0.5), (0, 0.25))),
        Glyph("58", ((0.5, 0, 0.5, 1), (0.5, 0.75, 0, 0.5), (0.5, 0.25))),
    ]

    def __init__(self):
        super().__init__("cirth", self.GLYPH_SPACING, self.GLYPHS)


# Certhas Daeron. According to LoR Appendix E:
# "The Certhas Daeron was originally designed to represent the sounds of Sindarin only.
# The oldest cirth were Nos 1, 2, 5, 6, 8, 9, 12; 18, 19, 22; 31, 35, 36; 39, 42, 46, 50
# and a certh varying between 13 and 15.
# The assignment of values was unsystematic. Nos 39, 42, 46, 50 were vowels and remained
# so in all later developments. Nos 13, 15 were used for h or s according as 35 was used
# for s and h."
#
# We arbitrarily assign 35 to s and 13 to h. 15 is unused.
# We also added 49 for "a", as it is a sound used in Sindarin.
CERTHAS_DAERON_MAP_DESC = {
    ("p", "P"): "1",
    ("b", "B"): "2",
    ("hw", "HW"): "5",
    ("m", "M"): "6",
    ("t", "T"): "8",
    ("d", "D"): "9",
    ("n", "N"): "12",
    ("h", "H"): "13",
    ("k", "K"): "18",
    ("g", "G"): "19",
    #    ("n", "N"): "22", # Retroflex nasal ?
    ("l", "L"): "31",
    ("s", "S"): "35",
    ("z", "Z"): "36",
    ("y", "Y"): "39",
    ("u", "U"): "42",
    ("e", "E"): "46",
    ("a", "A"): "49",
    ("o", "O"): "50",
}

# Angerthas Daeron = Certhas Daeron plus many additions
# "The extension and elaboration of this certhas was called in its older
# form the Angerthas Daeron, since the addiion to the old cirth and their
# reorganization was attributed to Daeron. The principal additions however
# the introduction of two new series 13-17 and 23-28 were actually most
# probably inventions of the Nolder of Eregion, since they were used for the
# representation of sounds not found in Sindarin."
#
# We still arbitrarily assign 35 to s and 13 to h. 15 unused.
ANGERTHAS_DAERON_MAP_DESC = {
    ("p", "P"): "1",
    ("b", "B"): "2",
    ("f", "F"): "3",
    ("v", "V"): "4",
    ("hw", "HW"): "5",
    ("m", "M"): "6",
    ("mb", "MB", "mh", "MH"): "7",  # MH only used for Elvish
    ("t", "T"): "8",
    ("d", "D"): "9",
    ("th", "TH"): "10",
    ("dh", "DH"): "11",
    ("n", "N"): "12",
    ("ch", "CH"): "13",
    ("j", "J"): "14",
    ("sh", "SH"): "15",
    ("zh", "ZH"): "16",
    ("nj", "NJ"): "17",
    ("k", "K"): "18",
    ("g", "G"): "19",
    ("kh", "KH"): "20",
    ("gh", "GH"): "21",
    #    ("n", "N"): "22", # Retroflex nasal ?
    ("kw", "KW"): "23",
    ("gw", "GW"): "24",
    ("khw", "KHW"): "25",
    ("ghw", "GHW"): "26",
    ("ngw", "NGW"): "27",
    ("nw", "NW"): "28",
    ("r", "R"): "29",
    ("rh", "RH"): "30",
    ("l", "L"): "31",
    ("lh", "LH"): "32",
    ("ng", "NG"): "33",
    ("s", "S"): "35",
    ("z", "Z"): "36",
    ("nd", "ND"): "38",
    ("y", "Y", "i", "I"): "39",
    ("u", "U"): "42",
    ("w", "W"): "44",
    ("e", "E"): "46",
    ("a", "A"): "49",
    ("o", "O"): "50",
    ("h", "H"): "54",
}

# Angerthas Moria: Angerthas daeron adapted by the Moria dwarves
# "The dwarves of Moria, as can be seen, introduced a number of unsystematic
# changes in value, as well as certain new cirth: 37, 40, 41, 45, 53, 55, 56.
# The dislocation in values was due mainly to two causes: (I) the alteration in
# the values of 34, 35 respectively to h (the clear or glottal beginning of a
# word with an initial vowel that appeared in Khuzdul), and s; (2) the abandonment
# of the Nos 14, 16 for which the Dwarves substituted 29, 30.
# The consequent use of 12 for r, the invention of 53 for n (and its confusion
# with 22); the use of 17 as z, to go with 54 in its value s, and the
# consequent use of 36 as n and the new certh 37 for ng may also be observed.
# The new 55, 56 were originally a halved form of 46 and were used for vowels
# like those heard in English butter, which were frequent in Dwarvish and in
# the Westron. When weak or evanescent they were often reduced to a mere stroke
# without a stem. This Angerthas Moria is represented in the tomb-inscription.
#
# So:
# - 13 becomes ch. 34 becomes h.
# - 14 (j) and 16 (zh) are removed and replaced by 29 (j) and 30 (zh)
# - 12 (n) is now given value r. 36 becomes n (retroflex nasal).
# - 17 (nj) becomes z.
# - 22 stays for n (confused with 53 but generally used by Tolkien).
# - 54 (h) becomes s.
# - 33 (ng) becomes nd. 37 is ng
# - 38 (nd) becomes nj
ANGERTHAS_MORIA_MAP_DESC = {
    ("p", "P"): "1",
    ("b", "B"): "2",
    ("f", "F"): "3",
    ("v", "V"): "4",
    ("hw", "HW"): "5",
    ("m", "M"): "6",
    ("mb", "MB", "mh", "MH"): "7",  # MH only used for Elvish
    ("t", "T"): "8",
    ("d", "D"): "9",
    ("th", "TH"): "10",
    ("dh", "DH"): "11",
    ("r", "R"): "12",
    ("ch", "CH"): "13",
    ("sh", "SH"): "15",
    ("z", "Z"): "17",
    ("k", "K"): "18",
    ("g", "G"): "19",
    ("kh", "KH"): "20",
    ("gh", "GH"): "21",
    ("n", "N"): "22",  # Confused with 53 ?
    ("kw", "KW"): "23",
    ("gw", "GW"): "24",
    ("khw", "KHW"): "25",
    ("ghw", "GHW"): "26",
    ("ngw", "NGW"): "27",
    ("nw", "NW"): "28",
    ("j", "J"): "29",
    ("zh", "ZH"): "30",
    ("l", "L"): "31",
    ("lh", "LH"): "32",
    ("nd", "ND"): "33",
    ("h", "H"): "34",
    ("s", "S"): "35",
    # ("n", "N"): "36", # Retroflex nasal
    ("ng", "NG"): "37",
    ("nj", "NJ"): "38",
    ("i", "I"): "39",
    ("y", "Y"): "40",
    ("hy", "HY"): "41",
    ("u", "U"): "42",
    ("w", "W"): "44",
    ("e", "E"): "46",
    ("a", "A"): "49",
    ("o", "O"): "50",
    # ("n", "N"): "53",
    ("s", "S"): "54",
}

# Angerthas Erebor
# "The Dwarves of Erebor used a further modification of this system, known as the
# mode of Erebor, and exemplified in the Book of Mazarbul. Its chief characteristics
# were: the use of 43 as z; of 17 as ks (x); and the invention of two new cirth
# 57 and 58 for ps and ts. They also reintroduced 14, 16 for the values j, zh; but
# used 29, 30 for g, gh, or as mere variant of 19, 21."
#
# 17 (z) becomes ks (x). 43 is used for z.
# 14 (j) and 16 (zh) are back.
# 19 (g) and 21 (gh) are replaced by 29 and 30
ANGERTHAS_EREBOR_MAP_DESC = {
    ("p", "P"): "1",
    ("b", "B"): "2",
    ("f", "F"): "3",
    ("v", "V"): "4",
    ("hw", "HW"): "5",
    ("m", "M"): "6",
    ("mb", "MB", "mh", "MH"): "7",  # MH only used for Elvish
    ("t", "T"): "8",
    ("d", "D"): "9",
    ("th", "TH"): "10",
    ("dh", "DH"): "11",
    ("r", "R"): "12",
    ("ch", "CH"): "13",
    ("j", "J"): "14",
    ("sh", "SH"): "15",
    ("zh", "ZH"): "16",
    ("ks", "KS", "x", "X"): "17",
    ("k", "K"): "18",
    ("kh", "KH"): "20",
    ("n", "N"): "22",  # Confused with 53 ?
    ("kw", "KW"): "23",
    ("gw", "GW"): "24",
    ("khw", "KHW"): "25",
    ("ghw", "GHW"): "26",
    ("ngw", "NGW"): "27",
    ("nw", "NW"): "28",
    ("g", "G"): "29",
    ("gh", "GH"): "30",
    ("l", "L"): "31",
    ("lh", "LH"): "32",
    ("nd", "ND"): "33",
    ("h", "H"): "34",
    ("s", "S"): "35",
    # ("n", "N"): "36", # Retroflex nasal
    ("ng", "NG"): "37",
    ("nj", "NJ"): "38",
    ("i", "I"): "39",
    ("y", "Y"): "40",
    ("hy", "HY"): "41",
    ("u", "U"): "42",
    ("z", "Z"): "43",
    ("w", "W"): "44",
    ("e", "E"): "46",
    ("a", "A"): "49",
    ("o", "O"): "50",
    # ("n", "N"): "53",
    ("s", "S"): "54",
}

FONT = Cirth()
