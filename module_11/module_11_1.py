# Requests
import requests
import json
from bs4 import BeautifulSoup

response = requests.get('https://www.binaryjazz.us/wp-json/genrenator/v1/genre/')
# Проверка статуса ответа
print(f'Status code: {response.status_code}')

data = response.json()
# Печать содержимого ответа в формате JSON
print(json.dumps(data, indent=4, ensure_ascii=False))

url = 'https://github.com/MikeR2405/urban-university/blob/master/module_10/module_10_4(without%20Lock).py'
headers = {'module_10': 'module_10_4(without%20Lock)'}

r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')
print(r.headers['Content-Type'])
print(r.text)
# # Теперь можем получить доступ к HTML-элементам и тексту
# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())  # печатает HTML в читаемом формате
# # или извлечь конкретный текст
# # print(soup.get_text())  # печатает текстовое содержимое HTML

# метод Options
options_response = requests.options(url, headers=headers)
print(f'Status code: {options_response.status_code}')
print(options_response.headers)

U = 'https://github.com/MikeR2405/urban-university/blob/master/'
r = requests.head(U, headers=headers)
print(r.status_code)
print(r.content)
'''в коде используются 3 различных метода библиотеки requests:
requests.get()
requests.options()
requests.head()'''
# Matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание линейного графика
plt.plot(x, y, marker='o')

# Добавление заголовка и меток осей
plt.title('Простой линейный график')
plt.xlabel('Ось Х')
plt.ylabel('Ось У')

# Отображение графика
plt.show()
'''В приведенном коде используется 4 функции из библиотеки matplotlib:
plt.plot(): Создает линейный график с заданными данными.
plt.title(): Добавляет заголовок к графику.
plt.xlabel(): Добавляет метку к оси X.
plt.ylabel(): Добавляет метку к оси Y.
plt.show(): Отображает график на экране.
Таким образом, в коде используется 5 функций из библиотеки matplotlib'''

#NumPy
import numpy as np


# Получение данных из API
response = requests.get('https://www.binaryjazz.us/wp-json/genrenator/v1/genre/')
data = response.json()

# Преобразование данных в массив numpy (предположим, что это список чисел)
data_list = [2, 3, 5, 7, 11]  # преобразовываем JSON в числовой список, если это возможно
data_array = np.array(data_list)

# Выполнение операций с использованием numpy
average = np.mean(data_array)
std_dev = np.std(data_array)

print(f'Average: {average}')
print(f'Standard Deviation: {std_dev}')
'''В приведенном коде использованы следующие методы из библиотеки numpy:
np.array() - Создает массив numpy из списка data_list.
np.mean() - Вычисляет среднее значение элементов массива data_array.
np.std() - Вычисляет стандартное отклонение элементов массива data_array.
Итак, в коде используется 3 метода библиотеки numpy.'''

