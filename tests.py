from json import dumps as j

from solution import address_line_solution


def easy_test1():
    assert address_line_solution("Winterallee 3") == j({"street": "Winterallee", "housenumber": "3"})


def easy_test2():
    assert address_line_solution("Musterstrasse 45") == j({"street": "Musterstrasse", "housenumber": "45"})


def easy_test3():
    assert address_line_solution("Blaufeldweg 123B") == j({"street": "Blaufeldweg", "housenumber": "123B"})


def medium_test1():
    r = address_line_solution("Am Bächle 23")
    assert address_line_solution("Am Bächle 23") == j({"street": "Am Bächle", "housenumber": "23"})


def medium_test2():
    assert address_line_solution("Auf der Vogelwiese 23 b") == j({"street": "Auf der Vogelwiese", "housenumber": "23 b"})


def hard_test1():
    assert address_line_solution("4, rue de la revolution") == j({"street": "rue de la revolution", "housenumber": "4"})


def hard_test2():
    assert address_line_solution("200 Broadway Av") == j({"street": "Broadway Av", "housenumber": "200"})


def hard_test3():
    assert address_line_solution("Calle Aduana, 29") == j({"street": "Calle Aduana", "housenumber": "29"})


def hard_test4():
    assert address_line_solution("Calle 39 No 1540") == j({"street": "Calle 39", "housenumber": "No 1540"})


def empty_address_test():
    assert address_line_solution("") == j({"street": "", "housenumber": ""})
