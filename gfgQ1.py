class Solution:
    def getSecondLargest(self, arr):
        arr.sort()
        largest = arr[-1]
        # Find the second largest
        second_largest = -1
        for i in range(len(arr)-2, -1, -1):
            if arr[i] < largest:
                second_largest = arr[i]
                break
        if second_largest == -1:
            print(-1)
        else:
            print(
                f"The largest element of the array is {largest} "
                f"and the second largest element is {second_largest}"
            )

cls = Solution()
inp = list(map(int, input("Enter array elements: ").split()))
cls.getSecondLargest(inp)