class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.file_name, 'r') as file:
                products = file.read()
            return products.splitlines()
        except FileNotFoundError:
            return []

    def add(self, *products):
        existing_products = self.get_products()
        existing_names = [line.split(',')[0] for line in existing_products]

        for product in products:
            if product.name not in existing_names:
                with open(self.file_name, 'a') as file:
                    file.write(str(product) + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')


# Первый запуск
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print("Первый запуск:")
print(p2)  # Выводит информацию о Spaghetti
s1.add(p1, p2, p3)  # Добавление продуктов

# Получаем актуальный список продуктов после первого добавления
products_after_first_add = s1.get_products()
for product in products_after_first_add:
    print(product)

# Второй запуск
print("\nВторой запуск:")
s1 = Shop()  # Создаем новый экземпляр Shop для имитации второго запуска
s1.add(p1, p2, p3)  # Повторно добавляем продукты

# Получаем актуальный список продуктов после второго добавления
products_after_second_add = s1.get_products()
for product in products_after_second_add:
    print(product)
