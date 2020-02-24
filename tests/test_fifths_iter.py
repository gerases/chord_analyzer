#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import pytest
from chord_finder.iterators.fifths_iter import FifthsIter


def test_fifths_iter():
    expect = ['g', 'd', 'a', 'e', 'b', 'f+',
              'd-', 'a-', 'e-', 'b-', 'f', 'c']
    actual = []

    for pitch in FifthsIter('c', 12):
        actual.append(pitch)
    assert expect == actual
