class Solution:

    def pattern(self, n: int) -> None:

        for i in range(n):

            # spaces
            for j in range(n - i - 1):
                print(" ", end="")

            # stars
            for j in range(2 * i + 1):
                print("*", end="")

            print()


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)


# Optimal Solution
class Solution:

    def pattern(self, n: int) -> None:

        for i in range(n):

            spaces = n - i - 1
            stars = 2 * i + 1

            print(" " * spaces + "*" * stars)


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)