#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Scale superclass"""

from chord_finder.utils import move_in_half_steps
from chord_finder.utils import lookup_pitch
from chord_finder.utils import musical_to_dec
from chord_finder.utils import dec_to_musical
from chord_finder.utils import spell_pitch_enharmonically
from chord_finder.common import PITCHES
from chord_finder.common import MAX_DISTANCE
from chord_finder.common import CHORD_PATTERNS
from chord_finder.common import DEC_TO_ROMAN
from chord_finder.iterators.non_accidental_iter import NonAccidentalIter
from chord_finder.iterators.scale_iter import ScaleIter


class Scale:
    def __init__(self, root, mode, distances):
        self.root = root
        self.mode = mode
        self.distances = distances
        self.member_to_distance = {}
        self.scale_members = []
        self.convert_distances_to_piches()

    def get_member_distance(self, scale_member):
        if scale_member == self.get_root():
            return '0'
        return self.member_to_distance[scale_member]

    def get_members(self):
        return self.scale_members

    def get_root(self):
        return self.root

    def convert_distances_to_piches(self):
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
        self.scale_members = result

    def fit_pitches_in_scale(self, pitches):
        matches = []
        scale_root = self.get_root()
        scale_iter = ScaleIter(self, scale_root)
        len_pitches_orig = len(pitches)
        i = 1
        for scale_member in scale_iter:
            pitch = pitches[0]
            if pitch == scale_member:
                matches.append({'degree': i,
                                'pitch': pitch,
                                'distance': scale_iter.distance_traveled})
                pitches.pop(0)
            if len(pitches) <= 0 or i > MAX_DISTANCE:
                break
            i += 1
        if len(matches) != len_pitches_orig:
            return []
        return matches

    def identify_chord(self, pitches):
        matches = self.fit_pitches_in_scale(pitches.copy())
        if len(matches) == 0:
            return None
        distances = [str(match['distance']) for match in matches]
        # if the root in the returned distance is not the first degree of
        # the scale, we need to subtract the distance of this first chord
        # member from the rest of the distances to get the pattern that can
        # be looked up in CHORD_PATTERNS.
        #
        # For example:
        #
        # if the pitches are ['d', 'f', 'a'] and we're in the key of C, the
        # distances are '2', '5', '9'. If we subtract 2 from 5 and 9, we'll
        # get 3 and 7. '37' is the minor chord pattern in CHORD_PATTERNS.
        pattern = [
            str(dec_to_musical(
                musical_to_dec(distance) - musical_to_dec(distances[0])
                ))
            for distance in distances[1:]]
        pattern_str = ''.join(pattern)
        if pattern_str not in CHORD_PATTERNS:
            return None
        chord = '%s %s' % (pitches[0].upper(), CHORD_PATTERNS[pattern_str])
        return chord, CHORD_PATTERNS[pattern_str]

    def get_all_triads(self):
        root_iter = ScaleIter(self, self.get_root(), limit=7)
        third_iter = ScaleIter(self, self.get_members()[2])
        fifth_iter = ScaleIter(self, self.get_members()[4])
        result = []
        degree = 1
        for root, third, fifth in zip(root_iter, third_iter, fifth_iter):
            name, chord_type = self.identify_chord([root, third, fifth])
            roman = DEC_TO_ROMAN[degree]
            if 'major' in chord_type:
                roman = roman.upper()
            result.append({'pitches': "%s%s%s" % (root, third, fifth),
                           'name': name,
                           'degree': degree,
                           'roman': roman,
                           })
            degree += 1
        return result

    def print(self, color=True):
        for member in self.scale_members:
            print('%-7s' % member, end="")
        print()
