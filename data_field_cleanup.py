def titlize_field(value):
    return value.title()

def trim_field(value):
    # Remove leading/trailing whitespace
    output = value.strip()
    if output[-1] == ".":
        # Remove any trailing full stop
        output = output[:-1]

    return output