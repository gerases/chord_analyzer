#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
