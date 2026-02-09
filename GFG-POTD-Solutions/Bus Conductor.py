class Solution:
    def findMoves(self, chairs, passengers):
        # code here
        chairs.sort()
        passengers.sort()
        moves=0
        
        for i in range(len(chairs)):
            moves += abs(chairs[i] - passengers[i])
        return moves
