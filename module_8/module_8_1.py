def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return f"{a + b:.3f}"
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        elif isinstance(a, (int, float)) and isinstance(b, str):
            return f"{a:.3f}" + b if isinstance(a, float) else str(a) + b
        elif isinstance(a, str) and isinstance(b, (int, float)):
            return a + f"{b:.3f}" if isinstance(b, float) else a + str(b)
    except TypeError:
        raise TypeError('Unsupported types')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
