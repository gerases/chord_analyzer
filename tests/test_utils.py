#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from chord_finder.common import ENHARM_FLAT_MODE
# from chord_finder.utils import distances_to_symbols, musical_to_dec
from chord_finder.common import ENHARM_SHARP_MODE
from chord_finder.utils import spell_pitch_enharmonically
from chord_finder.utils import find_pitches_in_scale
from chord_finder.major_scale import MajorScale


def test_find_pitches_in_scale():
    pitches = ['c', 'e', 'g']
    scale = MajorScale('c', ENHARM_SHARP_MODE)
    result = find_pitches_in_scale(pitches, scale)
    expected = [
                '%s-%s-%s' % (
                    m['scale_degree'],
                    m['scale_member'],
                    scale.get_member_distance(m['scale_member']))
                for m in result]
    assert expected == ['1-c-0', '3-e-4', '5-g-7']


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


# def test_distances_to_symbols():
#     assert distances_to_symbols('a', ['3', '7'], ENHARM_SHARP_MODE) == 'ace'
#     # assert distances_to_symbols('a', ['4', '7'], ENHARM_SHARP_MODE) == 'ac+e'
#     # assert distances_to_symbols('e-', ['4', '7'], ENHARM_FLAT_MODE) == 'e-gb-'


# def test_input_parsing():
#     assert parse_input('') == []
#     with pytest.raises(Exception) as error:
#         parse_input('y')
#     assert 'Illegal char' in str(error.value)
#     # '+' and '-' are only modifiers and must have
#     # an a-g preceding them
#     with pytest.raises(Exception) as error:
#         parse_input('+')
#     assert 'Error parsing input at position' in str(error.value)
#     assert parse_input('a+-') == ['a+-']
#     assert parse_input('a+b-') == ['a+', 'b-']
#     assert parse_input('a+-+++b-') == ['a+-+++', 'b-']


# def test_dec_to_musical():
#     for dec in range(1, 10):  # 10 is not included
#         assert dec_to_musical(dec) == dec
#     assert dec_to_musical(10) == 'a'
#     assert dec_to_musical(11) == 'b'
#     assert dec_to_musical(12) == 'c'


# def test_distance_in_semitones():
#     assert get_distance_in_semitones('c', 'c') == 0
#     assert get_distance_in_semitones('c', 'c+') == 1
#     assert get_distance_in_semitones('c', 'd-') == 1
#     assert get_distance_in_semitones('c', 'd') == 2
#     assert get_distance_in_semitones('c', 'd+') == 3
#     assert get_distance_in_semitones('c', 'e-') == 3
#     assert get_distance_in_semitones('c', 'e') == 4
#     assert get_distance_in_semitones('c', 'e+') == 5
#     assert get_distance_in_semitones('c', 'f') == 5
#     assert get_distance_in_semitones('c', 'f+') == 6
#     assert get_distance_in_semitones('c', 'g-') == 6
#     assert get_distance_in_semitones('c', 'g') == 7
#     assert get_distance_in_semitones('c', 'g+') == 8
#     assert get_distance_in_semitones('c', 'a-') == 8
#     assert get_distance_in_semitones('c', 'a') == 9
#     assert get_distance_in_semitones('c', 'a+') == 10
#     assert get_distance_in_semitones('c', 'b') == 11
#     assert get_distance_in_semitones('c', 'b-') == 10

#     assert get_distance_in_semitones('b', 'c') == 1
#     assert get_distance_in_semitones('b', 'b+') == 1

#     assert get_distance_in_semitones('a', 'c') == 3
#     assert get_distance_in_semitones('a', 'e-') == 6
#     assert get_distance_in_semitones('a', 'g-') == 9


# def test_simple_major():
#     assert analyze(['a', 'c+', 'e']) == {'A major': 'ac+e'}
#     assert analyze(['c', 'e', 'g']) == {'C major': 'ceg'}
#     assert analyze(['c', 'g', 'e']) == {'C major': 'ceg'}
#     assert analyze(['g', 'c', 'e']) == {'C major': 'ceg'}
#     assert analyze(['c-', 'e-', 'g-']) == {'C- major': 'c-e-g-'}


# def test_minor():
#     assert analyze(['e', 'g', 'b']) == {'E minor': 'egb'}
#     assert analyze(['e', 'b', 'g']) == {'E minor': 'egb'}
#     assert analyze(['g', 'b', 'e']) == {'E minor': 'egb'}


# def test_diminished():
#     assert analyze(['b', 'd', 'f']) == {'B diminished': 'bdf'}
#     assert analyze(['f', 'd', 'b']) == {'B diminished': 'bdf'}
#     assert analyze(['d', 'f', 'b']) == {'B diminished': 'bdf'}


# def test_augmented():
#     assert analyze(['c', 'e', 'g+']) == {'C augmented': 'ceg+',
#                                          'E augmented': 'eg+c',
#                                          'G+ augmented': 'g+ce'}


# def test_sus2():
#     assert analyze(['c', 'd', 'g']) == {'C sus2': 'cdg',
#                                         'G sus4': 'gcd'}


# def test_sus4():
#     assert analyze(['c', 'f', 'g']) == {'C sus4': 'cfg',
#                                         'F sus2': 'fgc'}


# def test_dominant_7th():
#     assert analyze(['a', 'c+', 'e', 'g']) == {'A dominant 7th': 'ac+eg'}


# def test_major_7th():
#     assert analyze(['a', 'c+', 'e', 'g+']) == {'A major 7th': 'ac+eg+'}
#     assert analyze(['b', 'd+', 'f+', 'a+']) == {'B major 7th': 'bd+f+a+'}


# def test_minor_7th():
#     assert analyze(['a', 'c', 'e', 'g']) == {'A minor 7th': 'aceg',
#                                              'C major 13th': 'cega'}


# def test_half_diminished_7th():
#     assert analyze(['a', 'c', 'e-', 'g']) == {'A half diminished 7th': 'ace-g'}


# def test_diminished_7th():
#     assert analyze(['a', 'c', 'e-', 'g-']) == {'A diminished 7th': 'ace-g-',
#                                                'C diminished 7th': 'ce-g-a',
#                                                'E- diminished 7th': 'e-g-ac',
#                                                'G- diminished 7th': 'g-ace-'}


# def test_major_ninth():
#     assert analyze(['c', 'e', 'g', 'd']) == {'C major 9th': 'cegd'}


# def test_major_eleventh():
#     assert analyze(['c', 'e', 'g', 'f']) == {'C major 11th': 'cegf'}


# def test_major_thirteenth():
#     assert analyze(['c', 'e', 'g', 'a']) == {'C major 13th': 'cega',
#                                              'A minor 7th': 'aceg'}
