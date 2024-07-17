import math

class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled=False):
        if len(sides) != self.sides_count:
            sides = [1] * self.sides_count
        self.__sides = sides if self.__is_valid_sides(*sides) else []
        self.__color = color if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference, *sides):
        super().__init__(sides, color)
        self.__radius = circumference / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(sides, color)
        self.__height = self.calculate_height()

    def calculate_height(self):
        # Используем формулу Герона для вычисления площади и высоты
        a, b, c = self.get_sides()
        s = self.__len__() / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        height = (2 * area) / a  # Высота, опущенная на сторону a
        return height

    def get_square(self):
        a = self.get_sides()[0]
        return 0.5 * a * self.__height

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(sides, color)
        if len(sides) == 1:
            self.set_sides(*([sides[0]] * 12))
        self.__volume = self.calculate_volume()

    def calculate_volume(self):
        a = self.get_sides()[0]
        return a ** 3

    def get_volume(self):
        return self.__volume

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
