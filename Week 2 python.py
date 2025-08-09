my_list = []
another_list = [50,60,70]

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

my_list.insert(1,15)
print(my_list)

my_list.extend(another_list)
print(my_list)

my_list.sort()

my_list = [10, 20, 30, 40, 50]

index_of_30 = my_list.index(30)

print("The index of 30 is:", index_of_30)
