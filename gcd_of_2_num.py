a=int(input("Enter first number:\n"))
b=int(input("Enter second number:\n"))
if a<b:
    num=a
else:
    num=b
for i in range(num,0,-1):
    if a%i==0 and b%i==0:
        break
print("GCD of " + str(a) + " and "+ str(b) + " is "+ str(i))
