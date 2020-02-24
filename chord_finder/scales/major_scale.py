#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chord_finder.scales.scale import Scale
from chord_finder.common import ENHARM_SHARP_MODE
from chord_finder.common import ENHARM_FLAT_MODE
from chord_finder.common import SHARP_TO_FLAT
from chord_finder.iterators.non_accidental_iter import NonAccidentalIter


class MajorScale(Scale):
    def __init__(self, root, mode=None):
        """
              W W H W W W H
        e.g: c d e f g a b c
              2 4 5 7 9 b c
        """
        distances = ['2', '4', '5', '7', '9', 'b']
        if mode == 'auto':
            if root in ['c', 'g', 'd', 'a', 'e', 'b', 'f+']:
                mode = ENHARM_SHARP_MODE
            else:
                mode = ENHARM_FLAT_MODE
                root = SHARP_TO_FLAT.get(root, root)
        elif mode is None:
            if root in ['c', 'g', 'd', 'a', 'e', 'b'] or '+' in root:
                mode = ENHARM_SHARP_MODE
            else:
                mode = ENHARM_FLAT_MODE
                root = SHARP_TO_FLAT.get(root, root)
        super(MajorScale, self).__init__(root, mode, distances)

    def __str__(self):
        return "major scale %s: %s" % (self.root)


def main():
    non_accident_iter = NonAccidentalIter('c', limit=7)
    major_keys = []
    for root in non_accident_iter:
        scale = MajorScale(root)
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
