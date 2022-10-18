class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftPtr, rightPtr, maxP = 0, 1, 0
        
        while rightPtr < len(prices):
            if prices[leftPtr] < prices[rightPtr]:
                profit = prices[rightPtr] - prices[leftPtr]
                maxP = max(maxP, profit)
            else:
                leftPtr = rightPtr
            rightPtr += 1
            
        return max(maxP, 0)
                
                
                
            
        