d = dict()
a =  [3, 6, 8, 2, 4, 8, 3, 1, 8, 9, 7, 0, 5, 5, 1]
for i in a:
    d[i] = d.get(i,0)+1

print(d)