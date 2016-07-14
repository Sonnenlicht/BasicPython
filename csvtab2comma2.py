#! python3

import csv
import operator

capitals = {}
with open('countryInfo.csv') as csv_file:
#with open('capitals-tab.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    contents_list = list(csv_reader)
    #headers = next(csv_reader)
    #print(headers)
    #for state, capital in csv_reader:
    #    capitals[state] = capital
    print(contents_list)

with open('countryInfo-comma.csv', 'w', newline='') as csv_file:
#with open('capitals-comma.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',') #, fieldnames=['capital','state'])
#    csv_writer.writerow(['State','Capital'])
    for items in contents_list:
        csv_writer.writerow(items)

