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
    if maps[0] == 1 or maps[1] == 2 or maps[2] == 3 or maps[3] == 4 or maps[4] == 5 or maps[5] == 6 or maps[6] == 7 or \
            maps[7] == 8 or maps[8] == 9:
        for i in victories:
            if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
                win = "Победил Игрок X"
            if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
                win = "Победил Игрок O"
    else:
        win="Ничья"

    return win

game_over = False
player1 = True

while game_over == False:

    # 1 вывести карту
    print_maps()

    # 2 делаем ход
    if player1 == True:
        step = input("Игрок X, ваш ход: ")
        if step.isdigit():
            step = int(step)
            if 1 <= step <= 9:
                if maps[step-1] != "O" and maps[step-1] != "X":
                    symbol = "X"
                    step_maps(step, symbol)
                    player1 = not (player1)
                else:
                    print("ячейка занята")
            else:
                print("Вы ввели число вне диапазона,пожалуйста введите число от 1 до 9")
        else:
            print("Вы ввели не числовое значение, пожалуйста введите число от 1 до 9")
    else:
        step = input("Игрок O, ваш ход: ")

        if step.isdigit():
            step = int(step)
            if 1 <= step <= 9:
                if maps[step-1] != "O" and maps[step-1] != "X":
                    symbol = "O"
                    step_maps(step, symbol)
                    player1 = not (player1)
                else:
                    print("ячейка занята")
            else:
                print("Вы ввели число вне диапазона,пожалуйста введите число от 1 до 9")
        else:
            print("Вы ввели не числовое значение, пожалуйста введите число от 1 до 9")

    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False


print_maps()

print( win)
