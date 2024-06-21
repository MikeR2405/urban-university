def divide(first,second):
    try:
        result= first/second
        return result
    except ZeroDivisionError:
        return f'Ошибка'

# divide(5,2)