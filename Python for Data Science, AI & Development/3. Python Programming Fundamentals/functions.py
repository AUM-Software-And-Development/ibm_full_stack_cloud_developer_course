def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a,"plus 1 =",b)
    return b

help(add)
add(1)
add(2)

def mult(a,b):
    '''
    mutliply a and b
    '''
    c=a*b
    return(c)
    print('This is not printed')

help(mult)
product = mult(12,2)
print(product)
print(mult(10.0, 3.14639))
print(mult("E", 4))

def square_plus1(a):
    '''
    Squares a number then adds one to it
    '''
    #local var b
    b = 1
    c = a*a
    d = c + 1
    print(a, 'with an exponent of 2 gets:',c,'plus 1 gets:',d)
    return d

help(square_plus1)
print(square_plus1(5))

x = 3
y = square_plus1(x)
print(y)

def MJ():
    print('Michael Jackson')

def MJ1():
    print('Michael Jackson')
    return(None)

MJ()
MJ1()

def con(a,b):
    return (a+b)

print(con("This", "is"))

# a and b calculation block1

a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5
c1   

# a and b calculation block2

a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5
c2   

# Make a Function for the calculation above

def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c)

a1 = 4
b1 = 5
c1 = Equation(a1, b1)
print(c1)

a2 = 0
b2 = 0
c2 = Equation(a2, b2)
print(c2)

album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(sum(album_ratings))

def type_of_album(artist,album,year_released):
    print(artist,album,year_released)
    return "modern" if year_released>1980 else "Oldie"

x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

def PrintList(the_list):
    for i in range(len(the_list)):
        print(the_list[i])

PrintList(['1',1,'the man', 'abc'])

def isGoodRating(rating=4):
    if(rating<7):
        print('This album sucks it\'s rating is',rating)
    else:
        print('this album is good its rating is',rating)
    
isGoodRating()
isGoodRating(10)

def printAll(*args): # All arguments are "packed" into args which acts like a tuple
    print('Num of arguments:', len(args))
    for i in range(len(args)):
        print(args[i])

printAll(1,2,2,3,4)

def printDictionary(**args):
    for key in args:
        print(key+":"+args[key])
#    for i in range (len(args)):
#        print (args[i][1]) <- has to be the key value

#err! printDictionary({"a":1,"b":2,"c":3,"d":4})
printDictionary(a='1',b='2',c='3',d='4') # requires singular arguments to work

