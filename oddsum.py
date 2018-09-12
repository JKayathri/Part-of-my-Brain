n=int(input("Enter n\n"))
sum=0
while n>0:
    rem=n%10
    n=int(n/10)
    if rem%2!=0:
        sum=sum+rem
print("Sum of odd digits"+ str(sum))
    
