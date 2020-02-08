#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import pytest
from chord_finder.NonAccidentalIter import NonAccidentalIter


def test_less_than_7():
    expect = ['a', 'b', 'c']
    actual = []
    for pitch in NonAccidentalIter('a', 3):
        actual.append(pitch)
    assert expect == actual


def test_7():
    expect = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    actual = []
    for pitch in NonAccidentalIter('a', 7):
        actual.append(pitch)
    assert expect == actual


def test_more_than_7():
    expect = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a']
    actual = []
    for pitch in NonAccidentalIter('a', 8):
        actual.append(pitch)
    assert expect == actual
