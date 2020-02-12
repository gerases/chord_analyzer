#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import pprint
import logging
import inspect
import argparse
import unicodedata

SPACE = unicodedata.lookup('SPACE')
COMMA = unicodedata.lookup('COMMA')

def main():
    parser = argparse.ArgumentParser(description='utils')
    parser.add_argument('-v', '--verbose', help='Be more verbose')
    args = parser.parse_args()

    
if __name__ == '__main__':
    main()
