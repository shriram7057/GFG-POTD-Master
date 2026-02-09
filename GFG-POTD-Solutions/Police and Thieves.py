class Solution:
    def catchThieves(self, arr, k):
        #code here
        police = []
        thief = []
        for i , c in enumerate(arr):
            if c =='P':
                police.append(i)
            else:
                thief.append(i)
        i = j = 0
        res = 0
        
        while i < len(police) and j < len(thief):
            if abs(police[i] - thief[j]) <= k:
                res += 1
                i += 1
                j += 1
            elif police[i] < thief[j]:
                i+=1
            else:
                j += 1
        return res
            