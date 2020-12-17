import csv 
from pprint import pprint
f = "/tmp/MOCK_DATA (1).csv"

def csv_to_dict(f):

    with open(f, ) as csvfile:
        reader = csv.DictReader(csvfile, )
        return [dict(row) for row in reader]

pprint(csv_to_dict(f))        
