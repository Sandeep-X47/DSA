class Solution:
    def pattern(self, n: int) -> None:
        for i in range(1,n+1):
            print("*"*i)

if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)

# 2 loops 
class Solution:

    def pattern(self, n: int) -> None:
        for i in range(1,n+1):
            for j in range(i):
                print("*",end="")
            print()    

if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)
    