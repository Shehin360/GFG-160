#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        
        length=len(arr)
        temparr=[0]*length
        d%=length  #to handle cases where d is greater than length of array
        
        for i in range(length-d):  #copying n-d elements to the temp array
            temparr[i] = arr[d + i]
        
        for j in range(d):          #copying first d elements to the last of temp array
            temparr[length - d + j] = arr[j]
            
        for k in range (length):
            arr[k] = temparr[k]
        
        for i in range(len(arr)):
         print(arr[i], end=" ")
result=Solution()
result.rotateArr([1, 2, 3, 4, 5], 2)  # Example usage