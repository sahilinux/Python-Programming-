## Creating an empty set
b = set()
print(type(b))

## Adding value to an empty set
b.add(4) 
b.add(4) 
b.add(5)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4, 5, 6))

## Accessing Elements
# b.add({4:5}) # cannot add list or dictionary to sets
print(b)

## legth of the set
print(len(b)) # Prints the length of this set

## Removel of an Item
b.remove(4) # Removes 4 from set b
# b.remove(14) # throws an error while trying to remove 14 (which is not present in the set)
print(b)

print(b.pop()) # Remove item from sets
print(b)

print(b.clear()) # Remove all the items
print(b)