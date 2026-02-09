import bisect
class Solution:
    def maxScore(self, s, jumps):
        # code here
        from collections import defaultdict
        n=len(s)
        can=defaultdict(set)
        for a,b in jumps:
            can[a].add(b)
        pos=defaultdict(list)
        for i,c in enumerate(s):
            pos[c].append(i)
        pref=[0] * (n+1)
        for i in range(n):
            pref[i+1] = pref[i] + ord(s[i])
        chars= set(s)
        prefChar = {c:[0] * (n+1) for c in chars}
        for i in range(n):
            for c in chars:
                prefChar[c][i+1] = prefChar[c][i]
            prefChar[s[i]][i+1] += 1
        dp=[-1] * n
        dp[0]=0
        for i in range(n):
            if dp[i]<0:
                continue
            c1=s[i]
            lst = pos[c1]
            idx = bisect.bisect_right(lst,i)
            if idx < len(lst):
                j=lst[idx]
                t=s[j]
                total = pref[j] - pref[i]
                remove=(prefChar[t][j] - prefChar[t][i]) * ord(t)
                score = total - remove
                dp[j] = max(dp[j],dp[i]+score)
            for ch in can[c1]:
                lst = pos[ch]
                idx = bisect.bisect_right(lst,i)
                if idx < len(lst):
                    j=lst[idx]
                    t=s[j]
                    total=pref[j] - pref[i]
                    remove = (prefChar[t][j] - prefChar[t][i]) * ord(t)
                    score = total - remove
                    dp[j] = max(dp[j],dp[i]+score)
        return max(dp)
                     
            
