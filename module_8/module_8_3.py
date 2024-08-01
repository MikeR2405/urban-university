class IncorrectVinNumber(Exception):
    def __init__(self, message="Некорректный vin номер"):
        self.message = message
        super().__init__(self.message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message="Некорректные номера автомобиля"):
        self.message = message
        super().__init__(self.message)


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

        try:
            self.__is_valid_vin(vin)
            self.__is_valid_numbers(numbers)
        except IncorrectVinNumber as exc:
            raise exc
        except IncorrectCarNumbers as exc:
            raise exc

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Некорректный диапозон для vin номера')
        return True

    def __is_valid_numbers(self, car_numbers):
        if not isinstance(car_numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(car_numbers) != 6:
            raise IncorrectCarNumbers('Некорректное длина номеров')
        return True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')