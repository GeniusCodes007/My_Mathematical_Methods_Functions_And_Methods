from Number_Bases.hexadecimal_conversions import Hexadecimal_Conversions, Base_Ten_Conversions



class Other_Base_Conversion:

    @staticmethod
    def other_base_to_base10(number:str, base_num:int) -> int | None:
        if base_num == 16:
            result = Hexadecimal_Conversions().hexa_to_base10(number)
            return result

        elif 1 <= base_num <= 10:
            try:
                num = int(number)
                number = str(abs(num))
                answer = 0
                c = len(number) - 1
                for digit in number:
                    if int(digit) >= base_num:
                        return None
                    n = int(digit) * (base_num ** c)
                    answer = answer + n
                    c = c - 1
                if num < 0:
                    return -answer
                return answer
            except ValueError:
                return None

    def inter_base_conversion(self, number:str,in_base_num:int, to_base_num:int)-> str | None:
        evaluate_1 = self.other_base_to_base10(number, in_base_num)
        ans = Base_Ten_Conversions().base10_to_other_base(str(evaluate_1), to_base_num)
        return ans

    def other_base_to_hexa(self, in_base_number:str,in_base:int)-> str | None:
        evaluate_1 = self.other_base_to_base10(in_base_number, in_base)
        ans = Base_Ten_Conversions().base10_to_hexa(str(evaluate_1))
        return ans

    def other_base_to_binary(self, in_base_number:str,in_base:int)-> str | None:
        evaluate_1 = self.other_base_to_base10(in_base_number, in_base)
        ans = Base_Ten_Conversions().base10_to_binary(str(evaluate_1))
        return ans

o = Other_Base_Conversion()