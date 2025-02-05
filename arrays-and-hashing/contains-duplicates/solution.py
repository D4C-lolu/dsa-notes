class Solution:
    def containsDuplicateWithSet(self, nums: List[int]) -> bool:
        numSet = set()
        for n in nums:
            if n in numSet:
                return True
            else:
                numSet.add(n)
        return False
        
        