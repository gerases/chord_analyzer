#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
from chord_finder.minor_scale import MinorScale
from chord_finder.common import ENHARM_SHARP_MODE
from chord_finder.common import ENHARM_FLAT_MODE
from chord_finder.utils import str2list


def test_build_minor_sharp_scales():
    mode = ENHARM_SHARP_MODE
    with open('tests/data/minor_sharp_scales.yaml') as handle:
        data = yaml.load(handle, Loader=yaml.FullLoader)

    scales = data['scales']
    for root in scales:
        scale = MinorScale(root, mode)
        assert scale.get_members() == scales[root]


def test_build_minor_flat_scales():
    mode = ENHARM_FLAT_MODE
    with open('tests/data/minor_flat_scales.yaml') as handle:
        data = yaml.load(handle, Loader=yaml.FullLoader)

    scales = data['scales']
    for root in scales:
        scale = MinorScale(root, mode)
        assert scale.get_members() == scales[root]


def test_member_to_distance():
    scale = MinorScale('a')
    assert scale.get_member_distance('a') == '0'
    assert scale.get_member_distance('b') == '2'
    assert scale.get_member_distance('c') == '3'
    assert scale.get_member_distance('d') == '5'
    assert scale.get_member_distance('e') == '7'
    assert scale.get_member_distance('f') == '8'
    assert scale.get_member_distance('g') == 'a'


def test_identify_chord():
    scale = MinorScale('a')
    assert scale.identify_chord(str2list('a c e'))[0] == 'A minor'
    assert scale.identify_chord(str2list('b d f'))[0] == 'B diminished'
    assert scale.identify_chord(str2list('c e g'))[0] == 'C major'
    assert scale.identify_chord(str2list('d f a'))[0] == 'D minor'
    assert scale.identify_chord(str2list('e g b'))[0] == 'E minor'
    assert scale.identify_chord(str2list('f a c'))[0] == 'F major'
    assert scale.identify_chord(str2list('g b d'))[0] == 'G major'


def test_get_triads():
    scale = MinorScale('a')
    triads = ["%s %s [%s]" % (triad['roman'], triad['pitches'], triad['name'])
              for triad in scale.get_all_triads()]
    assert triads == [
        'i ace [A minor]',
        'ii bdf [B diminished]',
        'III ceg [C major]',
        'iv dfa [D minor]',
        'v egb [E minor]',
        'VI fac [F major]',
        'VII gbd [G major]',
    ]
