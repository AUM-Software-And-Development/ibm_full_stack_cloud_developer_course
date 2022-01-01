# Comment syntax

import sys

print('Hello, Python!')
print(sys.version)

# frint("Error!")
# print("Error!)
# print("Unexecuted code")

types = type(12)
print(types)
types = type(12.12)
print(types)
types = type("twelve")
print(types)

print("Integers:")
types = type(-1)
print(types)
types = type(4)
print(types)
types = type(0)
print(types)

print("Floats:")
types = type(1.0)
print(types)
types = type(0.5)
print(types)
types = type(0.56)
print(types)

print("Bool:")
types = type(True)
print(types)
types = type(False)
print(types)

print('Typecasting:')
types = int('1')
print(types, type(types))
#err! types = int('1 or 2 people')
#err! print(types, type(types))
types = float('1.2')
print(types, type(types))
types = str('1')
print(types, type(types))
types = str('1.2')
print(types, type(types))

types = int(True)
print(types, type(types))
types = float(True)
print(types, type(types))
types = bool(1)
print(types, type(types))
types = bool(0)
print(types, type(types))

x = 43 + 60 + 16 + 41
print(x)
x = 50-60
print(x)
x = 5*5
print(x)
x = 25/5
print(x)
x = 25/6
print(x)