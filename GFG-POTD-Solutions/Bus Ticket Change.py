class Solution:
    def canServe(self, arr):
        # code here 
        five = ten = 0
        for x in arr:
            if x == 5:
                five += 1
            elif x == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else: #x == 20:
                if ten> 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True