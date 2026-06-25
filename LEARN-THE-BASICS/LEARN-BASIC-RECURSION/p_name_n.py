# p_name_n.py

class Solution:

    def print_name(self, n: int) -> None:
        if n == 0:
            return

        print("John")

        self.print_name(n - 1)

if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.print_name(n)