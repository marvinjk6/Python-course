# Strings - is just text, characters

name = 'MIKE'
toy = 'teddy bear'

# String format
print("My dog's name is {}, his favorite toy is {}".format(name, toy))


completeName = 'Jeferson Siqueira Júnior'

##### Strings Function

print('Cathing characters from strings:', completeName[0], completeName[1])

# Upper case
print('Upper:', completeName.upper())
print('Is Upper', name.isupper())
print('Two functions together:', name.lower().isupper())

# Lower case
print('Lower:', completeName.lower())
print('Is lower:', toy.islower())

# Length
print('Lenght:', len(completeName))

# Index - search for the first time the character appears
print('Index:', completeName.index('a'))

# Replace
print('Replace:', completeName.replace('Siqueira', 'Amaral'))




