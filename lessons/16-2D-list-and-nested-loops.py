## 2D Lists and Nested Loops in Python

list = [
    ["Mikal", "Trae", "Bob", "Jrue"],
    ["Bike", "Car", "Bus", "Skate"],
    ["Banana", "Apple", "Grapes", "Peache"]
]

# print(list[0])
# print(list[2][2])

for rows in list:
    for values in rows:
        print(values)