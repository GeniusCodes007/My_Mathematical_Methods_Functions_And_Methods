from typing import List
from Number_Bases.other_base_conversion import Other_Base_Conversion

"""
All these functions return 'None' for NoneType parameters
-> The functions 'add' and 'multiply' take multiple arguments
-> The functions 'subtract' and 'divide' take single arguments
"""

class Number_Base_Arithmetics:

    @staticmethod
    def add(answer_base: int, *base_lists:List[str: int]):
        answer = 0
        o = Other_Base_Conversion()
        for kl in base_lists:
            try:
                answer = answer + int(o.inter_base_conversion(kl[0], kl[1], 10))
            except TypeError:
                return None
        return o.inter_base_conversion(str(answer), 10, answer_base)

    @staticmethod
    def subtract(base_lists1: List[str: int], base_lists2: List[str: int]):
        o = Other_Base_Conversion()
        num_1 = o.other_base_to_base10(base_lists1[0], base_lists1[1])
        num_2 = o.other_base_to_base10(base_lists2[0], base_lists2[1])
        answer = num_1 - num_2
        return answer

    @staticmethod
    def multiply(answer_base: int, *base_lists: List[str: int]):
        answer = 1
        o = Other_Base_Conversion()
        for kl in base_lists:
            try:
                answer = answer * int(o.inter_base_conversion(kl[0], kl[1], 10))
            except TypeError:
                return None
        return o.inter_base_conversion(str(answer), 10, answer_base)

    @staticmethod
    def divide(base_lists1: List[str: int], base_lists2: List[str: int]):
        o = Other_Base_Conversion()
        num_1 = o.other_base_to_base10(base_lists1[0], base_lists1[1])
        num_2 = o.other_base_to_base10(base_lists2[0], base_lists2[1])
        answer = num_1 / num_2
        return answer


