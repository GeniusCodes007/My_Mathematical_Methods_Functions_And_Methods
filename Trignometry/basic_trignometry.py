from Arithmetics.basic_arithmetics import BasicArithmetics
import math

rem = BasicArithmetics()
whole = 360

def _360_check(num: float): return rem.mod_rem(num, 360)

class TrigRatios:

    @staticmethod
    def sine(angle:float)-> float:
        if _360_check(angle) == 30: return 0.5
        elif _360_check(angle) == 90: return 1.0
        elif _360_check(angle) == 150: return 0.5
        elif _360_check(angle) == 180: return 0.0
        elif _360_check(angle) == 210: return -0.5
        elif _360_check(angle) == 270: return -1.0
        elif _360_check(angle) == 330: return -0.5
        else:
            sin = math.sin(math.pi * (angle / 180))
            return float(sin)

    @staticmethod
    def cos(angle:float)-> float:
        if _360_check(angle) == 60: return 0.5
        elif _360_check(angle) == 90: return 0.0
        elif _360_check(angle) == 120: return -0.5
        elif _360_check(angle) == 240: return -0.5
        elif _360_check(angle) == 270: return -1.0
        elif _360_check(angle) == 300: return 0.5
        else:
            cos = math.cos(math.pi * (angle / 180))
            return float(cos)

    def tan(self, angle:float)-> float | None:
        try:
            sin = self.sine(angle)
            cosine = self.cos(angle)
            tan = sin / cosine
            return tan
        except ZeroDivisionError:
            return None

    @staticmethod
    def arc_sine(num:float)-> float | None:
        try:
            result = math.asin(num)
            result_in_degrees = math.degrees(result)
            return result_in_degrees
        except ValueError:
            return None

    @staticmethod
    def arc_cosine(num:float)-> float | None:
        try:
            result = math.acos(num)
            result_in_degrees = math.degrees(result)
            return result_in_degrees
        except ValueError:
            return None

    @staticmethod
    def arc_tangent(num:float)-> float | None:
        try:
            result = math.atan(num)
            result_in_degrees = math.degrees(result)
            return result_in_degrees
        except ValueError:
            return None

c = TrigRatios()

