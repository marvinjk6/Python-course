## Tuples are similar to lists, but lists are mutable and tuples are IMMUTABLE, it means you can't change any value in a tupple
# Allow repetead values
# we can mix various types of data in a tuple

tuple_numbers = (1, 2, 3, 1)
tuple_mix = ("Marvin", 18, True)
print(tuple_numbers)
print("Length:", len(tuple_numbers))
print("Type:", type(tuple_numbers))
print(tuple_mix)

## Checking the type of the values in a tupple
print("Type of the third element:",type(tuple_mix[2]))


## Tuple constructor
tuple_constructor = tuple(("Car", "Corolla", 40000, 2019, False))
print(tuple_constructor)

