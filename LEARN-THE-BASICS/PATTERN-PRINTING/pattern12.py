class Solution:
    def pattern(self, n: int) -> None:
        s = ""
        for i in range(1, n + 1):
            s += str(i)
            print(s, " "*((2*n)-(2*i)), s[::-1], sep="")
if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)

# loop solution
class Solution:

    def pattern(self, n: int) -> None:
        for i in range(1, n + 1):
            for j in range(1,i+1):
                print(j, end="")
            for j in range((2*n)-(2*i)):
                print(" ", end="")
            for j in range(i,0,-1):
                print(j, end="")  
            print()      
if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)