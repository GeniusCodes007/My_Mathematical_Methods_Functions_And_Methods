import math

from basic_frequent_functions import BasicFrequentFunctions


class BasicTrignometry(BasicFrequentFunctions):    

    def sine(self, base_num, angle):
        if self.mod_rem(angle, 360) == 30:
            return base_num * 1 / 2
        elif self.mod_rem(angle, 360) == 0:
            return 0.0
        elif self.mod_rem(angle, 360) == 90:
            return 1.0
        elif self.mod_rem(angle, 360) == 180:
            return base_num * 0.0
        elif self.mod_rem(angle, 360) == 270:
            return base_num * -1.0
        else:
            sin = math.sin(math.pi * (angle / 180))
            return float(base_num * sin)

    def cos(self, base_num, angle):
        if self.mod_rem(angle, 360) == 0:
            return 1.0 * base_num
        elif self.mod_rem(angle, 360) == 90:
            return 0.0 * base_num
        elif self.mod_rem(angle, 360) == 180:
            return -1.0 * base_num
        elif self.mod_rem(angle, 360) == 270:
            return 0.0 * base_num
        else:
            cos = math.cos(math.pi * (angle / 180))
            return float(base_num * cos)

    def tan(self, base_num, angle):
        try:
            sin = self.sine(base_num, angle)
            cosine = self.cos(base_num, angle)
            tan = sin / cosine
            return tan * base_num
        except ZeroDivisionError:
            return "For " + str(angle) + " The Result Is Undefined, " + "\nDivision By Zero Is Infinite"
    
    def arc_sine(self, num):
        try:
            result = math.asin(num)
            result_in_degrees = math.degrees(result)
            return result_in_degrees
        except ValueError:
            return f"Number: {num},Out of Range"

    def arc_cosine(self, num):
        try:
            result = math.acos(num)
            result_in_degrees = math.degrees(result)
            return result_in_degrees
        except ValueError:
            return f"Number: {num},Out of Range"

    def arc_tangent(self, num):
        try:
            result = math.atan(num)
            result_in_degrees = math.degrees(result)
            return result_in_degrees
        except ValueError:
            return f"Number: {num},Out of Range"
