class Solution:
    def pattern(self, n: int) -> None:

        for i in range(1, n + 1):

            for j in range(i):

                print(chr(65 + j), end="")

            print()


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)