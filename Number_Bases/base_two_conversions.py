from Number_Bases.base_ten_conversions import Base_Ten_Conversions

class Base_Two_Conversion:
    @staticmethod
    def binary_to_base10(number:str) -> int | None:
        try:
            num = int(number)
            number = str(abs(num))
            answer = 0
            c = len(number) -1
            for digit in number:
                if int(digit) > 1:
                    return None
                n = int(digit) * (2 ** c)
                answer = answer + n
                c = c- 1
            if num < 0:
                return -answer
            return answer
        except ValueError:
            return None

    def binary_to_hexa(self, number:str)-> str | None:
        evaluate_1 = self.binary_to_base10(number)
        ans = Base_Ten_Conversions().base10_to_hexa(str(evaluate_1))
        return ans

    def binary_to_other_base(self, number:str, base_num: int)-> str | None:
        evaluate_1 = self.binary_to_base10(number)
        ans = Base_Ten_Conversions().base10_to_other_base(str(evaluate_1), base_num)
        return ans

two = Base_Two_Conversion()
