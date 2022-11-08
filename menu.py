Урок 8. Python: от простого к практике. Продолжение Доделать решение задачи:
# Задача: Создать информационную систему
# позволяющую работать с сотрудниками некой компании \ студентами вуза


def option():
    print("\nВас приветствует информационная система обучения студентов!")
    ch = int(input('Введите что хотите сделать: \n \
    1: Поиск ID студента по фамилии \n \
    2: Посмотреть домашнее задание  \n \
    3: Выход\n \
    Ваш выбор: '))

    if ch == 1:
        Surn = str(input("Введите фамилию студента : "))
        if Surn in si.stud_card['Фамилия']:
            index = si.stud_card['Фамилия'].index(Surn)
        print(f"{si.stud_card['ID'][index]}, {si.stud_card['Имя'][index]},{si.stud_card['Фамилия'][index]}\n,{si.stud_card['Дата рождения'][index]}, {si.stud_card['Успеваемость'][index]}")
        print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()

    elif ch == 2:
        c = input('Введите ID студента для вывода учебного задания: ')
        if c in cab.class_card['ID']:
            index = cab.class_card['ID'].index(c)
            print(f" Сидит в классе - {cab.class_card['Предмет'][index]}\n\, аудитория - {cab.class_card['предмет'][index]}, это {cab.class_card['Ряд'][index]}, парта - {cab.class_card['Вид парты'][index]}, Имя: {si.stud_card['Имя'][index]}, Фамилия - {si.stud_card['Фамилия'][index]}, и успеваемасть у студента: {si.stud_card['Успеваемость'][index]}")
            print('\nХотите выполнить другую операцию??? Y или N: ')
            num = input()
            if num == 'Y' or 'y' or 'У' or 'у':
                option()
            exit()
    else:
        print('еще раз')
    exit()


option()
