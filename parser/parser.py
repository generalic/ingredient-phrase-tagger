from __future__ import print_function

import json
import os
import tempfile

from ingredient_phrase_tagger.training import utils

RESULTS_FILE = './results.txt'
OUTPUT_FILE = './results.json'
MODEL_FILE = '../tmp/model_file'


def parse_list(ingredients):
    _, tmpFile = tempfile.mkstemp()

    with open(tmpFile, 'w') as temp_file:
        temp_file.write(utils.export_data(ingredients))

    modelFilename = os.path.join(os.path.dirname(__file__), MODEL_FILE)

    os.system('crf_test -v 1 -m {} {} > {}'.format(modelFilename, tmpFile, RESULTS_FILE))
    os.system('rm {}'.format(tmpFile))

    ##########################################################################

    out = utils.import_data(open(RESULTS_FILE))
    os.system('rm {}'.format(RESULTS_FILE))
    return out


def parse_file(input_file):
    with open(input_file) as input, open(OUTPUT_FILE, 'w') as output:
        parsed = parse_list(input.readlines())
        output.write(json.dumps(parsed, indent=4))
