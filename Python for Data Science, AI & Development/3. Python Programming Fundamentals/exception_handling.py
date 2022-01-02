a = 1
try:
    b = int(input('Please enter a denominator for a '))
    a = a/b
    print('Success a=',a)
except(ZeroDivisionError, NameError):
    print('A zero division error, or a name error occurred.')
except(ValueError):
    print('a can\'t be divided by that')
except:
    print('The thing broke. We don\'t know why')

#With finally

a = 1
try:
    b = int(input('Please enter a denominator for a '))
    a = a/b
except(ZeroDivisionError, NameError):
    print('A zero division error, or a name error occurred.')
except(ValueError):
    print('a can\'t be divided by that')
except:
    print('The thing broke. We don\'t know why')
else:
    print('Success a=',a)
finally:
    print('Processing Complete')