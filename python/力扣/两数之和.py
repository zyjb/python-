# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。
l1 = [3,3]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # for i in nums:
        #     if target - i in nums:
        #         return [nums.index(i), nums.index(target - i)]

        for i in nums:
            if len(nums) <= 2 and nums[0]+nums[1]==target:
                print(nums[0],nums[1])
            elif len(nums)>2 and target - i in nums and (target - i) != nums:
                print[nums.index(i), nums.index(target - i)]

           # a = [nums.index(i), nums.index(target - i)]
                # return a if a[0]!=a[1] else [j for j, x in enumerate(nums) if x == (target - i)]

        # for k,v in hash.items():
        #     print(k,v)



s = Solution()
print(s.twoSum(l1,6))
