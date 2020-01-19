#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ChordFinder
from ChordFinder import get_distance_in_semitones, dec_to_musical
from ChordFinder import analyze


def test_dec_to_musical():
    for dec in range(1, 10):  # 10 is not included
        assert dec_to_musical(dec) == dec
    assert dec_to_musical(10) == 'a'
    assert dec_to_musical(11) == 'b'
    assert dec_to_musical(12) == 'c'


def test_distance_in_semitones():
    assert get_distance_in_semitones('c', 'c') == 0
    assert get_distance_in_semitones('c', 'c#') == 1
    assert get_distance_in_semitones('c', 'db') == 1
    assert get_distance_in_semitones('c', 'd') == 2
    assert get_distance_in_semitones('c', 'd#') == 3
    assert get_distance_in_semitones('c', 'eb') == 3
    assert get_distance_in_semitones('c', 'e') == 4
    assert get_distance_in_semitones('c', 'e#') == 5
    assert get_distance_in_semitones('c', 'f') == 5
    assert get_distance_in_semitones('c', 'f#') == 6
    assert get_distance_in_semitones('c', 'gb') == 6
    assert get_distance_in_semitones('c', 'g') == 7
    assert get_distance_in_semitones('c', 'g#') == 8
    assert get_distance_in_semitones('c', 'ab') == 8
    assert get_distance_in_semitones('c', 'a') == 9
    assert get_distance_in_semitones('c', 'a#') == 10
    assert get_distance_in_semitones('c', 'b') == 11
    assert get_distance_in_semitones('c', 'bb') == 10

    assert get_distance_in_semitones('b', 'c') == 1
    assert get_distance_in_semitones('b', 'b#') == 1

    assert get_distance_in_semitones('a', 'c') == 3
    assert get_distance_in_semitones('a', 'eb') == 6
    assert get_distance_in_semitones('a', 'gb') == 9


def test_major():
    assert analyze(['a', 'c#', 'e']) == ['A major']
    assert analyze(['c', 'e', 'g']) == ['C major']
    assert analyze(['c', 'g', 'e']) == ['C major']
    assert analyze(['g', 'c', 'e']) == ['C major']


def test_minor():
    assert analyze(['e', 'g', 'b']) == ['E minor']
    assert analyze(['e', 'b', 'g']) == ['E minor']
    assert analyze(['g', 'b', 'e']) == ['E minor']


def test_diminished():
    assert analyze(['b', 'd', 'f']) == ['B diminished']
    assert analyze(['f', 'd', 'b']) == ['B diminished']
    assert analyze(['d', 'f', 'b']) == ['B diminished']


def test_augmented():
    assert analyze(['c', 'e', 'g#']) == ['C augmented',
                                         'E augmented',
                                         'G# augmented']


def test_sus2():
    assert analyze(['c', 'd', 'g']) == ['C sus2', 'G sus4']


def test_sus4():
    assert analyze(['c', 'f', 'g']) == ['C sus4', 'F sus2']


def test_dominant_7th():
    assert analyze(['a', 'c#', 'e', 'g']) == ['A dominant 7th']


def test_major_7th():
    assert analyze(['a', 'c#', 'e', 'g#']) == ['A major 7th']


def test_minor_7th():
    assert analyze(['a', 'c', 'e', 'g']) == ['A minor 7th',
                                             'C major 13th']


def test_half_diminished_7th():
    assert analyze(['a', 'c', 'eb', 'g']) == ['A half diminished 7th']


def test_diminished_7th():
    assert analyze(['a', 'c', 'eb', 'gb']) == ['A diminished 7th',
                                               'C diminished 7th',
                                               'Eb diminished 7th',
                                               'Gb diminished 7th']


def test_major_ninth():
    assert analyze(['c', 'e', 'g', 'd']) == ['C major 9th']


def test_major_eleventh():
    assert analyze(['c', 'e', 'g', 'f']) == ['C major 11th']


def test_major_thirteenth():
    assert analyze(['c', 'e', 'g', 'a']) == ['C major 13th',
                                             'A minor 7th']
