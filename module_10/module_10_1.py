from time import sleep
from datetime import datetime
import threading

def wite_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'Какое-то слово № {i}\n')
        sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')

start_time = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

end_time = datetime.now()
print(f'Время выполнения: {end_time - start_time}')

start_time_threads = datetime.now()
threads = [
threading.Thread(target=wite_words, args=(10, 'example5.txt')),
threading.Thread(target=wite_words, args=(30, 'example6.txt')),
threading.Thread(target=wite_words, args=(200, 'example7.txt')),
threading.Thread(target=wite_words, args=(100, 'example8.txt'))]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time_threads = datetime.now()
print(f'Время выполнения: {end_time_threads - start_time_threads}')