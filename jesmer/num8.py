x = int(input())
min = 0
hora = 0
seg = 0
while x > 0:
    if min >= 60:
        hora +=1
        min -= 60
    if x >= 60:
        min +=1
        x -= 60
    else:
        seg = x
        x=0
print(f"{hora}:{min}:{seg}")