class Solution:
    def fac(self,n):
        pro=1
        for i in range(1,n+1):
            pro*=i
        return pro
    def climbStairs(self, n: int) -> int:
        way=0
        for i in range(0,n//2 + 1):
            for j in range(n+1):
                if (i*2 + j)==n:
                    way+=self.fac(i+j)/(self.fac(i)*self.fac(j))
        return int(way)