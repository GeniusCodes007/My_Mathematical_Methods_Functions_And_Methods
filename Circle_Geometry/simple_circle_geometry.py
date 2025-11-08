import math
from Arithmetics.basic_arithmetics import BasicArithmetics

class SimpleCircleGeometry:
    def __init__(self, radius):
        self.radius = radius
    
    def circumference(self):
        result = (44/7) * self.radius
        return result

    def area(self):
        result = (22 / 7) * (self.radius ** 2)
        return result

    def area_of_sector_angle_in_degree(self, angle):
        real_angle = BasicArithmetics().mod_rem(angle, 360)
        result = (real_angle / 360) * self.area()
        return result
    

    def area_of_sector_angle_in_radian(self, angle):
        result = (self.radius ** 2) * angle
        return result        
    
    def length_of_arc_angle_in_degree(self, angle_at_center):
        theta = math.pi * (angle_at_center / 180)
        length = self.circumference() * theta
        return length

    def length_of_arc_angle_in_radian(self, angle_at_center):
        length = self.radius * angle_at_center
        return length


circle1 = SimpleCircleGeometry(10)
