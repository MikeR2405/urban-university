first = int(input('Введите число:\n'))
second = int(input('Введите число:\n'))
third = int(input('Введите число:\n'))

if first == second and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)