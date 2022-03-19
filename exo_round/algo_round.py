
class callRound():

        
    def algoToCall(cls, number, n):
        return round(number, n)
    
    def round_nb(cls,float1, float2, nb, algoToCall):
        res = [algoToCall(float1, nb), algoToCall(float2, nb)]
        return res
    
    
obj = callRound()
obj.round_nb(2.25745, 21458, 2, obj.algoToCall)