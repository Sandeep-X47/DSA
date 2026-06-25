class Solution:
    def pattern(self, n: int) -> None:
        for i in range(n,0,-1):
            print("*"*i)
            
if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)

# 2 loops 
class Solution:

    def pattern(self, n: int) -> None:
        for i in range(n,0,-1):
            for j in range(i+1):
                print("*",end="")
            print()

if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)    