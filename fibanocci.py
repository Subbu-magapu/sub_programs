n = int(input("enter the n number terms="))

a , b = 0 , 1

print("Fibanocci series")

for i in range (n+1):
    print(a , end=" ")

    a, b =b, a+b