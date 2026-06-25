class Solution:

    def armstrong_number(self, num: int) -> bool:
        k = len(str(num))  # Number of digits
        sum = 0
        n = num

        while n > 0:
            ld = n % 10             # Last digit
            sum += ld ** k          # Add ld^k
            n = n // 10             # Remove digit

        return sum == num


if __name__ == "__main__":

    num = int(input())

    obj = Solution()

    print(obj.armstrong_number(num))