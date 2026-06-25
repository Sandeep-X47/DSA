# Brute Force Approach
class Solution:
    def rearrangeBySign(self, arr):
        pos = []
        neg = []
        n = len(arr)

        for i in arr:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)

        res = [0] * n
        for i in range(n//2):
            res[2*i] = pos[i]
            res[(2*i)+1] = neg[i]

        return res


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.rearrangeBySign(arr))


# Optimal Approach
class Solution:
    def rearrangeBySign(self, arr):
        n = len(arr)
        res = [0] * n
        posIndex, negIndex = 0, 1

        for i in arr:
            if i >= 0:
                res[posIndex] = i
                posIndex += 2
            else:
                res[negIndex] = i
                negIndex += 2

        return res


if __name__ == "__main__":
    arr = list(map(int, input().split()))

    obj = Solution()
    print(obj.rearrangeBySign(arr))    