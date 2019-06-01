class Figure:
    init:
    x
    y
    def x(self):
        pass

    def y(self):
        pass

    def width(self):
        pass

    def height(self):
        pass


    def perimeter(self):


    def area(self):



class Rectangle(Figure):
    init:
    init Figure
    def perimeter(self):
        return 2*(self.width() + self.height())

    def area(self):
        return self.width() * self.height()


class Ellipse(Figure):

    def perimeter(self):
        a = self.width()
        b = self.height()
        p = 4*(3.14  * a * b + (a - b))/(a + b)
        return p

    def area(self):
        return 3.14 * self.width() * self.height()
