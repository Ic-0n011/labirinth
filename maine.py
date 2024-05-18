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
labyrinth_size = randint(3, 47)
if labyrinth_size % 2 == 0:
    labyrinth_size += 1


# Создаем лабиринт
def create_labyrinth(labyrinth_size):
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


class Drill():
    def __init__(self, x=1, y=1) -> None:
        self.y = y
        self.x = x

    def drill(self) -> bool:
        # собираем доступные направления из кординат бура
        clean_passages = []
        crossroads = None
        if self.y + 2 < labyrinth_size:
            if labyrinth[self.y + 2][self.x] == 1:
                clean_passages.append((1, 0))
        if self.x + 2 < labyrinth_size:
            if labyrinth[self.y][self.x + 2] == 1:
                clean_passages.append((0, 1))
        if self.y - 2 > 0:
            if labyrinth[self.y - 2][self.x] == 1:
                clean_passages.append((-1, 0))
        if self.x - 2 > 0:
            if labyrinth[self.y][self.x - 2] == 1:
                clean_passages.append((0, -1))

        if len(clean_passages) > 1:
            crossroads = (self.x, self.y)

        if clean_passages:  # если есть доступные направления, бурим
            direction = choice(clean_passages)
            for _ in range(2):
                self.y += direction[0]
                self.x += direction[1]
                labyrinth[self.y][self.x] = 0
        else:  # иначе удаляемся
            return 'Del'
        return crossroads


# делаем в нем проходы
def drilling_labyrinth() -> None:
    # создаем бур, делаем вход и выход
    drills = []
    cord_fest_dril = randint(3, labyrinth_size-3)
    if cord_fest_dril % 2 == 0:
        cord_fest_dril += 1
    drills.append(Drill(cord_fest_dril, cord_fest_dril))
    labyrinth[drills[0].x][drills[0].y] = 0
    labyrinth[0][1] = 0
    labyrinth[labyrinth_size-1][labyrinth_size-2] = 0
    while True:
        # Перекресток - если направлений несколько, то сохраняем эту кординату
        for drill in drills:
            result = drill.drill()
            if result == 'Del':
                drills.remove(drill)
            elif result:
                drills.append(Drill(result[0], result[1]))
        if not drills:  # если перекрестковне осталось то заканчиваем бурить
            break


labyrinth = create_labyrinth(labyrinth_size)
drilling_labyrinth()
show(labyrinth)

# FIXME: бульдозер всегда ходит, но не всегда ломает стены
