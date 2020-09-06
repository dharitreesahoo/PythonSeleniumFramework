a = "Hello, World!"
print(len(a))

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.lower())

a = "Hello, World!"
print(a.upper())

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

x = "ain" not in txt
print(x)

a = [1,2,"Peter",4.50,"Ricky",5,6]
print(a[5])
#lsit in python
list = ["dharitree","avneesh","santosh"]
print(list[1])

list1=[]
for i in range(10):
    list1.append(i)
print(list1)

list = [1, 3, 5, 7, 9]

# Using for loop
for i in list:
    print(i)

list = [1, 3, 5, 7, 9]

# getting length of list
length = len(list)

# Iterating the index
# same as 'for i in range(len(list))'
for i in range(length):
    print(list[i])

# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]

# Getting length of list
length = len(list)
i = 0

# Iterating using while loop
while i < length:
    print(list[i])
    i += 1

# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]

# Using list comprehension
[print(i) for i in list]

print("*************")

list1 = [1,2,2,3,55,98,65,65,13,29]
# Declare an empty list that will store unique values
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
print("*************")
list1 = [3,4,5,9,10,12,24]
sum = 0
for i in list1:
    sum = sum+i
print("The sum is:",sum)

list1 = [1,2,3,4,5,6]
list2 = [7,8,9,2,10]
for x in list1:
    for y in list2:
        if x == y:
            print("The common element is:",x)

Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(Days)
print(type(Days))
print("looping through the set elements ... ")
for i in Days:
    print(i)   