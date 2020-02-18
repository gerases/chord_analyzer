#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chord_finder.common import ENHARM_SHARP_MODE
from chord_finder.utils import spell_pitch_enharmonically
from chord_finder.utils import str2list
from chord_finder.utils import musical_to_dec
from chord_finder.utils import dec_to_musical
from chord_finder.utils import get_distance_in_semitones


def test_str2list():
    assert str2list('a b c') == ['a', 'b', 'c']


def test_enharnomonic_spelling():
    # 'c' written in terms of 'b' is 'b+'
    assert spell_pitch_enharmonically('c', 'b', ENHARM_SHARP_MODE) == 'b+'

    # 'c' written in terms of 'a' is 'a+++'
    assert spell_pitch_enharmonically('c', 'a', ENHARM_SHARP_MODE) == 'a+++'

    # 'f' written in terms of 'e' is 'e+'
    assert spell_pitch_enharmonically('f', 'e', ENHARM_SHARP_MODE) == 'e+'


def test_musical_to_dec():
    assert musical_to_dec('a') == 10
    assert musical_to_dec('1') == 1


def test_dec_to_musical():
    for dec in range(1, 10):  # 10 is not included
        assert dec_to_musical(dec) == dec
    assert dec_to_musical(10) == 'a'
    assert dec_to_musical(11) == 'b'
    assert dec_to_musical(12) == 'c'


def test_distance_in_semitones():
    assert get_distance_in_semitones('c', 'c') == 0
    assert get_distance_in_semitones('c', 'c+') == 1
    assert get_distance_in_semitones('c', 'd-') == 1
    assert get_distance_in_semitones('c', 'd') == 2
    assert get_distance_in_semitones('c', 'd+') == 3
    assert get_distance_in_semitones('c', 'e-') == 3
    assert get_distance_in_semitones('c', 'e') == 4
    assert get_distance_in_semitones('c', 'e+') == 5
    assert get_distance_in_semitones('c', 'f') == 5
    assert get_distance_in_semitones('c', 'f+') == 6
    assert get_distance_in_semitones('c', 'g-') == 6
    assert get_distance_in_semitones('c', 'g') == 7
    assert get_distance_in_semitones('c', 'g+') == 8
    assert get_distance_in_semitones('c', 'a-') == 8
    assert get_distance_in_semitones('c', 'a') == 9
    assert get_distance_in_semitones('c', 'a+') == 10
    assert get_distance_in_semitones('c', 'b') == 11
    assert get_distance_in_semitones('c', 'b-') == 10

    assert get_distance_in_semitones('b', 'c') == 1
    assert get_distance_in_semitones('b', 'b+') == 1

    assert get_distance_in_semitones('a', 'c') == 3
    assert get_distance_in_semitones('a', 'e-') == 6
    assert get_distance_in_semitones('a', 'g-') == 9
