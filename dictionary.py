# создаем словари account
account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

# создаем словари user
user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

# создаем список user_list
user_list = [user1, user2, user3, user4]

# Просим ввести ключ
key = input('Введите ключ (name или account): ')

# Проверяем ключ
if str.lower(key) == 'name' or str.lower(key) == 'account':
    # выводим значение ключа
    n = 1
    for i in user_list:
        print('значение ключа name для юзера ' + str(n) + ' = ' + i['name'])
        n += 1
    
    # Запращиваем порядковый номер
    number = input('Введите порядковый номер: ')

    # Выводим информацию по порядковому номеру
    try:
        number = int(number)
        print('Данные по юзеру № ' + str(number) + ':')
        number -= 1
        print('имя: ' + str(user_list[number]['name']))
        print('возраст: ' + str(user_list[number]['age']))
        print('логин: ' + str(user_list[number]['account']['login']))
        print('пароль: ' + str(user_list[number]['account']['password']))
    except:
        print('Пользователь с указанным номером не найден')
    
    # Перемещение пользователя в конец списка
    move = input('Введите номер пользователя, которого нужно переместить в конец: ')
    
    try:
        move = int(move)
        move -= 1
        print('Список до изменения:')
        print(str(user_list))
        print('Пользователь с именем ' + str(user_list[move]['name']) + ' перемещен в конец')
        print('Список после изменения:')
        user_del = user_list.pop(move)
        user_list.append(user_del)
        print(user_list)
    except:
        print('Пользователь с указанным номером не найден')
    
    # Вычисляем средний возраст
    ages = [user1['age'], user2['age'], user3['age'], user4['age']]
    average_age = float(sum(ages) / len(ages))
    print('Средний возраст пользователей: ' + str(average_age))

else:
    print('Введенный ключ не найден')
