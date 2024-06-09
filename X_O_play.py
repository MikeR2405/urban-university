def draw_area():
    for i in area:
        print(*i)
    print()


def check_winner(area):
    # Проверка строк
    for row in area:
        if row.count(row[0]) == len(row) and row[0] != '*':
            return row[0]
    # Проверка столбцов
    for col in range(len(area[0])):
        check = []
        for row in area:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != '*':
            return check[0]
    # Проверка диагоналей
    if area[0][0] == area[1][1] == area[2][2] != '*':
        return area[0][0]
    if area[0][2] == area[1][1] == area[2][0] != '*':
        return area[1][1]
    return None


area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print("Добро пожаловать в крестики-нолики")
print("-----------------------------------")
draw_area()

for turn in range(1, 10):
    print(f'{turn}')
    if turn % 2 == 0:
        turn_char = "0"
        print('Ходят нолики')
    else:
        turn_char = 'x'
        print('Ходят крестики')

    while True:
        try:
            row = int(input('Введите номер строки (1,2,3):\n ')) - 1
            column = int(input('Введите номер столбца (1,2,3):\n')) - 1
            if row < 0 or row > 2 or column < 0 or column > 2:
                print('Номер строки или столбца вне допустимого диапазона. Пожалуйста, попробуйте снова.')
                continue
            if area[row][column] == '*':
                area[row][column] = turn_char
                break  # Выйти из цикла, если ход успешно сделан
            else:
                print('Ячейка уже занята, попробуйте снова!')
        except ValueError:
            print("Пожалуйста, введите корректные числа.")

    draw_area()

    winner = check_winner(area)
    if winner:
        print(f'Победитель: {winner}')
        break
    elif turn == 9:
        print('Ничья!')
        break
