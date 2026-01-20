num=int(input("enter the number to be checked:"))
temp=num
sum = 0
len = len(str(num))

while(temp>0):
    reminder=temp % 10
    sum += reminder ** len
    temp//=10
if(num==sum):
    print(num,"is a armstrong number")
else:
    print(num,"is not a armstrong number")
