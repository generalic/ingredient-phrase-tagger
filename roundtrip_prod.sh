#!/bin/sh
COUNT_TRAIN=179206

echo "generating training data..."
bin/generate_data --data-path=nyt-ingredients-snapshot-2015_v1.csv --count=$COUNT_TRAIN --offset=0 > tmp/train_file || exit 1

echo "training..."
crf_learn template_file tmp/train_file tmp/model_file || exit 1
