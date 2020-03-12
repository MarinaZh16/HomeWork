def up_f(string):
    return string.upper()


def low_f(string):
    return string.lower()
a='Hello, world!'
b='Welcome to California!'
c='Dream Team'
up_strings=list(map(up_f, (a, b, c)))

low_strings=list(map(low_f, (a, b, c)))
