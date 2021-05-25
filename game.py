import pygame

import random


def print_grid():
    print('<GRID>')
    for e__ in grid:
        print(' '.join(map(str, e__)))
    print('</GRID>')


def draw_grid():
    for y in range(n):
        for x in range(n):
            screen.blit(images[grid[y][x]],
                        (50 + 400 / 21 * (x + 1) + 400 / 21 * 4 * x, 50 + 400 / 21 * (y + 1) + 400 / 21 * 4 * y))


def list_sum(lst: list):
    r = []
    for elem in lst:
        r += elem
    return r


def add_number(choices: list = None):
    global grid
    if choices is None:
        choices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
    c = random.choice(choices)
    if all(list_sum(grid)):
        print('YOU LOST!')
        grid = [[0] * n for _ in range(n)]
        add_number()
        # raise IndexError('No free cells!')
    while True:
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        if not grid[i][j]:
            grid[i][j] = c
            return


def del_spaces():
    for i in range(n):
        j = 0
        while j < len(grid[i]):
            if grid[i][j]:
                j += 1
            else:
                del grid[i][j]


def move_left():
    cop = grid.copy()
    del_spaces()
    for i in range(n):
        for j in range(len(grid[i]) - 1):
            if grid[i][j] == grid[i][j + 1]:
                grid[i][j] *= 2
                grid[i][j + 1] = 0
    del_spaces()
    # Filling:
    for i in range(n):
        grid[i] = grid[i].copy() + [0] * (n - len(grid[i]))
    if cop != grid:
        add_number()


def move_right():
    cop = grid.copy()
    del_spaces()
    for i in range(n):
        for j in range(len(grid[i]) - 2, -1, -1):
            if grid[i][j] == grid[i][j + 1]:
                grid[i][j + 1] *= 2
                grid[i][j] = 0
    del_spaces()
    # Filling:
    for i in range(n):
        grid[i] = [0] * (n - len(grid[i])) + grid[i].copy()
    if cop != grid:
        add_number()


def transpose_array(lst: list):
    return [[lst[j][i] for j in range(n)] for i in range(n)]


def move_down():
    global grid
    cop = grid.copy()
    grid = transpose_array(grid)

    del_spaces()
    for i in range(n):
        for j in range(len(grid[i]) - 2, -1, -1):
            if grid[i][j] == grid[i][j + 1]:
                grid[i][j+1] *= 2
                grid[i][j] = 0
    del_spaces()
    # Filling:
    for i in range(n):
        grid[i] = [0] * (n - len(grid[i])) + grid[i].copy()
    grid = transpose_array(grid)
    if cop != grid:
        add_number()


def move_up():
    global grid

    cop = grid.copy()
    grid = transpose_array(grid)

    del_spaces()
    for i in range(n):
        for j in range(len(grid[i]) - 1):
            if grid[i][j] == grid[i][j + 1]:
                grid[i][j] *= 2
                grid[i][j + 1] = 0
    del_spaces()
    # Filling:
    for i in range(n):
        grid[i] = grid[i].copy() + [0] * (n - len(grid[i]))
    grid = transpose_array(grid)
    if cop != grid:
        add_number()


images = {2 ** i: pygame.transform.scale(pygame.image.load(f'{2 ** i}.png'), (400 // 21 * 4, 400 // 21 * 4)) for i in
          range(1, 22)}
images[0] = pygame.transform.scale(pygame.image.load('0.png'), (400 // 21 * 4, 400 // 21 * 4))
n = 4  # Size of the grid.
# grid = [[0] * n for _ in range(n)]
# add_number()
# add_number()
grid = [
    [2, 2, 8, 0],
    [2, 2, 4, 0],
    [4, 2, 2, 0],
    [8, 0, 2, 0],
]
grid.reverse()
pygame.init()
screen = pygame.display.set_mode((500, 500))
field = pygame.transform.scale(pygame.image.load(f'field{n}.png'), (400, 400))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.KEYUP and e.key == pygame.K_UP:
            move_up()
        if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
            move_down()
        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
            move_left()
        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
            move_right()
        if e.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_a] and \
                pygame.key.get_pressed()[pygame.K_d] and \
                pygame.key.get_pressed()[pygame.K_5] and \
                pygame.key.get_pressed()[pygame.K_1] and \
                pygame.key.get_pressed()[pygame.K_2]:
            print('DONE')
            add_number([512])

    screen.blit(field, (50, 50))
    draw_grid()
    pygame.display.flip()
