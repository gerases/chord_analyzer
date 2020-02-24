#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chord_finder.iterators.harmonic_iter import HarmonicIter


class FifthsIter:
    # Constructor
    def __init__(self, start, limit=0):
        self.total_iterations = 0
        self.limit = limit
        self.current_5th = start

    # Called when iteration is initialized
    def __iter__(self):
        return self

    def __next__(self):
        current_5th = self.current_5th
        self.total_iterations += 1
        if self.limit > 0 and self.total_iterations > self.limit:
            raise StopIteration
        harmonic_iter = HarmonicIter(self.current_5th, 8)
        for pitch in harmonic_iter:
            self.current_5th = pitch
        return current_5th
