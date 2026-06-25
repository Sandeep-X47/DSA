# Brute Force Approach:
class Solution:
    # Function to generate Pascal's Triangle up to numRows
    def generate(self, numRows):
        # Result list to hold all rows
        triangle = []

        # Loop for each row
        for i in range(numRows):
            # Create a row with size (i+1) and initialize all elements to 1
            row = [1] * (i + 1)

            # Fill elements from index 1 to i-1 (middle values)
            for j in range(1, i):
                # Each element = sum of two elements above it
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            # Add current row to the triangle
            triangle.append(row)

        return triangle


if __name__ == "__main__":
    obj = Solution()
    n = 5

    # Generate and print Pascal's Triangle
    result = obj.generate(n)
    for row in result:
        print(" ".join(map(str, row)))


# Better Approach: 
class Solution:
    # Function to generate the Nth row of Pascal's Triangle
    def getNthRow(self, N):
        # Result list to store the row
        row = []
        
        # First value of the row is always 1
        val = 1
        row.append(val)
        
        # Compute remaining values using the relation:
        # C(n, k) = C(n, k-1) * (n-k) / k
        for k in range(1, N):
            val = val * (N - k) // k
            row.append(val)
        
        return row

# Example usage
N = 5  # Example: 5th row
sol = Solution()
result = sol.getNthRow(N)

# Print the row
print(*result)


# Optimal Approach
class Solution:
    # Function to compute binomial coefficient (nCr)
    def findPascalElement(self, r, c):
        # Element is C(r-1, c-1)
        n = r - 1
        k = c - 1

        result = 1

        # Compute C(n, k) using iterative formula
        for i in range(k):
            result *= (n - i)
            result //= (i + 1)

        return result


# Main code to test the solution
if __name__ == "__main__":
    sol = Solution()
    r, c = 5, 3
    print(sol.findPascalElement(r, c))
