########################################################
#    PHAS1240 Session 9                                #
# Code to show an animation of the planetary orbits    #
# of two different planets around a stationary star    #
# Each planet has its own gravitational attraction     #
# to the star and their own masses, radius and         #
# velocity of orbit. The physics formulae involving    #
# the gravitational attraction between two object      #
# was used to caluculate the new position displacement # 
# and velocity of each moving planet                   #
# By Aasim Patel 04/12/14                              #
########################################################

from visual import sphere, vector, color, rate, mag

dt = 0.001 # timestep
dt_Planet_2 = 0.001 # timestep of second planet
step = 1 # loop counter
maxstep = 2000000 # maximum number of steps

#  Define the star, planets and constants
M = 1000 # mass of star (in units where G = 1)
mass = 1 # mass of planet
mass_Planet_2 = 0.001
initpos = vector(0,1,0) # initial position vector of Planet
initpos_Planet_2 = vector(0,1.5,0)
Planet = sphere(pos=initpos,radius=0.075*mass,color=color.blue,make_trail=True)#Define the initial position of the Planet, colour, radius and make trail
Planet.trail_object.color=color.white # make the trail white
Planet_2 = sphere(pos=initpos_Planet_2, radius = 100*mass_Planet_2, color=color.magenta,make_trail=True)#Define the initial position of the second planet, colour, radius and make trail
Planet_2.trail_object.color=color.green#colour of the trail of the second planet
Star = sphere(pos=(0,0,0),radius=0.2,color=color.yellow)
vel = vector(-25, 0, 0) # initial velocity of planet 1
vel_Planet_2 = vector(-25,0,0) # Velocity vector of second planet
G = 1.0#6.674*(10**(-11))    #Gravitational Attraction of first planet
G_Planet_2 = 1000000#The gravitational attraction of the second planet

while step <= maxstep: #While loop to determine the position of the planet and draw it until step is less than or equal to maxstep
   initpos = initpos + vel*dt #redefine the position of the first planet using the displacement equation r(t+deltat) = r(t) + v(dt)
   vel = vel - ((G*M*(initpos))/((mag(initpos))**3))*dt #redefine the velocity of the first planet using the formula v = v(t) - GMr/mag(r)^3 x dt where r is a vector and mag(r) means magnitude of r
   Planet.pos = initpos # draw the new position of the first planet
   step = step+1 # go up in steps by one
   rate(50)#set the rate of the first planet animation
   initpos_Planet_2 = initpos_Planet_2 + vel_Planet_2*dt_Planet_2 # redefine the position of the second planet
   vel_Planet_2 = vel_Planet_2 - ((G_Planet_2*mass_Planet_2*(initpos_Planet_2))/((mag(initpos_Planet_2))**3))*dt_Planet_2 #redefine the velocity of the second planet
   Planet_2.pos = initpos_Planet_2 # redraw the position of the second planet
   rate(50) #set the rate of the second planet animation
       
       
print("end of program")#print 'end of programme' when the animations have finished