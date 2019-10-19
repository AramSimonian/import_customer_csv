import csv
import numpy as np

def get_data(filename):
    with open(filename, "r") as cust:
        data_reader = csv.reader(cust)
        for row in data_reader:
            yield row

for row in get_data('contact_list .csv'):
    print(row)
