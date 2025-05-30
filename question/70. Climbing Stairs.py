class Solution:
    def climbStairs(self, n: int) -> int:
        #  def climb(n):
        #      if n==1: #only one step option is availble
        #          return 1
        #      if n ==2: # two options are possible : to take two 1-stpes or to only take one 2-steps
        #          return 2
        #      return climb(n-1) + climb(n-2)
        #  return climb(n)  
                ways = 1

        for i in range(1, (n // 2) + 1):
            product = 1

            for j in range(i, 2 * i):
                product *= (n - j) / (j - i + 1)

            ways += product

        return int(ways)