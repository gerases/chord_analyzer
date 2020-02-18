#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
from chord_finder.minor_scale import MinorScale
from chord_finder.common import ENHARM_SHARP_MODE
from chord_finder.common import ENHARM_FLAT_MODE


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
