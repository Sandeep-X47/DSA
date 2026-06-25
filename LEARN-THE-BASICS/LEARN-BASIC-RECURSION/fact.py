# fact.py
# Recursive Approach 
class Solution:

    def factorial(self, n: int) -> int:
        if n == 1:
            return 1
        return n * self.factorial(n - 1)


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    print(obj.factorial(n))

# Iterative Solution
class Solution:

    def factorial(self, n: int) -> int:
        total = 1
        for i in range(1, n + 1):
            total *= i
        return total


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    print(obj.factorial(n))    