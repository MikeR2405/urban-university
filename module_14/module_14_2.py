import sqlite3

# Подключение к базе данных
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Код из предыдущего задания: создание таблицы и вставка записей
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Вставка 10 записей в таблицу Users
users = [
    ('User  1', 'example1@gmail.com', 10, 1000),
    ('User  2', 'example2@gmail.com', 20, 1000),
    ('User  3', 'example3@gmail.com', 30, 1000),
    ('User  4', 'example4@gmail.com', 40, 1000),
    ('User  5', 'example5@gmail.com', 50, 1000),
    ('User  6', 'example6@gmail.com', 60, 1000),
    ('User  7', 'example7@gmail.com', 70, 1000),
    ('User  8', 'example8@gmail.com', 80, 1000),
    ('User  9', 'example9@gmail.com', 90, 1000),
    ('User  10', 'example10@gmail.com', 100, 1000)
]

cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users)
connection.commit()

# Обновление баланса для пользователей с нечетным id
cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 = 1')
connection.commit()

# Удаление пользователей с id, кратным 3
cursor.execute('DELETE FROM Users WHERE id % 3 = 1')
connection.commit()

# Удаление пользователя с id=6
cursor.execute('DELETE FROM Users WHERE id = 6')
connection.commit()

# Подсчет общего количества пользователей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчет суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Вывод среднего баланса
if total_users > 0:
    print(all_balances / total_users)
else:
    print("Нет записей для вычисления среднего баланса.")

# Закрытие соединения
connection.close()
