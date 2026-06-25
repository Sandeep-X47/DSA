class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # Return the longest palindrome found
        
        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome (center at i)
            odd_palindrome = expandAroundCenter(i, i)
            # Even-length palindrome (center between i and i+1)
            even_palindrome = expandAroundCenter(i, i + 1)
            # Update longest palindrome
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        
        return longest
