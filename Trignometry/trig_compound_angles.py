
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
