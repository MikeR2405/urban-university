import time
from multiprocessing import Pool
import os

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            all_data.append(line.strip())
            line = f.readline()
    return all_data

if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейное выполнение
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    line_time = time.time() - start_time
    print(f'Линейное выполнение: {line_time}')

    # Многопроцессное выполнение
    start = time.time()
    with Pool(processes=4) as p:
        p.map(read_info, filenames)
    multiprocessing_time = time.time() - start
    print(f'Многопроцессное выполнение: {multiprocessing_time}')