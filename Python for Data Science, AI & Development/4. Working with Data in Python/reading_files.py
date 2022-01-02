import urllib.request

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

example1 = "Example1.txt"
file1 = open(example1, "r")
print(file1)
print(file1.name)
print(file1.mode)
file1_content = file1.read()
print(file1_content)
print(type(file1_content))
file1.close()
#err! testContent = file1.read()

# Using with to automatically close it

with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))
    #note: as the read method is called, it autoincrements, and the index does not reset.

print("\nnew read\n")

with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))

print("\nnew read\n")

with open(example1, "r") as file1:
    print("This is a line read:",file1.readline())

print("\nnew read\n")

with open(example1, "r") as file1:
    print("This is a line read with a max of 4 chars:",file1.readline(4))
    print("This is a line read with a max of 4 chars:",file1.readline(4))

print("\nnew read\n")

with open(example1, "r") as file1:
    print("This is a line read with a max of 4 chars:",file1.readline(4))
    print("This is a line read with a max of 4 chars:",file1.readline(4))

print("\nnew read\n")

with open(example1, "r") as file1:
    i=0
    for line in file1:
        print("Iteration",str(i), ": ", line)
        i = i+1

print("\nnew read\n")

with open(example1, "r") as file1:
    file_as_list = file1.readlines()

print(file_as_list[0])