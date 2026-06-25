#string Solution
class Solution:
    def pattern(self, n: int) -> None:
        for i in range(n):
            print("*"*n)

if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)

# 2 for loops
class Solution:

    def pattern(self, n: int) -> None:
        for i in range(n):
            for j in range(n):
                print("*",end="")
            print()

if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)