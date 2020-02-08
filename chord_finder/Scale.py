#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chord_finder.utils import distances_to_symbols


class MajorScale:
    def __init__(self, root, mode):
        """
         W W H W W W H
        c d e f g a b c
        """
        distances = ['2', '4', '5', '7', '9', 'b']
        scale_members = distances_to_symbols(root, distances,
                                             mode, return_as_list=True)
        self.scale_members = scale_members
