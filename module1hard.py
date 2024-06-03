grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#  первое. Отсортируем студентов по алфовиту
sorted_students = sorted(students)
# теперь вычеслим средний бал студентов
# для этого задаем пустой словарь
average_grades={}
for i, student in enumerate(sorted_students):
    average_grade= sum(grades[i])/len(grades[i])
    average_grades[student]= average_grade
#  теперь все вместе выводим на экран средний бал и студент
print(average_grades)