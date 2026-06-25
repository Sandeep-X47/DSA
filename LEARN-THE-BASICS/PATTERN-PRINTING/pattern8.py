class Solution:
    def pattern(self, n: int) -> None:
        for i in range(n,0,-1):
            print(" "*(n-i)+"*"*(2*i-1))

if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)

# 2 Loops 
class Solution:

    def pattern(self, n: int) -> None:
        for i in range(n,0,-1):
            for j in range(n-i):
                print(" ", end="")
            for k in range(2*i-1):
                print("*", end="")
            print()

if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)