#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chord_finder.MajorScale import MajorScale
from chord_finder.common import ENHARM_SHARP_MODE, ENHARM_FLAT_MODE
import yaml

# def test_enharnomonic_spelling():
#     # 'c' written in terms of 'b' is 'b+'
#     assert spell_pitch_enharmonically('c', 'b', ENHARM_SHARP_MODE) == 'b+'

#     # 'c' written in terms of 'a' is 'a+++'
#     assert spell_pitch_enharmonically('c', 'a', ENHARM_SHARP_MODE) == 'a+++'

#     # 'f' written in terms of 'e' is 'e+'
#     assert spell_pitch_enharmonically('f', 'e', ENHARM_SHARP_MODE) == 'e+'


def test_build_major_sharp_scales():
    mode = ENHARM_SHARP_MODE
    with open('tests/data/major_sharp_scales.yaml') as file:
        data = yaml.load(file)

    for root in data:
        print(root)


# def test_build_major_flat_scales():
#     mode = ENHARM_FLAT_MODE
#     assert build_major_scale('f', mode) == ['f', 'g', 'a', 'b-', 'c', 'd',
#                                             'e']
#     assert build_major_scale('b-', mode) == ['b-', 'c', 'd', 'e-', 'f', 'g',
#                                              'a']
#     assert build_major_scale('e-', mode) == ['e-', 'f', 'g', 'a-', 'b-', 'c',
#                                              'd']
#     assert build_major_scale('a-', mode) == ['a-', 'b-', 'c', 'd-', 'e-', 'f',
#                                              'g']
#     assert build_major_scale('d-', mode) == ['d-', 'e-', 'f', 'g-', 'a-', 'b-',
#                                              'c']
#     assert build_major_scale('g-', mode) == ['g-', 'a-', 'b-', 'c-', 'd-',
#                                              'e-', 'f']
#     assert build_major_scale('c-', mode) == ['c-', 'd-', 'e-', 'f-', 'g-',
#                                              'a-', 'b-']
#     assert build_major_scale('f-', mode) == ['f-', 'g-', 'a-', 'b--', 'c-',
#                                              'd-', 'e-']
#     assert build_major_scale('b--', mode) == ['b--', 'c-', 'd-', 'e--', 'f-',
#                                               'g-', 'a-']
#     assert build_major_scale('e--', mode) == ['e--', 'f-', 'g-', 'a--', 'b--',
#                                               'c-', 'd-']
#     assert build_major_scale('a--', mode) == ['a--', 'b--', 'c-', 'd--', 'e--',
#                                               'f-', 'g-']
#     assert build_major_scale('d--', mode) == ['d--', 'e--', 'f-', 'g--', 'a--',
#                                               'b--', 'c-']
