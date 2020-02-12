#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import pytest
from chord_finder.scale_iter import ScaleIter
from chord_finder.major_scale import MajorScale
from chord_finder.common import ENHARM_FLAT_MODE


def test_less_than_7():
    scale = MajorScale('f', ENHARM_FLAT_MODE)
    expect = ['f', 'g', 'a']
    actual = []

    for pitch in ScaleIter(scale, start='f', limit=3):
        actual.append(pitch)
    assert expect == actual


def test_7():
    scale = MajorScale('f', ENHARM_FLAT_MODE)
    expect = ['f', 'g', 'a', 'b-', 'c', 'd', 'e']
    actual = []
    for pitch in ScaleIter(scale, start='f', limit=7):
        actual.append(pitch)
    assert expect == actual


def test_more_than_7():
    scale = MajorScale('f', ENHARM_FLAT_MODE)
    expect = ['f', 'g', 'a', 'b-', 'c', 'd', 'e', 'f']
    actual = []
    for pitch in ScaleIter(scale, start='f', limit=8):
        actual.append(pitch)
    assert expect == actual
