#!/usr/bin/env python
# encoding: utf-8

import sys
import re
from itertools import permutations


DISTANCE_TO_NAME = {
    1: 'minor second',
    2: 'major second',
    3: 'minor third',
    4: 'major third',
    5: 'perfect fourth',
    6: 'diminished fifth',
    7: 'perfect fifth',
    8: 'minor sixth',
    9: 'major sixth',
    'a': 'minor seventh',     # 10
    'b': 'major seventh',     # 11
    'e': 'major ninth',       # 14
    'h': 'major eleventh',    # 17
    'l': 'major thirteenth',  # 21
}

PITCHES = ['c', 'c+', 'd', 'd+', 'e', 'f', 'f+', 'g', 'g+', 'a', 'a+',
           'b']
MAX_DISTANCE = 40

SHARP_TO_FLAT = {
    'c+': 'd-',
    'd+': 'e-',
    'e+': 'f-',
    'f+': 'g-',
    'g+': 'a-',
    'a+': 'b-',
}


def distances_to_symbols(root, distances, mode):
    """Returns a string representation of the chord
    based on the given distances from the root
    """
    result = [root]
    root = move_in_half_steps(root[0:1], root[1:])
    pitch_index = PITCHES.index(root)
    pitches_max_index = len(PITCHES) - 1
    for distance in distances:
        pitch_index_at_distance = pitch_index + musical_to_dec(distance)
        while pitch_index_at_distance > pitches_max_index:
            pitch_index_at_distance =\
                pitch_index_at_distance - pitches_max_index - 1
        pitch = PITCHES[pitch_index_at_distance]
        if mode == 'flat' and len(pitch) > 1:
            result.append(SHARP_TO_FLAT[pitch])
        else:
            result.append(PITCHES[pitch_index_at_distance])
    return ''.join(result)


def parse_input(st):
    i = 0
    result = []
    allowed_chars = re.compile('[a-gA-G+-]')
    a_to_g_re = re.compile('[a-gA-G]')
    last_char_pos = -1
    while i < len(st):
        char = st[i]
        if not allowed_chars.match(char):
            raise Exception("Illegal char at position %s [%s]" % (i, char))
        if a_to_g_re.match(char):
            result.append(char)
            last_char_pos = len(result) - 1
        else:
            if last_char_pos < 0:
                raise Exception("Error parsing input at position %s [%s]" %
                                (i, char))
            result[last_char_pos] = result[last_char_pos] + char
        i += 1
    return result


def musical_to_dec(distance):
    """Converts musical distances (e.g.: 1, 2, a, b) to decimal integers"""

    chr_code = ord(distance)
    if chr_code >= 97:
        return chr_code - 97 + 10
    return int(distance)


def dec_to_musical(distance):
    """Converts numbers > 9 into a, b, ... n up to MAX_DISTANCE"""
    if distance > MAX_DISTANCE:
        print "Distance is too large (%s > %s)" % (distance, MAX_DISTANCE)
        sys.exit(1)

    # 1 to 9 is unchanged
    if distance < 10:
        return distance

    # 97 is the ascii for 'a'
    return chr(distance - 10 + 97)


def lookup_pitch(pitch):
    return PITCHES.index(pitch)


def move_in_half_steps(pitch, accidentals):
    if type(accidentals).__name__ == 'str':
        accidentals = list(accidentals)
    # start from the given pitch
    result = pitch
    for accidental in accidentals:
        if accidental == '+':
            if result == 'b':
                result = 'c'
            else:
                result = PITCHES[PITCHES.index(result) + 1]
        else:
            if result == 'c':
                result = 'b'
            else:
                result = PITCHES[PITCHES.index(result) - 1]
    return result


def get_distance_in_semitones(a, b, req_min_distance=-1):
    start, s_accidentals = a[0:1].lower(), a[1:]
    end, e_accidentals = b[0:1].lower(), b[1:]

    # adjust the start and end by the accidentals
    start = move_in_half_steps(start, s_accidentals)
    end = move_in_half_steps(end, e_accidentals)

    distance = 0
    while start != end:
        start = move_in_half_steps(start, '+')
        distance += 1
        if start == end and distance < req_min_distance:
            start = move_in_half_steps(start, '+')
            distance += 1
    return distance


# pylint: disable=too-many-locals
def analyze(user_input, permute=True):
    # Validate input
    #
    # First, turn the input into an array if it's a string
    if type(user_input).__name__ == 'str':
        user_input = parse_input(user_input)
    else:
        user_input = parse_input(''.join(user_input))

    mode = 'sharp'
    for char in user_input:
        if '-' in char:
            mode = 'flat'

    rex = re.compile('[a-gA-G][#b]*')
    for item in user_input:
        if not rex.match(item):
            print "Invalid input: %s" % item
            sys.exit(1)

    patterns = {
        '47': 'major',
        '37': 'minor',
        '48': 'augmented',
        '36': 'diminished',
        '27': 'sus2',
        '57': 'sus4',
        '47a': 'dominant 7th',
        '47b': 'major 7th',
        '37a': 'minor 7th',
        '36a': 'half diminished 7th',
        '369': 'diminished 7th',
        '47e': 'major 9th',
        '47h': 'major 11th',
        '47l': 'major 13th',
    }
    perms = permutations(user_input)
    possibles = {}
    for permutation in perms:
        distances = []
        root = permutation[0]
        len_user_input = len(user_input)
        req_minimum_distance = 0
        j = 1
        beyond_12th = None
        while j < len_user_input:
            unknown = permutation[j]
            distance = get_distance_in_semitones(root,
                                                 unknown,
                                                 req_minimum_distance)

            # Look beyond 12th only if we're looking at the 4th member of
            # the chord and nothing is found below the 12th. If this is not
            # done, then ['c', 'e', 'g', 'd'] will be identified as 'C
            # Major 9th'] twice. The first time will happen because 'd'
            # will be already looked up beyond the 12th semitone.
            #
            # With Major 13th (e.g.: 'c', 'e', 'g', 'a'), the 'a' will be
            # found below the 12th, but it's not a known chord and so it
            # won't be added and unless we check beyond the 12th, we won't
            # find the 13th chord.
            #
            # In other words, we need to look beyond the 12th only if it
            # has not been done already.
            if j == 3 and distance < 13:
                beyond_12th = get_distance_in_semitones(root,
                                                        unknown,
                                                        13)

            req_minimum_distance = distance + 1
            distances.append(str(dec_to_musical(distance)))
            j += 1
        pattern = ''.join(distances)
        if pattern in patterns:
            possibles["%s %s" % (root.capitalize(), patterns[pattern])] =\
                distances_to_symbols(root, distances, mode)
        if beyond_12th:
            distances[2] = str(dec_to_musical(beyond_12th))
            pattern = ''.join(distances)
            if pattern in patterns:
                possibles["%s %s" % (root.capitalize(), patterns[pattern])] =\
                    distances_to_symbols(root, distances, mode)
        if not permute:
            break
    return possibles


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Provide a few chord elements. Use + for sharps and - for flats."
        sys.exit(1)
    request = sys.argv[1]
    possibilities = analyze(request)
    if len(possibilities) < 1:
        print "Nothing found for %s" % request
        sys.exit(1)
    for possibility, symbols in possibilities.items():
        print "%s [%s]" % (possibility, symbols)
    sys.exit(1)
