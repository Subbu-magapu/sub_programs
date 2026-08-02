num = int(input("enter a number "))
order = len(str(num))

valu = 0

temp = num

while temp >0:
    digit = temp%10
    valu += digit ** order
    temp//=10

if num == valu:
    print(num, "is an armstrong number")

else:
    print(num,"not an armstrong")