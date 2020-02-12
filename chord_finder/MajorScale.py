#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chord_finder.NonAccidentalIter import NonAccidentalIter
from chord_finder.utils import move_in_half_steps
from chord_finder.utils import lookup_pitch
from chord_finder.utils import musical_to_dec
from chord_finder.utils import get_distance_in_semitones
from chord_finder.common import PITCHES
from chord_finder.common import ENHARM_SHARP_MODE
# from chord_finder.common import ENHARM_FLAT_MODE


class MajorScale:
    def __init__(self, root, mode):
        """
         W W H W W W H
        c d e f g a b c
        """
        self.distances = ['2', '4', '5', '7', '9', 'b']
        self.mode = mode
        self.root = root
        self.scale_members = self.distances_to_symbols(True)

    def get_members(self):
        return self.scale_members

    def __str__(self):
        print("major scale %s: %s" % (self.root, self.scale_members))

    # pylint: disable=unused-argument
    def spell_pitch_enharmonically(self, pitch, expected_base, mode):
        """
        Express a given sharpened/flattened pitch in terms of another pitch
        For example:

        # pitch | expected base |return value
        # ===================================
        # f     | e             |e+
        # f+    | e             |e++
        # f+++  | e             |e+++
        # b     | a             |a++
        # ...

        The number of accidentals to be added to the "expected base" can be
        determined with this formula:

        number of accidentals = semitone_distance between:
            "pitch" and "expected_base"
        """
        if pitch == expected_base:
            return pitch
        if mode == ENHARM_SHARP_MODE:
            # pylint: disable=fixme
            # TODO: check assumption that pitch is greater than expected_base
            distance = get_distance_in_semitones(expected_base, pitch)
            return "{0:s}{1:s}".format(expected_base, '+' * distance)
        else:
            distance = get_distance_in_semitones(pitch, expected_base)
            return "{0:s}{1:s}".format(expected_base, '-' * distance)

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
        print('root is %s' % non_accident_base)
        for distance in self.distances:
            dec_distance = musical_to_dec(distance)
            pitch_index_at_distance = pitch_index + dec_distance
            non_accident_base = non_accident_iter.__next__()
            while pitch_index_at_distance > pitches_max_index:
                pitch_index_at_distance =\
                    pitch_index_at_distance - pitches_max_index - 1
            pitch = PITCHES[pitch_index_at_distance]
            enharmonic_pitch =\
                self.spell_pitch_enharmonically(pitch,
                                                non_accident_base,
                                                self.mode)
            # print("HERE %s %s" % (pitch, non_accident_base))
            result.append(enharmonic_pitch)
        if return_as_list:
            return result
        else:
            return ''.join(result)
