
class Solution:
    def __init__(self):
        self.d = {}

    def climbStairs(self, n: int) -> int:
        return self.f(n)

    def f(self, n):
        if n in self.d.keys():
            return self.d.get(n)
        if n < 2:
            return 1
        r = self.f(n-1)+self.f(n-2)
        self.d[n] = r
        return r


s = Solution()
s.climbStairs(15)

