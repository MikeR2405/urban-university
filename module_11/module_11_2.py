import inspect

def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    try:
        info['attributes'] = dir(obj) if hasattr(obj,'__dict__') else 'Пустой объект'
    except Exception as e:
        info['attributes'] = "Нельзядостать атрибуты"
    try:
        info['methods'] = [m for m in dir(obj) if callable(getattr(obj, m))] if hasattr(obj, '__dir__')\
            else 'Пустой объект'
    except Exception as e:
        info['methods'] = "Нельзя достать методы"
    try:
        info['module'] = obj.__class__.__module__ if hasattr(obj, '__class__') else 'Нельзя определить модуль'
    except Exception as e:
        info['module'] = 'Нельзя определить модуль'
    try:
        info['docstring'] = obj.__doc__ if hasattr(obj,'__doc__') else 'Документация не доступна'
    except Exception as e:
        info['docstring'] = 'Документация не доступна'

    return info

number_info = introspection_info(42)
print(number_info)

