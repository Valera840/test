maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# Победные комбинации
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]
# Вывод карты
def print_maps():
    print(maps[0],maps[1],maps[2])
    print(maps[3],maps[4],maps[5])
    print(maps[6], maps[7],maps[8])

# Сделать ход
def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol

# Получить текущий результат игры

def get_result():
    win = ""
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"


    return win

game_over = False
player1 = True

while game_over == False:

    # 1 вывести карту
    print_maps()

    # 2 делаем ход
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок X, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок O, ваш ход: "))

    step_maps(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

print_maps()

print("Победил Игрок", win)
