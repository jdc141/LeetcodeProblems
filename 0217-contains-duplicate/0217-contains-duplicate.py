class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        foundNumbers = set()
        for i in nums:
            if i not in foundNumbers:
                foundNumbers.add(i)
            else:
                return True
        return False
        