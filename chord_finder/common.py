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
    'e': 'major ninth',       # 14
    'h': 'major eleventh',    # 17
    'l': 'major thirteenth',  # 21
}

SHARP_TO_FLAT = {
    'c+': 'd-',
    'd+': 'e-',
    'e+': 'f-',
    'f+': 'g-',
    'g+': 'a-',
    'a+': 'b-',
}
