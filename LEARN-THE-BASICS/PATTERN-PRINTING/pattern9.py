class Solution:
    def pattern(self, n: int) -> None:

        for i in range(n):

            spaces = n - i - 1
            stars = 2 * i + 1

            print(" " * spaces + "*" * stars)
        
        for i in range(n,0,-1):
            print(" "*(n-i)+"*"*(2*i-1))

if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)

