def set_value(prp, value):
    r = open('settings.txt').readlines()
    w = open('settings.txt', 'w')
    r[['THEME', 'BEST'].index(prp)] = repr(value) + '\n'

    w.write(''.join(r))
    w.close()


def get_values():
    global BEST
    global THEME
    THEME, BEST = [eval(value) for value in open('settings.txt').readlines()]


COORD = {
    'count': (30, 25),
    'best': (30, 105),
    'restart': (405, 25),
    'settings': (405, 105)
}
BEST = ...
THEME = ...
get_values()