#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scale import Scale
from chord_finder.common import ENHARM_SHARP_MODE
from chord_finder.common import ENHARM_FLAT_MODE
from chord_finder.common import DEC_TO_ROMAN
from chord_finder.non_accidental_iter import NonAccidentalIter
from chord_finder.scale_iter import ScaleIter


class MinorScale(Scale):
    def __init__(self, root, mode=None):
        """
              W H W W H W W
        e.g: a b c d e f g a
              2 3 5 7 8 a c

        """
        distances = ['2', '3', '5', '7', '8', 'a']
        if not mode:
            if root in ['a', 'e', 'b', 'f+', 'c+', 'g+', 'd+']:
                mode = ENHARM_SHARP_MODE
            else:
                mode = ENHARM_FLAT_MODE
        super(MinorScale, self).__init__(root, mode, distances)

    def __str__(self):
        return "minor scale %s: %s" % (self.root)

    def get_all_triads(self):
        root_iter = ScaleIter(self, self.get_root(), limit=7)
        third_iter = ScaleIter(self, self.get_members()[2])
        fifth_iter = ScaleIter(self, self.get_members()[4])
        result = []
        degree = 1
        for root, third, fifth in zip(root_iter, third_iter, fifth_iter):
            name = self.identify_chord([root, third, fifth])
            roman = DEC_TO_ROMAN[degree]
            if degree in [1, 4, 5]:
                roman = roman.upper()
            result.append({'pitches': "%s%s%s" % (root, third, fifth),
                           'name': name,
                           'degree': degree,
                           'roman': roman,
                           })
            degree += 1
        return result


def main():
    non_accident_iter = NonAccidentalIter('c', limit=7)
    major_keys = []
    for root in non_accident_iter:
        scale = MinorScale(root)
        major_keys.append(scale)
        print("key of %s: " % root, end="")
        print(scale.identify_chord(['a', 'c', 'e']))

    for scale in major_keys:
        print("=========== key of %s ================" % scale.get_root())
        triads = scale.get_all_triads()
        for triad in triads:
            print("\t%-5s %-20s%s" %
                  (triad['roman'], triad['pitches'], triad['name']))


if __name__ == '__main__':
    main()
