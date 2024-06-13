class Solution:
    fib_cache = [0] * 100
    fib_cache[1] = 1

    def find_fib(self, n):
        if n <= 1:
            return n
        elif self.fib_cache[n] > 0:
            return self.fib_cache[n]
        else:
            self.fib_cache[n] = self.fib_cache[n - 1] + self.fib_cache[n - 2]

    def fib(self, n: int) -> int:
        self.find_fib(n)

        return self.fib_cache[n]
