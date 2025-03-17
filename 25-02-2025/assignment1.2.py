import math
diameter=int(input("write the diameter of circle:   "))
angle=int(input("write the angle in degrees:    "))
arc_length=diameter/2*angle*math.pi/180
print(f"arc length = {arc_length}")