import datetime
import re
import locale

def titlize_field(value):
    return value.title()

def trim_field(value):
    # Remove leading/trailing whitespace
    output = value.strip()
    # Remove any trailing full stop
    if output[-1] == ".":
        output = output[:-1]

    return output

def format_date_field(value):
    locale.setlocale(locale.LC_ALL, 'en_GB')
    pat_mdy = r"^\d{1,2}\/\d{1,2}\/\d{2}$"
    pat_mdY = r"^\d{1,2}\/\d{1,2}\/\d{4}$"
    value_format = ""

    if re.match(pat_mdy, value):
        value_format = '%m/%d/%y'
    elif re.match(pat_mdY, value):
        value_format = '%m/%d/%Y'

    # Prepare the date value for output
    output = datetime.datetime.strptime(value, value_format)
    # Basic check to correct the year
    if output.year > datetime.datetime.now().year:
        output = output.replace(year=output.year-100)
    output = output.strftime('%d/%m/%Y')

    return output

def format_number_field(value):
    output = []
    for val in value:
        if val.isdigit():
            output.append(val)

    return "".join(output)

def format_mobile_field(value):
    # Pretty basic check - may need to check length?
    output = ""
    if value[:2] != "64":
        output = "64"

    return output + str(value)

def format_landline_field(value):
    # Pretty basic check - may need to check length?
    output = ""
    if value[:2] != "09":
        output = "09"

    return output + str(value)