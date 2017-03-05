import csv, codecs, sys
from collections import OrderedDict



def read_input():
    """ function opens csv file reads it and returns list of dictionaries containing all data mapped with keys """

    data_set = []
    list_of_dictinionaries = []
    keys = ['name', '100m', 'Long jump', 'Shot put', 'High jump', '400m', '110m hurdles', 'Discus throw', 'Pole vault',
            'Javelin throw', '1500m']

    with codecs.open('uploads/input.csv', 'r', 'utf8') as f:
        try:
            dialect = csv.Sniffer().sniff(f.read(1024), delimiters=',;')
            f.seek(0)
            reader = csv.reader(f)
            csv_list = list(reader)
            for item in range(len(csv_list)):
                data_set.append(csv_list[item][0].split(";"))
                list_of_dictinionaries.append(OrderedDict(zip(keys, data_set[item])))
            return list_of_dictinionaries
        except csv.Error as e:
            return 'Not valid values'
