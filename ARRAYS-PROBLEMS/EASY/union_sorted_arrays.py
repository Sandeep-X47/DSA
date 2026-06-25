# Using Set
class Solution:
    def unionArrays(self, arr1, arr2):
        st = set(arr1) | set(arr2)
        return list(st)


if __name__ == "__main__":
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    obj = Solution()
    print(obj.unionArrays(arr1, arr2))


# Using Dictionary or Hash Map
class Solution:
    def unionArrays(self, arr1, arr2):
        d = {}
        for num in arr1:
            d[num] = d.get(num, 0) + 1
        for num in arr2:
            d[num] = d.get(num, 0) + 1
        return sorted(d.keys())


if __name__ == "__main__":
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    obj = Solution()
    print(obj.unionArrays(arr1, arr2))


# Using Two Pointers (Optimal for Sorted Arrays)
class Solution:
    def unionArrays(self, arr1, arr2):
        i, j = 0, 0
        union = []
        
        # Edge cases for empty arrays
        if not arr1:
            return sorted(list(set(arr2)))  # Ensure unique elements
        if not arr2:
            return sorted(list(set(arr1)))

        # Traverse both arrays
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                # Add only if union is empty or element is not a duplicate
                if not union or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1  # Always increment to avoid infinite loop
            elif arr2[j] < arr1[i]:
                if not union or union[-1] != arr2[j]:
                    union.append(arr2[j])
                j += 1
            else:
                if not union or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
                j += 1

        # Process remaining elements of arr1
        while i < len(arr1):
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1

        # Process remaining elements of arr2
        while j < len(arr2):
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

        return union

if __name__ == "__main__":
    # Example Input: 
    # arr1: 1 2 2 3
    # arr2: 2 3 4 5
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    obj = Solution()
    print(obj.unionArrays(arr1, arr2))
