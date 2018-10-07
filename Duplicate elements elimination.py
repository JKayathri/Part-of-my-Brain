my_list=list()
total=int(input("Enter the number of elements"))
for i in range(0,total):
    my_list.insert(i,int(input("Enter the numbers:")))
final_list = [] 
for i in my_list: 
    if i not in final_list: 
        final_list.append(i) 
print(final_list)  
