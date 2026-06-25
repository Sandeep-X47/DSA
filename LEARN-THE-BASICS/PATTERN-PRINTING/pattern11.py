# Brute Force Solution
class Solution:
    def pattern(self, n: int) -> None:
        a = 1
        s = a
        for i in range(1, n + 1):
            for j in range(i):
                print(s, end="")
                s = int(not(s))
            print()
            s = int(not(a))
            a = s

if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)

# Better Solution
class Solution:

    def pattern(self, n: int) -> None:

        for i in range(1, n + 1):

            start = i % 2

            for j in range(i):

                print(start, end="")
                start = 1 - start

            print()


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)    


# String Solution
class Solution:

    def pattern(self, n: int) -> None:

        s = ""

        for i in range(1, n + 1):

            s = "".join(str((i + j) % 2) for j in range(i))
            print(s)


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)    