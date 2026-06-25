# Brute Force
class Solution:
    # Function to reverse the order of words in a string
    def reverseWords(self, s: str) -> str:
        # List to store words
        words = []
        
        # Temporary variable to store current word
        word = ""
        
        # Traverse each character in the string
        for ch in s:
            # If not space, add character to word
            if ch != " ":
                word += ch
            # If space and we have collected a word
            elif word:
                # Add word to list
                words.append(word)
                # Reset word
                word = ""
        
        # Add the last word if present
        if word:
            words.append(word)
        
        # Reverse the list of words
        words.reverse()
        
        # Join with single space
        return " ".join(words)

# Driver code
if __name__ == "__main__":
    obj = Solution()
    s = " amazing coding skills "
    print(obj.reverseWords(s))


# Optimal 
class Solution:
    # Function to reverse the order of words 
    def reverseWords(self, s: str) -> str:
        # Result string
        result = ""
        
        # Pointer starting from end
        i = len(s) - 1
        
        # Traverse from right to left
        while i >= 0:
            # Skip spaces
            while i >= 0 and s[i] == " ":
                i -= 1
            
            # If pointer out of bounds, break
            if i < 0:
                break
            
            # Mark end of word
            end = i
            
            # Move left until space or start
            while i >= 0 and s[i] != " ":
                i -= 1
            
            # Extract the word
            word = s[i + 1:end + 1]
            
            # Add space if result is not empty
            if result != "":
                result += " "
            
            # Append word
            result += word
        
        return result

# Driver code
if __name__ == "__main__":
    obj = Solution()
    s = " amazing coding skills "
    print(obj.reverseWords(s))
