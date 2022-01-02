import time
import sys
import numpy as np

a = ["0", 1, "two", "3", 4]

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

a = np.array([0,1,2,3,4])
print(a)
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])
print(type(a))
print(a.dtype)

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(type(b))
print(b.dtype)

c = np.array([20, 1, 2, 3, 4])
print(c)

c[0] = 100
print(c)

c[4] = 0
print(c)

d = c[1:4]
print(d)

c[3:5] = 300, 400
print (c)

select = [0,2,3]
d = c[select]
print(d)

a = np.array([0, 1, 2, 3, 4])
print(a)

print(a.size)
print(a.ndim)
print(a.shape)

a = np.array([1, -1, 1, -1])
mean = a.mean()
print(mean)

standard_deviation=a.std()
print(standard_deviation)

b = np.array([-1,2,3,4,5])
print(b)

min_b = b.min()
print(min_b)

u = np.array([1,0])
print(u)

v = np.array([0,1])
print(v)

z = u + v
print(z)

y = np.array([1,2])
print(y)

z = 2*y
print(z)

u = np.array([1, 2])
print(u)

v = np.array([3, 2])
print(v)

z = u * v
print(z)

#adds inner array values after multiplying them as combating arrays
print(np.dot(u,v))

u = np.array([1, 2, 3, -1]) 
print(u)
print(u+1)

print(np.pi)

x = np.array([0,np.pi/2,np.pi])
print(x)

y=np.sin(x)
print(y)

print(np.linspace(-2,2,num=5))
x = np.linspace(0,2*np.pi,num=100)
print(x)
y = np.sin(x)
print(y)