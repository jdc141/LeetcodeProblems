class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        leftPtr = 0
        for rightPtr in range(1, len(nums)):
            if nums[leftPtr] != nums[rightPtr]:
                leftPtr += 1
                nums[leftPtr] = nums[rightPtr]
                
        return leftPtr +1
            
                
        