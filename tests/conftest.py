#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from os.path import abspath, join, dirname

test_dir = dirname(abspath(__file__))
module_dir = abspath(join(test_dir, '..', 'chord_finder'))

sys.path.insert(0, module_dir)
