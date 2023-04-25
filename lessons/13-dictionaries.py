## Dictionaries are used to store data values in the key value pairs
# they are changeable, you can modify them
# they don't allow duplicate
# you can add several data types

dictionary = {
    "name": "Tim",
    "age": 18,
    "nationality": "African",
    "collegeDegree": True,
    "favoritesGames": ["The last of us", "Devil may cry", "Call of dutty", "Fifa"]
}

print(dictionary["name"])
print("Dictionary length:", len(dictionary))
print("List:", dictionary["favoritesGames"])
print("List first value:", dictionary["favoritesGames"][1])

## We can assign a variable with a dictionary key
nationality = dictionary["nationality"]
print(nationality)