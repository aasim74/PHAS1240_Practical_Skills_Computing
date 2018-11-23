###############################################################################################
# Code to perform an animation of a ball to travel in projectile motion in 2-dimensional space#                                                         #
#Aasim Patel, 27/11/14, Session 8 - Animations in Python                                      #
###############################################################################################

#Importing the functions we are going to be using in this code#
from visual import sphere, curve, color, display, rate
import numpy as np

# set up the scene
scene = display(x = 50, y = 50, width = 640, height = 480, center = (20,0,0))
ground = curve(pos=[(-5,0,0),(50,0,0)],color = color.green)

# initial ball coordinates (metres)
x0 = 0.0
y0 = 0.0
y = y0
g = 9.8 # gravitational acceleration, m/s2
dt = 0.01 # time interval for loop, in seconds

# input initial angle and velocity
dtheta = float(raw_input("Input the initial angle in degrees: "))
theta = np.radians(dtheta)
v0 = float(raw_input("Input the initial velocity in metres/second: "))
v1 = v0*0.5

# start the animation
ball = sphere(pos = (x0,y0,0),radius = 1,make_trail=True)
t = 0 # initial time
while y >= y0:
        t += dt
        x = x0 + (v0*t*np.cos(theta))
        y = y0 + (v0*t*np.sin(theta))-(0.5*g*(t**2))
        ball.pos = (x,y,0)
        rate(30)

r = ((v0**2)*np.sin(2*theta))/g # This is to calculate the range of the ball

print "total time ball was in the air (first flight) = ", t , "seconds"
print "total distance travelled travelled by the ball (first flight) = ", x, "metres"
print "the range of the ball (first flight)is  = ", r, "metres"

t0 = t
x_a = x
y_a = y
r_a = r 

#the ball will bounce again
t=0
v0 = 0.5*v0
x0 = x
y0 = y
y1 = y0
while y1>=y0:
    t += dt
    x1 = x0 + (v0*t*np.cos(theta))
    y1 = y0 + (v0*t*np.sin(theta))-(0.5*g*(t**2))
    ball.pos = (x1,y1,0)
    rate(30)
    
r = ((v0**2)*np.sin(2*theta))/g # This is to calculate the range of the ball

print "total time ball was in the air (second flight) for = ", t , "seconds"
print "total distance travelled travelled by the ball (second flight) = ", x, "metres"
print "the range of the ball (second flight) is = ", r, "metres"

t1 = t
x_b = x
y_b = y
r_b = r 
 
#this ball will bounce for the third time
t=0
v0 = 0.25*v0
x0 = x1
y0 = y1
y2 = y0
while y2>=y0:
    t += dt
    x2 = x0 + (v0*t*np.cos(theta))
    y2 = y0 + (v0*t*np.sin(theta))-(0.5*g*(t**2))
    ball.pos = (x2,y2,0)
    rate(30)
        
r = ((v0**2)*np.sin(2*theta))/g # This is to calculate the range of the ball

print "total time ball was in the air (third flight)for = ", t , "seconds"
print "total distance travelled travelled by the ball (third flight) = ", x, "metres"
print "the range of the ball (third flight) is = ", r, "metres"

t2 = t
x_c = x
y_c = y
r_c = r 

#This is going to calculate the totals of the distances and time taken for the ball in the air.
t_total = t0+t1+t2
x_total = x_a + x_b + x_c
y_total = y_a + y_b + y_c
r_total = r_a + r_b + r_c

#print the totals of the time and distance and range
print "TOTAL TIME IN THE AIR = ", t_total, "seconds"
print "THE TOTAL DISTANCE TRAVELLED BY THE BALL = ", x_total, "metres"
print "THE TOTAL RANGE OF THE BALL = ", r_total, "metres"
        