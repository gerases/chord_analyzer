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

For now, the input must be given as as a quoted string with pitch names
separated by spaces.

# Examples

```
$ ./ChordFinder.py 'a c e'
A minor

$ ./ChordFinder.py 'a c# e'
A major

$ ./ChordFinder.py 'a c eb g'
A half diminished 7th

$ ./ChordFinder.py 'a c e g'
A minor 7th

$ ./ChordFinder.py 'a c# e g#'
A major 7th

$ ./ChordFinder.py 'a c# e g'
A dominant 7th

$ ./ChordFinder.py 'a c eb gb'
A diminished 7th
C diminished 7th
Eb diminished 7th
Gb diminished 7th
```

# TODO

* Recognize more chrod types (e.g. suspended, 9, 11, 13, etc)
* Require fewer and not necessarily consecutive chars to start the analysis
* Accept input on stdin
