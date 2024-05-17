from random import randint, choice

"""
Лабиринт
    нечетное колличество (3x3 9x9 5x5 и тд)

    ⬛⬜🟥🟩🟦

    ⬛⬛⬛⬛⬛
    ⬜⬜⬛⬜⬛
    ⬛⬜⬛⬜⬜
    ⬛⬜⬜⬜⬛
    ⬛⬛⬛⬛⬛

    полностью заполняем стенами -> кидаем бульдозер(начн в четн клетке)
      который делает нам проход(если в двух клетках от него стены - он их ломает)
        заканчивает когда в четных нет стен
          все четные свободны | есть выход
"""
labyrinth_size = 30


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


# показ лабиринта
def show(labyrinth):
    for col in labyrinth:
        cells = []
        for cell in col:
            if cell == 1:
                cells.append('⬛')
            else:
                cells.append('⬜')
        print(*cells)


# делаем в нем проходы
def drilling_labyrinth() -> None:
    # создаем кординаты бура, делаем вход и выход
    drill = [1, 1]
    labyrinth[drill[0]][drill[1]] = 0
    labyrinth[0][1] = 0

    labyrinth[labyrinth_size][labyrinth_size-1] = 0
    crossroads = []
    while True:
        clean_passages = []
        # собираем доступные направления из кординат бура
        if drill[0] + 2 < labyrinth_size:
            if labyrinth[drill[0] + 2][drill[1]] == 1:
                clean_passages.append((1, 0))
        if drill[1] + 2 < labyrinth_size:
            if labyrinth[drill[0]][drill[1] + 2]  == 1:
                clean_passages.append((0, 1))
        if drill[0] - 2 > 0:
            if labyrinth[drill[0] - 2][drill[1]] == 1:
                clean_passages.append((-1, 0))
        if drill[1] - 2 > 0:
            if labyrinth[drill[0]][drill[1] - 2] == 1:
                clean_passages.append((0, -1))
        
        # Перекресток - если направлений несколько, то сохраняем эту кординату
        if clean_passages:
            crossroads.append([drill[0], drill[1]])
        
        if clean_passages:  # если есть доступные направления, бурим
            direction = choice(clean_passages)
            for _ in range(2):
                drill[0] += direction[0]
                drill[1] += direction[1]
                labyrinth[drill[0]][drill[1]] = 0
        elif crossroads:  # иначе перемещаемся на прошлые перекрестки
            drill = crossroads[-1]
            crossroads.pop(-1)
        else:  # если перекрестковне осталось то заканчиваем бурить
            break
        


labyrinth = create_labyrinth(labyrinth_size)
drilling_labyrinth()
show(labyrinth)