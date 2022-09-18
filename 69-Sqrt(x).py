from math import floor, sqrt

class Solution():
    def mySqrt(self, x):
        res = x
        print(x, res)

        while not res * res - x < 1: # 72, 16
            res = (res + x / res) / 2 # 5, 3
        return int(res)



obj = Solution()
print(obj.mySqrt(9))

print(type(floor(sqrt(9))))