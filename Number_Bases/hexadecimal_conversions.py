from Number_Bases.base_ten_conversions import Base_Ten_Conversions

hexa_extras = ["A", "B", "C", "D", "E", "F"]
decimals = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

class Hexadecimal_Conversions:
    @staticmethod
    def hexa_to_base10(number:str)-> int | None:
        num = 0
        count = len(number) - 1
        for digit in number:
            if digit.upper() in hexa_extras :
                no = hexa_extras.index(digit.upper()) + 10
                numb = no * (16 ** count)
                num = num + numb
                count = count - 1
            elif digit in decimals:
                numb = int(digit) * (16 ** count)
                num = num + numb
                count = count - 1
            else:
                return None
        return num

    def hexa_to_binary(self, number:str) -> str | None:
        evaluate_1 = self.hexa_to_base10(number)
        ans = Base_Ten_Conversions().base10_to_binary(str(evaluate_1))
        return ans

    def hexa_to_other_base(self, number:str, base_num: int) -> str | None:
        evaluate_1 = self.hexa_to_base10(number)
        ans = Base_Ten_Conversions().base10_to_other_base(str(evaluate_1), base_num)
        return ans


h = Hexadecimal_Conversions().hexa_to_other_base("2ea", 16)
