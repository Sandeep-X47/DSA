# Brute Force Approach: O(N^2) time complexity
class Solution:
    # Function to count subarrays with XOR equal to B
    def countSubarraysXOR(self, A, B):
        # Initialize count of valid subarrays
        count = 0
        # Traverse all starting points
        for i in range(len(A)):
            # Maintain xor of current subarray
            xorVal = 0
            # Extend subarray till end
            for j in range(i, len(A)):
                # Update xor
                xorVal ^= A[j]
                # If xor equals B, increment count
                if xorVal == B:
                    count += 1
        return count


def main():
    # Input array
    A = [4, 2, 2, 6, 4]
    # Target xor
    B = 6

    sol = Solution()
    print(sol.countSubarraysXOR(A, B))


if __name__ == "__main__":
    main()


# Optimal Approach: O(N) time complexity using Hash Map
class Solution:
    # Function to count subarrays with given XOR
    def countSubarrays(self, A, k):
        # Store frequency of prefix XORs
        freq = {0: 1}
        
        # Current prefix XOR
        prefixXor = 0
        # Answer count
        count = 0

        # Traverse array
        for num in A:
            # Update prefix XOR
            prefixXor ^= num

            # Compute required XOR
            target = prefixXor ^ k

            # If target exists in map, add its frequency
            if target in freq:
                count += freq[target]

            # Store current prefix XOR in map
            freq[prefixXor] = freq.get(prefixXor, 0) + 1

        return count


# Driver code
A = [4, 2, 2, 6, 4]
k = 6
sol = Solution()
print(sol.countSubarrays(A, k))
