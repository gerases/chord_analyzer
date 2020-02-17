#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Global contants"""

PITCHES = ['c', 'c+', 'd', 'd+', 'e', 'f', 'f+', 'g', 'g+', 'a', 'a+', 'b']
PITCHES_FLAT = ['c', 'b', 'b-', 'a', 'a-', 'g', 'g-', 'f', 'e', 'e-', 'd',
                'd-']
SHARP_KEYS = ['c', 'g', 'd', 'a', 'e', 'b', 'f+', 'c+', 'g+', 'd+', 'a+',
              'e+', 'b+']
FLAT_KEYS = ['f', 'b-', 'e-', 'a-', 'd-', 'g-']
MAX_DISTANCE = 23
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

CHORD_PATTERNS = {
    '47': 'major',
    '37': 'minor',
    '48': 'augmented',
    '36': 'diminished',
    '27': 'sus2',
    '57': 'sus4',
    '47a': 'dominant 7th',
    '47b': 'major 7th',
    '37a': 'minor 7th',
    '36a': 'half diminished 7th',
    '369': 'diminished 7th',
    '47e': 'major 9th',
    '47h': 'major 11th',
    '47l': 'major 13th',
}

DEC_TO_ROMAN = {
    1: 'i',
    2: 'ii',
    3: 'iii',
    4: 'iv',
    5: 'v',
    6: 'vi',
    7: 'vii',
}
