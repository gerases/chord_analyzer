#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
from chord_finder.major_scale import MajorScale
from chord_finder.common import ENHARM_SHARP_MODE, ENHARM_FLAT_MODE
from chord_finder.utils import spell_pitch_enharmonically


def test_enharnomonic_spelling():
    # 'c' written in terms of 'b' is 'b+'
    assert spell_pitch_enharmonically('c', 'b', ENHARM_SHARP_MODE) == 'b+'

    # 'c' written in terms of 'a' is 'a+++'
    assert spell_pitch_enharmonically('c', 'a', ENHARM_SHARP_MODE) == 'a+++'

    # 'f' written in terms of 'e' is 'e+'
    assert spell_pitch_enharmonically('f', 'e', ENHARM_SHARP_MODE) == 'e+'


def test_build_major_sharp_scales():
    mode = ENHARM_SHARP_MODE
    with open('tests/data/major_sharp_scales.yaml') as handle:
        data = yaml.load(handle, Loader=yaml.FullLoader)

    scales = data['scales']
    for root in scales:
        scale = MajorScale(root, mode)
        assert scale.get_members() == scales[root]


def test_build_major_flat_scales():
    mode = ENHARM_FLAT_MODE
    with open('tests/data/major_flat_scales.yaml') as handle:
        data = yaml.load(handle, Loader=yaml.FullLoader)

    scales = data['scales']
    for root in scales:
        scale = MajorScale(root, mode)
        assert scale.get_members() == scales[root]


def test_member_to_distance():
    scale = MajorScale('c', ENHARM_SHARP_MODE)
    assert scale.get_member_distance('c') == '0'
    assert scale.get_member_distance('d') == '2'
    assert scale.get_member_distance('e') == '4'
    assert scale.get_member_distance('f') == '5'
    assert scale.get_member_distance('g') == '7'
    assert scale.get_member_distance('a') == '9'
    assert scale.get_member_distance('b') == 'b'
