# coding=utf-8
from __future__ import print_function

import json
import os
import tempfile

from ingredient_phrase_tagger.training import utils

RESULTS_FILE = './results.txt'
OUTPUT_FILE = './results.json'
MODEL_FILE = './model_file'


def parse_lines(ingredients):
    _, tmpFile = tempfile.mkstemp()

    with open(tmpFile, 'w') as temp_file:
        temp_file.write(utils.export_data(ingredients).encode('utf-8'))

    modelFilename = os.path.join(os.path.dirname(__file__), MODEL_FILE)

    os.system('crf_test -v 1 -m {} {} > {}'.format(modelFilename, tmpFile, RESULTS_FILE))
    os.system('rm {}'.format(tmpFile))

    ##########################################################################

    parsed = utils.import_data(open(RESULTS_FILE))
    os.system('rm {}'.format(RESULTS_FILE))
    return parsed


def parse_file(input_file):
    with open(input_file) as input, open(OUTPUT_FILE, 'w') as output:
        parsed = parse_lines(input.readlines())
        output.write(json.dumps(parsed, indent=4))
