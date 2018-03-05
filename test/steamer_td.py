import nltk

nltk.download('wordnet')
lemimatizer = nltk.WordNetLemmatizer()

print(lemimatizer.lemmatize("having"))

units = {
    "cups": u"cup",
    "tablespoons": u"tablespoon",
    "teaspoons": u"teaspoon",
    "pounds": u"pound",
    "ounces": u"ounce",
    "cloves": u"clove",
    "sprigs": u"sprig",
    "pinches": u"pinch",
    "bunches": u"bunch",
    "slices": u"slice",
    "grams": u"gram",
    "heads": u"head",
    "quarts": u"quart",
    "stalks": u"stalk",
    "pints": u"pint",
    "pieces": u"piece",
    "sticks": u"stick",
    "dashes": u"dash",
    "fillets": u"fillet",
    "cans": u"can",
    "ears": u"ear",
    "packages": u"package",
    "strips": u"strip",
    "bulbs": u"bulb",
    "bottles": u"bottle"
}

for x, y in units.items():
    print(x + ' ' + y)

for k in units.keys():
    print(lemimatizer.lemmatize(k))

print(lemimatizer.lemmatize('larger'))
