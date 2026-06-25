#Single loop
class Solution:
    def pattern(self, n: int) -> None:

        s = ""

        for i in range(1, n + 1):
            s += str(i)

        for i in range(n, 0, -1):
            print(s[:i])


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)

#2 loops
class Solution:

    def pattern(self, n: int) -> None:
        for i in range(n,0,-1):
            s = ""
            for j in range(1, i + 1):
                s += str(j)
            print(s)      

if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)    