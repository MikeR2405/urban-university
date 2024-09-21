import inspect

def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    try:
        info['attributes'] = [name for name, value in inspect.getmembers(obj) if not name.startswith('_')]
    except Exception as e:
        info['attributes'] = "Нельзя достать атрибуты"
    try:
        info['methods'] = [name for name, value in inspect.getmembers(obj) if callable(value) and not name.startswith('_')]
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

