""" Програма зберігання паролей
Автор Мирослав Пасічний
Завдання:
1 - доробити функцію save_password()
2 - реалізувати функцію encode_password()
3 - реалізувати функцію decode_password() """

import json

#Завантаження файлу бази даних зі збереженими паролями
def load_database():
    try:
        with open("database.txt", "r") as f: 
            database = f.read().replace("'", "\"")
            database = json.loads(database)        
    except:
        database = {}
    return database 

#Збереження оновлених паролів у файл бази даних
def save_database(database):
    try:
        f = open("database.txt", "w")
        f.write(str(database))
        f.close
        return True
    except:
        return False

def encode_password(pwd):
    """ Тут ТИ маєш реалізувати алгоритм "шифрування" рядка, який передається в цю функцію під назвою змінної "pwd",
    # таким чином, щоб всі символи в ньому змінилися унікальним чином.
    # Ця функція має повертати "зашифрований" рядок під тією самою назвою змінної - 'pwd'  """ 
    return pwd

def decode_password(pwd):
    """ Тут ТИ маєш реалізувати зворотний алгоритм "розшифрування" рядка, який передається в цю функцію під назвою змінної "pwd",
    таким чином, щоб всі символи в ньому повернулися до свого початкового значення.
    Ця функція має повертати "розшифрований" рядок під тією самою назвою змінної - 'pwd' """
    return pwd

def save_password():
    print("\tSAVENIG NEW PASSWORD")
    #Запитати користувача, для якого акаунту він бажає зберегти пароль, він має ввести одним словом наприклад: "capibara@gmail.com"    
    account = input("\tPlease, indicate the account for which your whant to save the password\nAccount:")
    
    """ АЛЕ ПОЧНИ З ЦЬОГО:
     Тут ТОБІ необхідно запропонувати користувачу ввести його пароль для збереження
     Отриманий пароль потрыбно зашифрувати, використовуючи функцію encode_password(),
     та зберегти пару пов'язаних значень - "назва акаунта" : "зашифрований пароль" - у відповідну структуру
     даних, яка зберігається у змінній під назвою 'database' """

    # Збереження новленої бази даних у файл 
    if save_database(database):
        print("Password", database[account], "for account", account, "successfully saved!\n", )
    else:
        print("Ooops! Something went wrong. Database was not updated with your new password :(")


def view_password():
    #Показати користувачу перелік наявних акаунтів, для яких збережені паролі

    accounts = list(database)
    print("\n\tSAVED ACCOUNTS:", len(accounts))
    for acc in accounts:
        i = accounts.index(acc) + 1
        print("\t\t", i, "-", acc)
    #Запитати у користувача номер акаунту, для якого потрібно показати пароль
    account = int(input("\tPlese, select the number of account, for which you whant to see the password:"))
    #Отримати зашифрований пароль з бази даних 
    try:
        pwd = database[accounts[account-1]]
        #Розшифрувати пароль задопомогою функції decode_password()
        pwd = decode_password(pwd)
        #Показати користувачу розшифрований пароль
        print("Password is:")
        print(pwd)
    except:
        #Повідомити, якщо користувач ввів неправильний індекс 
        print("Incorrect index!")

#Головний цикл програми. Щоб завершити і вийти з програми, користувач має обрати "3"
while True:
    database = load_database()
    print("\nMAIN MENU\n\t1. save password \n\t2. view password \n\t3. quit")
    choose = input("select number: ")
    if choose == "1":
        save_password()
    elif choose == "2":
        if len(database):
            view_password()
        else:
            print("Datadase file absent, corrupted or empty. View option will be available after saveing at least one entry.")
    elif choose == "3":
        exit()