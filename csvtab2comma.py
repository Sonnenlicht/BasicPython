#! python3

import csv
import operator

capitals = {}
with open('countryInfo.csv') as csv_file:
#with open('capitals-tab.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    headers = next(csv_reader)
    print(headers)
    for state, capital in csv_reader:
        capitals[state] = capital
print(capitals)

with open('countryInfo-comma.csv', 'w', newline='') as csv_file:
#with open('capitals-comma.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',') #, fieldnames=['capital','state'])
    csv_writer.writerow(['State','Capital'])
    for state,capital in capitals.items():
        csv_writer.writerow([state,capital])

