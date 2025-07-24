class Solution:
    def pushZerosToEnd(self, arr):
        count = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[count] = arr[count], arr[i]
                count += 1

# Example usage:
arr = [0, 1, 0, 3, 12]
Solution().pushZerosToEnd(arr)
print(arr)  # Output: [1, 3, 12, 0, 0]