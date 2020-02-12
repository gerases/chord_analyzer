#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ScaleIter:
    # Cosntructor
    def __init__(self, scale_obj, start, limit=0):
        self.index = scale_obj.get_members().index(start)
        self.members = scale_obj.get_members()
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
        if self.index > len(self.members) - 1:
            self.index = 0
        return self.members[index]
