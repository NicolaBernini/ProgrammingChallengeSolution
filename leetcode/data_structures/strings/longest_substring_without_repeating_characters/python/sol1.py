class Solution:
    
    class Memory:
        def __init__(self):
            self.memory = dict()
            self.idx_min = 0 
            self.idx_max = 0
            
        def is_present(self, c):
            return c in self.memory.keys()
        
        def del_until(self, c):
            new_mem = dict()
            self.idx_min = self.memory[c]
            self.idx_max = 0
            for k in self.memory.keys():
                if self.memory[k] > self.idx_min:
                    temp = self.memory[k] - self.idx_min
                    new_mem[k] = temp
                    self.idx_max = max(self.idx_max,temp)
            self.memory = new_mem
            self.idx_min = 0
                    
        def add(self, c):
            self.idx_max += 1
            self.memory[c] = self.idx_max
            
        def get_length(self):
            return self.idx_max - self.idx_min
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = 0
        res = 0
        m = self.Memory()
        
        for c in s:
            if m.is_present(c):
                res = max(res, m.get_length())
                m.del_until(c)
            m.add(c)
        res = max(res, m.get_length())
        return res
    
        
        


