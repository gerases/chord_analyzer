#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chord_finder.common import PITCHES


class HarmonicIter:
    # Constructor
    def __init__(self, start, limit=0):
        self.pitch_set = PITCHES
        self.index = self.pitch_set.index(start)
        self.total_iterations = 0
        self.limit = limit

    # Called when iteration is initialized
    def __iter__(self):
        return self

    def __next__(self):
        index = self.index
        self.total_iterations += 1
        self.index += 1
        if self.limit > 0 and self.total_iterations > self.limit:
            raise StopIteration
        if self.index > len(self.pitch_set) - 1:
            self.index = 0
        return self.pitch_set[index]
