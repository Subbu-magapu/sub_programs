num = int(input("enter a number "))
order = len(str(num))

val = 0

temp = num

while temp >0:
    digit = temp%10
    val += digit ** order
    temp//=10

if num == val:
    print(num, "is an armstrong number")

else:
    print(num,"not an armstrong")