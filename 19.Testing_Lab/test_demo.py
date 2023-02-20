def add(x, y):
    return x + y


def test_add__when_5_and_2__expect_7():
    expected = 7
    actual = add(5, 2)

    if expected == actual:
        print('OK')
    else:
        print('Wrong')

def test_add__when_10_and_5__expect_15():
    expected = 15
    actual = add(10, 5)

    if expected == actual:
        print('OK')
    else:
        print('Wrong')

def test_add__when_None_and_2__expect_exception():
    expected = 0
    actual = add(None, 2)

    if actual == expected:
        print('OK')
    else:
        print('Wrong')


test_add__when_5_and_2__expect_7()
test_add__when_10_and_5__expect_15()