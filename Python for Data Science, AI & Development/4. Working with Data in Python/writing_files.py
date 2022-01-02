#Write line as a file
example2 = 'Example2.txt'
def readfile2():
    '''
    Opens the specified global file
    '''
    with open(example2, 'r') as file2:
        print(file2.read())


with open(example2, 'w') as file2:
    file2.write('This is line A')

readfile2()

with open(example2, 'w') as file2:
    file2.write("This is line A\n")
    file2.write("This is line B\n")

readfile2()

Lines = ["This is line A\n", 'This is line B\n', 'This is line C\n']
print(Lines)

with open(example2, 'w') as file2:
    for line in Lines:
        print(line)
        file2.write(line)

readfile2()

with open(example2, 'w') as file2:
    file2.write("Overwritten\n")

readfile2()

#append so as not to overwrite

with open(example2, 'a') as file2:
    file2.write("This is line C\n")
    file2.write("This is line D\n")
    file2.write("This is line E\n")

readfile2()

#other modes

#    r+ : Reading and writing. Cannot truncate the file.
#    w+ : Writing and reading. Truncates the file.
#    a+ : Appending and Reading. Creates a new file, if none exists.

# works like c++ tellp seekp format. The seek method has to be called
# to move the index within an addressable array of bytes

with open(example2, 'a+') as file2:
    file2.write('This file is being appended to\n')
    print(file2.tell())
    file2.seek(0,0)
    print(file2.read())

#copy

with open('Example2.txt', 'r') as file2:
    with open('Example3.txt', 'w') as copy_as_file3:
        for line in file2:
            copy_as_file3.write(line)

# niche uses

# overwrite and then truncate(remove) all of the data that follows the pointer
with open('Example2.txt', 'r+') as testwritefile:
    data = testwritefile.readlines()
    testwritefile.seek(0,0) #write at beginning of file
   
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    #testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())