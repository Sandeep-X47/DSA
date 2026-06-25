class Solution:

    def palindrome_number(self, n: int) -> bool:
        N = n
        if n < 0:
            return False
        original = n
        reverse = 0
        while N > 0:
            reverse = reverse * 10 + N % 10
            N //= 10

        return reverse == original


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    print(obj.palindrome_number(n))
    