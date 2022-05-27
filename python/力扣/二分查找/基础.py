# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
#         mid = len(nums) // 2
#
#         if target == nums[mid]:
#             return mid
#         if target > nums[mid]:
#             return self.search(target=target, nums=nums[mid+1:])
#         if target < nums[mid]:
#             return self.search(target=target, nums=nums[:mid-1])
#

#
# 学术派     实战派
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, r = 0, len(nums)-1
        while left <= r:
            mid = (left+r)//2
            _ = nums[mid]
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                left = mid + 1
        return -1

l = [-10,-8,-5,4,6,9,14,15,167,345]
S = Solution()
print(S.search(l, 9))


