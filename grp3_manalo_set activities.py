# ACTIVITY 1: REMOVE DUPLICATES

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)
print (unique_numbers)

# ACTIVITY 2: ADD AND REMOVE

fruits = {"apple", "banana"}

# Add "orange"
fruits.add("orange")

# Remove "banana"
fruits.remove("banana")
print(fruits)

# ACTIVITY 3: SET OPERATIONS

A = {1, 2, 3}
B = {3, 4, 5}

# Union (all elements)
print(A | B)

# Intersection (common elements)
print(A & B)

# ACTIVITY 4: (CHALLENGE): COMMON STUDENTS

classA = {"John", "Ana", "Mark"}
classB = {"Ana", "Mark", "liza"}

# Student in both classes
print (classA & classB)

# All students
print (classA | classB)
