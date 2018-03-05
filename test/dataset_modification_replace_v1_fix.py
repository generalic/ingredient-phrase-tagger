# encoding=utf-8
from functional import seq


def process_line(line):
    if ',tablespoons,' in line:
        return line.replace(',tablespoons,', ',tablespoon,')
    if ',teaspoons,' in line:
        return line.replace(',teaspoons,', ',teaspoon,')
    if ',cups,' in line:
        return line.replace(',cups,', ',cup,')
    if ',pounds,' in line:
        return line.replace(',pounds,', ',pound,')
    if ',lbs,' in line:
        return line.replace(',lbs,', ',lb,')
    if ',quarts,' in line:
        return line.replace(',quarts,', ',quart,')
    if ',quarts,' in line:
        return line.replace(',quarts,', ',quart,')
    if ',quarts,' in line:
        return line.replace(',quarts,', ',quart,')
    if ',segments,' in line:
        return line.replace(',segments,', ',segment,')
    if ',sticks,' in line:
        return line.replace(',sticks,', ',stick,')
    if ',cloves,' in line:
        return line.replace(',cloves,', ',clove,')
    if ',Tbsp.,' in line:
        return line.replace(',Tbsp.,', ',tbsp,')
    if ',liters,' in line:
        return line.replace(',liters,', ',liter,')
    if ',dashes,' in line:
        return line.replace(',dashes,', ',dash,')
    if ',slices,' in line:
        return line.replace(',slices,', ',slice,')
    if ',cans,' in line:
        return line.replace(',cans,', ',can,')
    if ',stems,' in line:
        return line.replace(',stems,', ',stem,')
    if ',stalks,' in line:
        return line.replace(',stalks,', ',stalk,')
    if ',sprigs,' in line:
        return line.replace(',sprigs,', ',sprig,')
    if ',bunches,' in line:
        return line.replace(',bunches,', ',bunch,')
    if ',cubes,' in line:
        return line.replace(',cubes,', ',cube,')
    if ',racks,' in line:
        return line.replace(',racks,', ',rack,')

    return line


if __name__ == '__main__':
    input_file_path = '../nyt-ingredients-snapshot-2015_v1.csv'
    output_file_path = '../nyt-ingredients-snapshot-2015_v1_fix.csv'

    with open(output_file_path, 'w') as output:
        seq.open(input_file_path, mode='r') \
            .map(process_line) \
            .for_each(lambda l: output.write('{}'.format(l.encode('utf-8'))))

    # line = '132962,1 1/2 pounds savoy cabbage,savoy cabbage,1.5,,pounds,'
    # print(process_line(line))
    #
    # lines = [
    #     '152910,1 tablespoon lemon juice,lemon juice,1.0,0.0,tablespoon,',
    #     '152911,1 tablespoons white wine vinegar,white wine vinegar,1.0,0.0,tablespoon,',
    #     '152912,1/4 pound crumbled blue cheese,blue cheese,0.25,0.0,pound,crumbled',
    #     '152916,1 pounds thick asparagus,asparagus,1.0,0.0,pound,',
    #     '152918,1 teaspoons dill, roughly chopped,dill,1.0,0.0,teaspoons,',
    #     '152919,1 tablespoons parsley, roughly chopped,parsley,1.0,0.0,tablespoons,',
    #     '152920,1 tablespoon chives, roughly chopped (plus chive flowers to garnish if available),chives,1.0,0.0,tablespoon,',
    #     '152920,1 tablespoon chives, roughly chopped (plus chive flowers to garnish if available),chives,1.0,0.0,tablespoon,',
    #     '152958,2 ounces rye or bourbon,rye,2.0,0.0,ounce,',
    #     '152959,1 ounces Campari,Campari,1.0,0.0,ounce,',
    #     '152960,1 ounce sweet vermouth (I love a half and half mixture of Cinzano Rosso and Carpano Antica Formula).,sweet vermouth,1.0,0.0,ounce,',
    #     '153206,120 grams (approximately 2/3 cup) golden raisins,golden raisins,120.0,0.0,gram,',
    #     '153207,125 grams (approximately 1 cup) millet meal or fine cornmeal,millet meal,125.0,0.0,gram,',
    #     '153208,60 grams (approximately 1/2 cup) cornstarch,cornstarch,60.0,0.0,gram,',
    #     '153209,150 grams (approximately 1 1/4 cups) almond flour,almond flour,150.0,0.0,gram,'
    # ]
    #
    # for x in [process_line(line) for line in lines]:
    #     print(x)
