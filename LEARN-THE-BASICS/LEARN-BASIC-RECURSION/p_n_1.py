# p_n_1.py
# Forward Recursion
class Solution:

    def print_n_to_1(self, n: int) -> None:
        if n == 0:
            return
        print(n, end=" ")
        self.print_n_to_1(n - 1)


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.print_n_to_1(n)
    print()

# Backward Recursion
class Solution:

    def print_n_to_1(self, current,n: int) -> None:
        if current == n+1:
            return
        self.print_n_to_1(current + 1, n)
        print(current, end=" ")


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.print_n_to_1(1,n)    