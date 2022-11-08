# 3. Создайте программу для игры в ""Крестики-нолики"".

area = [i for i in range(1,10)]
def drawArea(a):#функция прорисовки игрового поля
    print('-'*13)
    print('|', a[0], '|', a[1], '|', a[2], '|')
    print('-'*13)
    print('|', a[3], '|', a[4], '|', a[5], '|')
    print('-'*13)
    print('|', a[6], '|', a[7], '|', a[8], '|')

hod = 1#переменная подсчета хода
player=['X', 'O']#список знаков игроков
def inputPlayer(a, znak):
    global hod
    print('в какую клеточку поставить символ', znak, '?')#вопрос игроку
    answer = int(input())#ответ игрока
    #проверка на наличие клетки вообще и в частности на свободную
    if answer > 0 and answer < 10 and answer in area:
        a[answer-1] = znak#записать в клетку знгак игрока вместо цифры
        hod += 1
    else:
        #если клетка занята или вообще нет такой, то давать сообщение
        print('В данную клеточку нельзя поставить', znak, 'ее либо нет, либо она занята.')

#победная комбинация
winComb = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#функция проверки победф
def checkWin():
    for element in winComb:#проход по победной комбинации
        if area[element[0]]==area[element[1]]==area[element[2]]:
            return area[element[1]]

def gamePlay():#функция запуска игры
    global hod
    drawArea(area)#прорисовка поля в начале игры
    while hod < 10:#играем до девяти ходов
        if hod%2 != 0:#проверяем, какой игрок ходит
            inputPlayer(area, player[0])#передаем ход первому игроку
        else:
            inputPlayer(area, player[1])#передаем ход второму игроку
        drawArea(area)#рпорисовка поля после каждого хода

        if checkWin() == player[0] or checkWin() == player[1]:
            print('ПОБЕДА:', checkWin())
            break
        elif hod > 9:
            print('НИЧЬЯ')

gamePlay()