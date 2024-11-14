class Figure:
    sides_count = 0

    def __init__(self, colors, *sides):
        if self.sides_count == 12 and len(sides) == 1:
            self.__sides = [sides[0] for _ in range(12)]
        elif self.sides_count == len(sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1 for i in range(self.sides_count)]
        self.__color = list(colors)
        filled = True

    def get_color(self):
        return(self.__color)

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            return 0

    def __is_valid_sides(self, m):
        if len(m) != len(self.__sides):
            return False
        for i in m:
            if i < 1 or type(i) != int:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        m = [i for i in new_sides]
        if self.__is_valid_sides(m):
            self.__sides = m


class Circle(Figure):
    sides_count = 1

    def __init__(self, colors, *sides):
        super().__init__(colors, *sides)
        self.__radius = self.get_sides()[0]/(2*3.1415)

    def get_sqare(self):
        return 3.1415*self.__radius**2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, colors, *sides):
        super().__init__(colors, *sides)

    def get_square(self):
        a, b, c = self.get_sides()[0], self.get_sides()[1], self.get_sides()[2]
        p = sum([a, b, c])/2
        return (p*(p-a)*(p-b)*(p-c))**0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, colors, *sides):
        super().__init__(colors, *sides)

    def get_volume(self):
        a = self.get_sides()[0]
        return a**3


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