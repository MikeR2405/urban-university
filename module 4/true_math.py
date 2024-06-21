from math import inf

def divide(first,second):
    try:
        result= first/second
        return result
    except ZeroDivisionError:
        return inf

