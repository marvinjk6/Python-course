# List Functions / Methods
numbers = [8, 52, 39, 100, 77, 22]
fruits = ['Banana', 'Apple', "Watermelon", 'Orange', 'Pineapple', 'Grapes']

#### Adding a list to another
#numbers.extend(fruits)
#print(numbers)

### Append - Add an item to the end of the list
#fruits.append('Peache')
#print(fruits)

### Insert - Insert an item at a given position. The first argument is the index of the element before which to insert 
#fruits.insert(2, 'Lemon')
#print(fruits)

### Remover - Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
#fruits.remove('Apple')
#print(fruits)

### Clear - Remove all items from the list. Equivalent to del a[:]
#fruits.clear()
#print(fruits)

### Index - Returns the index of a value in a list
#print("Pineapple's index: ", fruits.index('Pineapple'))

### Count - Return the number of times x appears in the list
#print(fruits.count('Strawberry'))

### Sort - put the list in order
#numbers.sort()
#print('Sort:', numbers)

### Reverse - Reverse the elements of the list in place.
#numbers.reverse()
#print('Reverse:', numbers)

### Copy - Return a shallow copy of the list
#list3 = fruits.copy()
#print('List 3 is a copy of fruits:', list3)

### Pop - removes the last value of a list
#fruits.pop()
fruits.pop(1) # the pop method also allow to choose an index to remove
print(fruits)

### delete - we can delete the list - this is different from clear method
# when we use clear the list is avaiable in our code
# when the list is deleted it becomes unavailable 
#del numbers
#print(numbers) # name 'numbers' is not defined
