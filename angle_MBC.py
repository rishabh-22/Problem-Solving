# find the angle between base and hypotenuse of a triangle.


import math

# int(input())
height = 10
base = 10

hypotenuse = math.sqrt(height*height + base*base)

print(hypotenuse)
angle = math.acos(base/hypotenuse)
# tan = math.tan(height/base)
# print("tan:", tan)

# print(base/hypotenuse)
print(math.floor(angle * 180 / 3.14))
