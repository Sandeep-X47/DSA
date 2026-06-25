# Brute Force Approach 
def number_of_inversions(arr):
    cnt = 0 # Initialize inversion count
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                cnt += 1 # Increment if inversion found
    return cnt

# Driver code
arr = [5, 4, 3, 2, 1]
inversions = number_of_inversions(arr)
print("The number of inversions is:", inversions)



# Optimized Approach using Merge Sort
def merge(arr, low, mid, high):
    # Temporary array
    temp = []

    # Starting indices of left and right halves
    left = low
    right = mid + 1

    # Variable to count inversions
    cnt = 0

    # Merge elements in sorted order
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid - left + 1)  # Count inversions
            right += 1

    # Copy remaining elements of left half
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # Copy remaining elements of right half
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copy back to original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return cnt

def mergeSort(arr, low, high):
    # Variable to count inversions
    cnt = 0

    if low >= high:
        return cnt

    mid = (low + high) // 2

    # Count inversions in left half
    cnt += mergeSort(arr, low, mid)
    # Count inversions in right half
    cnt += mergeSort(arr, mid + 1, high)
    # Count inversions during merge
    cnt += merge(arr, low, mid, high)

    return cnt

def numberOfInversions(arr):
    return mergeSort(arr, 0, len(arr) - 1)

# Input array
a = [5, 4, 3, 2, 1]

# Count inversions
cnt = numberOfInversions(a)
print("The number of inversions are:", cnt)
