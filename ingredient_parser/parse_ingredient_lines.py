#!/usr/bin/env python

from __future__ import print_function
import sys
from parser import parse_file

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: parse-ingredients.py <INPUT_FILE>\n')
        sys.exit(1)

    parse_file(sys.argv[1])
