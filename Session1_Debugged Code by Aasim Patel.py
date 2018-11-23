##############################################################################
#Debugged code to calculate velocity and time taken given the gravitational acceleration ,g, initial velocity ,v0, Initial Displacement,y0, and Final Displacement,y #
#Aasim Patel, 02/10/14#
##############################################################################

#Start#
from math import sqrt

# Known Values - gravitational acceleration,g, Initial Velocity, v0, Initial Displacement, y0, Final Displacement, y #
g = -9.81 # ms**-2 #
v0 = 10 # ms**-1 #
y0 = 15 # m #
y = 0.0 # m # 

# Calculate velocity, ms**-1 and time taken, s #
v2 = v0**2 + 2*g*(y-y0)
vel = sqrt(v2)

if v0 > 0:
    print "v0 is positive" 
else:
    print "v0 is less than or equal to zero"

time = -(vel + v0)/g

# Display Results - time taken, s and the velocity, ms**-1 #
print "time taken = " , time, "s"
print "velocity" , vel, "ms-1"

# End #