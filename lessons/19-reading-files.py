'''
Sometimes when coding with Python we might want to work woth some external files
and document, excel spreadsheet or an html file

the file needs to be in the same folder of our python file
Second argument:
    r - means read the file;
    w - means write on the file, deleting what was written before, can be used to create a new file;
    a - means append, we can modify the file or make any changes;
    r+ - means we want to read and writing;

Methods to read:
    readable() - returns true or false, we use it to know if the file is being read;
    readline() - reads the first line, if used again reads the next line and so on;
    readlines() - reads all lines;

'''

countries_file = open('C:/Users/Marvin Tavares/Python/Python-course/lessons/countries.txt', 'r')

##print(countries_file.readable())

##print(countries_file.readline()) 

##print(countries_file.readlines()) 

##print(countries_file.readlines()[2])

for lines in countries_file.readlines():
    print(lines)

countries_file.close()