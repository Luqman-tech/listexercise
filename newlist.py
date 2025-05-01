#create list
my_list = []
#append content
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insert 15 at index 1
my_list . insert(1 ,15)
#add [50, 60, 70] to list
my_list.extend([50, 60, 70])
#remove last element
my_list.pop()
#sort list in ascending order
my_list.sort()
#find and print index of value 30
index_of_30 = my_list.index(30)
print("index of 30:", index_of_30) 
