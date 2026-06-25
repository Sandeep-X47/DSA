#Brute Force
class Solution:
    def pattern(self, n: int) -> None:
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j, end="")
            print()
if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)


#Optimal Solution
class Solution:

    def pattern(self, n: int) -> None:
        s = ""
        for i in range(1,n+1):
            s += str(i)
            print(int(s))
        
if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)    