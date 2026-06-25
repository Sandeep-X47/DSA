class Solution:
    def pattern(self, n: int) -> None:
        for i in range(n):
            print(chr(65 + i) * (i + 1))

if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)

