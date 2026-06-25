class Solution:
    def pattern(self, n: int) -> None:
        s = ""
        for i in range(n):
            s += s.join(chr(65+i))

        for i in range(n,0,-1):
            print(s[0:i])    

if __name__ == "__main__":

    n = int(input())

    obj = Solution()

    obj.pattern(n)