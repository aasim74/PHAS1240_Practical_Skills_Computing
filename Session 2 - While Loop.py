##############################################################################
#Code to estimate the value of pi using the Madhava/Gregory/Leibniz approximation of pi#
#Aasim Patel 17/10/14#
##############################################################################

#Define the intitial values
n=0
tolerance = float(raw_input("Please inut your tolerance value "))
newterm=1
value = 0

#set condition and apply the summation formula#
while abs(newterm) > tolerance:
    newterm = ((-1)**n)/(2*n+1.0)
    n=n+1
    print "the newterm = ", newterm
    value = value + newterm
    print "Adding", newterm, "to our sequence"
    
#print the value of the pi/4 approximation when the condition is not applied#
print "the approximation of pi/4 = " ,value

#How many terms are used in the sequence?#
print "the number of terms used in this sequence = " , n

#print the estimation of pi using the formula#
estpi = value * 4
print "therefore the approximated value of pi = ", estpi

#import the actual value of pi from numpy#
from numpy import pi
print "the actual value of pi = " , pi

#Compare the actual value of pi with the estmated value and find the difference#
difference = pi-estpi
print "the difference between the pi values = ", difference 

#It is justified that the accuracy of the approximation is dependent on the tolerance value# 
#The accuracy of the approximation is at the same decimal places as the tolerance value#
#It is justified that the approximated value of pi is accurate to n decimal places for the tolerance of 1e-n#
#It took 25.1 seconds approximately for the programme to calculate the value of pi when the tolerance value is set to 1e-8#
#It took more than 40 minutes for the programme to calculate the approximation of pi when the tolerace is set to 1e-20#
#This is a good method of calculating the approximated value of pi because we can set the tolerance to whichever accuracy we want#
#One problem with this programme is that, if we want to find higher accuracies for the approximated value of pi, it takes very long#
#A better way to calculate an approximation of the value of pi would be to use a better programm or computer which can carry out calculations faster e.g. a better central processing unit (cpu) would carry out calculations faster (intel core i7 5960x instead of an intel core i5 vpro)
