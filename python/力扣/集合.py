# l = [1,1,2]
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         return len(set(nums)),list(set(nums))
# s = Solution()
# print(s.removeDuplicates(l))
# l1 = [1,2,3]
# l2 = ['a','b','c']
# l1[3:]=l2
# print(l1)

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        b = 0
        for i in nums:
            b = i ^ b
        return b

d = {
    'name1':'zhao'
}
print(d.get('name'))
print(d)
d['year'] = '18'
print(d)


