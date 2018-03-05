# encoding=utf-8
from functional import seq

UNITS_DICT = {
    ' tablespoon ': {
        'replacement': ' tbsp ',
        'count': 11072
    },
    ' tablespoons ': {
        'replacement': ' tbsp ',
        'count': 22006
    },
    ' teaspoon ': {
        'replacement': ' tsp ',
        'count': 19510
    },
    ' teaspoons ': {
        'replacement': ' tsp ',
        'count': 6270
    },
    ' pound ': {
        'replacement': ' lb ',
        'count': 6470
    },
    ' pounds ': {
        'replacement': ' lbs ',
        'count': 4924
    },
    ' ounce ': {
        'replacement': ' oz ',
        'count': 1224
    },
    ' ounces ': {
        'replacement': ' oz ',
        'count': 5958
    },
    ' gram ': {
        'replacement': ' g ',
        'count': 2034
    },
    ' grams ': {
        'replacement': ' g ',
        'count': 50
    }
}


def process_line(line):
    global LAST_NUMBER
    for key in UNITS_DICT:
        if key in line:
            unit_data = UNITS_DICT[key]
            # count = unit_data['count']
            # unit_data['count'] = count - 1
            # if count == 0:
            #     break

            line = line.replace(key, unit_data['replacement'])
            index = line.index(',')
            result = '{}{}'.format(LAST_NUMBER, line[index:].encode('utf-8'))
            LAST_NUMBER += 1
            return result

    return None


LAST_NUMBER = 179207

if __name__ == '__main__':
    input_file_path = '../nyt-ingredients-snapshot-2015.csv'
    output_file_path = '../nyt-ingredients-snapshot-2015_v2.csv'

    with open(output_file_path, 'w') as output:
        seq.open(input_file_path, mode='r') \
            .map(lambda l: l) \
            .for_each(lambda l: output.write('{}'.format(l.encode('utf-8'))))

    with open(output_file_path, 'a') as output:
        seq.open(input_file_path, mode='r') \
            .map(process_line) \
            .filter(bool) \
            .for_each(lambda l: output.write('{}'.format(l)))

    print(LAST_NUMBER)

    #
    # lines = [
    #     '152910,1 tablespoons lemon juice,lemon juice,1.0,0.0,tablespoons,',
    #     '152911,1 tablespoon white wine vinegar,white wine vinegar,1.0,0.0,tablespoon,',
    #     '152912,1/4 pound crumbled blue cheese,blue cheese,0.25,0.0,pound,crumbled',
    #     '152916,1 pound thick asparagus,asparagus,1.0,0.0,pound,',
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
    #
    # for x in [process_line(line) for line in lines]:
    #     print(x)
