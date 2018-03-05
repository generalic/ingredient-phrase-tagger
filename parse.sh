#!/usr/bin/env bash
python bin/parse-ingredients.py test/input.txt > test/results.txt
python bin/convert-to-json.py test/results.txt > test/results.json
