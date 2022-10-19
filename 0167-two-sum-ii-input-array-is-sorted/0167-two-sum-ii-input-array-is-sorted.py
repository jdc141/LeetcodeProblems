class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPoint , rightPoint = 0 , len(numbers) - 1
        
        while leftPoint < rightPoint:
            total = numbers[leftPoint] + numbers[rightPoint]
            if total > target:
                rightPoint -= 1
            elif total < target:
                leftPoint += 1
            else:
                return [leftPoint + 1, rightPoint + 1]
        