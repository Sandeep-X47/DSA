# Brute Force Approach
class FrequencyCounter:
    def countFreq(self, arr):
        n = len(arr)                     # Get array length
        visited = [False] * n           # Track if an element has already been counted
        maxFreq = 0                     # Store max frequency seen so far
        minFreq = n                     # Store min frequency (start high)
        maxEle = 0                      # Element with max frequency
        minEle = 0                      # Element with min frequency

        for i in range(n):

            # Skip already processed elements
            if visited[i]:
                continue

            # Count frequency of arr[i]
            count = 1
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    visited[j] = True   # Mark as visited
                    count += 1

            # Update max frequency info
            if count > maxFreq:
                maxEle = arr[i]
                maxFreq = count

            # Update min frequency info
            if count < minFreq:
                minEle = arr[i]
                minFreq = count

        # Print results
        print("The highest frequency element is:", maxEle)
        print("The lowest frequency element is:", minEle)
        print()


if __name__ == "__main__":
    fc = FrequencyCounter()                     # Create object
    arr = [10, 5, 10, 15, 10, 5]                # Sample input
    fc.countFreq(arr)                           # Run frequency analysis



# Optimized Approach using Hash Map
class FrequencyCounter:
    def Frequency(self, arr):
        freq_map = {}                # Dictionary to store frequency of each element

        # Count frequencies
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1

        maxFreq = 0
        minFreq = len(arr)
        maxEle = 0
        minEle = 0

        # Iterate through dictionary to find max and min frequency elements
        for element, count in freq_map.items():
            if count > maxFreq:
                maxFreq = count
                maxEle = element

            if count < minFreq:
                minFreq = count
                minEle = element

        # Print results
        print("The highest frequency element is:", maxEle)
        print("The lowest frequency element is:", minEle)
        print()

if __name__ == "__main__":
    fc = FrequencyCounter()
    arr = [10, 5, 10, 15, 10, 5]
    fc.Frequency(arr)
