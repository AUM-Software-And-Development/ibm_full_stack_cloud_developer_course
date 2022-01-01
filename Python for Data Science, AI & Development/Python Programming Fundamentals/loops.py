# Use of range

print(range(3))

dates = [1982,1980,1973]
N = len(dates)
for i in range(N):
    print(dates[i])

for i in range(0,8):
    print(i)

for year in dates:
    print(year)

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0,5):
    print('before square', i, 'is', squares[i])
    squares[i] = "white"
    print('After square', i, 'is', squares[i])

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year!=1973):
    print(year)
    i = i + 1
    year = dates[i]

print('year =',year,'It took',i, 'iterations to get out of the loop')