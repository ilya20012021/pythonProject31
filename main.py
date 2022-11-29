import add
import file
import sort
import update
import where

print('Привет! Начнем работу!')
n = 1
while(n != 0):
    m = ["создать файл(нажмите 1)","cортрировка по столбцу(нажмите 2)","вывод записей,после введенного времени(нажмите 3)","дополнение записей(нажмите 4)","обновление информации(нажмите 5)"]
    print(f'Выберите, что вашей душеньке угодно:')
    for i in m:
        print(i)
    s = str(input())
    if(s == "1"):
        file.create()
    elif(s == "2"):
        sort.values()
    elif(s == "3"):
        where.condition()
    elif(s == "4"):
        add.add()
    elif (s == "5"):
        update.upd()
    else:
        print("Такой функции нет!")
    ans = ["да","нет"]
    print(f"Хотите ли вы продолжить работу с данным ПО?")
    for i in ans:
        print(i)
    s = str(input("Введите ответ:"))
    if(s == ans[0]):
        n += 1
    elif(s == ans[1]):
        break
    else:
        print("Ничего непонятно")

print("Спасибо, что выбрали меня!")