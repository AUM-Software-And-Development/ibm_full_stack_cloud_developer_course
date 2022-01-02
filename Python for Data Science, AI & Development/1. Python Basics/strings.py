string = 'Michael Jackson'
print(string[0])
print(string[6])
print(string[13])

print(string[-1])
print(string[-15])

length = len(string)
print(length)

print(string[0:4])
print(string[8:12])
print(string[::2])
print(string[0:5:2])

opinion = string + " is the best"
print(opinion)

print(string + "\n is the best" )
print(string + "\t is the best" )
print(string + "\\ is the best" )
print(string + r"\ is the best" )

a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)

opinion = opinion.replace('Michael', 'Janet')
print(opinion)

print(string.find('el'))
print(string.find('Jack'))
#err! print(string.find(Jasdfaasdf))