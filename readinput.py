import csv
def read_csv():
    final_list = []
    list_of_dictinionaries = []
    keys = ['name', '100m', 'Long jump', 'Shot put', 'High jump', '400m', '110m hurdles', 'Discus throw', 'Pole vault', 'Javelin throw', '1500m' ]

    with open('Decathlon.csv', 'r') as f:
        reader = csv.reader(f)
        csv_list = list(reader)
    for item in range(len(csv_list)):
        final_list.append(csv_list[item][0].split(";"))
        list_of_dictinionaries.append(dict(zip(keys, final_list[item])))
    return list_of_dictinionaries

print(len(read_csv()))
