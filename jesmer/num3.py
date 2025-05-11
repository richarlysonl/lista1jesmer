a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
positivo=[]
array = [a, b, c, d, e, f]
for i in range(len(array)):
    if  array[i] > 0:
        positivo.append(array[i])
media = sum(positivo) / len(positivo)
print(f"{len(positivo)} valores positivos")
print(f"{media:.2f}")