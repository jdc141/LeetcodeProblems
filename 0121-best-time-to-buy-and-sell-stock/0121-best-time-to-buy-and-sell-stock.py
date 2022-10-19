class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        leftPoint, rightPoint = 0 , 0
        while rightPoint < len(prices):
            if prices[rightPoint] > prices[leftPoint]:
                profit = prices[rightPoint] - prices[leftPoint]
                maxP = max(maxP, profit)
            else:
                leftPoint = rightPoint
            rightPoint += 1
        return maxP
                
                
            
        