def solution(data, n):
    if len(data)<100:
        j = 1    
        newlist = []
        for x in range(0, len(data)-1, 1):
            for y in range(x+1, len(data), 1):
                if data[x] == data[y]:
                    j=j+1
            if j>n:
                newlist.append(data[x])
            j = 1
        newdata = [i for i in data if i not in newlist]
        if n == 0:
            newdata = []
    return newdata