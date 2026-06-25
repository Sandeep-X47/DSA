# fib.py

class Solution:

    def fibonacci(self, n: int) -> int:
        # Edge case: if n is 0, print only 0
        if n == 0:
            print(0)
            # Special case: if n is 1, print first two Fibonacci numbers
        elif n == 1:
            print("0 1")
        # General case: compute and print Fibonacci series
        else:
            fib = [0] * (n + 1)  # List to store Fibonacci numbers
            fib[0] = 0
            fib[1] = 1

            # Fill the list using bottom-up dynamic programming
            for i in range(2, n + 1):
                fib[i] = fib[i - 1] + fib[i - 2]

            return fib


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    num = obj.fibonacci(n)
    print(" ".join(str(i) for i in num))
    print()

# Recursive approach
class Solution:

    def fibonacci(self, n: int, fib: list) -> int:
        # Base cases
        if n == 0:
            return fib[0]
        elif n == 1:
            return fib[1]

        # Compute the Fibonacci number recursively and store it in the list
        fib[n] = self.fibonacci(n - 1, fib) + self.fibonacci(n - 2, fib)
        return fib[n]


if __name__ == "__main__":

    n = int(input())
    fib = [0] * (n + 1)  # List to store Fibonacci numbers
    fib[0] = 0
    fib[1] = 1
    obj = Solution()

    obj.fibonacci(n,fib)  
    print(" ".join(str(i) for i in fib))
