from array import*
my_array = array('i', [1,2,3,4,5])
for i in my_array:
    print(i)
my_array.append(6)
for i in my_array:
    print(i)

my_array.insert(0,9)
for i in my_array:
    print(i)
my_array2=array('i',[7,8,9,10])
my_array.extend(my_array2)
for i in my_array:
    print(i)
my_array.remove(4)
for i in my_array:
    print(i)
my_array = array('i', [1,2,3,4,5])
print(my_array.index(5))
my_array.reverse()
for i in my_array:
    print(i)