# Brute Force Approach
class Solution:
    def leaders(self, arr):
        n = len(arr)
        leaders = []

        for i in range(n):
            is_leader = True

            for j in range(i + 1, n):
                if arr[i] < arr[j]:
                    is_leader = False
                    break

            if is_leader:
                leaders.append(arr[i])

        return leaders


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.leaders(arr))


# Optimal Approach
class Solution:
    def leaders(self, arr):
        n = len(arr)
        leaders = []
        max_from_right = arr[n - 1]
        leaders.append(max_from_right)

        for i in range(n - 2, -1, -1):
            if arr[i] > max_from_right:
                max_from_right = arr[i]
                leaders.append(max_from_right)

        return leaders[::-1]


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.leaders(arr))#     