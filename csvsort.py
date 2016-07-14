#! python3

import csv
import operator

capitals = {}
with open('us-state-capitals.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    print(headers)
    for state, capital in csv_reader:
        capitals[state] = capital

list_capitals = []
#list_capitals = sorted(capital.items(), key=operator.itemgetter(1))

list_capitals = sorted(capitals.items(), key=lambda x: x[1])
print(list_capitals)

with open('capitals-sort.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',') #, fieldnames=['capital','state'])
    csv_writer.writerow(['State','Capital'])
    for state,capital in list_capitals:
        csv_writer.writerow([state,capital])

##with open('capitals-tab.csv', 'w', newline='') as csv_file:
#    csv_writer = csv.writer(csv_file, delimiter='\t') #, fieldnames=['capital','state'])
#    csv_writer.writerow(['State','Capital'])
#    for state,capital in list_capitals:
#        csv_writer.writerow([state,capital])

