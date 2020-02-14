#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chord_finder.utils import musical_to_dec


class ScaleIter:
    # Constructor
    def __init__(self, scale_obj, start, limit=0):
        self.scale = scale_obj
        self.members = scale_obj.get_members()
        self.index = self.members.index(start)
        self.distance_base = 0
        self.total_iterations = 0
        self.limit = limit
        self.distance_traveled = 0

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
            self.distance_base = 12
        member = self.members[index]
        member_distance = self.scale.get_member_distance(member)
        distance = self.distance_base + musical_to_dec(member_distance)
        self.distance_traveled = distance
        return self.members[index]
