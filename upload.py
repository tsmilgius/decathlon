
import csv, math



final_list = []
list_of_dictinionaries = []
keys = ['name', '100m', 'Long jump', 'Shot put', 'High jump', '400m', '110m hurdles', 'Discus throw', 'Pole vault', 'Javelin throw', '1500m' ]
with open('Decathlon.csv', 'r') as f:
    reader = csv.reader(f)
    csv_list = list(reader)

for item in range(len(csv_list)):
    final_list.append(csv_list[item][0].split(";"))
for items in range(len(final_list)):
    list_of_dictinionaries.append(dict(zip(keys, final_list[item])))



track_events_keys = ['100m', '400m', '110m hurdles', '1500m' ]
track_events_values = [list_of_dictinionaries[0][x] for x in track_events_keys]
print(track_events_values)

track_formula = int(25.4347 * math.pow ((18 - 13.43), 1.81))
print (track_formula)

field_events_keys = ['Long jump', 'Shot put', 'High jump', 'Discus throw', 'Pole vault', 'Javelin throw' ]
field_events_values = [list_of_dictinionaries[0][x] for x in field_events_keys]
print(field_events_values)
