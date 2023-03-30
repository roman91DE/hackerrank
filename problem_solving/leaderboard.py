from bisect import bisect_right


def climbingLeaderboard(ranked, player):
    
    ret = []
    ranked = sorted(list(set(ranked)))
    
    for score in player:
        insertaion_point = bisect_right(ranked, score)
        ret.append(len(ranked) - insertaion_point + 1)
        
            
    return ret
            
            

a1 = [7]
a2 = [100, 100, 50, 40, 40, 20, 10]


b1 = [4]
b2 = [5, 25, 50, 120]

climbingLeaderboard(a2,a1)
climbingLeaderboard(b2,b1)