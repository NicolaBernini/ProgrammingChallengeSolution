class Solution:
    
    def get_max_digits(self, n):
        i=0
        while (n//(10**i)>0): 
            i=i+1
        return i
    
    def read_at_pos(self, n, i):
        """ Returns the digit of number n at position i from the right, without converting to a string
        """
        return (n//(10**i))%10
        
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        d = self.get_max_di gits(n=x)
        for i in range(d//2):
            if self.read_at_pos(x,i) != self.read_at_pos(x,d-i-1): return False
        return True
        
        
