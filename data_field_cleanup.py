import datetime
import re

def titlize_field(value):
    return value.title()

def trim_field(value):
    # Remove leading/trailing whitespace
    output = value.strip()
    if output[-1] == ".":
        # Remove any trailing full stop
        output = output[:-1]

    return output

def format_date_field(value):
    pat_mdy = r"^\d{1,2}\/\d{1,2}\/\d{2}$"
    pat_mdY = r"^\d{1,2}\/\d{1,2}\/\d{4}$"
    value_format = ""

    if re.match(pat_mdy, value):
        value_format = '%m/%d/%y'
    elif re.match(pat_mdY, value):
        value_format = '%m/%d/%Y'

    output = datetime.datetime.strptime(value, value_format).strftime('%d/%m/%Y')
    return output