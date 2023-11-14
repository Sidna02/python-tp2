s1 = [1, 2, 3, 4, 5]
s = []
for i, j in enumerate(s1):
    s.append(s1[-i-1])
print(s)
