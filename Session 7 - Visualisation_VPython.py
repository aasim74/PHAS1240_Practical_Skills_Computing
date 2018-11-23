#Code to create a 3-dimensional model of a Sodium Chloride Atom involving seperate Sodium and Chorine Atoms
#Aasim Patel 20/11/14 Session 7

#import main functions from numpy and functions from visual python
import numpy as np
from visual import sphere, curve, size, color

#set the variables
a=0.2
num = 12 #number of atoms
r = 0.5 #radius of each atom
M = 0 #initial value for the Madelung constant

#Defining positions i, j and k and drawing the atoms in the range from -num to num+1 or -L to L since -num = -L and num+1 = L
for i in range(-num, num+1):
    for j in range (-num, num+1):
        for k in range (-num, num+1):
            if i==0 and j==0 and k==0:
                central = sphere(pos = (0,0,0), radius = r, color=color.blue) #if i, j and k are all 0, then draw a sphere at the centre (origin)
            else: #if i,j and k are not 0 then complete the following commands
                if (i+j+k) % 2: #if i+j+k are odd, then minus the potential from the Madelung constant
                    M = M - 1/(np.sqrt(i**2 + j**2 + k**2))
                    chlorineatom = sphere(pos = (i,j,k), radius = r/1.5, color=color.red)#Draw a chlorine atom when the value of i+j+k is odd
                    print "the sum of i, j and k is ", i+j+k    #print the value of i+j+k
                else:
                    M = M + 1/(np.sqrt(i**2 + j**2 + k**2))
                    sodiumatom = sphere(pos = (i,j,k), radius = r, color=color.green) #Draw a Sodium atom when the value of i+j+k is even

print "the value of M is ", M # print the value of M