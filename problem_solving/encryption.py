import math

def encryption(s, debug=False):
    ns = s.replace(" ", "").strip()
    L = len(ns)

    L_squarred = math.sqrt(L)
    L_squarred_floored = math.floor(L_squarred)
    L_squarred_ceiled = math.ceil(L_squarred)
    
    seq = [n for n in range(L_squarred_floored, L_squarred_ceiled + 1)]
    
    if len(seq) >= 2:
        rows = seq[-2]
        cols = seq[-1]
        if not rows * cols >= L:
            rows = cols
    else:
        rows, cols = seq[0], seq[0] 
            
    
    # assert L_squarred_floored <= rows <= cols <= L_squarred_ceiled
    # assert rows * cols >= L

    grid_s = [[] for _ in range(rows)]
    ridx = 0
    for cidx, char in enumerate(ns):
        if (cidx % cols == 0) and (cidx != 0):
            ridx += 1
        grid_s[ridx].append(char)

    if debug:
        print(ns, L, L_squarred)
        print(rows, cols)
        for row in grid_s:
            print(row)

    rs = ""
    for ci in range(cols):
        for ri in range(rows):
            try:
                rs += grid_s[ri][ci]
            except:
                pass
        rs += " "

    if debug:
        print(ns, L, L_squarred)
        print(rows, cols)
        for row in grid_s:
            print(row)
        print(rs)



    return rs

    
case1 = "if man was meant to stay on the ground god would have given us roots"
case2 = "haveaniceday"
case3 = "chillout"


encryption(case1, debug=True)
encryption(case2, debug=True)
encryption(case3, debug=True)