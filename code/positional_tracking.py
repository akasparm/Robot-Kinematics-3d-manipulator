
#--------------Importation of required libraries-----------------------
from math import *
import matplotlib.pyplot as plt



#--------------Variable declaration------------------------------------
x_initial = float(input("Enter initial x coordinate:"))                                 #Initial position of x
y_initial = float(input("Enter initial y coordinate:"))                                 #Initial position of y
theta_initial = radians(float(input("Enter initial orientation(Φ in degree):")) + 90)   #Initial orientation
t = int(input("Enter time(seconds):"))                                                           #Time till the vehicle will move
alpha = radians(float(input("Enter steering angle(alpha in degree):")))                 #Steering angle
w = float(input("Enter rotational speed omega(rad/s):"))                                #Rotaional speed of the wheel(Omega)


#List generation of x, y, and theta to record position and orientation
x = []                                                                         
y = []
theta = []
a = 0.0625*w*tan(alpha)

cx = x_initial - 0.25*w*sin(theta_initial)/a
cy = y_initial + 0.25*w*cos(theta_initial)/a


#--------------Loop for recording the values per second----------------
for i in range(0,t+1):

    theta_instantaneous = a*i + degrees(theta_initial)    
    x_instantaneous = 0.25*w*sin(radians(theta_instantaneous))/a + cx
    y_instantaneous = -0.25*w*cos(radians(theta_instantaneous))/a + cy

    # x_instantaneous = round(x_instantaneous,2)                                          #To reduce the long float values
    # y_instantaneous = round(y_instantaneous,2)                                          #To reduce the long float values

#Appending the instantaneous values in the position and orienation list to keep the record
    x.append(x_instantaneous)                                                           
    y.append(y_instantaneous)                                                           
    theta.append(theta_instantaneous)                                                       


print("\n\n\nFinal position of the vehicle(x, y, Φ): ", "(", x[-1], ", ", y[-1], ", ", (theta[-1]-90)%360, ")\n\n")

#Plotting the final x and y position
plt.xlabel('x coordinate')
plt.ylabel('y coordinate')
plt.title('Vehicle Trajectory')
plt.plot(x,y)
plt.show()

