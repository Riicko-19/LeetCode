class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_a = set(range(1, len(nums) + 1))
        b = set(nums)
        result = list(set_a.difference(b))
        return(result)
        