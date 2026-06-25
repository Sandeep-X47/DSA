# Brute Force Approach:
class Solution:
    # Function to find repeating and missing numbers
    def findMissingRepeatingNumbers(self, nums):
        
        # Size of the array
        n = len(nums) 
        repeating, missing = -1, -1

        # Find the repeating and missing number:
        for i in range(1, n + 1):
            # Count the occurrences:
            cnt = nums.count(i)

            # Check if i is repeating or missing
            if cnt == 2:
                repeating = i
            elif cnt == 0:
                missing = i

            """ If both repeating and missing
            are found, break out of loop"""
            if repeating != -1 and missing != -1:
                break

        # Return [repeating, missing]
        return [repeating, missing]

if __name__ == "__main__":
    nums = [3, 1, 2, 5, 7, 6, 7, 5]
    
    # Create an instance of Solution class
    sol = Solution()

    result = sol.findMissingRepeatingNumbers(nums)
    
    # Print the repeating and missing numbers found
    print(f"The repeating and missing numbers are: {{{result[0]}, {result[1]}}}")


# Better Approach:
class Solution:
    # Function to find repeating and missing numbers
    def findMissingRepeatingNumbers(self, nums):
        
        # Size of the array
        n = len(nums)
        
        # Hash array to count occurrences
        hash = [0] * (n + 1)
        
        # Update the hash array:
        for num in nums:
            hash[num] += 1

        repeating = -1
        missing = -1
        
        # Find the repeating and missing number:
        for i in range(1, n + 1):
            if hash[i] == 2:
                repeating = i
            elif hash[i] == 0:
                missing = i

            """ If both repeating and missing
            are found, break out of loop"""
            if repeating != -1 and missing != -1:
                break
        
        # Return [repeating, missing]
        return [repeating, missing]

if __name__ == "__main__":
    nums = [3, 1, 2, 5, 7, 6, 7, 5]
    
    # Create an instance of Solution class
    sol = Solution()
    
    result = sol.findMissingRepeatingNumbers(nums)
    
    # Print the repeating and missing numbers found
    print(f"The repeating and missing numbers are: {{{result[0]}, {result[1]}}}")


# Optimal Approach: 1
class Solution:
    # Function to find repeating and missing numbers
    def findMissingRepeatingNumbers(self, nums):
        
        # Size of the array
        n = len(nums)

        # Sum of first n natural numbers
        SN = (n * (n + 1)) // 2

        # Sum of squares of first n natural numbers
        S2N = (n * (n + 1) * (2 * n + 1)) // 6

        """ Calculate actual sum (S) and sum 
            of squares (S2) of array elements """
        S = 0
        S2 = 0
        for num in nums:
            S += num
            S2 += num * num

        # Compute the difference values
        val1 = S - SN

        # S2 - S2n = X^2 - Y^2
        val2 = S2 - S2N

        # Calculate X + Y using X + Y = (X^2 - Y^2) / (X - Y)
        val2 = val2 // val1

        """ Calculate X and Y from X + Y and X - Y
            X = ((X + Y) + (X - Y)) / 2
            Y = X - (X - Y) """
        x = (val1 + val2) // 2
        y = x - val1

        # Return the results as [repeating, missing]
        return [int(x), int(y)]

nums = [3, 1, 2, 5, 7, 6, 7, 5]

# Create an instance of Solution class
sol = Solution()

result = sol.findMissingRepeatingNumbers(nums)

# Print the repeating and missing numbers found
print(f"The repeating and missing numbers are: {{{result[0]}, {result[1]}}}")


# Optimal Approach: 2
class Solution:
    # Function to find repeating and missing numbers
    def findMissingRepeatingNumbers(self, nums):
        
        # size of the array
        n = len(nums)

        xr = 0

        for i in range(n):
            # XOR of all elements in nums
            xr = xr ^ nums[i] 
            
            # XOR of numbers from 1 to n
            xr = xr ^ (i + 1)  

        # Get the rightmost set bit in xr
        number = (xr & ~(xr - 1))

        # Group the numbers based on the differentiating bit
        # Number that falls into the 0 group
        zero = 0 
        
        # Number that falls into the 1 group
        one = 0  

        for i in range(n):
            """ Check if nums[i] belongs to the 1 group
             based on the differentiating bit"""
            if (nums[i] & number) != 0:
                
                # XOR operation to find numbers in the 1 group
                one = one ^ nums[i]
                
            else:
                # XOR operation to find numbers in the 0 group
                zero = zero ^ nums[i]

        # Group numbers from 1 to n based on differentiating bit
        for i in range(1, n + 1):
            
            # Check if i belongs to the 1 group 
            # based on the differentiating bit
            if (i & number) != 0:
                # XOR operation to find numbers in the 1 group
                one = one ^ i
                
            else:
                # XOR operation to find numbers in the 0 group
                zero = zero ^ i

        # Count occurrences of zero in nums
        cnt = 0

        for i in range(n):
            if nums[i] == zero:
                cnt += 1

        if cnt == 2:
            """ zero is the repeating number,
             one is the missing number"""
            return [zero, one]

        """ one is the repeating number, 
        zero is the missing number"""
        return [one, zero]

if __name__ == "__main__":
    nums = [3, 1, 2, 5, 7, 6, 7, 5]
    
    # Create an instance of Solution class
    sol = Solution()

    result = sol.findMissingRepeatingNumbers(nums)

    # Print the repeating and missing numbers found
    print(f"The repeating and missing numbers are: {{{result[0]}, {result[1]}}}")
