class Figure:
    def __init__(self):
        pass

    def x(self):
        pass

    def y(self):
        pass

    def width(self):
        pass

    def height(self):
        pass

    def perimeter(self):
        pass

    def area(self):
        pass

    @staticmethod
    def __check_type(x, y, width, height):
        if not isinstance(x, (int, float)):
            raise ValueError('Invalid type')
        if not isinstance(y, (int, float)):
            raise ValueError('Invalid type')
        if not isinstance(width, (int, float)):
            raise ValueError('Invalid type')
        if not isinstance(height, (int, float)):
            raise ValueError('Invalid type')


class Rectangle(Figure):
    def __init__(self, x, y, width, height):
        super().__init__()
        Figure._Figure__check_type(x, y, width, height)
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def perimeter(self):
        return 2*(self.width() + self.height())

    def area(self):
        return self.width() * self.height()


class Ellipse(Figure):
    def __init__(self, x, y, width, height):
        super().__init__()
        Figure._Figure__check_type(x, y, width, height)
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def perimeter(self):
        a = self.width()
        b = self.height()
        p = 4*(3.14 * a * b + (a - b))/(a + b)
        return p

    def area(self):
        return 3.14 * self.width() * self.height()


class CloseFigure(Figure):
    def __init__(self):
        super().__init__()


