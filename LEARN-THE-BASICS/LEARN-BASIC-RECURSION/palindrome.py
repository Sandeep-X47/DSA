# palindrome.py
# Brute force approach
class Solution:

    def is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        # Loop to check if the string is a palindrome
        while left < right:
            # Skip non-alphanumeric characters on the left side
            if not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters on the right side
            elif not s[right].isalnum():
                right -= 1
            # If characters are different, it's not a palindrome
            elif s[left].lower() != s[right].lower():
                return False
            else:
                # Move towards the middle if characters are the same
                left += 1
                right -= 1
        return True  # The string is a palindrome if the loop completes


if __name__ == "__main__":

    s = input()

    obj = Solution()

    print(obj.is_palindrome(s))

# Optimal Solution (Recursive approach)
class Solution:

    def is_palindrome(self, s: str) -> bool:
        # Preprocess the string: remove non-alphanumeric characters and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        return self._is_palindrome_helper(s, 0, len(s) - 1)

    def _is_palindrome_helper(self, s: str, left: int, right: int) -> bool:
        # Base case: if left >= right, we've checked all character pairs
        if left >= right:
            return True
        # If characters at the current positions don't match, it's not a palindrome
        if s[left] != s[right]:
            return False
        # Recursively check the remaining substring
        return self._is_palindrome_helper(s, left + 1, right - 1)


if __name__ == "__main__":

    s = input()

    obj = Solution()

    print(obj.is_palindrome(s))

