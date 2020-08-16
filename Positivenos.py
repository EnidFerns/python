my_list = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    my_list.append(ele) 
print("list: ",my_list) 

op=list(filter(lambda x: (x>0),my_list))
print("output: ",op)
