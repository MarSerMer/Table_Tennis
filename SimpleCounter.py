WINNING_POINTS: int = 11
BALANCE_POINTS: int = 10
BAL_DIFF: int = 2  # balance difference
CHANGE_PLACE_POINT: int = 5

print("Определите первого игрока. Он будет подавать первым. ")
player1 = input("Введите фамилию и имя первого игрока: ")
player2 = input("Введите фамилию и имя второго игрока: ")
final_game = bool(input("Это решающая партия? Введите 1 если да, введите 0 если нет: "))


def simple_counter(player1: str, player2: str, final_game: bool) -> None:
    print("Далее вводите 1 при выигрыше очка первым игроком, либо вводите 2 при выигрыше очка вторым игроком.")
    count1: int = 0
    count2: int = 0
    pl1: list[int] = [1, 2, 5, 6, 9, 10, 13, 14, 17, 18]
    pl2: list[int] = [3, 4, 7, 8, 11, 12, 15, 16, 19, 20]
    serve: int = 1
    while True:
        if count1 == BALANCE_POINTS and count2 == BALANCE_POINTS:
            print("Баланс!")
            balance_count(player1, player2)
            break
        elif count1 == WINNING_POINTS:
            print(f'Счёт {player1} {count1} : {player2} {count2}.\nПобедитель {player1}')
            break
        elif count2 == WINNING_POINTS:
            print(f'Счёт {player2} {count2} : {player1} {count1}.\nПобедитель {player2}')
            break
        elif (serve in pl1) and count1 != WINNING_POINTS and count2 != WINNING_POINTS:
            print(f'Счёт {player1} {count1} : {player2} {count2}')
            print("Подаёт " + player1)
            while True:
                temp = int(input("Очко выиграл: "))  # не терпит пустого ввода и всего, что не интуется!
                if temp == 1:
                    count1 += 1
                    if final_game and count1 == 5:
                        print("Поменяйтесь местами")
                        final_game = False
                    serve += 1
                    break
                elif temp == 2:
                    count2 += 1
                    if final_game and count2 == 5:
                        print("Поменяйтесь местами")
                        final_game = False
                    serve += 1
                    break
                else:
                    print(
                        f'Неправильный ввод. Введите цифру 1, если выиграл " {player1}, либо цифру 2, если выиграл {player2}')

        elif (serve in pl2) and count1 != WINNING_POINTS and count2 != WINNING_POINTS:
            print(f"Счёт {player2} {count2} : {player1} {count1}")
            print("Подаёт " + player2)
            while True:
                temp = int(input("Очко выиграл: "))  # не терпит пустого ввода и всего, что не интуется!
                if temp == 1:
                    count1 += 1
                    if final_game and count1 == 5:
                        print("Поменяйтесь местами")
                    serve += 1
                    break
                elif temp == 2:
                    count2 += 1
                    if final_game and count2 == 5:
                        print("Поменяйтесь местами")
                    serve += 1
                    break
                else:
                    print(
                        "Неправильный ввод. Введите цифру 1, если выиграл " + player1 + ", либо цифру 2, если выиграл " + player2 + " ")


def balance_count(player1, player2):
    serveBal = 1  # первый подающий всегда тот же игрок, который первым подавал в основной партии
    count1 = BALANCE_POINTS
    count2 = BALANCE_POINTS
    while True:  # считаем баланс, он играется до разницы в 2 очка
        if serveBal == 1:
            print(f'Счёт {player1} {count1} : {player2} {count2}')
            print("Подаёт " + player1)
            while True:
                temp = int(input("Очко выиграл: "))  # не терпит пустого ввода и всего, что не интуется!
                if temp == 1:
                    count1 += 1
                    serveBal = 2
                    break
                elif temp == 2:
                    count2 += 1
                    serveBal = 2
                    break
                else:
                    print(
                        "Неправильный ввод. Введите цифру 1, если выиграл " + player1 + ", либо цифру 2, если выиграл " + player2 + " ")
            if count1 == count2 + BAL_DIFF:
                print(f'Счёт {player1} {count1} : {player2} {count2}')
                print("Победитель " + player1)
                break
            if count2 == count1 + BAL_DIFF:
                print(f"Счёт {player2} {count2} : {player1} {count1}")
                print("Победитель " + player2)
                break
        elif serveBal == 2:
            print(f"Счёт {player2} {count2} : {player1} {count1}")
            print("Подаёт " + player2)
            while True:
                temp = int(input("Очко выиграл: "))  # не терпит пустого ввода и всего, что не интуется!
                if temp == 1:
                    count1 += 1
                    serveBal = 1
                    break
                elif temp == 2:
                    count2 += 1
                    serveBal = 1
                    break
                else:
                    print(
                        "Неправильный ввод. "
                        "Введите цифру 1, если выиграл " + player1 + ", либо цифру 2, если выиграл " + player2 + " ")
            if count1 == count2 + BAL_DIFF:
                print(f'Счёт {player1} {count1} : {player2} {count2}')
                print("Победитель " + player1)
                break
            if count2 == count1 + BAL_DIFF:
                print(f"Счёт {player2} {count2} : {player1} {count1}")
                print("Победитель " + player2)
                break


if __name__ == '__main__':
    simple_counter(player1, player2, final_game)
