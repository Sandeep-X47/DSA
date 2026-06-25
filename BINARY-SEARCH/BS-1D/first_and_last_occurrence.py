# Brute-force approach to find the last occurrence of a key in a sorted list
def solve(n: int, key: int, v: list[int]) -> int:
    # initialize result as not found
    res = -1
    # scan from the end toward the start
    for i in range(n - 1, -1, -1):
        # update and stop when match found
        if v[i] == key:
            res = i
            break
    # return index or -1
    return res

# program entry
def main():
    # set size
    n = 7
    # set key to search
    key = 13
    # define input list
    v = [3, 4, 13, 13, 13, 20, 40]
    # print last occurrence index (or -1)
    print(solve(n, key, v))

# run main
if __name__ == "__main__":
    main()


# Optimized approach using binary search to find the last occurrence of a key in a sorted list
def solve(n: int, key: int, v: list[int]) -> int:
    # initialize search bounds and result
    start, end, res = 0, n - 1, -1

    # binary search loop
    while start <= end:
        # compute mid safely
        mid = start + (end - start) // 2
        # when match found, store index and move right
        if v[mid] == key:
            res = mid
            start = mid + 1
        # when key is smaller, move left
        elif key < v[mid]:
            end = mid - 1
        # otherwise move right
        else:
            start = mid + 1
    # return last occurrence or -1
    return res

# program entry
def main():
    # define input size and key
    n = 7
    key = 13
    # define sorted list
    v = [3, 4, 13, 13, 13, 20, 40]
    # print last occurrence index (or -1)
    print(solve(n, key, v))

# run main
if __name__ == "__main__":
    main()
