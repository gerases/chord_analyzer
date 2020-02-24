#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chord_finder.utils import move_in_half_steps


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
        self.total_iterations += 1
        if self.limit > 0 and self.total_iterations > self.limit:
            raise StopIteration
        pitch = move_in_half_steps(self.current_5th, '+' * 7)
        self.current_5th = pitch
        return pitch
