import csv
import numpy as np

def add_contact():
    pass

def get_data(filename):
    with open(filename, "r") as cust:
        data_reader = csv.reader(cust)
        for row in data_reader:
            yield row

csv_data = get_data('contact_list .csv')
header_row = next(csv_data)
print("header:")
print(header_row)

for data_row in csv_data:
    print(data_row)

