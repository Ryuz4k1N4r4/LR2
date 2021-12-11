
# Online Python - IDE, Editor, Compiler, Interpreter

n = int(input("Число:"))
temp = n
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if(temp == rev):
    print("Палиндром")
else:
    print("Не палиндром")
