class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x,-n)
        if n == 0:
            return 1
        elif n % 2 == 1:
            return self.myPow(x, n//2) * self.myPow(x, n//2) * x
        else: 
            return self.myPow(x, n//2) * self.myPow(x, n//2)
        
        