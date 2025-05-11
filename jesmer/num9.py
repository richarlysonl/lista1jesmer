impar = []
par = []
for i in range(0,15):
    x = int(input())
    if x % 2 == 1:
        if len(impar) < 5:
            impar.append(x)
        else:
            for j in range(0,5):
                print(f"impar[{j}] = {impar[j]}")
            impar = []
            impar.append(x)
        
    else:
        if len(par) < 5:
            par.append(x)
        else:
            for j in range(0,5):
                print(f"par[{j}] = {par[j]}")
            par = []
            par.append(x)

for i in range(len(impar)):
    print(f"impar[{i}] = {impar[i]}")
for i in range(len(par)):
    print(f"par[{i}] = {par[i]}")