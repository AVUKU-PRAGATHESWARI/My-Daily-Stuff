class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        pre = 1
        for i in range(n):
            res[i] = pre
            pre *= nums[i]
        post = 1
        for j in range(n-1,-1,-1):
            res[j] = res[j]*post
            post *= nums[j]
        return res