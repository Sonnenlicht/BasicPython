import datetime
#import timedelta
import random
import sys

def parse_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d")

#start-string, end_string = sys.argv[1:]

start_date, end_date = map(parse_date, sys.argv[1:])
delta = (end_date - start_date).days
random_days = random.randint(0, delta.days)
print(random_days)
