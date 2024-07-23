import string
import re


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = {}

    def get_all_words(self):
        if self.all_words:
            return self.all_words

        for file_name in self.file_names:
            words = []
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    for line in file:
                        line = line.lower()
                        line = re.sub(r"[{}]".format(re.escape(string.punctuation.replace("'", ""))), '', line)
                        words.extend(line.split())
                self.all_words[file_name] = words
            except FileNotFoundError:
                print(f'Файл {file_name} не найден.')

        return self.all_words

    def find(self, word):
        self.get_all_words()
        result = {}

        for file_name, words in self.all_words.items():
            if word.lower() in words:
                result[file_name] = words.index(word.lower()) + 1

        return result

    def count(self, word):
        self.get_all_words()
        result = {}

        for file_name, words in self.all_words.items():
            result[file_name] = words.count(word.lower())

        return result


# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('text'))  # Позиция слова
print(finder2.count('text'))  # Количество слов
