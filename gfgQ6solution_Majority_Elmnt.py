class Solution:
    def findMajority(self, arr):
        # code here
        n=len(arr)
        freq = {}
        res = []
        
        for ele in arr:  #frequency counting
            freq[ele] = freq.get(ele, 0) + 1
            
        for ele, cnt in freq.items():
            
            if cnt > n/3:
                res.append(ele)
        
        if len(res) >= 2 and res[0] > res[1]:  #swaping
            res[0] , res [1] = res[1] , res[0]
        return res
# Example usage:
arr = [1, 2, 3, 1, 2, 1, 1, 2, 3]
solution = Solution()
output = solution.findMajority(arr)
print(output)  # Output: [1, 2] or [2, 1] depending on the order of elements    
