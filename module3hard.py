def calculate_structure_sum(data_structure):
    sum_ = 0
    for i in data_structure:
        if isinstance(i, (list, tuple, set)):
            sum_ += calculate_structure_sum(i)
        elif isinstance(i, dict):
            for key in i.keys():
                try:
                    num = float(key) if '.' in key \
                        else int(key)
                    sum_ += num
                except ValueError:
                    sum_ += len(key)
            sum_ += calculate_structure_sum(list(i.values()))
        elif isinstance(i, (int, float)):
            sum_ += i
        elif isinstance(i, str):
            try:
                num = float(i) if '.' in i else int(i)
                sum_ += num
            except ValueError:
                sum_ += len(i)
    return sum_

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
