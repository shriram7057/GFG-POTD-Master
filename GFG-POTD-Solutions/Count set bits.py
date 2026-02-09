class Solution:
    def countSetBits(self,n):
        # code here
        if n== 0:
            return 0
        x=n.bit_length()-1
        power=1<<x
        
        bits_till_power=x*(power>>1)
        msb_bits=n-power+1
        
        rest=n-power
        return bits_till_power+msb_bits+self.countSetBits(rest)