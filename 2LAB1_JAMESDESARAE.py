# Desarae James
# 09/27/2026
# P2LAB1
# This program ill calculate the diameter, circumference, and area of a circle

# Import Math module to use the constant, math.PI
# Import math

# Get radius from user 
import math


radius=float(input("Enter the radius of the circle: ")) 
print()

#calculate diameter
diameter=2*radius

#Display diameter with 1 decimal point
print("The diameter of the circle is: {:.1f}".format(diameter))

# Calculate circumference
circumference=2*math.pi*radius

#Display circumference with 1 decimal point
print("The circumference of the circle is: {:.1f}".format(circumference))

#Calculate circumference
circumference=2*math.pi*radius

#Display circumference with 2 decimal places
print("The circumference of the circle is: {:.2f}".format(circumference))

#Calculate area
area=math.pi*radius**2

#Display area with 3 decimal places
print("The area of the circle is: {:.3f}".format(area))



