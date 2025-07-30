class Solution:
    def maximumProfit(self, prices):
        # code here
        minElm = prices[0]
        n = len(prices)
        res = 0
        
        for i in range(1, n):
            minElm = min(minElm , prices[i])
            
            res = max(res, prices[i] - minElm)
            
        return res

ans = Solution()
ans.maximumProfit([7, 1, 5, 3, 6, 4])  # Example usage
