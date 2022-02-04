
from math import *

R1=float(input("grand rayon"))
R2=float(input("petit rayon"))
h=float(input("hauteur"))
V=pi*h/3*(R1**2+R2**2+R1*R2)
print("Le volume du pot est ", V)
