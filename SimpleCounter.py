WINNING_POINTS = 11
BALANCE_POINTS = 10
BAL_DIFF = 2 #balance difference

print("Определите первого игрока. Он будет подавать первым. ")
player1 = input ("Введите фамилию первого игрока: ")
player2 = input ("Введите фамилию второго игрока: ")

def SimpleCounter(player1, player2):

    print("Далее вводите 1 при выигрыше очка первым игроком, либо вводите 2 при выигрыше очка вторым игроком.")
    count1 = 0
    count2 = 0
    pl1 = [1,2,5,6,9,10,13,14,17,18,21,23]
    pl2 = [3,4,7,8,11,12,15,16,19,20,22,24]
    serve = 1
    while True:
        if  count1==BALANCE_POINTS and count2==BALANCE_POINTS:
            print("Баланс!")
            Balance_count(player1,player2)
            break
        elif count1 == WINNING_POINTS:
            print("Победил " + player1)
            break
        elif count2 == WINNING_POINTS:
            print("Победил " + player2)
            break
        elif (serve in pl1) and count1!=WINNING_POINTS and count2!=WINNING_POINTS:
            print(f'Счет {player1} {count1} : {player2} {count2}')
            print("Подает " + player1)
            while True:
                temp = int(input("Очко выиграл: ")) # не терпит пустого ввода и всего, что не интуется!
                if temp == 1:
                    count1 += 1
                    serve += 1
                    break
                elif temp == 2:
                    count2 += 1
                    serve += 1
                    break
                else:
                    print(f'Неправильный ввод. Введите цифру 1, если выиграл " {player1}, либо цифру 2, если выиграл {player2}')

        elif (serve in pl2) and count1!=WINNING_POINTS and count2!=WINNING_POINTS:
            print(f"Счет {player2} {count2} : {player1} {count1}")
            print("Подает " + player2)
            while True:
                temp = int(input("Очко выиграл: ")) # не терпит пустого ввода и всего, что не интуется!
                if temp == 1:
                    count1 += 1
                    serve += 1
                    break
                elif temp == 2:
                    count2 += 1
                    serve += 1
                    break
                else:
                    print(
                        "Неправильный ввод. Введите цифру 1, если выиграл " + player1 + ", либо цифру 2, если выиграл " + player2 + " ")

def Balance_count(player1, player2): 
    serveBal = 1 #первый подающий всегда тот же игрок, который первым подавал в основной партии
    count1 = BALANCE_POINTS
    count2 = BALANCE_POINTS
    while True: # считаем баланс, он играется до разницы в 2 очка
        if serveBal==1:
            print("Подает " + player1)
            while True:
                temp = int(input("Очко выиграл: ")) # не терпит пустого ввода и всего, что не интуется!
                if temp == 1:
                    count1 += 1
                    serveBal=2
                    break
                elif temp == 2:
                    count2 += 1
                    serveBal=2
                    break
                else:
                    print(
                        "Неправильный ввод. Введите цифру 1, если выиграл " + player1 + ", либо цифру 2, если выиграл " + player2 + " ")
            if count1==count2+BAL_DIFF:
                print("Выиграл " + player1)
                break
            if count2==count1+BAL_DIFF:
                print("Выиграл " + player2)
                break
        elif serveBal==2:
            print("Подает " + player2)
            while True:
                temp = int(input("Очко выиграл: ")) # не терпит пустого ввода и всего, что не интуется!
                if temp == 1:
                    count1 += 1
                    serveBal=1
                    break
                elif temp == 2:
                    count2 += 1
                    serveBal=1
                    break
                else:
                    print(
                        "Неправильный ввод. "
                        "Введите цифру 1, если выиграл " + player1 + ", либо цифру 2, если выиграл " + player2 + " ")
            if count1==count2+BAL_DIFF:
                print("Выиграл " + player1)
                break
            if count2==count1+BAL_DIFF:
                print("Выиграл " + player2)
                break

SimpleCounter(player1,player2)

