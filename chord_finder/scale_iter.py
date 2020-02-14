#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ScaleIter:
    # Constructor
    def __init__(self, scale_obj, start, limit=0):
        self.members = scale_obj.get_members()
        self.index = self.members.index(start)
        self.total_iterations = 0
        self.limit = limit
        self.distance_base = 0

    # Called when iteration is initialized
    def __iter__(self):
        return self

    def __next__(self):
        index = self.index
        self.total_iterations += 1
        self.index += 1
        if self.limit > 0 and self.total_iterations > self.limit:
            raise StopIteration
        if self.index > len(self.members) - 1:
            self.index = 0
            # root to root is 12 semitones. this means we're wrapping
            # around the scale
            self.distance_base = 12
        scale_member = self.members[index]
        distance = scale_obj.get_member_distance(index)
        return self.members[index], self.distance_base += ?
