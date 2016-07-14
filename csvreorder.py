#! python3

import csv

capitals = {}
with open('us-state-capitals.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    print(headers)
    for state, capital in csv_reader:
        capitals[state] = capital

print(capitals)
with open('capitals-reverse.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',') #, fieldnames=['capital','state'])
    csv_writer.writerow(['Capital','State'])
    for state,capital in capitals.items():
        csv_writer.writerow([capital,state])
        #print(row)
    
        
