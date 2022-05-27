# s = "qweryq"
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         l = ''
#         temp = 0
#         for i in s:
#             if i not in l:
#                 l = l+i
#             else:
#                 if len(l)>temp:
#                     temp = len(l)
#                     l = ''
#                     l = l+i
#         return temp






# ss = Solution()
# print(ss.lengthOfLongestSubstring(s))





class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = strs[0]
        if len(result)==0:
            return ''
        for i in strs:
            result = self.merge(i,result)
            print(result)
            if len(result)==0:
                return ''
        return result
    def merge(self,a,b):
        s1 = ''
        s2 = ''
        for idx,val in enumerate(min(a,b)):
            s1 = s1 + a[idx]
            s2 = s2 + b[idx]
            if s1 != s2:
                return s1[:-1]
        return s1

s = Solution()
# print(s.merge('flower','flow'))
print(s.longestCommonPrefix(["flower","flow","flight"]))






















