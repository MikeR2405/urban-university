# import math
#
#
# def square(x):
#     d = x ** 2
#     return d
#
#
# a = 5
# b = square(2)
# print(a)
# print(b)
# print(globals())

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()
inner_function() # вызывает ошибку т.к. фун-ция находиться внутри test_function и работает внутри нее


