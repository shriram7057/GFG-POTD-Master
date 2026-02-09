class Solution:
    def countSubstr (self, s, k):
        # Code here
        from collections import defaultdict
        def atMost(k):
            freq = defaultdict(int)
            left = 0
            res = 0
            distinct= 0
            
            for right in range(len(s)):
                if freq[s[right]] == 0:
                    distinct += 1
                freq[s[right]] += 1
                
                while distinct > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        distinct -= 1
                    left += 1
                res += right - left + 1
            return res
        return atMost(k) - atMost(k-1)