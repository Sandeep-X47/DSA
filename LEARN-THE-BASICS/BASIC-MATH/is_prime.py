# Brute Force Approach
class Solution:

    def is_prime(self, n: int) -> bool:
        cnt = 0  # Initialize a counter variable to count the number of factors

        # Loop through numbers from 1 to n
        for i in range(1, n + 1):
            # If n is divisible by i without any remainder
            if n % i == 0:
                cnt += 1  # Increment the counter

        # If the number of factors is exactly 2 (1 and the number itself), it's prime
        return cnt == 2


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    print(obj.is_prime(n))

# Optimized Approach  
class Solution:

    def is_prime(self, n: int) -> bool:
        cnt = 0  # Initialize a counter variable to count the number of factors

        # Loop through numbers from 1 to the square root of n
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                cnt += 1  # If n is divisible by i, increment the counter

                # If n is not a perfect square, count its reciprocal factor
                if n // i != i:
                    cnt += 1
                    
            if cnt > 2:  # If the count exceeds 2, n is not prime
                return False

        # If the number of factors is exactly 2 (1 and the number itself), it's prime
        return cnt == 2


if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    print(obj.is_prime(n))  