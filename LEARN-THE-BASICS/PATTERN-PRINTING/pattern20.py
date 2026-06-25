class Solution:
    def pattern(self, n: int) -> None:
        for i in range(1,n+1):
            print("*"*i, end="") 
            print(" "*((2*n)-(2*i)), end="")
            print("*"*i)
        N = n-1    
        for i in range(N,0,-1):
            print("*"*i,end="")
            print(" "*((2*n)-(2*i)), end="")
            print("*"*i)
if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)

# Single loop solution
class Solution:

    def pattern(self, n: int) -> None:
         # Initialize spaces between star blocks
        spaces = 2 * n - 2

        # Loop for rows
        for i in range(1, 2 * n):
            # Calculate stars for first half
            stars = i

            # Adjust stars for second half
            if i > n:
                stars = 2 * n - i

            # Print left stars
            print("*" * stars, end="")

            # Print spaces
            print(" " * spaces, end="")

            # Print right stars
            print("*" * stars)

            # Adjust spaces for next row
            if i < n:
                spaces -= 2
            else:
                spaces += 2
if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)