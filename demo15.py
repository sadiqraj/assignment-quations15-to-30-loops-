num=int(input("enter the 4 degit num:"))
res=0
while num>0:
    digit=num%10
    res=res+digit
    num=num//10
print("sum 4 digit sum is",res)