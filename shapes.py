class Circle:
    def __init__(self, r):
        self.r = r

    def circle_area(self):
        area = (3.142)*(self.r*self.r)
        return area

    def circle_circumference(self):
        circumference = 2*(3.142)*self.r
        return circumference

class Square:
    def __init__(self, a):
        self.a = a

    def square_area(self):
        area = self.a*self.a
        return area

    def square_perimeter(self):
        perimeter = 4*self.a
        return perimeter

class Rectangle:
    def __init__(self, w, l):
        self.w = w
        self.l = l

    def rectangle_area(self):
        area = self.w*self.l
        return area

    def rectangle_perimeter(self):
        perimeter = 2*(self.w+self.l)
        return perimeter

class Sphere:
    def __init__(self, r):
        self.r = r

    def surface_area(self):
        s_area = 4*(3.142)*(self.r*self.r)
        return s_area

    def sphere_volume(self):
        volume = (4/3)*(3.142*self.r*self.r*self.r)
        return volume
        
                        