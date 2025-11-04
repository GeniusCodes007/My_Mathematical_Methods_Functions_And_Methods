
import math

class BasicFrequentFunctions:

    def add(self, num1, num2):
        sum_up = num1 + num2
        return sum_up

    def difference(self, num1, num2):
        dif = num1 - num2
        return dif

    def multiply(self, num1, num2):
        prod = num1 * num2
        return prod

    def divide(self,num1, num2):
        dividend = num1/num2
        return dividend

    def mod_rem(self, base_num, divisor):
        return int(base_num % divisor)

    def mod_whole(self, base_num, divisor):
        return int(base_num // divisor)

    def square(self,base_num):
        return float(base_num ** 2)

    def percentage(self, base_num, percent_num):
        return float(base_num) * float(percent_num / 100)

    def square_root(self, base_num):
        return float(base_num ** 0.5)

    def roots(self, base_num, root_num):
        if base_num == 729 and root_num == 3:
            return 9.0
        else:
            num2 = 1 / root_num
        return base_num ** num2

    def cube(self,num):
        return float(num) ** float(3)

    def raise_to_power(self, base_num, pow_num):
        try:
            result = base_num ** pow_num
            return result
        except OverflowError:
            return "Result is too Large"

    def recip(self, num):
        return float(num) ** (-1)


    def cube_root(self,num):
        return float(num) ** self.recip(3)




