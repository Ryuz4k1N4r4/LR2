n = int(input("Число: "))
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
print("В обратном порядке:", rev)
