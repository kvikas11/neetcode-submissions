class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hs={}
        for i,n in enumerate(nums):
            hs[n]=i
        for i, n in enumerate(nums):
            diff=target-n
            if diff in hs and hs[diff]!=i:
                return [i,hs[diff]]
             
