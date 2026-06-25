# p_1_n.py
# Forward Recursion
class Solution:

    def print_1_to_n(self,current, n: int) -> None:
        if current == n:
            return

        print(current + 1, end = " ")

        self.print_1_to_n(current + 1, n)


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.print_1_to_n(0,n)
    print()

# Backward Recursion
class Solution:

    def print_1_to_n(self, n: int) -> None:
        if n == 0:
            return

        self.print_1_to_n(n - 1)

        print(n, end = " ")


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.print_1_to_n(n)    