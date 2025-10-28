from Arithmetics.basic_arithmetics import BasicArithmetics
import math

class TrigMethods:

    @staticmethod
    def sine(angle:float):
        if BasicArithmetics().mod_rem(angle, 360) == 30:
            return 1 / 2
        elif BasicArithmetics().mod_rem(angle, 360) == 0:
            return 0.0
        elif BasicArithmetics().mod_rem(angle, 360) == 90:
            return 1.0
        elif BasicArithmetics().mod_rem(angle, 360) == 180:
            return 0.0
        elif BasicArithmetics().mod_rem(angle, 360) == 270:
            return -1.0
        else:
            sin = math.sin(math.pi * (angle / 180))
            return float(sin)

    @staticmethod
    def cos(angle:float):
        if BasicArithmetics().mod_rem(angle, 360) == 0:
            return 1.0
        elif BasicArithmetics().mod_rem(angle, 360) == 60:
            return 0.5
        elif BasicArithmetics().mod_rem(angle, 360) == 90:
            return 0.0
        elif BasicArithmetics().mod_rem(angle, 360) == 180:
            return -1.0
        elif BasicArithmetics().mod_rem(angle, 360) == 270:
            return 0.0
        else:
            cos = math.cos(math.pi * (angle / 180))
            return cos

    def tan(self, angle:float):
        try:
            sin = self.sine(angle)
            cosine = self.cos(angle)
            tan = sin / cosine
            return tan
        except ZeroDivisionError:
            return "For " + str(angle) + " The Result Is Undefined"

    @staticmethod
    def arc_sine(num:float):
        try:
            result = math.asin(num)
            result_in_degrees = math.degrees(result)
            return result_in_degrees
        except ValueError:
            return f"Number: {num},Out of Range"

    @staticmethod
    def arc_cosine(num:float):
        try:
            result = math.acos(num)
            result_in_degrees = math.degrees(result)
            return result_in_degrees
        except ValueError:
            return f"Number: {num},Out of Range"

    @staticmethod
    def arc_tangent(num:float):
        try:
            result = math.atan(num)
            result_in_degrees = math.degrees(result)
            return result_in_degrees
        except ValueError:
            return f"Number: {num},Out of Range"

c = TrigMethods()

class TrigCompoundAngles:

    @staticmethod
    def sineAddition(A, B):
        return f"Sin({A}) Cos({B}) + Cos({A}) Sin({B})"

    @staticmethod
    def cosineAddition(A, B):
        return f"Cos({A}) Cos({B}) + Sin({A}) Sin({B})"

    @staticmethod
    def tangentAddition(A, B):
        return f"( Tan({A}) + Tan({B}) ) / ( 1 - Tan({A}) Tan({B}) )"
