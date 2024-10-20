import sqlite3


def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL,
            image_path TEXT NOT NULL )
    ''')
    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products


def add_products():
    products = [
        ('Product1', 'Описание 1', 100, r'C:\Users\SONY\PycharmProjects\URBAN\module_14\files\1.png'),
        ('Product2', 'Описание 2', 200, r'C:\Users\SONY\PycharmProjects\URBAN\module_14\files\2.png'),
        ('Product3', 'Описание 3', 300, r'C:\Users\SONY\PycharmProjects\URBAN\module_14\files\3.png'),
        ('Product4', 'Описание 4', 400, r'C:\Users\SONY\PycharmProjects\URBAN\module_14\files\4.png')
    ]

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.executemany('INSERT INTO Products (title, description, price, image_path) VALUES (?, ?, ?, ?)', products)

    conn.commit()
    conn.close()

    if __name__ == '__main__':
        initiate_db()  # Инициализация базы данных
        add_products()  # Добавление продуктов
