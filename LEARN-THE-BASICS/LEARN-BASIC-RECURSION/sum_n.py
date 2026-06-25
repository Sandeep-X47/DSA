# sum_n.py
# Recursive Approach
class Solution:

    def sum_n(self, n: int) -> int:
        if n == 1:
            return 1
        return n + self.sum_n(n - 1)


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    print(obj.sum_n(n))

# Iterative Approach
class Solution:

    def sum_n(self, n: int) -> int:
        total = 0
        for i in range(1, n + 1):
            total += i
        return total


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    print(obj.sum_n(n))

# Formula Approach
class Solution:

    def sum_n(self, n: int) -> int:
        return n * (n + 1) // 2


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    print(obj.sum_n(n))        