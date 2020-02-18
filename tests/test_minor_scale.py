#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chord_finder.minor_scale import MinorScale


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
