my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0

while index < len(my_list):
    current_element = my_list[index]

    if current_element > 0:
        print(current_element)

    elif current_element == 0:
        index += 1
        continue

    else:
        break
    index += 1
