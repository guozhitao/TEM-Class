import numpy as np
import math
 
# Crystal Lattice Parameters {a, b, c, alpha, beta, gamma}
a = 4
b = 6
c = 5
alpha = math.radians(90)
beta = math.radians(120)
gamma = math.radians(90)

# Direct Metric Tensor, g
g = np.mat([[a*a, a*b*round(math.cos(gamma),5), a*c*round(math.cos(beta),5)],
            [b*a*round(math.cos(gamma),5), b*b, b*c*round(math.cos(alpha),5)],
            [c*a*round(math.cos(beta),5), c*b*round(math.cos(alpha),5), c*c]])

# Reciprocal Metric Tensor, G
G = np.linalg.inv(g)

# Volume of the Direct Unit Cell, v
v = math.sqrt(a*a*b*b*c*c*(1 - (math.cos(alpha))**2 - (math.cos(beta))**2 - (math.cos(gamma))**2 + 2*math.cos(alpha)*math.cos(beta)*math.cos(gamma)))

# Volume of the Reciprocal Unit Cell, V
V = 1/v

# Direct Structure Metric Tensor, aij
F = math.cos(beta)*math.cos(gamma)-math.cos(alpha)

aij = np.mat([[a, b*round(math.cos(gamma),5), c*round(math.cos(beta),5)],
              [0, b*round(math.sin(gamma),5), -round(c*F/math.sin(gamma),5)],
              [0, 0, round((v/(a*b*math.sin(gamma))),5)]])

# Reciprocal Structure Metric Tensor, bij
bij = aij*G

# Length of the Direct Lattice Vector, d
t1 = 1
t2 = 0
t3 = 1
t4 = -2
t5 = 0
t6 = 1

T1 = np.mat([t1, t2, t3])
T2 = np.mat([[t1],
             [t2],
             [t3]])
T3 = np.mat([[t4],
             [t5],
             [t6]])
T4 = np.mat([t4, t5, t6])
d = math.sqrt(T1*g*T3)

# Length of the Reciprocal Lattie Vector, D
g1 = 1
g2 = 0
g3 = 1
g4 = -2
g5 = 0
g6 = 1

G1 = np.mat([g1, g2, g3])
G2 = np.mat([[g1],
             [g2],
             [g3]])
G3 = np.mat([[g4],
             [g5],
             [g6]])
G4 = np.mat([g4, g5, g6])
#D = math.sqrt(G1*G*G3)

# Angle between the Direct Lattice Vectors, theta
theta = math.acos((T1*g*T3)/math.sqrt(T1*g*T2*T4*g*T3))

# Angle between the Reciprocal Lattice Vectors, THETA
THETA = math.acos((G1*G*G3)/math.sqrt(G1*G*G2*G4*G*G3))

print(math.degrees(THETA))


