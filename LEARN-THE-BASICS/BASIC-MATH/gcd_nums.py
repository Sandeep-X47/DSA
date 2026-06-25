from numpy import gcd

# Brute Force Approach
class Solution:

    def gcd_numbers(self, a: int, b: int) -> int:
        # Initialize gcd to 1
        gcd = 1

        # Iterate from 1 up to
        # the minimum of a and b
        for i in range(1, min(a, b) + 1):
            # Check if i is a common
            # factor of both a and b
            if a % i == 0 and b % i == 0:
                # Update gcd to the
                # current common factor i
                gcd = i

        # Return the greatest
        # common divisor (gcd)
        return gcd

if __name__ == "__main__":

    a = int(input())
    b = int(input())

    obj = Solution()

    print(obj.gcd_numbers(a, b))



# Better Approach
class Solution:

    def gcd_numbers(self, a: int, b: int) -> int:
        # Iterate from the minimum of
        # a and b down to 1
        # Start from the minimum of a and b
        # because the GCD cannot
        # exceed the smaller number
    
        for i in range(min(a, b), 0, -1):
            # Check if i is a common
            # factor of both a and b
            if a % i == 0 and b % i == 0:
                # If i is a common factor,
                # return it as the GCD
                return i
        # If no common factors are found,
        # return 1 (as 1 is always a
        # divisor of any number)
        return 1

if __name__ == "__main__":

    a = int(input())
    b = int(input())

    obj = Solution()

    print(obj.gcd_numbers(a, b))



# Optimal Approach
class Solution:

    def gcd_numbers(self, a1: int, b1: int) -> int:
        a = a1
        b = b1
        # Continue loop as long as both
        # a and b are greater than 0
        while a > 0 and b > 0:
            # If a is greater than b,
            # subtract b from a and update a
            if a > b:
                # Update a to the remainder
                # of a divided by b
                a = a % b
            # If b is greater than or equal
            # to a, subtract a from b and update b
            else:
                # Update b to the remainder
                # of b divided by a
                b = b % a
        # Check if a becomes 0,
        # if so, return b as the GCD
        if a == 0:
            return b
        # If a is not 0,
        # return a as the GCD
        return a

if __name__ == "__main__":

    a1 = int(input())
    b1 = int(input())

    obj = Solution()

    print(obj.gcd_numbers(a1, b1))
