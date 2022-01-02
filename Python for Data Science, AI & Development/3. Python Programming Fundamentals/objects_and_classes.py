import matplotlib.pyplot as plt

class Circle(object):
    #Ctr
    def __init__(self,radius=3,color='blue'):
        self.radius=radius
        self.color=color

    def add_radius(self, r):
        self.radius = self.radius+r
        return self.radius

    def drawCircle(self):
        plt.gca().add_patch (plt.Circle ((0,0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

RedCircle=Circle(10, 'red')

#print object methods
help(RedCircle)

print(RedCircle.radius, RedCircle.color)

RedCircle.radius=1
print(RedCircle.radius, RedCircle.color)

#RedCircle.drawCircle()

print('Radius of object:', RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object after adding two to the radius using its add_radius method:', RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object after adding five to the radius using its add_radius method:', RedCircle.radius)

BlueCircle = Circle(radius=100)
print(BlueCircle.radius)
print(BlueCircle.color) # default

#BlueCircle.drawCircle()

class Rectangle(object):
    #Ctr
    def __init__(self, width=2, height=3, color='r'):
        self.width = width
        self.height = height
        self.color = color

    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), self.width,self.height,fc=self.color))
        plt.axis('scaled')
        plt.show()

SkinnyBlueRectangle = Rectangle(2, 10, 'blue')

help(SkinnyBlueRectangle)

print("Rectangle:",SkinnyBlueRectangle.height, SkinnyBlueRectangle.width, SkinnyBlueRectangle.color)
#SkinnyBlueRectangle.drawRectangle()

FatYellowRectangle = Rectangle(20,5,'yellow')
print("Rectangle:",FatYellowRectangle.height, FatYellowRectangle.width, FatYellowRectangle.color)
FatYellowRectangle.drawRectangle()