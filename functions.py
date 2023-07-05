import re

def is_none(params):
    return params["kad_number"] is None or params["latitude"] is None or params["longitude"] is None

def check_coordinates(params):
    pattern = r'^[-]?\d{1,3}\.\d{1,10}$'
    return not (re.match(pattern, params["latitude"]) and re.match(pattern, params["longitude"]))

def check_kad_num(params):
    # регулярка для формата АА:ВВ:CCCCСCC:ККK
    pattern = r'^\d{2}\:\d{2}\:\d{6,7}\:\d{2,3}'
    return not re.match(pattern, params["kad_number"])

def is_none_id(params):
    return params["id"] is None