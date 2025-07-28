class Solution:
    def nextPermutation(self, arr):
        # code here
        n=len(arr)
        pivot = -1
        
        for i in range(n-2, -1, -1):   #finding the pivot point
            if arr[i] < arr[i+1]:
                pivot = i
                break
            
        if pivot == -1:
            arr.reverse()
            return
        
        for i in range(n-1, pivot, -1):  #swapping the values
            if arr[i] > arr[pivot]:
                arr[i],arr[pivot] = arr[pivot],arr[i]
                break
            
        left = pivot + 1
        right = n-1
        
        while left < right:     #reversing the array after the pivot value
            arr[left], arr[right] = arr[right], arr[left]
            left +=1
            right -=1
            

# Example usage
result = Solution()
arr = [1, 2, 3, 6, 5, 4]
result.nextPermutation(arr)
print(arr)  # Output should be the next permutation of the array