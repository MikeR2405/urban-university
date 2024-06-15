# def func_with_params(a, b=2, c=None):
#     if c is None:
#         c = []
#         c.append(a)
#     print(c)
#
#
#
# func_with_params(10)
# func_with_params(4)
# func_with_params(5)
# func_with_params(6)

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2, "привет")
print_params(3, 56, False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'hello', False]
values_dict = {'a': 2, 'b': 'stroka', 'c': None}

print_params(*values_list)
print_params(**values_dict)

values_list2 = [54.32, 'Строка']

print_params(*values_list2, 42)
