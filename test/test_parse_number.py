import decimal

from ingredient_phrase_tagger.training import utils


def test_mixed_number():
    s = '2 3/7'
    assert utils.parseNumbers(s) - decimal.Decimal.from_float(2.43) < 1e-6
