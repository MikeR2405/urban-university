import random

first_number = random.randint(3, 20)
print(f'первое случайное число: {first_number}')

result = ''
used_pairs = set()

for num1 in range(1, 20):
    for num2 in range((num1+1), 20):
        if first_number % (num1 + num2) == 0:
            pair = tuple(sorted((num1, num2)))
            if pair not in used_pairs:
                result += str(num1) + str(num2)
                used_pairs.add(pair)

print(f"Нужный пароль: {result}")
