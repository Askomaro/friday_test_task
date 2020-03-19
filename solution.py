import re
from json import dumps as j


def address_line_solution(address: str) -> dict:
    pattern = '(No |no |NO )\d+|\d+(,|$|\w$)|, \d+|^\d+|\d+(?! No|no|NO) \w+'
    match = re.search(pattern, address)
    match_el = match.group()

    house_number = match_el.replace(',', '').strip()
    street = address.replace(match_el, '').strip()
    result = {'street': street, 'housenumber': house_number}

    return j(result)
