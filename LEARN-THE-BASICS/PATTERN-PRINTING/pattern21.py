class Solution:
    def pattern(self, n: int) -> None:
        # Outer loop for rows
        for i in range(n):
            # Inner loop for columns
            for j in range(n):
                # Print star if it's a border cell
                if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                    print("*", end="")
                # Print space otherwise
                else:
                    print(" ", end="")
            # Move to next line after each row
            print()
if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)

# Single Loop Solution
class Solution:

    def pattern(self, n: int) -> None:
        for i in range(n):
            if i == 0 or i == n - 1:
                print("*" * n)
            else:
                print("*" + " " * (n - 2) + "*")
                
if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)