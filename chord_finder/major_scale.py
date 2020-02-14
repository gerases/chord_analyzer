#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chord_finder.non_accidental_iter import NonAccidentalIter
from chord_finder.utils import move_in_half_steps
from chord_finder.utils import lookup_pitch
from chord_finder.utils import musical_to_dec
from chord_finder.utils import spell_pitch_enharmonically
from chord_finder.common import PITCHES
from chord_finder.common import SHARP_KEYS
from chord_finder.common import FLAT_KEYS
from chord_finder.common import ENHARM_SHARP_MODE
from chord_finder.common import ENHARM_FLAT_MODE


def build_major_scales():
    result = []
    for root in SHARP_KEYS:
        scale = MajorScale(root, ENHARM_SHARP_MODE)
        result.append(scale)
    for root in FLAT_KEYS:
        scale = MajorScale(root, ENHARM_FLAT_MODE)
        result.append(scale)
    return result


class MajorScale:
    def __init__(self, root, mode):
        """
         W W H W W W H
        e.g: c d e f g a b c
        """
        self.distances = ['2', '4', '5', '7', '9', 'b',
                          'e', 'g', 'h', 'j', 'l', 'n']
        self.mode = mode
        self.root = root
        self.member_to_distance = {}
        self.scale_members = self.distances_to_symbols(return_as_list=True)

    def get_member_distance(self, scale_member):
        if scale_member == self.get_root():
            return '0'
        return self.member_to_distance[scale_member]

    def get_members(self):
        return self.scale_members

    def get_root(self):
        return self.root

    def __str__(self):
        return "major scale %s: %s" % (self.root, self.scale_members)

    def distances_to_symbols(self, return_as_list):
        """Returns an enharomonic string representing the chord
        based on the given distances from the root
        """
        result = [self.root]
        non_accident_base, accidentals = self.root[0:1], self.root[1:]
        start = move_in_half_steps(non_accident_base, accidentals)
        pitch_index = lookup_pitch(start)
        pitches_max_index = len(PITCHES) - 1
        non_accident_iter = NonAccidentalIter(non_accident_base)
        non_accident_base = non_accident_iter.__next__()
        # print('root is %s' % non_accident_base)
        for distance in self.distances:
            dec_distance = musical_to_dec(distance)
            pitch_index_at_distance = pitch_index + dec_distance
            non_accident_base = non_accident_iter.__next__()
            while pitch_index_at_distance > pitches_max_index:
                pitch_index_at_distance =\
                    pitch_index_at_distance - pitches_max_index - 1
            pitch = PITCHES[pitch_index_at_distance]
            enharmonic_pitch =\
                spell_pitch_enharmonically(pitch,
                                           non_accident_base,
                                           self.mode)
            # print("HERE %s %s" % (pitch, non_accident_base))
            result.append(enharmonic_pitch)
            self.member_to_distance[enharmonic_pitch] = distance
        if return_as_list:
            return result
        else:
            return ''.join(result)
