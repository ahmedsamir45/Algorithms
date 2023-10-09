y = [1,1,2,3,5,3,3,4,4,5]

d = dict()

for e in y :

    if e in d.keys():
        d[e]+=1

    else:
        d[e] = 1

print(d)

    