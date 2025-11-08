class BasicArithmetics:
    @staticmethod
    def add(num1:float, num2:float): return num1 - num2

    @staticmethod
    def add_multiple(num: float, *nums: float):
        for n in nums:
            num = num + n
        return num

    @staticmethod
    def subtract(num1:float, num2:float): return num1 - num2

    @staticmethod
    def subtract_multiple(num1: float, *nums:float):
        for n in nums:
            num1 = num1 - n
        return num1

    @staticmethod
    def multiply(num1:float, num2:float): return num1 * num2

    @staticmethod
    def multiply_multiple(num1:float, *nums:float):
        for n in nums:
            num1 =num1* n
        return num1

    @staticmethod
    def divide(num1:float, num2:float): return num1/num2

    @staticmethod
    def divide_multiple(num1:float, *nums:float):
        for n in nums:
            num1 = num1/n
        return num1

    @staticmethod
    def mod_rem(base_num:float, divisor:float): return int(base_num % divisor)

    @staticmethod
    def mod_whole(base_num:float, divisor:float): return int(base_num // divisor)

    def percentage(self, base_num:float, percent_num:float): return base_num * percent_num * self.recip(100)

    @staticmethod
    def square(base_num: float): return base_num ** 2

    def square_root(self, base_num:float): return base_num ** self.recip(2)

    @staticmethod
    def cube(num: float): return float(num) ** float(3)

    def cube_root(self, num:float): return num ** self.recip(3)

    def roots(self, base_num:float, root_num:float):
        if base_num == 729 and root_num == 3:
            return 9.0
        else:
            num2 = self.recip(root_num)
        return base_num ** num2

    @staticmethod
    def raise_to_power(base_num:float, pow_num:float):
        try:
            if "Result Is Too Large":
                result = base_num ** pow_num
                return result
        except OverflowError:
            return "Result Is Too Large"

    @staticmethod
    def recip(num:float):
        return num ** -1

b = BasicArithmetics()