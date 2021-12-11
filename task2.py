n = []
a = []
b = []
c = []
n = [int(i) for i in input("Введите числа").split()]
for i in range(len(n)):
    if n[i] % 2 == 0:
        a.append(n[i])
    if n[i] % 3 == 0:
        b.append(n[i])
    if n[i] % 5 == 0: 
        c.append(n[i])
        
print("Делятся на 2")        
for x in range(len(a)):
    print(a[x], end=" ")
print(" ")    

print("Делятся на 3") 
for x in range(len(b)):
    print(b[x], end=" ")
print(" ") 

print("Делятся на 5") 
for x in range(len(c)):
    print(c[x], end=" ")
print(" ") 

pass
