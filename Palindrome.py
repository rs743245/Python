num=int(input("enter the number:"))
temp=num
rev=0

while(temp>0):
    a=temp%10
    rev=rev*10+a
    temp=temp//10
if (rev==num):
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome number")



