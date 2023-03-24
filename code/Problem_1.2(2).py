#-------------------------------Importation of required libraries------------------------------------
from sympy import *

#------------------------------Declaration of variables and symbols----------------------------------
Θ1, Θ2, Θ3 = symbols("Θ1 Θ2 Θ3")
l1, l2, l3 = symbols("l1 l2 l3")
Θ1_dot, Θ2_dot, Θ3_dot = symbols("Θ1_dot Θ2_dot Θ3_dot")
dot = '\u0307'
x_dot = symbols("x" + dot)
y_dot = symbols("y" + dot)
Φ_dot = symbols("Φ_dot")
s1 = sin(Θ1)
s12 = sin(Θ1+Θ2)
s123 = sin(Θ1+Θ2+Θ3)
c1 = cos(Θ1)
c12 = cos(Θ1+Θ2)
c123 = cos(Θ1+Θ2+Θ3)

#-----------------------------Equations on which jacobian is defined---------------------------------
#x_dot = - (l1*s1 + l2*s12 + l3*s123)*Θ1_dot - (l2*s12 + l3*s123)*Θ2_dot - l3*s123*Θ3_dot
#y_dot = (l1*c1 + l2*c12 + l3*c123)*Θ1_dot + (l2*c12 + l3*c123)*Θ2_dot + l3*c123*Θ3_dot
#phi_dot = Θ1_dot + Θ2_dot + Θ3_dot

#---------------------------------Creation of Jacobian Matrix----------------------------------------
j11 = - (l1*s1 + l2*s12 + l3*s123)
j12 = - (l2*s12 + l3*s123)
j13 = - l3*s123
j21 = (l1*c1 + l2*c12 + l3*c123)
j22 = (l2*c12 + l3*c123)
j23 = l3*c123
j31, j32, j33 = 1, 1, 1

J = Matrix([[j11, j12, j13], [j21, j22, j23], [j31, j32, j33]])
J_inverse = J.inv()
print("\n\nJacobian Inverse: ", J_inverse, "\n\n")


p_dot = Matrix([[x_dot], [y_dot], [Φ_dot]])                                     #Velocity matrix
q_dot = J_inverse*p_dot                                                         #Joint velocity matrix

print("Θ1_dot = ", q_dot[0], "\n\n")
print("Θ2_dot = ", q_dot[1], "\n\n")
print("Θ3_dot = ", q_dot[2], "\n\n")


