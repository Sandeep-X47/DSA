class Solution:
    def pattern(self, n: int) -> None:
        for i in range(n):
            print("*"*(n-i)," "*((4*i)//2),"*"*(n-i))
        for j in range(n):
            print("*"*(j+1)," "*((4*(n-j-1))//2),"*"*(j+1))
if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)

    