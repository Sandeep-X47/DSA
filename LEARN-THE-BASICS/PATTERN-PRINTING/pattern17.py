class Solution:

    def pattern(self, n: int) -> None:
        for i in range(n):
            print(" " * (n - i - 1), end="")
            
            ch = ord('A')
            breakpoint = (2 * i + 1) // 2

            for j in range(1, 2 * i + 2):
                print(chr(ch), end="")
                if j <= breakpoint:
                    ch += 1
                else:
                    ch -= 1
            print()
        
if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)