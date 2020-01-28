# Purpose

The grand idea is that given a set of musical notes, the module should print
all possible chords where all of those notes participate in the chord.  They
wouldn't need to be consecutive but could occur in any order. The current
version needs at least three consecutive letters. The following chord types
are distinguished:

* Minor
* Major
* Dominant 7th
* Major 7th
* Minor 7th
* Half diminished 7th
* Diminished 7th
* Major "add" 9th
* Major "add" 11th
* Major "add" 13th

For now, the input must be given as as a quoted string with pitch names
separated by spaces.

# Examples

```
$ ./ChordFinder.py 'ace'
A minor

$ ./ChordFinder.py 'ac+e'
A major

$ ./ChordFinder.py 'ace-g'
A half diminished 7th

$ ./ChordFinder.py 'aceg'
A minor 7th

$ ./ChordFinder.py 'ac+eg+'
A major 7th

$ ./ChordFinder.py 'ac+eg'
A dominant 7th

$ ./ChordFinder.py 'ace-g-'
A diminished 7th
C diminished 7th
Eb diminished 7th
Gb diminished 7th
```

# TODO

* Require fewer and not necessarily consecutive chars to start the analysis
* Accept input on stdin
