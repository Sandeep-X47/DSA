class Solution:
    def linearSearch(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1            

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())

    obj = Solution()
    print(obj.linearSearch(arr, target))
