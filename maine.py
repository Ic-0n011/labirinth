from random import randint, choice

"""
Лабиринт
    нечетное колличество (3x3 9x9 5x5 и тд)

    [1][1][1][1][1]
    [ ][ ][1][ ][1]
    [1][ ][1][ ][ ]
    [1][ ][ ][ ][1]
    [1][1][1][1][1]

    полностью заполняем стенами -> кидаем бульдозер(начн в четн клетке)
      который делает нам проход(если в двух клетках от него стены - он их ломает)
        заканчивает когда в четных нет стен
          все четные свободны | есть выход
"""
labyrinth_size = 15


# Создаем лабиринт

def create_labyrinth(labyrinth_size):
    if labyrinth_size % 2 == 0:
        labyrinth_size += 1
    labyrinth = []
    for n in range(labyrinth_size):
        labyrinth.append([])
        for _ in range(labyrinth_size):
            labyrinth[n].append(1)
    return labyrinth


def show(labyrinth):
    for col in labyrinth:
        cells = []
        for cell in col:
            if cell == 1:
                cells.append('[+]')
            else:
                cells.append('[ ]')
        print(*cells)


labyrinth = create_labyrinth(labyrinth_size)


# делаем в нем проходы

def drilling_labyrinth(labyrinth, labyrinth_size):
    drill_cords = [1, 1]
    drilling = True
    labyrinth[drill_cords[0]][drill_cords[1]] = 0
    while drilling:
        direction = []
        if 0 < drill_cords[1] - 2:
            direction.append((0, -1))
        if drill_cords[1] + 2 < labyrinth_size:
            direction.append((0, 1))
        if 0 < drill_cords[0] - 2:
            direction.append((-1, 0))
        if drill_cords[0] + 2 < labyrinth_size:
            direction.append((1, 0))

        if direction and randint(0, 100) != 1: # TODO: ЧЕТНОСТЬ
            choice_direction = choice(direction)
            show(labyrinth)
            for _ in range(2):
                print(drill_cords, choice_direction)
                drill_cords[0] += choice_direction[0]
                drill_cords[1] += choice_direction[1]
                labyrinth[drill_cords[0]][drill_cords[1]] = 0
        else:
            drilling = False
            break
    return labyrinth


labyrinth = drilling_labyrinth(labyrinth, labyrinth_size)


