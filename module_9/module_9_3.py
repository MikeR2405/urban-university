first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i) - len(s) for i, s in zip(first, second) if len(i) != len(s))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))  # если мы предполагаем, что списки одинаковой длинны
# second_result = (len(first[i])==len(second[i]) for i in range(min(len(first), len(second)))) - если предполагаем, что списки разные
# и тогда используется min для определения минимальной из длин этих двух списков. 
# Это число будет максимальным количеством итераций, которые мы можем выполнить в генераторном выражении, 
# чтобы не выйти за границы одного из списков.
print(list(first_result))
print(list(second_result))
