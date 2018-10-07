n=int(input("Enter the binary value"))
count=-1
sum=0
while(n!=0):
    r=n%10
    n=int(n/10)
    count=count+1
    sum=sum+(2**count)*r
print("Decimal value is "+ str(sum))
