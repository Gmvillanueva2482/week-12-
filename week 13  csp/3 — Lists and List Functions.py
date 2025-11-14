# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# lists are part of the collections family in Phyton

my_list=[1, 2, 3, 4, 5]
print(my_list) # {1, 2, 3, 4, 5}
print(len(my_list))  # 5
print(type(my_list)) # <class 'list'>
print(my_list[0])# 1
print(my_list[1:4]) # [2,3,4]
print(my_list[1:]) # [2,3,4,5]
print(my_list[:-1]) # [1,2,3,4]
# reverse the list
print(my_list[::-1]) #[5,4,3,2,1]
#Modifying a list
my_list.append(6) # adds 6 to the end of the list
print(my_list)
#add 7 and 8 to the end of the list
my_list.append([7,8,9,10,11])
print(my_list)
#add 9 and 10 to the end of the list
my_list.append([9,10])
print(my_list)
#remove the last item
my_list.pop()
print(my_list)
#remove the second term
my_list.pop(2)
print(my_list)
#sort the list in ascending order
#my_list.sort()
print(my_list)
# reverse the list
my_list.reverse()
print(my_list)

my_list.reverse()
print(my_list)
#remove the list
#my_list.remove()
print(my_list)
#add 50 more to the end of the list
new_list = list(range(12, 120))
print(new_list)
my_list.append(new_list)
print(my_list)

newer_list = list(range(120,620))
print(newer_list)
my_list.append(newer_list)
print(len(my_list))
# print every 3rd item in the list
print(my_list[::3])
print(my_list[::10])
# remove ebery 3rd item in the list
del my_list [::3]
print(len(my_list))
print(my_list)
#list functions
# .append()- adds an item to the end of the list
# .extend()- adds multiple items to the end of the list
# .pop()- removes and returns an item at a given index
# .remove()- removes the first occerence of a specific value
# .sort() - sorts the list in ascending order
# .reverse()- reverses tje order of the list
#####################################################################
# why is a list more useful than a varible?
# A list can hold muliple values
# while a varible can only hold one value
cake= ['chocolate', 'vanilla', 'red velvet', 'carrot']

print(cake[0])

print(cake[-1])

cake[0] = 'strawberry'
print(cake)

cake.append('lemon')
print(cake)
cake[1]='choclate'
print(cake)
#remove the last cake
cake.pop()
print(cake)
#inset a new cake 
cake.insert(2, 'funfetti')
print(cake)






# Examples:

my_list=['apple','banana','cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

#my_list.append('grape')
#print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)

#Practice Problems:

# Create a list with 5 of your favorite foods.  
avorite_foods=[ 'mango','steak','tacos','chicken','corn']
# Print the second and last item.
print(avorite_foods[3:5])
# Add a new item using .append().
avorite_foods.append('gum')
print(avorite_foods)
# Remove the first item using .pop(0).
avorite_foods.pop(0)
print(avorite_foods)
# Reverse your list using .reverse().
avorite_foods.reverse()
print(avorite_foods)
# Create a list of 3 lists (matrix), and access the middle element.


my_set={1,2,3,4,5}
print(my_set)
print(type(my_set))

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)
# check if an item is in the set

print( 4 in my_set) #True
print( 3 in my_set) #False

my_tuple=(1,2,3,4,5)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[1:4])
