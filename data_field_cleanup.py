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