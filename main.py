# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Объявление переменных
completed_homeworks = 12
spent_hours = 1.5
course_name = 'Python'
# Вычисление времени на одно задание
time_per_task = spent_hours / completed_homeworks

# Вывод строки с использованием переменных
print(f"Курс: {course_name}, всего задач:{completed_homeworks}, затрачено часов: {spent_hours}, среднее время выполнения {time_per_task} часа.")