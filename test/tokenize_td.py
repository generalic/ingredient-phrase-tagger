from ingredient_phrase_tagger.training import utils

if __name__ == '__main__':

    ingredient_lines = [
        '2 cups (500ml) whole milk',
        '2 cups lime juice',
        '4 tablespoons (25g) unsweetened cocoa powder, natural or Dutch-process',
        '1 tbsp salt',
        '1 tsp salt',
        '1 oz salt',
        '1 lb (25g) unsweetened cocoa powder, natural or Dutch-process',
        '1 lbs whole milk',
        '1 lbs salt',
        '1 g salt',
        '21 g milk',
        '1 g half and half',
        '1 g butter unsalted'
    ]

    for i in ingredient_lines:
        print(utils.tokenize(i))
