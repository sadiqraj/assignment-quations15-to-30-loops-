numbers=0
n=int(input("enter the number of elements=\t"))
for i in range(1,n+1):
    allElements=int(input("enter element:"))
    numbers.append(allElements)
even_lst=[]
odd_lst=[]
for j in numbers:
    if j% 2==0:
        even_lst.append(j)
    else:
        odd_lst.append(j)
print("even number list \t:",even_lst)
print("odd number list \t:",odd_lst)