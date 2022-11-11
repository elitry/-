positions = list(range(1, 10))

def drawing(board): #задание поля
    return print(board[6:9], board[3:6], board[0:3], sep="\n") #поле адаптировано под ПК, а именно под цировую клавиатуру

drawing(positions) #отрисовка готового поля

def game():
    turn = 'X'
    count = 0
    for i in range(10): #сам процесс игры, постановки своего символа на поле
        print("На какую позицию поставить" + ' ' + turn + "?")
        move = int(input())
        if positions[move-1] not in ('X','O'):
            positions[move-1] = turn
            count += 1
        else:
            print("Эта позиция уже занята")
        drawing(positions)
        if count >= 5: #проврека возможного выигрыша
            if ((positions[7] == positions [8] == positions [9]) \
                or (positions[4] == positions[5] == positions [6]) \
                or (positions[1] == positions [2] == positions [3]) \
                or (positions[1] == positions [4] == positions [7]) \
                or (positions[2] == positions [5] == positions [9]) \
                or (positions [3] == positions[6] == positions [9]) \
                or (positions[1] == positions[5] == positions [9]) \
                or (positions[3] == positions[5] == positions [7])):
                print("Игра окончена," +turn + "победил!" )
        if count == 9: #проверка ничьей
            print("Игра окончена, ничья!")
        if turn == 'X': #смена хода игроков
            turn = 'O'
        else:
            turn = 'X'
game()