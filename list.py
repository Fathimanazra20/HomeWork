creating a list

fruits = ["apple","banana","orange","mango"]
print (fruits)

accessing elements

colors = ['white','black','silver','golden','beige']
print("first element:",colors[0])
print("third element:",colors[2])
print("last element:",colors[-1])

modifying a list

numbers = [10,20,30,40,50]
numbers[1] = 25
numbers.append(60)
print(numbers)


list slicing

names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = names[:3]
print(subset)

looping through a list

numbers = list(range(1, 11))
for i in numbers:
    print(i**2)

list methods:append and extend

shoppingcart = []
shoppingcart.append('milk')
shoppingcart.append('bread')
shoppingcart.append('eggs')
shoppingcart.extend(['butter', 'cheese'])
print(shoppingcart)

finding maximum and minimum in a list

numbers = [45, 22, 88, 56, 92, 33]
max=max(numbers)
min=min(numbers)
print(max)
print(min)

counting occurrences

letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
a= letters.count('a')
print(a)

list comprehension  

square = [i**2 for i in range(11) if i % 2 == 0]
print(square)

removing duplicates

nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
Num = list(set(nums))
print(Num)
