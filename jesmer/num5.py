x= int(input())
y=[]
for i in range(1001):
    for j in range(x):
        y.append(j)
    print(f"N[{i}] = {y[i]}")