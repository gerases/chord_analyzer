#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
from chord_finder.scales.major_scale import MajorScale
from chord_finder.common import ENHARM_SHARP_MODE
from chord_finder.common import ENHARM_FLAT_MODE
from chord_finder.utils import str2list


def test_build_major_sharp_scales():
    with open('tests/data/major_sharp_scales.yaml') as handle:
        data = yaml.load(handle, Loader=yaml.FullLoader)

    scales = data['scales']
    for root in scales:
        scale = MajorScale(root, ENHARM_SHARP_MODE)
        assert scale.get_members() == scales[root]


def test_build_major_flat_scales():
    with open('tests/data/major_flat_scales.yaml') as handle:
        data = yaml.load(handle, Loader=yaml.FullLoader)

    scales = data['scales']
    for root in scales:
        scale = MajorScale(root, ENHARM_FLAT_MODE)
        assert scale.get_members() == scales[root]


def test_member_to_distance():
    scale = MajorScale('c')
    assert scale.get_member_distance('c') == '0'
    assert scale.get_member_distance('d') == '2'
    assert scale.get_member_distance('e') == '4'
    assert scale.get_member_distance('f') == '5'
    assert scale.get_member_distance('g') == '7'
    assert scale.get_member_distance('a') == '9'
    assert scale.get_member_distance('b') == 'b'


def test_fit_pitches_to_scale():
    scale = MajorScale('c')
    pitches = ['c', 'd', 'e', 'f', 'g', 'a', 'b',
               'c', 'd', 'e', 'f', 'g', 'a', 'b']
    matches = scale.fit_pitches_in_scale(pitches)
    expected = ['%s-%s-%s' % (m['degree'], m['pitch'], m['distance'])
                for m in matches]
    assert expected == [
                '1-c-0',
                '2-d-2',
                '3-e-4',
                '4-f-5',
                '5-g-7',
                '6-a-9',
                '7-b-b',
                '8-c-c',   # 12
                '9-d-e',   # 14
                '10-e-g',  # 16
                '11-f-h',  # 17
                '12-g-j',  # 19
                '13-a-l',  # 21
                '14-b-n',  # 23
                ]

    # c+ is not in the scale, so no matches should be returned
    pitches = ['c+']
    assert scale.fit_pitches_in_scale(pitches) == []


def test_identify_chord():
    scale = MajorScale('c')
    assert scale.identify_chord(str2list('c e g'))[0] == 'C major'
    assert scale.identify_chord(str2list('d f a'))[0] == 'D minor'
    assert scale.identify_chord(str2list('e g b'))[0] == 'E minor'
    assert scale.identify_chord(str2list('f a c'))[0] == 'F major'
    assert scale.identify_chord(str2list('g b d'))[0] == 'G major'
    assert scale.identify_chord(str2list('a c e'))[0] == 'A minor'
    assert scale.identify_chord(str2list('b d f'))[0] == 'B diminished'


def test_get_triads():
    scale = MajorScale('c')
    triads = ["%s %s [%s]" % (triad['roman'], triad['pitches'], triad['name'])
              for triad in scale.get_all_triads()]
    assert triads == [
        'I ceg [C major]',
        'ii dfa [D minor]',
        'iii egb [E minor]',
        'IV fac [F major]',
        'V gbd [G major]',
        'vi ace [A minor]',
        'vii bdf [B diminished]',
    ]
