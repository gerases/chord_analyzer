#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Global contants"""

PITCHES = ['c', 'c+', 'd', 'd+', 'e', 'f', 'f+', 'g', 'g+', 'a', 'a+', 'b']
PITCHES_FLAT = ['c', 'b', 'b-', 'a', 'a-', 'g', 'g-', 'f', 'e', 'e-', 'd',
                'd-']
SHARP_KEYS = ['c', 'g', 'd', 'a', 'e', 'b', 'f+', 'c+', 'g+', 'd+', 'a+',
              'e+', 'b+']
FLAT_KEYS = ['f', 'b-', 'e-', 'a-', 'd-', 'g-']
MAX_DISTANCE = 40
ENHARM_FLAT_MODE = 'flat'
ENHARM_SHARP_MODE = 'sharp'

DISTANCE_TO_NAME = {
    1: 'minor second',
    2: 'major second',
    3: 'minor third',
    4: 'major third',
    5: 'perfect fourth',
    6: 'diminished fifth',
    7: 'perfect fifth',
    8: 'minor sixth',
    9: 'major sixth',
    'a': 'minor seventh',     # 10
    'b': 'major seventh',     # 11
    'c': 'major seventh',     # 12
    'd': 'major seventh',     # 13
    'e': 'major ninth',       # 14
    'f': 'major ninth',       # 15
    'g': 'major ninth',       # 16
    'h': 'major eleventh',    # 17
    'i': 'major eleventh',    # 18
    'j': 'major eleventh',    # 19
    'k': 'major eleventh',    # 20
    'l': 'major thirteenth',  # 21
    'm': 'major thirteenth',  # 22
    'n': 'major thirteenth',  # 23
}

SHARP_TO_FLAT = {
    'c+': 'd-',
    'd+': 'e-',
    'e+': 'f-',
    'f+': 'g-',
    'g+': 'a-',
    'a+': 'b-',
}
