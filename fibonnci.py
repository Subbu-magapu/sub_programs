n = int(input("enter a number="))

a = 0
b = 1

for x in range(n):
    c = a+b
    print(c)
    a = b
    b = c
   