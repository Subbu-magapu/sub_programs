n=int(input("enter a largest number="))
a=int(input("enter a largest number="))
b=int(input("enter a largest number="))

if n>=a and  n>=b:
    print(n,"is the largest number")

elif a>=n and a>=b:
    print(a,"is the largest number")

elif b>=n and b>=a:
    print(b,"the largest number")