# Create a list

L = ['Michael Jackson', 10.1, 1982]
print('The list:\n',L)

print('Element using negative and positive index 0 or -3:\n Positive:',L[0],'\n Negative:',L[-3])
print('Element using negative and positive index 1 or -2:\n Positive:',L[1],'\n Negative:',L[-2])
print('Element using negative and positive index 2 or -1:\n Positive:',L[2],'\n Negative:',L[-1])

L = ['Michael Jackson', 10.1, 1982, [1,2], ("A",1)]
print('The list:\n',L)

print('Sliced at [3:3]:\n', L[3:3])
print('Sliced at [3:4]:\n', L[3:4])
print('Sliced at [3:5]:\n', L[3:5])

L = ["Michael Jackson", 10.2]
print('New list:\n',L)
L.extend(['pop', 10])
print('Extended ["pop", 10]:\n',L)
L.append(['a', 'b'])
print('Appended ["a", "b"]:\n',L)

A = ["disco", 10, 1.2]
print('Before A[0] change:', A)
A[0] = 'hard rock'
print('After A[0] change:', A)

# Splitting
print('Splitting "hard rock"')
print('hard rock'.split())

print('Splitting "A,B,C,D on commas"')
print('A,B,C,D'.split(','))

# References
print('\nReferences:\n')
A = ['hard rock', 10, 1.2]
B = A
print('When B = A')
print('A:',A)
print('B:',B)

print('B[0]:',B[0])
A[0] = 'banana'
print('B[0] after the address it references (A[0]) was changed:',B[0])

print('\nCloning/Creating new references:\n')
B = A[:]
print('A:', A)
print('When B=A[:]:', B)
A = 'Hard rock'
print('A was changed. A:',A)
print('B:',B)