#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import pytest
from chord_finder.iterators.harmonic_iter import HarmonicIter
from chord_finder.common import PITCHES


def test_harmonic_iter():
    expect = PITCHES
    expect.append('c')
    expect.append('d')
    actual = []

    for pitch in HarmonicIter('c', len(expect)):
        actual.append(pitch)
    assert expect == actual
