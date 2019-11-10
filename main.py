import csv
import numpy as np
import db_connect as dbc

def add_contact(cur, data_row_dict):
    contact_id = 0
    cur.callproc('usp_add_contact', [data_row_dict['title']
                                    , data_row_dict['first_name']
                                    , data_row_dict['last_name']
                                    , data_row_dict['company_name']
                                    , data_row_dict['date_of_birth']
                                    , data_row_dict['notes']
                                    , contact_id])
    return contact_id    

def get_data_row(filename):
    # open the file
    with open(filename, "r") as cust:
        data_reader = csv.reader(cust)
        for row in data_reader:
            # return a row from the file
            yield row

def process_data_row(data_row):
    output = {}
    output['title'] = data_row[1]
    output['first_name'] = data_row[2]
    output['last_name'] = data_row[3]
    output['company_name'] = data_row[0]
    output['date_of_birth'] = data_row[5]
    output['notes'] = data_row[15]

    return output
    
def upload_csv(filename):
    # get a handle on the generator used to upload the file
    csv_data = get_data_row(filename)

    # the first row is assumed to be the header row
    # and is to be discarded
    # TODO: need checks on how well-formed the file is?
    next(csv_data)
    # print("header:")
    # print(header_row)

    cur = dbc.connect_db()

    # now work through each row
    for data_row in csv_data:
        dict_data_row = process_data_row(data_row)
        add_contact(cur, dict_data_row)


upload_csv('contact_list .csv')