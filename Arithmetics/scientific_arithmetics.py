
class Scientific_Arithmetics:

    @staticmethod
    def factorial(n:int):
        answer = 1
        for n in range(n):
            answer = answer* (n + 1)
        return answer

    def permutate(self, n:int, r:int): return self.factorial(n) / self.factorial(n - r)

    def combine(self, n, r): return self.permutate(n, r) / self.factorial(r)

b = Scientific_Arithmetics()