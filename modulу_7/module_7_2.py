def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings):
            # Получаем текущую позицию в файле
            byte_position = file.tell()
            # Записываем строку в файл
            file.write(string + '\n')
            # Сохраняем позицию и строку в словаре
            strings_positions[(line_number + 1, byte_position)] = string

    return strings_positions

# # Пример использования
# result = custom_write('output.txt', ['Text for tell.', 'Используйте кодировку utf-8.'])
# print(result)
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)