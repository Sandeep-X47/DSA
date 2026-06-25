class Solution:

    def reverse_number(self, n: int) -> int:
        sign = 1 if n >= 0 else -1
        N = abs(n)
        reversed_num = 0

        while N > 0:
            digit = N % 10
            N //= 10
            reversed_num = reversed_num * 10 + digit

        if reversed_num > 2**31 - 1 or reversed_num < -2**31:
            return 0    

        reversed_num *= sign
        return reversed_num


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    print(obj.reverse_number(n))