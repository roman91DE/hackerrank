def cutTheSticks(arr):
    ret = []
    while not len(set(arr)) <= 1:
        ret.append(len(arr))
        min_len = min(arr)
        while min_len in arr:
            arr.remove(min_len)
        arr = [x - min_len for x in arr]
    else:
        ret.append(len(arr))
        
    return ret




case1 = [8, 8, 14, 10, 3, 5, 14, 12]

for val in cutTheSticks(case1):
    print(val)

"""
8
7
6
4
3
2
"""