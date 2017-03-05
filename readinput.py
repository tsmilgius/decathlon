import csv
from collections import OrderedDict


def read_csv():
    """ function opens csv file reads it and returns list of dictionaries containing all data mapped with keys """

    final_list = []
    list_of_dictinionaries = []
    keys = ['name', '100m', 'Long jump', 'Shot put', 'High jump', '400m', '110m hurdles', 'Discus throw', 'Pole vault',
            'Javelin throw', '1500m']

    with open('Decathlon.csv', 'r') as f:
        reader = csv.reader(f)
        csv_list = list(reader)
    for item in range(len(csv_list)):
        final_list.append(csv_list[item][0].split(";"))
        list_of_dictinionaries.append(OrderedDict(zip(keys, final_list[item])))
    return list_of_dictinionaries
