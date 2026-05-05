class Solution:
    def sumXOR(self, arr):
        n = len(arr)
        total = 0
        
        for bit in range(32):
            count1 = 0
            for x in arr:
                if x & (1 << bit):
                    count1 += 1
            
            count0 = n - count1
            total += (count1 * count0) * (1 << bit)
        
        return total