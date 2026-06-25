import math

# Brute Force Approach
class Solution:

    def print_divisors(self, N: int) -> None:
        res = []
        for i in range(1, N + 1):
            if N % i == 0:
                res.append(i)
        return res        


if __name__ == "__main__":

    N = int(input())

    obj = Solution()

    print(obj.print_divisors(N))

# Optimal Approach
class Solution:

    def print_divisors(self, N: int) -> None:
        # Create list to store divisors
        res = []

        # Loop from 1 to square root of N
        for i in range(1, int(math.isqrt(N)) + 1):
            # Check if i divides N
            if N % i == 0:
                # Add i to result
                res.append(i)

                # If N // i is not the same, add that too
                if i != N // i:
                    res.append(N // i)

        # Return the list of divisors
        return res       


if __name__ == "__main__":

    N = int(input())

    obj = Solution()

    print(obj.print_divisors(N))