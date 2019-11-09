import csv
import numpy as np

def add_contact():
    pass

def get_data_row(filename):
    # open the file
    with open(filename, "r") as cust:
        data_reader = csv.reader(cust)
        for row in data_reader:
            # return a row from the file
            yield row

def upload_csv(filename):
    # get a handle on the generator used to upload the file
    csv_data = get_data_row(filename)

    # the first row is assumed to be the header row
    # and is to be discarded
    # TODO: need checks on how well-formed the file is?
    next(csv_data)
    # print("header:")
    # print(header_row)

    # now work through each row
    for data_row in csv_data:
        print(data_row)


upload_csv('contact_list .csv')