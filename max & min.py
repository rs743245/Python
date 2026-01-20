num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
num3=int(input("enter 3rd number:"))

if(num1==num2==num3):
    print("3 numbers are equal")
    exit
if(num1>num2) and ((num1>num3)):
    print(f"{num1}is the maximum number")
elif(num2>num1) and (num2>num3):
    print(f"{num2}is the maximum number")
else:
    print(f"{num3}is the maximum number")

if(num1<num2) and ((num1<num3)):
    print(f"{num1}is the minimum number")
elif(num2<num1) and (num2<num3):
    print(f"{num2}is the minimum number")
else:
    print(f"{num3}is the minimum number")


