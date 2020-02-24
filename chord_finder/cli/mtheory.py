#!/usr/bin/env python
# encoding: utf-8

import argparse
from chord_finder.scales.major_scale import MajorScale
from chord_finder.scales.minor_scale import MinorScale


def print_scale(args):
    if args.major:
        for scale in args.major:
            MajorScale(scale).print()
    else:
        for scale in args.minor:
            MinorScale(args.major).print()


def print_circle_of_5ths():
    print("=> Circle of 5ths")
    for scale in ['c', 'g', 'd', 'a', 'e', 'b', 'f+']:
        MajorScale(scale).print()
    print("=> Circle of 4ths")
    for scale in ['f', 'b-', 'e-', 'a-', 'd-', 'g-']:
        MajorScale(scale).print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test')
    parser.add_argument('-v', '--verbose', help='Be more verbose')
    parser.add_argument('-M', '--major', nargs='+',
                        help='Print one or more major scales')
    parser.add_argument('-m', '--minor', nargs='+',
                        help='Print one or more minor scales')
    parser.add_argument('--circle', action='store_true',
                        help='Print circle of fifths')
    args = parser.parse_args()

    if args.major:
        print_scale(args)
    if args.minor:
        print_scale(args)
    if args.circle:
        print_circle_of_5ths()
