def address_line_solution(address: str)-> dict:
    pass


def easy_test1():
    assert address_line_solution("Winterallee 3") == {"street": "Winterallee", "housenumber": "3"}


def easy_test2():
    assert address_line_solution("Musterstrasse 45") == {"street": "Musterstrasse", "housenumber": "45"}


def easy_test3():
    assert address_line_solution("Blaufeldweg 123B") == {"street": "Blaufeldweg", "housenumber": "123B"}


def medium_test1():
    assert address_line_solution("Am Bächle 23") == {"street": "Am Bächle", "housenumber": "23"}


def medium_test2():
    assert address_line_solution("Auf der Vogelwiese 23 b") == {"street": "Auf der Vogelwiese", "housenumber": "23 b"}


def hard_test1():
    assert address_line_solution("4, rue de la revolution") == {"street": "rue de la revolution", "housenumber": "4"}


def hard_test2():
    assert address_line_solution("200 Broadway Av") == {"street": "Broadway Av", "housenumber": "200"}


def hard_test3():
    assert address_line_solution("Calle Aduana, 29") == {"street": "Calle Aduana", "housenumber": "29"}


def hard_test4():
    assert address_line_solution("Calle 39 No 1540") == {"street": "Calle 39", "housenumber": "No 1540"}


if __name__ == '__main__':
    easy_test1()
    easy_test2()
    easy_test3()

    medium_test1()
    medium_test2()

    hard_test1()
    hard_test2()
    hard_test3()

