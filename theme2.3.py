class Figure:
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

    def perimeter(self):
        pass

    def area(self):
        pass


class Rectangle(Figure):
    def x(self):
        return self.x

    def y(self):
        return self.y

    def width(self):
        return self.width

    def height(self):
        return self.height

    def perimeter(self):
        return 2*(self.width() + self.height())

    def area(self):
        return self.width() * self.height()


class Ellipse(Figure):
    def x(self):
        pass

    def y(self):
        pass

    def width(self):
        pass

    def height(self):
        pass

    def perimeter(self):
        a = self.width()
        b = self.height()
        p = (3.14  * a * b + (a - b))/(a + b)

    def area(self):
        return 3.14 * self.width() * self.height()
    