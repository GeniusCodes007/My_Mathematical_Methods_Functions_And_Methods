import math


class SimpleCircleGeometry:
    def __init__(self, radius):
        self.radius = radius
    @staticmethod
    def mod_rem(base_num, divisor):
        return int(base_num % divisor)
    
    def circumference(self):
        result = (44/7) * self.radius
        return result

    def area(self):
        result = (22 / 7) * (self.radius ** 2)
        return result

    def area_of_sector_angle_in_degree(self, angle):
        real_angle = self.mod_rem(angle, 360)
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
print(circle1.area())
print(circle1.area_of_sector_angle_in_degree(180))
print(circle1.circumference())
print(circle1.length_of_arc_angle_in_radian(1.4))
print(circle1.mod_rem(14,9))