table=int(input("Enter the no. of multiplication tables:\n"))
for i in range(1,table):
    tab_num=int(input("Enter the multiplication table you want\n "))
    for j in range(1,11):
        mul=j*tab_num
        print(str(j) + " * " + str(tab_num) +" = " + str(mul) +" \n ")
    print("\n")
