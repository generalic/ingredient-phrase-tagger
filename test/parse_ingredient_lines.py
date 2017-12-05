#!/usr/bin/env python

from __future__ import print_function

import json
import os
import sys
import tempfile

from ingredient_phrase_tagger.training import utils

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: parse-ingredients.py FILENAME\n')
        sys.exit(1)

    FILENAME = sys.argv[1]
    RESULTS_FILE = './results.txt'
    OUTPUT_FILE = './results.json'

    _, tmpFile = tempfile.mkstemp()

    with open(FILENAME) as input_file, open(tmpFile, 'w') as temp_file:
        temp_file.write(utils.export_data(input_file.readlines()))

    tmpFilePath = '../tmp/model_file'
    modelFilename = os.path.join(os.path.dirname(__file__), tmpFilePath)

    os.system('crf_test -v 1 -m {} {} > {}'.format(modelFilename, tmpFile, RESULTS_FILE))
    os.system('rm {}'.format(tmpFile))

    ##########################################################################

    with open(OUTPUT_FILE, 'w') as testfile:
        testfile.write(json.dumps(utils.import_data(open(RESULTS_FILE)), indent=4))
