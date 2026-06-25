# Brute 
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if strings are of the same length
        if len(s) != len(goal):
            return False  

        # Try all possible rotations of s
        for i in range(len(s)):
            # Generate a rotated version of s
            rotated = s[i:] + s[:i]  
            # If the rotated version matches goal, return True
            if rotated == goal:
                return True  

        # If no rotation matches, return False
        return False  

# Test case
sol = Solution()
print(sol.rotateString("rotation", "tionrota"))

# Optimal Approach
class Solution:
# Strings must be of the same length to be rotations of each other
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False  
        doubled_s = s + s  # Concatenate s with itself
        return goal in doubled_s  # Check if goal is a substring of s + s
        
sol = Solution()
print(sol.rotateString("rotation", "tionrota"))